from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Sales
from .serializers import SalesSerializer
from products.models import Products
from django.http import Http404

# Create your views here.

class SalesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sale = Sales.objects.all()
        serializer = SalesSerializer(sale, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            product_id = serializer.validated_data['product'].id
            quantity = serializer.validated_data['quantity']
            try:
                product = Products.objects.get(pk=product_id)
                if product.stock >= quantity:
                    product.stock -= quantity
                    product.save()
                    total = quantity * product.price
                    serializer.validated_data['total'] = total
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Not enough stock'}, status=status.HTTP_400_BAD_REQUEST)
            except Products.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SalesDetailView(APIView):
    def get_object(self, pk):
        try:
            return Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        sale = self.get_object(pk)
        serializer = SalesSerializer(sale)
        return Response(serializer.data)
