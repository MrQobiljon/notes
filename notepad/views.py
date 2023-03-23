from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import permissions

from .models import Plan
from .serializers import PlanSerializer, UserSerializer
# Create your views here.



class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.filter(author=self.request.user)


class UsersViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser, permissions.IsAuthenticated)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
