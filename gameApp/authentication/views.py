from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from authentication.serializers import UserSerializer,UserCreateSerializer
from django.contrib.auth.models import User
import jwt,json
from django.core.mail import send_mail
import rest_framework.permissions as permissions
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
class UserRegister(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            data = { "email" : serializer.data["email"], "first_name" : serializer.data["first_name"], "last_name" : serializer.data["last_name"] } # Some unique field for reference
            secret_key = "GAMEAPPISFUNNY"
            algorithm = "HS256" # You can use MD5 or whatever you want
            token_code_data=jwt.encode(data, secret_key, algorithm)
            url = 'http://192.168.0.103:8080/user_register/confirm/'+token_code_data.decode('utf-8')
            # # user = serializer.save()
            # if user:
            #     # token = Token.objects.create(user=user)
            #     # json = serializer.data
            #     # json['token'] = token.key
            #     return Response("User Registration Completed but Pending for Verification", status=status.HTTP_201_CREATED)
            try:
                send_mail('Verificaion link for Game App', url, 'bharathreddyk113@gmail.com', [serializer.data["email"]])
            except:
                return Response("Please try again later after some time/Report here @ bharathkadapala@gmail.com", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response("User Registration Completed but Pending for Verification", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class UserCreate(APIView):
#     def post(self, request, format='json'):
#         serializer = UserCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             user_instance = serializer.save()
#             secret_key = "GAMEAPPISFUNNY"
#             algorithm = "HS256"
#             print (serializer.data)
#             token_decoded_data=jwt.decode(serializer.data["token"], secret_key, algorithm)
#             if token_decoded_data["email"]==serializer.data["email"]:
#                 user_instance.save()
#                 return Response("User Registration And Activation Successful", status=status.HTTP_200_OK)
#             else:
#                 return Response("Please Register Again. Looks like a bot request", status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def UserConfirm(request,user_id):
    if request.method == 'GET':
        try:
            info=jwt.decode(user_id,'GAMEAPPISFUNNY', "HS256")
            info['token'] = user_id
        except:
            # pass
            return Response("Please register again..",status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(info)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def UserCreateView(request):
    if request.method=='POST':
        try:
            received_json_data=json.loads(request.body)
            print(received_json_data["token"])
        except:
            return JsonResponse({'error': 'A bad request'}, status=400)
            # return Response("A bad request",status=status.HTTP_400_BAD_REQUEST)
        secret_key = "GAMEAPPISFUNNY"
        try:
            token_decoded_data=jwt.decode(received_json_data["token"], secret_key, "HS256")
        except:
            return JsonResponse({'error': 'Please register again..'}, status=400)
            # return Response("Please register again..",status=status.HTTP_400_BAD_REQUEST)
        if token_decoded_data['email'] == received_json_data['email']:
            if User.objects.filter(email = token_decoded_data['email']).exists():
                return JsonResponse({'error': 'email'}, status=409)
                # return Response("Email already exists",status=status.HTTP_409_CON)
            elif User.objects.filter(username = received_json_data['username']).exists():
                return JsonResponse({'error': 'username'}, status=409)
                # return Response("User already exists with that username",status=status.HTTP_409_CON)
            else:
                user = User.objects.create_user(username = received_json_data['username'],password = received_json_data['password'],email = token_decoded_data['email'],first_name=received_json_data['first_name'],last_name=received_json_data['last_name'])
                user.save( )
                return JsonResponse({'success': True}, status=200)
                # return Response("User Registration Complete", status=status.HTTP_200_OK)
        return JsonResponse({'error': 'Register with the same email provided for authentication.'}, status=400)
        # return Response("Register with the same email provided for authentication.",status=status.HTTP_409_CON)
    return JsonResponse({'error': 'GET NOT ALLOWED'}, status=400)
    # return Response(status=status.HTTP_400_BAD_REQUEST)
