from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from professors.models.teacher import TeacherModel
from api.serializers.teacher_serializers import TeacherSerializer

@csrf_exempt

def teacher_list(request):

    if request.method == "GET":
        teacher = TeacherModel.objects.all()
        serializer= TeacherSerializer(teacher, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data= JSONParser().parse(request)
        serializer=TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        
@csrf_exempt
def teacher_detail(request, pk):
    try:
        teacher = TeacherModel.objects.get(pk=pk)
    except TeacherModel.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == "GET":
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT":
        data= JSONParser().parse(request)
        serializer = TeacherSerializer(teacher, data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        
        
    elif request.method == "DELETE":
        teacher.delete()
        return HttpResponse(status=204)

    
