from django.urls import path, include
from rest_framework import routers
from .views import SalesDataViewSet

router = routers.DefaultRouter()
router.register(r"sales_data", SalesDataViewSet)
urlpatterns = [
    path('', include(router.urls)),

]