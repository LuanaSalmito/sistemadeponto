from .regimejornada import urlpatterns as regimejornada_patterns
from .colaborador import urlpatterns as colaborador_patterns
from .usuario import urlpatterns as usuario_patterns
from .registroponto  import urlpatterns as registroponto_patterns
from .resumojornada import urlpatterns as resumojornada_patterns


urlpatterns = [
    *regimejornada_patterns,
    *colaborador_patterns,
    *usuario_patterns,
    *registroponto_patterns,
    *resumojornada_patterns,
    
]
