from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_management.common.utils import api_response, api_error_response
from django.http import Http404
from foundation.models import Status
from foundation.serializers import StatusSerializer

modelName = "Status"

class status_list(APIView):
    def get(self, request):
         try:
             status = Status.objects.all()
             serializer = StatusSerializer(status, many=True)
             return api_response(serializer.data, modelName, 'get')
         except Exception as e:
             return api_error_response([str(e)])

    def post(self, request):   
        try:
            serializer = StatusSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'save')
            return api_error_response(serializer.errors)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

class status_detail(APIView):
    def get_object(self, pk):
        try:
            return Status.objects.get(pk=pk)
        except Status.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            status = self.get_object(pk)
            serializer = StatusSerializer(status)
            return api_response(serializer.data, modelName, 'get')
        except Http404:
            return api_error_response(["Status not found"])
        except Exception as e:
            return api_error_response([str(e)])

    def put(self, request, pk):
        try:
            status = self.get_object(pk)
            serializer = StatusSerializer(status, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'update')
            return api_error_response(serializer.errors)
        except Http404:
            return api_error_response(["Status not found"])
        except Exception as e:
            return api_error_response([str(e)])

    def delete(self, request, pk):
        try:
            status = self.get_object(pk)
            status.delete()
            return api_response('', modelName, 'delete')
        except Http404:
            return api_error_response(["Status not found"])
        except Exception as e:
            return api_error_response([str(e)])
