import requests
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import OrderSerializer
from rest_framework import status

class GoogleOAuthCallback(APIView):
    def get(self, request):
        code = request.GET.get('code')

        token_url = 'https://oauth2.googleapis.com/token'
        token_data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_CLIENT_SECRET,
            'redirect_uri': settings.REDIRECT_URI,
            'grant_type': 'authorization_code',
        }

        token_response = requests.post(token_url, data=token_data).json()

        access_token = token_response.get('access_token')
        refresh_token = token_response.get('refresh_token')

        # Get user info
        user_info = requests.get(
            'https://www.googleapis.com/oauth2/v1/userinfo',
            params={'access_token': access_token}
        ).json()

        email = user_info.get('email')
        user, _ = User.objects.get_or_create(username=email, defaults={'email': email})

        jwt_token = RefreshToken.for_user(user)

        return Response({
            'access_token': str(jwt_token.access_token),
            'refresh_token': str(jwt_token),
            'google_access_token': access_token,
            'google_refresh_token': refresh_token
        })
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    if request.method == 'GET':
        orders = request.user.order_set.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    data = request.data
    serializer = OrderSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
