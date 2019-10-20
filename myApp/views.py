from django.shortcuts import render, get_object_or_404
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from myApp.tables import InvestmentTable
from .serializers import InvestmentSerializer
from .models import Investment
from .forms import InvestmentForm
from rest_framework import viewsets
from .filters import InvestmentsFilter


class InvestmentViewSet(viewsets.ModelViewSet):
    serializer_class = InvestmentSerializer
    queryset = Investment.objects.all()
    filter_class = InvestmentsFilter


class InvestmentTableView(SingleTableView, FilterView):
    model = Investment
    table_class = InvestmentTable
    template_name = 'myApp/investment_table.html'
    filterset_class = InvestmentsFilter
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = InvestmentsFilter(self.request.GET, queryset=self.get_queryset())
        return context


def investment_create_view(request):
    form = InvestmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InvestmentForm()
    context = {
        'form': form
    }
    return render(request, "myApp/investment_create.html", context)


def investment_detail_view(request, investment_id):
    investment = get_object_or_404(Investment, pk=investment_id)
    form = InvestmentForm(instance=investment)
    context = {
        'form': form,
    }
    return render(request, "myApp/investment_detail.html", context)