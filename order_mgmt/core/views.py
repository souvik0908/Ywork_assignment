

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializer import OrderSerializer
from rest_framework import status



@api_view(['GET'])
def get_token(request):
    if  request.user.is_authenticated:
        refresh = RefreshToken.for_user(request.user)
        return Response({
            'refresh':str(refresh),
            'access': str(refresh.access_token)
        })
    return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)


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
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
