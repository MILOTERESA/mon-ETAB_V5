from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from user.models.user import CustomUserModel
from api.serializers.user_serializers import UserSerializer


@csrf_exempt

def user_list(request):

    if request.method == "GET":
        teacher = CustomUserModel.objects.all()
        serializer= UserSerializer(teacher, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data= JSONParser().parse(request)
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def user_detail(request, pk):
    try:
        user = UserModel.objects.get(pk=pk)
    except UserModel.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = UserSerializer(teacher)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data= JSONParser().parse(request)
        serializer = UserSerializer(user, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        
        
    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=204)

    
