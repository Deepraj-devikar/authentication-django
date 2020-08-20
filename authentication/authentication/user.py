from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class RegisterUser(APIView):
    """
    create a new user.
    """
    def post(self, request, format=None):
    	data=request.data
    	user = User.objects.create_user(data['username'], data['email'], data['password'])
    	user.last_name = data['last_name']
    	user.save()
    	token = Token.objects.create(user=user)
    	print(token.key)
    	return Response({'msg' : 'success', 'token': token.key}, status=status.HTTP_201_CREATED)

class LoginUser(APIView):
    """
    log in user.
    """
    def post(self, request, format=None):
    	data=request.data
    	user = authenticate(username=data['username'], password=data['password'])
    	if user is not None:
    		token = Token.objects.get(user=user)
    		print(token.key)
    		return Response({'msg' : 'success', 'token': token.key}, status=200)
    	else:
    		return Response({'msg' : 'not success'}, status=401)

class UserInfo(APIView):
    """
    if user login.
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
    	user = request.user
    	print(user)
    	userInfo = User.objects.get(username = user)
    	print(userInfo.email)
    	print(userInfo.email, userInfo.username, userInfo.last_name)
    	if userInfo is not None:
    		info = {
    			'email': userInfo.email,
    			'name' : userInfo.username,
    			'last_name' : userInfo.last_name,
    		}
    		return Response({'msg' : 'success', 'user': info}, status=status.HTTP_201_CREATED)
    	else:
    		return Response({'msg' : 'not success'}, status=Http404)