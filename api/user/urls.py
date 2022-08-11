from rest_framework import routers
from django.urls import path, include

from .views import UserViewSet, signin, signout, validate


router = routers.DefaultRouter()
router.register(r'', UserViewSet)
urlpatterns = [
    path('login', signin, name='signin'),
    path('logout/<int:id>', signout, name='signout'),
    path('validate', validate, name='validate'),
    path('', include(router.urls))
]