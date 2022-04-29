from django.db import models

# Create your models here.
#from django.db import models

# todo/todo_api/models.py
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class CountryMaster(models.Model):
    countryName = models.CharField(max_length = 180)
    countryCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task

class BusinessFuncMaster(models.Model):
    businessFuncName = models.CharField(max_length = 180)
    businessFuncCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task

class RoleMaster(models.Model):
    roleName = models.CharField(max_length = 180)
    roleCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task

class ScopeMaster(models.Model):
    scopeFilterName = models.CharField(max_length = 180)
    scopeFilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    #updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)  
    
    
    def __str__(self):
        return self.task

class ValueMaster(models.Model):
    valueFilterName = models.CharField(max_length = 180)
    valueFilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True) 
    scopeMasterid = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True) 
    
    def __str__(self):
        return self.task

class ProductGranularityMaster(models.Model):
    productGranularityfilterName = models.CharField(max_length = 180)
    productGranularityfilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    #updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True) 
    #scopeMasterid = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True) 
    
    def __str__(self):
        return self.task 


class SpacialGranularityMaster(models.Model):
    spacialGranularityfilterName = models.CharField(max_length = 180)
    spacialGranularityfilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    #updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True) 
    #scopeMasterid = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True) 
    
    def __str__(self):
        return self.task

class MarketMaster(models.Model):
    marketName = models.CharField(max_length = 180)
    marketCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    
    def __str__(self):
        return self.task     

class MeasureMaster(models.Model):
    measureName = models.CharField(max_length = 180)
    measureCode = models.CharField(max_length = 10)
    marketMasterId = models.ForeignKey(MarketMaster,on_delete = models.CASCADE, blank=True,null=True)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    marketMasterId = models.ForeignKey(MarketMaster,on_delete = models.CASCADE, blank=True,null=True)
    def __str__(self):
        return self.task

class ConstraintMaster(models.Model):
    constraintName = models.CharField(max_length = 180)
    constraintCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    
    def __str__(self):
        return self.task