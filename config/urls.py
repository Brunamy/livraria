from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from livraria.views import CategoriaViewSet

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"editora", EditoraViewSet)
router.register(r"autores", AutorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls))
]
