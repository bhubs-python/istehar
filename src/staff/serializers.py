from rest_framework import serializers

from . import models
from home import models as home_model


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


#sub category serializer
class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = home_model.SubCatagory
        fields = ('id', 'name', )
