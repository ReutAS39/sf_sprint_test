
from rest_framework import serializers

from pereval.models import PerevalAdded, Coords, Level, Users, Images, PerevaladdedImages


from rest_framework import serializers

# class Base64ImageField(serializers.ImageField):
#     """
#     A Django REST framework field for handling image-uploads through raw post data.
#     It uses base64 for encoding and decoding the contents of the file.
#
#     Heavily based on
#     https://github.com/tomchristie/django-rest-framework/pull/1268
#
#     Updated for Django REST framework 3.
#     """
#
#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid
#
#         # Check if this is a base64 string
#         if isinstance(data, six.string_types):
#             # Check if the base64 string is in the "data:" format
#             if 'data:' in data and ';base64,' in data:
#                 # Break out the header from the base64 content
#                 header, data = data.split(';base64,')
#
#             # Try to decode the file. Return validation error if it fails.
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')
#
#             # Generate file name:
#             file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
#             # Get the file name extension:
#             file_extension = self.get_file_extension(file_name, decoded_file)
#
#             complete_file_name = "%s.%s" % (file_name, file_extension, )
#
#             data = ContentFile(decoded_file, name=complete_file_name)
#
#         return super(Base64ImageField, self).to_internal_value(data)
#
#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr
#
#         extension = imghdr.what(file_name, decoded_file)
#         extension = "jpg" if extension == "jpeg" else extension
#
#         return extension


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
    data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title')
        verbose_name = 'Изображение'

# class ImagesSerializer(serializers.ModelSerializer):
#     data = Base64ImageField(
#         max_length=None, use_url=True,
#     )
#
#     class Meta:
#         model = Images
#         fields = ('data', 'title', )

# class PerevaladdedImagesImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PerevaladdedImages
#         fields = ('__all__')
#         verbose_name = 'ПереИзобр'


class UsersSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Users
        fields = ('email', 'phone', 'fam', 'name', 'otc',)
        verbose_name = 'Пользователь'


class PerevalSerializer(serializers.ModelSerializer):
    user = UsersSerializer()
    coords = CoordsSerializer()
    level = LevelSerialize()
    images = ImagesSerializer(many=True)
    #add_time = serializers.DateTimeField(read_only=True)
    #status = serializers.CharField(read_only=True)
    #imagess = PerevaladdedImagesImagesSerializer()

    class Meta:
        model = PerevalAdded
        exclude = ('id',)

    # def create(self, validated_data):
    #     users_data = validated_data.pop('user')
    #     coords_data = validated_data.pop('coords')
    #     image_data = validated_data.pop('images')
    #     levels_data = validated_data.pop('level')
    #     coords = Coords.objects.create(**coords_data)
    #     level = Level.objects.create(**levels_data)
    #     if Users.objects.filter(email=users_data['email']).exists():
    #         user = Users.objects.get(email=users_data['email'])
    #         pereval = PerevalAdded.objects.create(user=user, coords=coords, level=level, **validated_data)
    #         for img in image_data:
    #             image = Images.objects.create(**img)
    #             PerevaladdedImages.objects.create(images=image, perevaladded=pereval)
    #         return pereval
    #
    #     else:
    #        user = Users.objects.create(**users_data)
    #        pereval = PerevalAdded.objects.create(user=user, coords=coords, level=level, **validated_data)
    #     for img in image_data:
    #         image = Images.objects.create(**img)
    #         PerevaladdedImages.objects.create(images=image, perevaladded=pereval)
    #     return pereval

    def create(self, validated_data):
        users_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        image_data = validated_data.pop('images')
        levels_data = validated_data.pop('level')
        coords = Coords.objects.create(**coords_data)

        if Level.objects.filter(winter=levels_data['winter'],
                                summer=levels_data['summer'],
                                autumn=levels_data['autumn'],
                                spring=levels_data['spring']
                                ).exists():
            level = Level.objects.get(winter=levels_data['winter'],
                                      summer=levels_data['summer'],
                                      autumn=levels_data['autumn'],
                                      spring=levels_data['spring']
                                      )
        else:
            level = Level.objects.create(**levels_data)

        if Users.objects.filter(email=users_data['email']).exists():
            user = Users.objects.get(email=users_data['email'])
        else:
            user = Users.objects.create(**users_data)

        pereval = PerevalAdded.objects.create(user=user, coords=coords, level=level, **validated_data)
        for img in image_data:
            image = Images.objects.create(**img)
            PerevaladdedImages.objects.create(images=image, perevaladded=pereval)
        return pereval


# class PerevalUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         exclude = ('fam', 'email', 'phone')


    def update(self, instance, validated_data):

        coords_data = validated_data.pop('coords')
        image_data = validated_data.pop('images')
        levels_data = validated_data.pop('level')
        coords = instance.coords
        level = instance.level
        #print(image_data)

        #print(image_data.instance_set.all()[0])


        coords.latitude = coords_data.get('latitude', coords.latitude)
        coords.longitude = coords_data.get('longitude', coords.longitude)
        coords.height = coords_data.get('height', coords.height)
        coords.save()

        level.winter = levels_data.get('winter', level.winter)
        level.summer = levels_data.get('summer', level.summer)
        level.autumn = levels_data.get('autumn', level.autumn)
        level.spring = levels_data.get('spring', level.spring)
        if Level.objects.filter(winter=levels_data['winter'],
                                summer=levels_data['summer'],
                                autumn=levels_data['autumn'],
                                spring=levels_data['spring']
                                ).exists():
            instance.level = Level.objects.get(winter=levels_data['winter'],
                                               summer=levels_data['summer'],
                                                 autumn=levels_data['autumn'],
                                                 spring=levels_data['spring']
                                      )
            instance.level.save()
        else:
            instance.level = Level.objects.create(winter=levels_data['winter'],
                                                  summer=levels_data['summer'],
                                                  autumn=levels_data['autumn'],
                                                  spring=levels_data['spring'])
            instance.level.save()


        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get("connect", instance.connect)
        instance.save()
        return instance

class PerevalSubmitDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'