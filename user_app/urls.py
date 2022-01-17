from django.urls import path

from . import views

urlpatterns = [
    path('createtable', views.createTable),
    path('createuser', views.createUser),
    path('createuserpost', views.createUserPost),
    path('createuserexperience', views.createUserExperience),
    path('createuserfollow', views.createUserFollow),
    path('createuserfriend', views.createUserFriend),
    path('createuserlike', views.createUserLike),
    path('createusercomment', views.createUserComment),
    path('viewuser', views.viewUser),





]