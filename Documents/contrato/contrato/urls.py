from django.urls import path
from contrato.views import index, cadastro_contrato, cadastro_empresa


urlpatterns = [
    path('', index, name='index'),
    path('cadastro_contrato/', cadastro_contrato, name='cadastro_contrato'),
    path('cadastro_empresa/', cadastro_empresa, name='cadastro_empresa'),
    
]
