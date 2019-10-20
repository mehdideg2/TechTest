import django_filters
from .models import Investment


class InvestmentsFilter(django_filters.FilterSet):
    ville = django_filters.CharFilter()
    etat_d_avancement = django_filters.CharFilter()
    class Meta:
        model = Investment
        fields = ['id', 'ville', 'etat_d_avancement', ]