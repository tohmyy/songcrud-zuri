from django.urls import path
from . import views


urlpatterns = [
    path('', views.song_api), #localhost:8000/api
    # path('api/product', include('products.urls')) #can be used this way(it works)
]