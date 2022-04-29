
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

class MarketMaster(models.Model):
    marketName = models.CharField(max_length = 180)
    marketCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task     

class MeasureMaster(models.Model):
    measureName = models.CharField(max_length = 180)
    measureCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    
    def __str__(self):
        return self.task    


class ScopeMaster(models.Model):
    scopefilterName = models.CharField(max_length = 180)
    scopefilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    #updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)  
    
    
    def __str__(self):
        return self.task   

class OperatorMaster(models.Model):
    operatorName = models.CharField(max_length = 180)
    #operatorCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    #updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True) 
    scopeMasterid = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True) 
    
    def __str__(self):
        return self.task       




class ValueMaster(models.Model):
    valuefilterName = models.CharField(max_length = 180)
    valuefilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True) 
    scopeMasterid = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True) 
    
    def __str__(self):
        return self.task   


class ProductgranularityMaster(models.Model):
    productgranularityfilterName = models.CharField(max_length = 180)
    productgranularityfilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    #updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True) 
    #scopeMasterid = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True) 
    
    def __str__(self):
        return self.task 


class SpacialgranularityMaster(models.Model):
    spacialgranularityfilterName = models.CharField(max_length = 180)
    spacialgranularityfilterCode = models.CharField(max_length = 10)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    #updatedBy   = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True) 
    #scopeMasterid = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True) 
    
    def __str__(self):
        return self.task 





