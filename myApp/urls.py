from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'myApp'

router = routers.DefaultRouter()
router.register(r'investments', views.InvestmentViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:investment_id>/', views.detail, name='detail'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
