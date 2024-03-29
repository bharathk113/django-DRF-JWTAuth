from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    # username = serializers.CharField(
    #         max_length=150,required=True,
    #         validators=[UniqueValidator(queryset=User.objects.all())]
    #         )
    # password = serializers.CharField(max_length=128,min_length=8, write_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'],validated_data['first_name'],validated_data['last_name'])
        return user

    class Meta:
        model = User
        fields = ('id','email','first_name','last_name')
class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            max_length=150,required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    token = serializers.CharField(max_length=1000,required=True,write_only=True)
    password = serializers.CharField(max_length=128,min_length=8, write_only=True)
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=150)
    def send_token(self,validated_data):
        tokenstr=self.token
        return tokenstr
    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], email= validated_data['email'],first_name= validated_data['first_name'],last_name=validated_data['last_name'],password=validated_data['password'])
    #     return user
    class Meta:
        model = User
        fields = ('id','email','first_name','last_name','password','username','token')
