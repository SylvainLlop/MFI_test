from rest_framework import serializers
from peak_app.models import Peak


class PeakSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peak
        fields = ['name', 'lat', 'lon', 'altitude']