#APIVIEW


from django.shortcuts import render
from .models import Products
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





class ProductView(APIView):
    

    def post(self,request):
        serializer=ProductSerializer()
        if request.method=='POST':
            serializer=ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                pname=serializer.data.get('pname')  #get pname from serializer
                request.session['pr']=pname    #pname set in session storage
                d=request.session.get('pr')    #for get pname stored in p
                print('session data is:',d)
                request.session.clear()         #for clearing session storage
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self,request):
        pro=Products.objects.all()
        serializer=ProductSerializer(pro,many=True)
       
        return Response(data=serializer.data,status=status.HTTP_202_ACCEPTED)
    
    
    def put(self,request,pk):
        p=Products.objects.get(pid=pk)
        serializer=ProductSerializer(p,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)
    
    def patch(self,request,pk):
        p=Products.objects.get(pid=pk)
        serializer=ProductSerializer(p,partial=True,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)
    

    def delete(self,request,pk):
        p=Products.objects.get(pid=pk)
        p.delete()
        return Response(status=status.HTTP_200_OK)
'''  


#Viewsets
from . models import Products
from . serializers import ProductSerializer
from rest_framework import viewsets

'''

        