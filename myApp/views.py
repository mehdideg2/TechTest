from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


from myApp.serializers import InvestmentSerializer
from .models import Investment
from rest_framework import viewsets, generics


def index(request):
    field_names = [f.name for f in Investment._meta.fields]
    data = [[getattr(ins, name) for name in field_names]
            for ins in Investment.objects.prefetch_related().all()]
    return render(request, 'myApp/index.html', {'field_names': field_names, 'data': data})


def detail(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)    # return 404 if investment_id doesn't exist !
    return render(request, 'myApp/detail.html', {'investment': investment})


class InvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()
