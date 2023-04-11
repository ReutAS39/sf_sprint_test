from rest_framework import serializers

from pereval.models import PerevalAdded, Coords, Level, Users, Images, PerevaladdedImages


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        verbose_name = 'Координаты'
        exclude = ('id',)


class LevelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Level
        exclude = ('id',)


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('data', 'title')
        verbose_name = 'Изображение'

# class PerevaladdedImagesImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PerevaladdedImages
#         fields = ('__all__')
#         verbose_name = 'ПереИзобр'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'phone', 'fam', 'name', 'otc',)
        verbose_name = 'Пользователь'

class PerevalSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerialize()
    images = ImagesSerializer(many=True)
    #imagess = PerevaladdedImagesImagesSerializer()
    class Meta:
        model = PerevalAdded
        exclude = ('id', 'status')





