from django.urls import path

from rest_framework.routers import SimpleRouter

from notepad.views import PlanViewSet, UsersViewSet

router = SimpleRouter()

router.register('plan', PlanViewSet, basename='plans')
router.register('users', UsersViewSet, basename='users')

urlpatterns = router.urls