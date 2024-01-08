from django.shortcuts import render
from .models import Blog
from .serializer import BlogSerializer
from rest_framework import mixins, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class BlogView(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'id'
    
    def get(self,request,id):
        if id:
            return self.retrieve(request,id)
        try:
            return self.list(request)
        except Exception as e:
            return Response(data=str(e),status=403) 

    def put(self,request,id):
        try:
            return self.update(request,id)
        except Exception as e:
            return Response(data=str(e),status=403) 
    
    def delete(self,request,id):
        try:
           return self.destroy(request,id)
        except Exception as e:
            return Response(data=str(e),status=403) 
    
class BlogDetailView(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get(self,request):
        try:
            return self.list(request)
        except Exception as e:
            return Response(data=str(e),status=403) 
            
    def post(self,request):
        response={}
        try:
            return self.create(request)
        except Exception as e:
            response['data']=str(e)
            response['status']=403
        return Response(response)
        
        
