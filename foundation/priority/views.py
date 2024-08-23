from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from foundation.models import Priority
from foundation.serializers import PrioritySerializer
from user_management.common.utils import api_response, api_error_response
from django.http import Http404

modelName = "Priority"
notFound = "Priority not found"
ModelName = Priority
SerializerName = PrioritySerializer


class PriorityList(APIView):
    def get(self, request):
         try:
             requestData = ModelName.objects.all()
             serializer = SerializerName(requestData, many=True)
             return api_response(serializer.data, modelName, 'get')
         except Exception as e:
             return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):   
        try:
            serializer = SerializerName(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'save')
            return api_error_response(serializer.errors)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

class PriorityDetail(APIView):
    def get_object(self, pk):
        try:
            return ModelName.objects.get(pk=pk)
        except ModelName.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            requestData = self.get_object(pk)
            serializer = SerializerName(requestData)
            return api_response(serializer.data, modelName, 'get')
        except Http404:
            return api_error_response([notFound], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            requestData = self.get_object(pk)
            serializer = SerializerName(requestData, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'update')
            return api_error_response(serializer.errors)
        except Http404:
            return api_error_response([notFound], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            requestData = self.get_object(pk)
            requestData.delete()
            return api_response('', modelName, 'delete',status.HTTP_204_NO_CONTENT)
        except Http404:
            return api_error_response([notFound], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)
