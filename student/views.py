from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from. import forms 
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserUpdateForm

# Create your views here.

# def home(request):
#   return render(request, 'index.html')



class getAllStudent(ListView):
  model = models.Student
  template_name = 'index.html'
  context_object_name ='students'
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_actions'] = False  
        return context


class CreateStudent(LoginRequiredMixin, CreateView):
  model = models.Student
  form_class = forms.StudentForm
  success_url = reverse_lazy('User_profile')
  template_name = 'createStudent.html'
  
  def form_valid(self, form):
    """If the form is valid, save the associated model."""
    # student = form.save(commit=False)
    # student.user = self.request.user
    # student.save()
    form.instance.created_by = self.request.user  
    messages.success(self.request, "Student added successfully!")
    return super().form_valid(form)
  


class Update_student(LoginRequiredMixin, UpdateView):
  model = models.Student
  form_class = forms.StudentForm
  template_name = 'createStudent.html'
  success_url = reverse_lazy('User_profile')
  pk_url_kwarg = 'pk' 
  
  def get_context_data(self, **kwargs):
      """Insert the form into the context dict."""
      context = super().get_context_data(**kwargs)
      context['edit'] = True
      messages.success(self.request, "Student record updated successfully!")
      return context

  def form_valid(self, form):
      return super().form_valid(form)
  


class Delete_student(LoginRequiredMixin, DeleteView):
    model = models.Student
    pk_url_kwarg ='pk'
    success_url = reverse_lazy('User_profile')
    template_name = 'deleteUrl.html' 
    def delete(self, request, *args, **kwargs):
      messages.error(self.request, "Student record deleted!") 
      return super().delete(request, *args, **kwargs)
    


class User_profile(LoginRequiredMixin, ListView):
  model = models.Student
  template_name = 'userProfile.html'
  context_object_name ='students'

  def get_queryset(self):
        """Filter students by the current user"""
        return models.Student.objects.filter(created_by=self.request.user)
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_actions'] = True  
        return context



class User_create(CreateView):
  model = models.User
  form_class = forms.UserForm
  success_url = reverse_lazy('User_login')
  template_name = 'userSignUp.html' 
  def form_valid(self, form):
    """If the form is valid, save the associated model."""
    self.object = form.save()
    return super().form_valid(form)
  


class User_login(LoginView):
  template_name = 'userLogin.html'  
  # redirect_authenticated_user = True  # Redirect if the user is already logged in
  success_url = reverse_lazy('User_profile')
  def get_success_url(self):
      """Customize the success URL if needed."""
      messages.success(self.request, "Login successful! Welcome.")  
      return self.success_url 
  


class User_update(LoginRequiredMixin, UpdateView):
  model = models.User
  form_class = UserUpdateForm
  template_name = 'userSignUp.html'
  success_url = reverse_lazy('User_profile')
  pk_url_kwarg = 'pk' 
  
  def get_context_data(self, **kwargs):
      """Insert the form into the context dict."""
      context = super().get_context_data(**kwargs)
      context['edit'] = True
      return context


class User_logout(LogoutView):
   next_page = 'Home'
   def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, "You have been logged out.")  
        return super().dispatch(request, *args, **kwargs)




