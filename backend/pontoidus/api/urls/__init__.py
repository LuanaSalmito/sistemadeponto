from .registroponto import RegistroPontoViewSet
from .jornada import JornadaViewSet
from .tipojornada import TipoJornadaViewSet
from .user import UserViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'registros', RegistroPontoViewSet)
router.register(r'jornadas', JornadaViewSet)
router.register(r'tipojornadas', TipoJornadaViewSet)
router.register(r'users', UserViewSet)

urlpatterns = router.urls
