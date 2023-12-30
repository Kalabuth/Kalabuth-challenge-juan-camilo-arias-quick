from django.urls import path
from . import views

urlpatterns = [
   
    #Clients
    path('register-clients/', views.client_registration_view, name='crear-usuario'),
    path('login/', views.client_login_view, name='login'),
    path('export-clients/', views.export_user, name='export_user'),
    path('upload-clients/', views.bulk_upload_clients, name='upload_clients'),
    path('list/clients/', views.list_clients, name='list-clients'),
    path('update/client/<int:pk>/', views.update_client, name='update-client'),
    path('delete/client/<int:pk>/', views.delete_client, name='delete-client'),
    path('client/<int:pk>/',  views.client_detail, name='client_detail'),

    
    #Bills
    path('create/bill/', views.create_bill, name='create-bill'),
    path('list/bills/', views.list_bills, name='list-bills'),
    path('update/bill/<int:pk>/', views.update_bill, name='update-bill'),
    path('delete/bill/<int:pk>/', views.delete_bill, name='delete-bill'),
    path('bill/<int:pk>/',  views.bill_detail, name='bill_detail'),


    #Bills-product
    path('create/bill_product/', views.create_bills_product, name='create-bills-product'),
    path('list/bills_products/', views.list_bills_products, name='list-bills-products'),
    path('update/bills_product/<int:pk>/', views.update_bills_product, name='update-bills-product'),
    path('delete/bills_product/<int:pk>/', views.delete_bills_product, name='delete-bills-product'),
    path('bill_product/<int:pk>/',  views.bill_product_detail, name='bill_product_detail'),


    #Products
    path('create/product/', views.create_product, name='create-product'),
    path('list/products/', views.list_products, name='list-products'),
    path('update/product/<int:pk>/', views.update_product, name='update-product'),
    path('delete/product/<int:pk>/', views.delete_product, name='delete-product'),
    path('product/<int:pk>/',  views.product_detail, name='product_detail'),

]
