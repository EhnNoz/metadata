from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import TitleRecord
from .serializers import TitleRecordSerializer
from .permissions import IsOwnerOrAdmin, AdminWriteRestrictedFields

class TitleRecordViewSet(viewsets.ModelViewSet):
    queryset = TitleRecord.objects.all()
    serializer_class = TitleRecordSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, AdminWriteRestrictedFields]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return self.queryset
        return self.queryset.filter(owner=user)
