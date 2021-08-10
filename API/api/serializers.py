# api/serializers.py
from rest_framework import serializers
from boletes.models import Bolete

class BoleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolete
        fields = ('name', 'description', 'genus', 'species', 'common_name', 'tells', 'other_info', 'science_notes', 'edibility', 'chemical_tests', 'links',)