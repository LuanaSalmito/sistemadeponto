from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.models.registroponto import RegistroPonto
from api.serializers.registroponto import RegistroPontoSerializer
from api.permissions.todos import TodosPodemVer, TodosPodemCriar, TodosPodemEditar

class RegistroPontoViewSet(viewsets.ModelViewSet):
    queryset = RegistroPonto.objects.all()
    serializer_class = RegistroPontoSerializer
    permission_classes = [IsAuthenticated | TodosPodemEditar | TodosPodemVer | TodosPodemCriar]

    def get_queryset(self):
        
        if self.request.user.is_authenticated:
            return self.queryset.filter(colaborador__usuario=self.request.user)
        return self.queryset.none()

    def perform_create(self, serializer):
        
        colaborador = self.request.user.colaborador
        serializer.save(colaborador=colaborador)
