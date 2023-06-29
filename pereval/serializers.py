from rest_framework import serializers
from .models import PerevalAdded, Coords, Images

class ImagesSerializer(serializers.ModelSerializer):
    img = serializers.URLField()

    class Meta:
        model=Images
        fields = ['title', 'img']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'



class PerevalAddedSerializer(serializers.ModelSerializer):
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        fields = '__all__'

    def create(self, validated_data):
        coord_data = validated_data.pop('coords')
        coord_ = Coords.objects.create(**coord_data)
        images = validated_data.pop('images')

        pereval_added = PerevalAdded.objects.create(coords=coord_, **validated_data)

        for image in images: #извлекаем ссылки на картинки и сохраняем в бд
            img_ = image.pop('img')
            title_ = image.pop('title')
            Images.objects.create(pereval=pereval_added, img=img_, title=title_) #создали перевал

        return pereval_added