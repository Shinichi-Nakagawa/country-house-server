from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
from house.models import HouseMetrics
from house.permissions import IsOwnerOrReadOnly
from house.serializers import HouseMetricsSerializer, UserSerializer


class MetricsViewSet(viewsets.ModelViewSet):
    queryset = HouseMetrics.objects.all()
    serializer_class = HouseMetricsSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
