from django.urls import path

from . import views

urlpatterns = [
    # /myApp
    path('', views.index, name='index'),
    # /myApp/id/
    path('<int:investment_id>/', views.detail, name='detail'),
    # /myApp/id/results
    path('<int:investment_id>/results/', views.results, name='results'),
    # /myApp/id/vote
    path('<int:investment_id>/vote/', views.vote, name='vote'),
]
