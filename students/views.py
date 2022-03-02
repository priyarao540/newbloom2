from urllib import response
from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import *
from .models import *

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
# Create your views here.
def home(request):
    obj = Books.objects.all()
    print(obj)
    print(obj[0].name)
    return HttpResponse(obj)

class BookViewSet(ModelViewSet):
    serializer_class   = BookSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return Books.objects.all()



class RegisterAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes =(AllowAny,)


    def post(self,request):
        user = request.data
        serializer = RegisterSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        print(user_data)
        return Response({"status":"success","message":"User Registered Successfully"},status=status.HTTP_201_CREATED)





