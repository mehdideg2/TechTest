from django.db import models

class Investment(models.Model):

    def __str__(self):
        return self.titreoperation

    titreoperation = models.CharField(max_length=200)
    entreprise = models.CharField(max_length=200, blank=True)
    annee_de_livraison = models.CharField(max_length=200, blank=True)
    ville = models.CharField(max_length=200, blank=True)
    mandataire = models.CharField(max_length=200, blank=True)
    ppi = models.CharField(max_length=200, blank=True)
    lycee = models.CharField(max_length=200, blank=True)
    notification_du_marche = models.DateField(null=True)
    codeuai = models.CharField(max_length=200, blank=True)
    longitude = models.FloatField(default=0.0)
    etat_d_avancement = models.CharField(max_length=200, blank=True)
    montant_des_ap_votes_en_meu = models.FloatField(default=0)
    cao_attribution = models.DateField(null=True)
    latitude = models.FloatField(default=0.0)
    maitrise_d_oeuvre = models.CharField(max_length=200, blank=True)
    mode_de_devolution = models.CharField(max_length=200, blank=True)
    annee_d_individualisation = models.IntegerField(default=0)
    enveloppe_prev_en_meu = models.FloatField(default=0.0)
