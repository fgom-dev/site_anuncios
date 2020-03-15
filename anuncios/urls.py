from django.urls import path

from .views import home, categoria


urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', categoria, name='categoria'),
]
