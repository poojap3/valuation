from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class VAppSerializer(serializers.Serializer):

    class Meta:
        model=VApp
        fields="__all__"


class SiteVisitSerializer(serializers.Serializer):

    class Meta:
        model=SiteVisit
        fields="__all__"



class RoleRefSerializer(serializers.Serializer):

    class Meta:
        model=RoleRef
        fields="__all__"



# class BankSubmissionSerializer(serializers.Serializer):
#
#         class Meta:
#             model=BankSubmission
#             fields="__all__"




class FieldReportSerializer(serializers.Serializer):

        class Meta:
            model=FieldReport
            fields="__all__"




class IssueSerializer(serializers.Serializer):

    class Meta:
        model=Issue
        fields="__all__"




class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields ="__all__"



class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
