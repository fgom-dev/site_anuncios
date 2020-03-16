from django.urls import path

from .views import home, categoria, anuncio


urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', categoria, name='categoria'),
    path('anuncio/<int:anuncio_id>', anuncio, name='anuncio'),
]
