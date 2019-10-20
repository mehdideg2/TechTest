from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'myApp'

router = routers.DefaultRouter()
router.register(r'investments', views.InvestmentViewSet)

urlpatterns = [
    path('', views.InvestmentTableView.as_view()),
    path('api/', include(router.urls)),
    path('create/', views.investment_create_view, name='create'),
    path('detail/<int:investment_id>/', views.investment_detail_view, name='detail2'),
]
