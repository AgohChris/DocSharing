from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Document, UserProfile
from .forms import DocumentForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

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
    return redirect('home')

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
    userprofile = UserProfile