import django_tables2 as tables
from .models import Investment

class InvestmentTable(tables.Table):
    class Meta:
        model = Investment
        template_name = "django_tables2/bootstrap.html"
        # id = tables.Column(attrs={"td": {"class": "my-class"}})
        fields = ('titreoperation', 'entreprise',)