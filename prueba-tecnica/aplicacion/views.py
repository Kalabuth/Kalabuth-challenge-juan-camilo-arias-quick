import csv
import json
from django.db import transaction
from datetime import  datetime
from rest_framework import status
from rest_framework.response import Response
from aplicacion.models import Clients, Bills, Products, BillsProducts
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Clients
from rest_framework.exceptions import NotFound, ParseError, ValidationError, AuthenticationFailed
from aplicacion.task import generate_csv_export
from aplicacion.serializadores import (ClientRegistrationSerializer, ClientLoginSerializer, 
                                        BillsProductsSerializer, BillsSerializer, ProductsSerializer, ClientsSerializer)



## POST ##

@api_view(['POST'])
@transaction.atomic
@permission_classes([AllowAny])
def client_registration_view(request):
    if request.method == 'POST':
        serializer = ClientRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'El registro del cliente fue exitoso', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def create_bill(request):
    serializer = BillsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'El registro de la factura fue exitoso', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def create_product(request):
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'El registro del producto fue exitoso', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def create_bills_product(request):
    serializer = BillsProductsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'El registro de la factura-producto fue exitoso', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


## GET LIST ##

@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def list_clients(request):
    clients = Clients.objects.all()
    serializer = ClientsSerializer(clients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def list_bills(request):
    bills = Bills.objects.all()
    serializer = BillsSerializer(bills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def list_products(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def list_bills_products(request):
    bills_products = BillsProducts.objects.all()
    serializer = BillsProductsSerializer(bills_products, many=True)
    return Response(serializer.data)



## PUT ##

@api_view(['PUT'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def update_client(request, pk):
    client = Clients.objects.filter(pk=pk).first()
    serializer = ClientRegistrationSerializer(client, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Actualización exitosa', 'data': serializer.data},status=status.HTTP_200_OK)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def update_bill(request, pk):
    bill = Bills.objects.filter(pk=pk).first()
    serializer = BillsSerializer(bill, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Actualización exitosa', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    product = Products.objects.filter(pk=pk).first()
    serializer = ProductsSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Actualización exitosa', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def update_bills_product(request, pk):
    bills_product = BillsProducts.objects.filter(pk=pk).first()
    serializer = BillsProductsSerializer(bills_product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Actualización exitosa', 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



## DELETE ##

@api_view(['DELETE'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def delete_client(request, pk):
    client = Clients.objects.filter(pk=pk).first()
    client.delete()
    return Response({'message': 'Eliminación exitosa'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def delete_bill(request, pk):
    bill = Bills.objects.filter(pk=pk).first()
    bill.delete()
    return Response({'message': 'Eliminación exitosa'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    product = Products.objects.filter(pk=pk).first()
    product.delete()
    return Response({'message': 'Eliminación exitosa'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def delete_bills_product(request, pk):
    bills_product = BillsProducts.objects.filter(pk=pk).first()
    bills_product.delete()
    return Response({'message': 'Eliminación exitosa'}, status=status.HTTP_204_NO_CONTENT)


## GET By ID ##

@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def client_detail(request, pk):
    try:
        client = Clients.objects.filter(pk=pk).first()
    except Clients.DoesNotExist:
        return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ClientsSerializer(client)
    return Response(serializer.data)


@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def bill_detail(request, pk):
    try:
        bill = Bills.objects.filter(pk=pk).first()
    except Bills.DoesNotExist:
        return Response({"error": "Factura no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BillsSerializer(bill)
    return Response(serializer.data)


@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    try:
        product = Products.objects.filter(pk=pk).first()
    except Products.DoesNotExist:
        return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductsSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def bill_product_detail(request, pk):
    try:
        bill_product = BillsProducts.objects.filter(pk=pk).first()
    except BillsProducts.DoesNotExist:
        return Response({"error": "Relación Factura-Producto no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    serializer = BillsProductsSerializer(bill_product)
    return Response(serializer.data)


## LOGIN

@api_view(['POST'])
@transaction.atomic
def client_login_view(request):
    if request.method == 'POST':
        serializer = ClientLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user =  Clients.objects.filter(email=email).first()
            
            if user:
                if not user.check_password(password):
                    return Response({'error': 'La contraseña es incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)
                
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'message': 'Inicio de sesión exitosa', 'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


## EXPORT CLIENTS

@api_view(['POST'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def export_user(request):
    generate_csv_export.delay(email_user=request.user.email)
    return Response({'message':'El documento fue enviado al correo: '+str(request.user.email)}, status=status.HTTP_200_OK)
    
    
## UPLOAD CLIENTS

@api_view(['POST'])
@transaction.atomic
@permission_classes([IsAuthenticated])
def bulk_upload_clients(request):
    if request.method == 'POST':
        try:
            csv_file = request.FILES['file']  # Asegúrate de que el nombre del campo coincida con tu formulario
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_file)

            for row in csv_reader:
                client_data = {
                    'email': row['Email'],
                    'document': row['Document'],
                    'document_type': row['Document type'],
                    'first_name': row['First Name'],
                    'last_name': row['Last Name'],
                    'password': row['Password']
                }

                serializer = ClientRegistrationSerializer(data=client_data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response({'error': serializer.errors}, status=400)

            return Response({'message': 'Datos cargados exitosamente'}, status=201)

        except Exception as e:
            return Response({'error': str(e)}, status=500)

    return Response({'error': 'Método no permitido'}, status=405)