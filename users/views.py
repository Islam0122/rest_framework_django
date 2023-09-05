from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from . import serializers
from .models import ConfirmationCode
from rest_framework.viewsets import ModelViewSet, generics

'''registration_user'''
# @api_view(['POST'])
# def registration_user_api_view(request):
#     serializer = serializers.UserRegistrationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(data=serializer.data, status=201)
'''registration_user -> cvb -> MODELVIEWSET'''


class Registration_userViewSet(ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)


'''confirm_user_api_view'''
# @api_view(['POST'])
# def confirm_user_api_view(request):
#     code = request.data.get('code')
#     try:
#         confirmation_code = ConfirmationCode.objects.get(code=code)
#         if confirmation_code.is_expired():
#             return Response(data={"error": "Confirmation code has expired. Please register again."}, status=400)
#         user = confirmation_code.user
#         user.is_active = True
#         user.save()
#         return Response(data={"message": "User successfully confirmed."}, status=200)
#     except ConfirmationCode.DoesNotExist:
#         return Response(data={"error": "Invalid confirmation code."}, status=400)
'''confirm_user_api_view -> cbv -> '''


class confirm_userViewPost(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        code = request.data.get('code')
        try:
            confirmation_code = ConfirmationCode.objects.get(code=code)
            if confirmation_code.is_expired():
                return Response(data={"error": "Confirmation code has expired. Please register again."}, status=400)
            user = confirmation_code.user
            user.is_active = True
            user.save()
            return Response(data={"message": "User successfully confirmed."}, status=200)
        except ConfirmationCode.DoesNotExist:
            return Response(data={"error": "Invalid confirmation code."}, status=400)


'''login_user_api_view'''
# @api_view(['POST'])
# def login_user_api_view(request):
#     serializer = serializers.UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = authenticate(**serializer.validated_data)
#     if user:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})
#     return Response(status=401, data={'error': 'Invalid credentials'})

'''login_user_api_view -> cvb -> MODELVIEWSET '''


class login_userViewSet(ModelViewSet):
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(status=401, data={'error': 'Invalid credentials'})
