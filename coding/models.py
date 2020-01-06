from django.db import models

# Create your models here.
class Code(models.Model):
    q1 = models.BooleanField("q1", help_text="Vind je dit leuk?")
    q2 = models.BooleanField("q2", help_text="Waar ga je heen?")
