from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin
from .forms import RegisterForm

from awwards.models import Profile, Project
from django.http import JsonResponse
from .serializers import ProjectSerializer, ProfileSerializer



# Create your views here.	# Create your views here.

def project(request):
   project = Project.objects.all()
   serializer = ProjectSerializer(project, many=True)
   return JsonResponse(serializer.data, safe=False)


def profile(request):
   profile = Profile.objects.all()
   serializer = ProfileSerializer(profile, many=True)
   return JsonResponse(serializer.data, safe=False)





def login(request):	
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      try:
         user = User.objects.get(username=username, password=password)

      except:
         messages.error(request, 'Invalid username or password')

      user = authenticate(request, username=username, password=password)
      if user is not None:
         authlogin(request,user)
         return redirect('home')
      else:
         messages.error(request, 'Invalid username or password')


   return render(request, 'awwards/login.html') 

def register(request):
   register_form = RegisterForm()
   if request.method == 'POST':
      form = RegisterForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False)
         user.save()
         profile = Profile(username=request.user.username)
         profile.save()

      return redirect('login')
   context = {
      'form': register_form,
   }


   return render(request, 'awwards/register.html', context)


def logout(request):
   return redirect('login')