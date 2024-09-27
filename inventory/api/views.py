from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inventory.models import Inventory_Items
from .serializers import ItemSerializer,UserLoginSerializer,UserRegistrationSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
import logging


# Registration View
class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(username=username)
                if not user.check_password(password):
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get the logger instance for your inventory app
logger = logging.getLogger('inventory')

class ItemListCreate(APIView):
    permission_classes = [IsAuthenticated]  # Require JWT authentication

    def get(self, request):
        try:
            logger.info("Fetching all items")  # Log the action
            items = Inventory_Items.objects.all()
            serializer = ItemSerializer(items, many=True)
            logger.debug(f"Fetched {len(items)} items.")  # Log additional info
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching items: {e}")  # Log the error
            return Response({"error": "Failed to fetch items"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            logger.info("Creating a new item")  # Log the creation attempt
            serializer = ItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.debug(f"Item created with ID {serializer.data['id']}")  # Log creation details
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.warning(f"Invalid item data: {serializer.errors}")  # Log validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating item: {e}")  # Log the error
            return Response({"error": "Failed to create item"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ItemDetail(APIView):
    permission_classes = [IsAuthenticated]  # Require JWT authentication

    def get(self, request, pk):
        try:
            logger.info(f"Fetching item with ID {pk}")  # Log the fetch attempt
            item = get_object_or_404(Inventory_Items, pk=pk)
            serializer = ItemSerializer(item)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching item {pk}: {e}")  # Log the error
            return Response({"error": f"Failed to fetch item {pk}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            logger.info(f"Updating item with ID {pk}")  # Log the update attempt
            item = get_object_or_404(Inventory_Items, pk=pk)
            serializer = ItemSerializer(item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.debug(f"Item {pk} updated successfully")  # Log update success
                return Response(serializer.data)
            logger.warning(f"Invalid update data for item {pk}: {serializer.errors}")  # Log validation error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error updating item {pk}: {e}")  # Log the error
            return Response({"error": f"Failed to update item {pk}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            logger.info(f"Deleting item with ID {pk}")  # Log the delete attempt
            item = get_object_or_404(Inventory_Items, pk=pk)
            item.delete()
            logger.debug(f"Item {pk} deleted successfully")  # Log deletion success
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting item {pk}: {e}")  # Log the error
            return Response({"error": f"Failed to delete item {pk}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
