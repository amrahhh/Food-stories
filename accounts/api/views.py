from django.contrib.auth import login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from accounts.api.serializers import UserLoginSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)
        user_serializer = UserLoginSerializer(user)
        
        return Response(user_serializer.data, )
