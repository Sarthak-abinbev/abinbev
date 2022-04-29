from rest_framework import serializers
from .models import CountryMaster

from .models import RoleMaster, MeasureMaster, MarketMaster
from .models import BusinessFuncMaster
from .models import ScopeMaster, ValueMaster
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

class ScopeMasterSerializer(serializers.ModelSerializer):
    class Meta:
       model = ScopeMaster
       fields = ["scopeFilterName","scopeFilterCode","id"]

class ValueMasterSerializer(serializers.ModelSerializer):
    class Meta:
       model = ValueMaster
       fields = ["valueFilterName","valueFilterCode","id","scopeMasterid"]

class MeasureMasterSerializer(serializers.ModelSerializer):
    class Meta:
       model = MeasureMaster
       fields = ["measureName","measureCode","id","marketMasterId"] 

