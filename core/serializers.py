from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "password", "email", 'user_type', "first_name", "last_name"]


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'user_type', 'first_name', 'last_name']