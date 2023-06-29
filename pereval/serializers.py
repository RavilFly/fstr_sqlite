from rest_framework import serializers
from .models import PerevalAdded, Coords

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'



class PerevalAddedSerializer(serializers.ModelSerializer):
    coords = CoordsSerializer()


    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        coord_data = validated_data.pop('coords')
        coord_ = Coords.objects.create(**coord_data)
        pereval_added = PerevalAdded.objects.create(coords=coord_, **validated_data)

        return pereval_added