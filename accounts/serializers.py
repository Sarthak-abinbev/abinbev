from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
#from django.contrib.auth.models import User
#from django.contrib.accounts.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth import get_user_model
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        #  token['username'] = user.username
        #token['username'] = user.email
        token['email'] = user.email
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    first_name = serializers.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('first_name','password', 'password2', 'email', 'countryId', 'roleId', 'businessFuncId')
        
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            #username=validated_data['username'],
            #username=validated_data['email'],
            email=validated_data['email'],
            #,
            first_name =validated_data['first_name'],
            countryId=validated_data['countryId'],
            roleId=validated_data['roleId'],
            businessFuncId=validated_data['businessFuncId']
            
        )

        user.set_password(validated_data['password'])
        user.save()

        return user