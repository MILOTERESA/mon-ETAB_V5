from django.urls import path, include, re_path
from rest_framework import routers

# from api.apiviews.student_api_view import student_list , student_detail
# from api.apiviews.teacher_api_view import teacher_list , teacher_detail
# from api.apiviews.user_api_view import user_list , user_detail
# from api.apiviews.index_api_view import index_api
from .viewset.absence import AbsenceViewSet
from .viewset.school import SchoolViewSet
from .viewset.role_user import RoleUserViewSet
from .viewset.address import AddressViewSet
from .viewset.student_card import StudentcardViewSet
from .viewset.app_setting import App_settingViewSet
from .viewset.student import StudentViewSet
from .viewset.teacher import TeacherViewSet
from .viewset.user import UserViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'teacher', TeacherViewSet)
router.register(r'user', UserViewSet)
router.register(r'absence' , AbsenceViewSet)
router.register( r'address' , AddressViewSet, basename="address")
router.register(r'app_setting' , App_settingViewSet)
router.register(r'role_user' , RoleUserViewSet)
router.register(r'school' , SchoolViewSet)
router.register(r'student_card' , StudentcardViewSet)



# app_name='api'

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns =[
    # path('', index_api, name='index_api' ),
    path('',include(router.urls)),
    
    # path('student/', student_list, name='student' ),
    # path('teacher/', teacher_list, name='teacher' ),
    # path('user/', user_list, name='user' ),
    
    
    # path('user/<int:pk>/', user_detail, name='user' ),
    # path('student/<int:pk>/', student_detail, name='student' ),
    # path('teacher/<int:pk>/', teacher_detail, name='teacher' ),
    re_path(r'swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    
    
]