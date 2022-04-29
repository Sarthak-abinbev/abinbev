from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import (
    CountryMaster , MeasureMaster , MarketMaster , OperatorMaster,ScopeMaster,ValueMaster,ProductgranularityMaster,SpacialgranularityMaster
)
from .models import BusinessFuncMaster
from .models import RoleMaster
from .serializers import CountryMasterSerializer
from .serializers import BusinessFuncMasterSerializer
from .serializers import (
    RoleMasterSerializer , Marketmasterserializer,Measuremasterserializer,Operatoremasterserializer,Scopemasterserializer,Valuemasterserializer,Productgranularitymasterserializer,Spacialgranularitymasterserializer
)
#from rest_framework.decorators import authentication_classes, permission_classes


class CountryMasterListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        countryMaster = CountryMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = CountryMasterSerializer(countryMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BusinessFuncMasterListApiView(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = [] 
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        BusinessFuncMaster = BusinessFuncMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = BusinessFuncMasterSerializer(BusinessFuncMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RoleMasterListApiView(APIView):
    authentication_classes = [] #disables authentication
    permission_classes = []
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        RoleMaster =RoleMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = RoleMasterSerializer(BusinessFuncMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Marketmasterlistapiview(APIView):
   # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        marketMaster = MarketMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = Marketmasterserializer(marketMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Measuremasterlistapiview(APIView):
   # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        measureMaster = MeasureMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = Measuremasterserializer(measureMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 


class Scopemasterlistapiview(APIView):
   # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        scopefilterMaster = ScopeMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = Scopemasterserializer(scopefilterMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




class Operatormasterlistapiview(APIView):
   # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        operatorMaster = OperatorMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = Operatoremasterserializer(operatorMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Valuefiltermasterlistapiview(APIView):
   # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        valuefilterMaster = ValueMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        #valuefilterMaster = ValueMaster.objects.get(id = ScopeMaster['id'])
        serializer = Valuemasterserializer(valuefilterMaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Prgranularitymasterlistapiview(APIView):
   # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        productgranularitymaster = ProductgranularityMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = Productgranularitymasterserializer(productgranularitymaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Spacialgrmasterlistapiview(APIView):
   # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        spacialgranularitymaster = SpacialgranularityMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = Spacialgranularitymasterserializer(spacialgranularitymaster, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)









        # 2. Create
        '''
        def post(self, request, *args, **kwargs):
        '''
        #Create the Todo with given todo data
        '''
        data = {
            'task': request.data.get('task'), 
            'completed': request.data.get('completed'), 
            'user': request.user.id
        }
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        '''