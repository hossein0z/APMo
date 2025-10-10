from User.models import Abs_User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = Abs_User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Abs_User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


