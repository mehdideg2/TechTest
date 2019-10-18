from django.db import models
from django.db.models import IntegerField
from django.utils import timezone
import datetime


class Investment(models.Model):

    def __str__(self):
        return self.titreoperation

    titreoperation = models.CharField(max_length=200)
    entreprise = models.CharField(max_length=200)
    annee_de_livraison = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    mandataire = models.CharField(max_length=200)
    ppi = models.CharField(max_length=200)
    lycee = models.CharField(max_length=200)
    notification_du_marche = models.DateField(null=True, blank=True)
    codeuai = models.CharField(max_length=200)
    longitude = models.FloatField(default=0.0)
    etat_d_avancement = models.CharField(max_length=200)
    montant_des_ap_votes_en_meu = IntegerField(default=0)
    cao_attribution = models.DateField(null=True, blank=True)
    latitude = models.FloatField(default=0.0)
    maitrise_d_oeuvre = models.CharField(max_length=200)
    mode_de_devolution = models.CharField(max_length=200)
    annee_d_individualisation = models.IntegerField(default=0)
    enveloppe_prev_en_meu = models.FloatField(default=0.0)
