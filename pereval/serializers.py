from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import PerevalAdded, Coords, Images, Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['name', 'email', 'phone']

class ImagesSerializer(serializers.ModelSerializer):
    img = serializers.URLField()

    class Meta:
        model=Images
        fields = ['title', 'img']

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']



class PerevalAddedSerializer(WritableNestedModelSerializer):
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)
    user = UsersSerializer()

    class Meta:
        model = PerevalAdded
        fields = ('id', 'status', 'beauty_title', 'title',\
                  'other_titles', 'connect', 'user', 'coords', \
                  'images', 'winter', 'spring', 'summer', 'autumn')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        email = user_data.get('email')

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            user = Users.objects.create(**user_data)

        coord_data = validated_data.pop('coords')
        coord_ = Coords.objects.create(**coord_data)
        images = validated_data.pop('images')

        pereval_added = PerevalAdded.objects.create(coords=coord_, user=user, **validated_data)

        for image in images: #извлекаем ссылки на картинки и сохраняем в бд
            img_ = image.pop('img')
            title_ = image.pop('title')
            Images.objects.create(pereval=pereval_added, img=img_, title=title_)

        return pereval_added