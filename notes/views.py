from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404


@method_decorator(login_required, name="dispatch")
class NoteListView(ListView):
    model = Note
    template_name = "notes/note_list.html"

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

@method_decorator(login_required, name="dispatch")
class NoteDetailView(DetailView):
    model = Note
    template_name = "notes/note_detail.html"
    
    def get_queryset(self):
        # Filtramos las notas del usuario actual
        return Note.objects.filter(user=self.request.user)
    
    def get_object(self, queryset=None):
        # Intentamos obtener la nota con el 'pk' proporcionado en la URL
        obj = super().get_object(queryset)
        
        # Si la nota no pertenece al usuario actual, lanzamos un error 404
        if obj.user != self.request.user:
            raise Http404("No existe esta nota o no tienes permiso para verla.")
        
        return obj

@method_decorator(login_required, name="dispatch")
class NoteCreateView(CreateView):
    model = Note
    fields = ["title", "body"]
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("note_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")