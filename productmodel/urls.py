from django.urls import path
#from .views import productAPIView,productDetails
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.MyProduct, name='product'),
    path('form', views.productForm, name='form'),
    
]

