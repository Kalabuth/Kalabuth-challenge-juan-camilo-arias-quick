from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.hashers import make_password

from aplicacion.models import Clients, Bills, BillsProducts, Products


class ClientRegistrationSerializer(serializers.ModelSerializer):
    
    def validate_password(self, value):
        return make_password(value)
        
    class Meta:
        model = Clients
        fields = ('document', 'first_name', 'last_name', 'email', 'password', 'document_type')
        validators = [
                UniqueTogetherValidator(
                    queryset=Clients.objects.all(),
                    fields = ['document_type', 'document'],
                    message = 'Ya existe un registro con el tipo de documento y el número de documento ingresado'
                )
            ]
        
        
class ClientLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class BillsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillsProducts
        fields = '__all__'