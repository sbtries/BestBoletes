from django.db import models

class Bolete(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    name_in_naboletes = models.CharField(max_length=250, blank=True, null=True)
    genus = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    common_name = models.CharField(max_length=500,blank=True, null=True)
    tells = models.TextField(blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)
    science_notes = models.TextField(blank=True, null=True)
    edibility = models.TextField(blank=True, null=True)
    chemical_tests = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name