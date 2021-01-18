from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'username',
            'phone',
            'city',
            'avatar',
        ]


class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password2', 'email', 'city', 'phone', 'avatar', ]

    def save(self, *args, **kwargs):
        user = CustomUser(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            city=self.validated_data['city'],
            avatar=self.validated_data['avatar'],
            phone=self.validated_data['phone'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user

