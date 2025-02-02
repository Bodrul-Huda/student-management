from django.urls import path
from . import views



urlpatterns = [
    path('', views.getAllStudent.as_view(), name='Home'),
    path('create/', views.CreateStudent.as_view(), name='CreateStudent'),
    path('update/<int:pk>', views.Update_student.as_view(), name='Update_student'),
    path('delete/<int:pk>', views.Delete_student.as_view(), name='Delete_student'),
    path('profile/', views.User_profile.as_view(), name='User_profile'),
    path('user/', views.User_create.as_view(), name='User_create'),
    path('login/', views.User_login.as_view(), name='User_login'),
    path('logout/', views.User_logout.as_view(), name='User_logout'),
    path('user_update/<int:pk>', views.User_update.as_view(), name='User_update'),
    
    

]


