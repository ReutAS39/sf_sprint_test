from rest_framework import serializers

from pereval.models import PerevalAdded, Coords, Level, Users

class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        verbose_name = 'Координаты'
        exclude = ('id',)


class LevelSerialize(serializers.ModelSerializer):
    class Meta:
        model = Level
        exclude = ('id',)


class PerevalSerializer(serializers.ModelSerializer):
    # user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerialize()
    # images = ImagesSerializer(many=True)

    class Meta:
        model = PerevalAdded
        exclude = ('id', 'status')


class UsersSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    fam = serializers.CharField(source='last_name')
    otc = serializers.CharField(source='patronymic')
    email = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'otc', 'phone')
        verbose_name = 'Пользователь'