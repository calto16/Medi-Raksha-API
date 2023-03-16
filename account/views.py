from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from medicine.models import Medicine
from medicine.serializers import MedicineSerializer
from django.db.models import Q
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Account
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

@api_view(['POST'])
def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"success" : "true"})
    else:
        return Response({"success" : "false"})
    
@api_view(['GET'])
def userData(request):
    account = request.user.account
    data = {
        'username' : str(request.user),
        'type' : str(account.type),
    }
    return Response(data)

@api_view(['POST'])
def registerUser(request):
    user_form = UserCreationForm(request.POST)
    print(user_form)
    if user_form.is_valid():
        user = user_form.save(commit=False)
        user.email = request.POST.get('email')
        account = Account(user=user)
        user.save()
        account.save()
        login(request, user)
        return redirect('profile-update')
    return Response({"success" : "true"})

@api_view(['GET'])
def logoutUser(request):
    logout(request)
    return redirect('login')