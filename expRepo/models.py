from msilib.schema import Class
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#from django.db import models

# todo/todo_api/models.py
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

from masterApi.models import MeasureMaster, ConstraintMaster, ScopeMaster, SpacialGranularityMaster, ProductGranularityMaster

class ExperimentRepo(models.Model):

    experimentId = models.AutoField(primary_key= True)
    experimentName = models.CharField(unique= True,max_length= 100,null= False,blank= False)
    experimentOwnerId = models.ForeignKey(User,on_delete=models.CASCADE,blank= False,null= False)
    marketMasterId = models.ForeignKey(MeasureMaster,on_delete=models.CASCADE,blank= False,null= False)
    spacialGranularityMasterId = models.ForeignKey(SpacialGranularityMaster,on_delete=models.CASCADE,blank= False,null= False)
    productGranularityMasterId = models.ForeignKey(ProductGranularityMaster,on_delete=models.CASCADE,blank= False,null= False)
    status = models.CharField(max_length= 100,null= False,blank= False)
    measurementStartDate = models.DateField()
    measurementEndDate = models.DateField()
    testStartDate = models.DateField()
    testEndDate = models.DateField()
    referenceEndDate = models.DateField()
    referenceStartDate = models.DateField()
    hypothesis = models.CharField(max_length= 100)
    numberOfGroups = models.PositiveIntegerField(blank= False,null= False)
    isCostAssociated = models.BooleanField(default= False, blank=True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    createdAt   = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True) 

    def __str__(Self) :
        return Self.task




class SuccessMetric(models.Model):

    successMetricId = models.AutoField(primary_key= True)
    measureMasterId = models.ForeignKey(MeasureMaster,on_delete = models.CASCADE, blank=True,null=True) 
    expRepoId = models.ForeignKey(ExperimentRepo,on_delete = models.CASCADE, blank=True,null=True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.task

class GroupDetails(models.Model):

    groupDetailsId = models.AutoField(primary_key= True)
    expRepoId = models.ForeignKey(ExperimentRepo,on_delete = models.CASCADE, blank=True,null=True)
    groupName = models.CharField(max_length= 200,null= False,blank= False)
    groupDescription = models.CharField(max_length= 400,null= False,blank= False)
    costPerExperiment = models.PositiveIntegerField(blank= False,null= False)
    percentageAllocation = models.PositiveIntegerField(blank= False,null= False)
    isControlGroup    = models.BooleanField(default = False, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.task

class Factor(models.Model):

    factorId = models.AutoField(primary_key= True)
    expRepoId = models.ForeignKey(ExperimentRepo,on_delete = models.CASCADE, blank=True,null=True)
    factorName = models.CharField(max_length= 200,null= False,blank= False)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.task

class Levels(models.Model):

    levelId = models.AutoField(primary_key= True)
    expRepoId = models.ForeignKey(ExperimentRepo,on_delete = models.CASCADE, blank=True,null=True)
    levelName = models.CharField(max_length= 200,null= False,blank= False)
    levelDescription = models.CharField(max_length= 400,null= False,blank= False)
    levelCost = models.PositiveIntegerField(blank= False,null= False)
    levelPercentageAssign = models.PositiveIntegerField(blank= False,null= False)
    isControlGroup    = models.BooleanField(default = False, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)
    factorId = models.ForeignKey(Factor,on_delete = models.CASCADE, blank=True,null=True)
    
    def __str__(self):
        return self.task


class Constraints(models.Model):
    constraintId = models.AutoField(primary_key= True)
    expRepoId = models.ForeignKey(ExperimentRepo,on_delete = models.CASCADE, blank=True,null=True)
    constraintMasterId = models.ForeignKey(ConstraintMaster,on_delete = models.CASCADE, blank=True,null=True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)

    def __str__(Self) :
        return Self.task

class ScopeFilters(models.Model):
    scopeFilterId = models.AutoField(primary_key= True)
    expRepoId = models.ForeignKey(ExperimentRepo,on_delete = models.CASCADE, blank=True,null=True)
    scopeFilterMasterId = models.ForeignKey(ScopeMaster,on_delete = models.CASCADE, blank=True,null=True)
    scopeFilterValue = models.CharField(max_length= 200,null= False,blank= False)
    scopeFilterOperator = models.CharField(max_length= 200,null= False,blank= False)
    scopeFilterOperation = models.CharField(max_length= 200,null= False,blank= False)
    isFirstSelected = models.BooleanField(default = False, blank = True)
    isActive    = models.BooleanField(default = False, blank = True)
    isDelete    = models.BooleanField(default = False, blank = True)
    createdtime = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updatedtime = models.DateTimeField(auto_now = True, blank = True)

    def __str__(Self) :
        return Self.task
