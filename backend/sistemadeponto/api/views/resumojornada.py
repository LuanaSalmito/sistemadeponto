from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.permissions.todos import TodosPodemCriar, TodosPodemVer
from api.models.resumojornada import ResumoJornada
from api.serializers.resumojornada import ResumoJornadaSerializer

class ResumoJornadaViewSet(viewsets.ModelViewSet):
    queryset = ResumoJornada.objects.all()
    serializer_class = ResumoJornadaSerializer
    permission_classes = [IsAuthenticated | TodosPodemVer | TodosPodemCriar]

    def get_queryset(self):
       
        if self.request.user.is_authenticated and not self.request.user.is_staff:
            return self.queryset.filter(colaborador__usuario=self.request.user)
        return self.queryset

    def perform_create(self, serializer):
        
        instance = serializer.save()
        instance.calcular_resumo()
