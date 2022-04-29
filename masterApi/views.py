
import json
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import CountryMaster, BusinessFuncMaster, RoleMaster, ValueMaster, ScopeMaster, MeasureMaster
from .serializers import CountryMasterSerializer, BusinessFuncMasterSerializer, RoleMasterSerializer, ScopeMasterSerializer, ValueMasterSerializer, MeasureMasterSerializer
#from rest_framework.decorators import authentication_classes, permission_classes
from django.db import connection
from django.conf import settings

class CountryMasterListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    
    def get(self, request, *args, **kwargs):
        
        try:
            countryMaster = CountryMaster.objects.filter(isActive = 1).filter(isDelete = 0)
            serializer = CountryMasterSerializer(countryMaster, many=True)
            businessFuncMaster = BusinessFuncMaster.objects.filter(isActive = 1).filter(isDelete = 0)
            serializer2 = BusinessFuncMasterSerializer(businessFuncMaster, many=True)
            roleMaster = RoleMaster.objects.filter(isActive = 1).filter(isDelete = 0)
            serializer3 = RoleMasterSerializer(roleMaster, many=True)

            return Response({'countryMaster':serializer.data,'businessFuncMaster':serializer2.data,'roleMaster':serializer3.data,'code':'200','message':'SUCCESSFULLY RECEIVED THE DATA'}, status=status.HTTP_200_OK)

        except:
            return Response({"status": "error", "data": "", "code":"404", "message":"Some error in input"}, status=status.HTTP_400_BAD_REQUEST)


class BusinessFuncMasterListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    
    
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        businessFuncMaster = BusinessFuncMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = BusinessFuncMasterSerializer(businessFuncMaster, many=True)
        return Response({'data':serializer.data,'code':'200','message':'SUCCESS'}, status=status.HTTP_200_OK)

class RoleMasterListApiView(APIView):
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
        roleMaster = RoleMaster.objects.filter(isActive = 1).filter(isDelete = 0)
        serializer = RoleMasterSerializer(roleMaster, many=True)
        return Response({'data':serializer.data,'code':'200','message':'SUCCESS'}, status=status.HTTP_200_OK)


class ScopeMasterListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, id=None):
        if id:
            item = ScopeMaster.objects.get(id=id)
            serializer = ScopeMasterSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ScopeMaster.objects.all().filter(isActive = 1).filter(isDelete = 0)
        serializer = ScopeMasterSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class ValueMasterListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    
    def get(self, request, id=None):
        dbName = settings.DATABASES['default']['NAME']
        if id:
             
            item = ValueMaster.objects.get(id=id).filter(isActive = 1).filter(isDelete = 0)
            serializer = ValueMasterSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = ValueMaster.objects.all().filter(isActive = 1).filter(isDelete = 0)
        serializer = ValueMasterSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class ValueMasterListbyScopeApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    #authentication_classes = [] #disables authentication
    #permission_classes = [] #disables permission
    permission_classes = [permissions.IsAuthenticated]
    # 1. List all
    def get(self, request, id=None):
        dbName = settings.DATABASES['default']['NAME']
        tbName = "scopefiltersmasterdatatb"

        if id:
    
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM "+dbName+"."+tbName+" where %s is Not null", [id])
                #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
                row = ValueMasterListbyJsonApiView.dictfetchall(cursor)
               
            return Response({"status": "success", "data": row, "code":200, "message":"success"}, status=status.HTTP_200_OK)

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM "+dbName+"."+tbName)
                rowAll = ValueFilterOperationsApiView.dictfetchall(cursor)
               
           
        return Response({"status": "success", "data": rowAll,"code":200, "message":"success"}, status=status.HTTP_200_OK)


class ValueMasterListbyJsonApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    #authentication_classes = [] #disables authentication
    #permission_classes = [] #disables permission
    # 1. List all
    permission_classes = [permissions.IsAuthenticated]

    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
                ]

    def post(self, request, id=None):
        
        try:
            data = request.data["scopeFilterList"]
            columnCode = request.data["scopeMasterCode"]
            
            dbName = settings.DATABASES['default']['NAME']
            tbName = "scopefiltersmasterdatatb"
            queryDb=""
            queryDbAnd = "SELECT "+columnCode+"  from "+dbName+"."+tbName+" where "
            queryDbOr =""
            data2 = json.loads(data)
            firstFlag = 0
            andFlag = 0
            scopeListFlag =0

            for scopeFilterInput in data2:
                scopeListFlag =1
                print(scopeFilterInput)
                scopeMasterCode1 = scopeFilterInput["scopeMasterCode"]
                operator1 = scopeFilterInput["operator"]
                operation1 = scopeFilterInput["operation"]
                value1 = scopeFilterInput["value"]

            

                if operator1 == "EQUALS":
                    operator1 = "="

                if operator1 == "GREATERTHAN":
                    operator1 = ">"

                if operator1 == "LESSTHAN":
                    operator1 = "<"

                '''
                if firstFlag == 0:
                    firstFlag = firstFlag+1
                    operation1 = "1"
                '''

                if operation1 == "0":
                    queryDbOr = queryDbOr+" Union SELECT "+columnCode+"  from "+dbName+"."+tbName+" where "+scopeMasterCode1+operator1+value1

                if operation1 == "1":
                    queryDbAnd = queryDbAnd+ scopeMasterCode1+operator1+value1 + " AND "
                    andFlag = 1
                

            if andFlag == 1:
                queryDbAnd = queryDbAnd[0:-4]
                queryDb = queryDbAnd + queryDbOr

            if andFlag == 0:
                queryDb = queryDbOr[6:]

            if scopeListFlag == 0:
                queryDb = "Select "+columnCode+"  from "+dbName+"."+tbName

            with connection.cursor() as cursor:
                cursor.execute(queryDb)
                #cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
                #rowNew = cursor.fetchall()
                rowNew = ValueMasterListbyJsonApiView.dictfetchall(cursor)
                #return row
        
        
            return Response({"status": "success", "scopeFilterValue":rowNew, "code":200, "message":"success"}, status=status.HTTP_200_OK)

        except:
            return Response({"status": "error", "data": "", "code":"400", "message":"Some error in input"}, status=status.HTTP_400_BAD_REQUEST)


class MeasureMasterListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [].
    authentication_classes = [] #disables authentication
    permission_classes = [] #disables permission
    # 1. List all
    def get(self, request, marketMasterId=None):
        try:

            if marketMasterId:
                #item = MeasureMaster.objects.get(marketMasterId=marketMasterId)
                item = MeasureMaster.objects.all().filter(isActive = 1).filter(isDelete = 0).filter(marketMasterId = marketMasterId)
                serializer = MeasureMasterSerializer(item, many=True)
                return Response({"status": "success", "data": serializer.data, "code":"200","message":"success"}, status=status.HTTP_200_OK)

            items = MeasureMaster.objects.all().filter(isActive = 1).filter(isDelete = 0)
            serializer = MeasureMasterSerializer(items, many=True)
            return Response({"status": "success", "data": serializer.data, "code":"200","message":"success"}, status=status.HTTP_200_OK)
        
        except:
            return Response({"status": "error", "data": "", "code":"400", "message":"Some error in input"}, status=status.HTTP_400_BAD_REQUEST)
