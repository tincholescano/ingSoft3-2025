from django.urls import path, include
from .views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", NoteListView.as_view(), name="note_list"),
    path("<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("new/", NoteCreateView.as_view(), name="note_create"),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
