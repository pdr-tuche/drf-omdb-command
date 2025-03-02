from .views import FilmesViewSet, UsuariosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UsuariosViewSet)
router.register(r'filmes', FilmesViewSet)

urlpatterns = router.urls
