from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import *
from .models import *


class MyView(APIView):
	def get(self, request, format=None):
		message = {
			'Response': 200,
			'Message' : "Welcome to Django Rest Api"	
		}

		return Response(message)


class LearnView(generics.CreateAPIView):
	serializer_class = TestSerializers

	def get_queryset(self):
		# return Test.objects.filter(user=self.request.user, active=True)
		return Test.objects.all()

	def create(self, serializer):
		serializer = TestSerializers(data=self.request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LearnDetailView(APIView):
    #permission_classes = [IsAuthenticated]
  
    def get_object(self):
        try:
            return Test.objects.all()
        except Test.DoesNotExist:
            raise Http404

    def get(self):
        try:
            tests = self.get_object(request)
            serializer = TestSerializers(tests)
            return Response(serializer.data)
        except Test.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)




# class WeatherView(generics.CreateAPIView):
#     # permission_classes = [IsAuthenticated]
#     serializer_class = DemoSerializer

#     def create(self, request, *args, **kwargs):
#     	try:
#     		zip_code = request.data.get('name')
#     		city = request.data.get('city')
#     		age = request.data.get('age')
#     		return super().create(request, *args, **kwargs)
#     	except Exception as e:
#     		return Response ({
#     			"Message": "Failed"
#     			})