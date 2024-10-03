from rest_framework import viewsets,status,mixins
from api.serializers.user_serializers import UserSerializer
from user.models.user import CustomUserModel
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin,viewsets.GenericViewSet):

    queryset= CustomUserModel.objects.all()
    
    serializer_class= UserSerializer
    
    
    
    
    @action(detail=False, methods=['post'])
    def create_user_with_crypt(self, request, pk=None):
        data = JSONParser().parse(request)
        password = data['password']
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save(password=make_password(password))
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    @action(detail=True, methods=['patch'], url_path='set-password')
    def set_password(self, request, pk=None):
        user = self.get_object() 
        data = request.data
        password = data.get('password') 

        if not password:
            return Response({'error': 'Le mot de passe est requis'}, status=400)


        user.password = make_password(password)
        user.save()

        return Response({'status': 'Mot de passe changer avec succès'}, status=200)


    