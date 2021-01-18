from rest_framework import serializers
from .models import Images, Product, Sex, Brand, Material, ZipType


class SexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sex
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = "__all__"


class ZipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipType
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user')
    sex_name = serializers.CharField(source='sex')
    corpus_material_name = serializers.CharField(source='corpus_material')
    bezel_material_name = serializers.CharField(source='bezel_material')
    zip_type_name = serializers.CharField(source='zip_type')


    class Meta:
        model = Product
        fields = [
            'id',
            'user_username',
            'name',
            'id_number',
            'description',
            'price',
            'year',
            'sex_name',
            'brand_name',

            # Калибр
            'caliber',
            'base_caliber',
            'cruising_range',

            # Корпус
            'corpus_material_name',
            'back_cap',
            'jewelry',

            # Циферблат и стрелки
            'spraying',
            'dial1',
            'dial2',
            'dial3',


            # Браслет
            'bracer_name',
            'zip_type_name',
            'zip_material_name',

            # Функции
            'chronograf',
            'calendar_on_4_years',
            'alarm_clock',
            'month_indicator',
            'year_calendar',
            'eternal_calendar',
            'gmt',
            'jump_hour',
        ]


class ProductSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Images
        fields = [
            'id',
            'ad',
            'image',
        ]


class PropertiesSerializers(serializers.Serializer):
    sex = SexSerializer(read_only=True, many=True)
    brand = BrandSerializer(read_only=True, many=True)
    material = MaterialSerializer(read_only=True, many=True)
    zip_type = ZipTypeSerializer(read_only=True, many=True)
