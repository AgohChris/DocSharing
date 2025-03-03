from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Document, UserProfile
from .form import DocumentForm, UserProfileForm, CustomCreationForm, PasswordResetNewPasswordForm, PasswordRresetCodeForm, PasswordResetEmailForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
import random as rd



@login_required
def home(request):
    return render(request, 'home.html')



def register(request):
    if request.method == 'POST':
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def upload_file(request):
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            return redirect('file_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_file.html', {'form': form})



@login_required
def file_list(request):
    documents = Document.objects.all()
    return render(request, 'file_list.html', {'documents': documents})



@login_required
def file_detail(request, id):
    document = get_object_or_404(Document, id=id)
    return render(request, 'file_detail.html', {'document': document})



@login_required
def file_delete(request, id):
    document = get_object_or_404(Document, id=id)
    if request.method == "POST":
        document.delete()
        return redirect('file_list')
    return render(request, 'file_delete.html', {'document': document})



@login_required
def userProfile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
           form.save()
           return redirect('home')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'user_profile.html', {'form': form})


def password_reset_email(request):
    if request.method == "POST":
        form = PasswordResetEmailForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                code = str(rd.randint(1000, 9999))
                user.profile.reset_code = code
                user.profile.save()
                
                send_mail(
                    'Doc Sharing Password Reset',
                    f'Votre Code est : {code}', 'agohchris90@gmail.com', 
                    [email], fail_silently=False
                )
                return redirect('password_reset_code')
    else:
        form = PasswordResetEmailForm()
    return render(request, 'password_reset_email.html', {'form': form})


def password_reset_code(request):
    if request.method == "POST":
        form = PasswordRresetCodeForm(request.POST)
        
        if form.is_valid():
            code = form.cleaned_data['code']
            user = User.objects.filter(profile__reset_code=code).first()
            if user:
                return redirect('password_reset_new_password')
        else:
            form = PasswordRresetCodeForm()
        return render(request, 'password_reset_code.html', {'form': form})
    

def password_reset_new_password(request):
    if request.method == "POST":
        form = PasswordResetNewPasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            
            if password1 == password2:
                user = User.objects.filter(profile__reset_code=request.session['reset_code']).first()
                
                if user:
                    user.password = make_password(password1)
                    user.profile.reset_code = ''
                    user.save()
                    return redirect('login')
    else:
        form = PasswordResetNewPasswordForm()
    return render(request, 'password_reset_new_password.html', {'form': form})