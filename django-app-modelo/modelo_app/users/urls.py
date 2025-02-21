from django.urls import path

from . import views

urlpatterns = [
    path("", views.indexUsers, name="indexusers"),
    path("create", views.createUserView, name="createuserView"),
    path("createUser", views.createUser, name="createUser"),
    path("details-user-id/<int:id>", views.userDetail, name="userDetail")
]