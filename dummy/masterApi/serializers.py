from rest_framework import serializers
from .models import CountryMaster
from .models import (
    MarketMaster , MeasureMaster , OperatorMaster , ScopeMaster ,ValueMaster,ProductgranularityMaster,SpacialgranularityMaster
    )
from .models import RoleMaster
from .models import BusinessFuncMaster
class CountryMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryMaster
        fields = ["countryName", "countryCode","id"]

class RoleMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleMaster
        fields = ["roleName", "roleCode","id"]

class BusinessFuncMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessFuncMaster
        fields = ["businessFuncName", "businessFuncCode","id"]

class Marketmasterserializer(serializers.ModelSerializer):
    class Meta:
       model = MarketMaster
       fields = ["marketName","marketCode","id"]        

class Measuremasterserializer(serializers.ModelSerializer):
    class Meta:
       model = MeasureMaster
       fields = ["measureName","measureCode","id"]  


class Scopemasterserializer(serializers.ModelSerializer):
    class Meta:
       model = ScopeMaster
       fields = ["scopefilterName","scopefilterCode","id"]        


class Operatoremasterserializer(serializers.ModelSerializer):
    class Meta:
       model = OperatorMaster
       fields = ["operatorName","id"]            

class Valuemasterserializer(serializers.ModelSerializer):
    class Meta:
       model = ValueMaster
       fields = ["valuefilterName","valuefilterCode","id"]  


class Productgranularitymasterserializer(serializers.ModelSerializer):
    class Meta:
       model = ProductgranularityMaster
       fields = ["productgranularityfilterName","productgranularityfilterCode","id"]


class Spacialgranularitymasterserializer(serializers.ModelSerializer):
    class Meta:
       model = SpacialgranularityMaster
       fields = ["spacialgranularityfilterName","spacialgranularityfilterCode","id"]