from django.urls import path, include
from apps.customers.views import CustomersViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', CustomersViewset)

urlpatterns = [
    path('', include(router.urls)),
]