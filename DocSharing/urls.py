from django.contrib import admin
from django.urls import path
from share import views 
from django.conf import settings
from django.conf.urls.static import static

#home, register, login_view, logout_view, upload_file, file_detail, file_delete, file_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_file, name='upload_file'),    
    path('files/', views.file_list, name='file_list'),
    path('files/<int:id>/', views.file_detail, name='file_detail'),
    path('files/<int:id>/delete/', views.file_delete, name='file_delete'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)