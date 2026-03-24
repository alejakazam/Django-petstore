from django.urls import path
from .views import main, tienda

urlpatterns = [
    path('', main, name='main'),
    path('tienda', tienda, name = 'tienda')

]