import django_tables2 as tables
from .models import Investment

class InvestmentTable(tables.Table):
    show_detail = tables.TemplateColumn('<a href="detail/{{record.id}}">Detail</a>')
    class Meta:
        model = Investment
        template_name = "django_tables2/bootstrap.html"
        # id = tables.Column(attrs={"td": {"class": "my-class"}})
        fields = ('titreoperation', 'entreprise', 'annee_de_livraison', 'ville', 'mandataire', 'ppi', 'lycee',
                  'notification_du_marche', 'codeuai', 'longitude', 'etat_d_avancement', 'montant_des_ap_votes_en_meu',
                  'cao_attribution', 'latitude', 'maitrise_d_oeuvre', 'mode_de_devolution', 'annee_d_individualisation',
                  'enveloppe_prev_en_meu')