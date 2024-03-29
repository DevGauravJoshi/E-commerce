from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

from .models import ShopModel
from .serializers import ShopModelSerializer

ALLOWED_CATEGORIES = ["New & Featured", "Men", "Women", "Kids", "Sale"]


# Create your views here.
class ShopCategoryView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, category):
        try:
            if category in ALLOWED_CATEGORIES:
                category_data = ShopModel.objects.filter(category=category)
                serializer = ShopModelSerializer(category_data, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
