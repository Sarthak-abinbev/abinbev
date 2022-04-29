# Create your views here.
from itertools import count
import json
from django.shortcuts import render

from django.db import transaction, IntegrityError

# Create your views here.
# todo/todo_api/views.py
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import ExperimentRepo#,Experimentcount
from .models import SuccessMetric
from .models import GroupDetails, Factor, Levels, Constraints, ScopeFilters

from .serializers import ExperimentRepoSerializer, SuccessMetricSerializer, GroupDetailsSerializer, FactorSerializer, LevelsSerializer,ExperimentCountSerializer
from .serializers import ConstraintsSerializer, ScopeFiltersSerializer

#from rest_framework.decorators import authentication_classes, permission_classes
from django.db import connection
from django.conf import settings
from rest_framework.renderers import JSONRenderer


class ExperimentRepoView(APIView):
    queryset = ExperimentRepo.objects.count()
    print (queryset)

    #authentication_classes = [] #disables authentication
    #permission_classes = [] #disables permission
    permission_classes = [permissions.IsAuthenticated]
    @transaction.atomic
    def post(self, request):
        serializer = ExperimentRepoSerializer(data=request.data)
        #serializeGroup = GroupDetailsSerializer(data=request.data.groupDetail)
       
        serializer11 = serializer
        experimentIdData ="0"
        #try:
        if serializer.is_valid():
                    
                    current_user = request.user
                    
                    serializerNew = ExperimentRepo(experimentName=serializer.data["experimentName"], measurementStartDate=serializer.data["measurementStartDate"], measurementEndDate=serializer.data["measurementEndDate"], 
                    testStartDate=serializer.data["testStartDate"], testEndDate=serializer.data["testEndDate"], referenceEndDate=serializer.data["referenceEndDate"], referenceStartDate=serializer.data["referenceStartDate"], hypothesis=serializer.data["hypothesis"], numberOfGroups=serializer.data["numberOfGroups"],
                    isCostAssociated=serializer.data["isCostAssociated"], experimentOwnerId_id = current_user.id, productGranularityMasterId_id=serializer.data["productGranularityMasterId"], spacialGranularityMasterId_id=serializer.data["spacialGranularityMasterId"], marketMasterId_id =serializer.data["marketMasterId"])
                    
                    
                    serializerNew.save()
                                
                    groupList = json.loads(request.data["groupDetail"])

                    
                    batchGroupList = [GroupDetails(groupName=row['groupName'], groupDescription=row['groupDescription'],
                    costPerExperiment=row['costPerExperiment'], percentageAllocation=row['percentageAllocation'],
                    isControlGroup=row['isControlGroup'], expRepoId=serializerNew) for row in groupList]
                    
                    GroupDetails.objects.bulk_create(batchGroupList)
                    
                    successMetricList = json.loads(request.data["successMetricList"])
                    batchSuccessMetricList = [SuccessMetric(measureMasterId_id=row['measureMasterId'], expRepoId=serializerNew) for row in successMetricList]
                    SuccessMetric.objects.bulk_create(batchSuccessMetricList)
                    
                    
                    factorList = json.loads(request.data["factorList"])
                    

                    for factor in factorList:
                        print(factor)
                        factorName = factor["factorName"]
                        serializerFactor = FactorSerializer(data=factor)
                        
                        objFactor = Factor(factorName=factorName, expRepoId=serializerNew)
                        objFactor.save()
                        levelListJson =factor["levelList"]
                        
                        
                        levelList = levelListJson
                        batchLevelList = [Levels(levelName=row['levelName'], levelDescription=row['levelDescription'],
                        levelCost=row['levelCost'], levelPercentageAssign=row['levelPercentageAssign'],
                        isControlGroup=row['isControlGroup'], factorId=objFactor) for row in levelList]
                        Levels.objects.bulk_create(batchLevelList)
                    
                    constraintList = json.loads(request.data["constraintList"])
                    batchConstraintList = [Constraints(constraintMasterId_id=row['constraintMasterId'], expRepoId=serializerNew) for row in constraintList]
                    Constraints.objects.bulk_create(batchConstraintList)

                    scopeList = json.loads(request.data["scopeList"])
                    batchScopeList = [ScopeFilters(scopeFilterMasterId_id=row['scopeFilterMasterId'], expRepoId=serializerNew, scopeFilterValue=row['scopeFilterValue'],scopeFilterOperator=row['scopeFilterOperator'],
                    scopeFilterOperation=row['scopeFilterOperation'],isFirstSelected=row['isFirstSelected']) for row in scopeList]
                    ScopeFilters.objects.bulk_create(batchScopeList)
                    return Response({"status": "success", "data": serializer11.data, "code":"200", "message":"SUCCESS"}, status=status.HTTP_200_OK) 
        else:
            return Response({"status": "error", "data": serializer.errors, "code":"40022", "message":"Some error in input"}, status=status.HTTP_400_BAD_REQUEST)
       

''''
class ExperimentRepoCount(APIView):

    #authentication_classes = [] #disables authentication
    #permission_classes = [] #disables permission
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):

            experimentcount = ExperimentRepo.objects.all().count()
            #experimentcount = ExperimentRepo.objects.annotate(lead_count=count('isActive',filter=Q(status="1")))
            serializer3 = ExperimentRepoSerializer(experimentcount, many=True)
            return Response({'data':serializer3.data,'code':'200','message':'SUCCESS'}, status=status.HTTP_200_OK)

class UserCountView(APIView):
    """
    A view that returns the count of active users.
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        user_count = User.objects.count()
        content = {'user_count': user_count}
        return Response(content)

        @api_view(['GET'])
@renderer_classes([JSONRenderer])
def user_count_view(request, format=None):
    """
    A view that returns the count of active users in JSON.
    """
    user_count = User.objects.filter(active=True).count()
    content = {'user_count': user_count}
    return Response(content)

class CountCViewSet(APIView):
     #renderer_classes = [JSONRenderer]
    
     def get_count(request):
        queryset = ExperimentRepo.objects.count()
        #serializer_class = ExperimentCountSerializer
        content = {'user_count': queryset}
       
        if request == 'GET':

            return render(request,content)
'''''''''''

class TotalExperiment(APIView):
    def get(self, request, format=None):
        Total_exp_count = ExperimentRepo.objects.count()
        exp_count_inprogress = ExperimentRepo.objects.filter(status='InProgress').count()
        content = {'Total exp_count': Total_exp_count}
        #content2 = {'Total InProgress exp_count': exp_count_inprogress}
        return Response(content)
        #return Response(content2)
        #return Response(content)


class TotalInProgressExperiment(APIView):
    def get(self, request, format=None):
        exp_count_inprogress = ExperimentRepo.objects.filter(status='InProgress').count()
        content2 = {'Total InProgress exp_count': exp_count_inprogress}
        return Response(content2)

class TotalInProgressExperiment(APIView):
    def get(self, request, format=None):
        exp_count_inprogress = ExperimentRepo.objects.filter(status='InProgress').count()
        content2 = {'Total InProgress exp_count': exp_count_inprogress}
        return Response(content2)

class TotalNotStartedExperiment(APIView):
    def get(self, request, format=None):
        exp_count_NotStarted = ExperimentRepo.objects.filter(status='Not Started').count()
        content2 = {'Total Not Started exp_count': exp_count_NotStarted}
        return Response(content2)     

class TotalCompletedExperiment(APIView):
    def get(self, request, format=None):
        exp_count_Completed = ExperimentRepo.objects.filter(status='Completed').count()
        content2 = {'Total Completed exp_count': exp_count_Completed}
        return Response(content2)                
