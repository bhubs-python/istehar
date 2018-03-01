from rest_framework import serializers

from . import models


#district serializer
class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.District
        fields = ('id', 'name', )


#thana serializer
class ThanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Thana
        fields = ('id', 'name', )
