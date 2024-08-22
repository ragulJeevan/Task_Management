from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_management.models import User
from user_management.serializers import UserSerializer
from user_management.common.utils import api_response, api_error_response
from django.http import Http404

modelName = "User"

class UserList(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return api_response(serializer.data, modelName, 'get')
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'save')
            return api_error_response(serializer.errors)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            user = self.get_object(pk)
            serializer = UserSerializer(user)
            return api_response(serializer.data, modelName, 'get')
        except Http404:
            return api_error_response(["User not found"], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            user = self.get_object(pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return api_response(serializer.data, modelName, 'update')
            return api_error_response(serializer.errors)
        except Http404:
            return api_error_response(["User not found"], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            user = self.get_object(pk)
            user.delete()
            return api_response('', modelName, 'delete',status.HTTP_204_NO_CONTENT)
        except Http404:
            return api_error_response(["User not found"], status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return api_error_response([str(e)], status.HTTP_500_INTERNAL_SERVER_ERROR)
