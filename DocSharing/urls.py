from django.contrib import admin
from django.urls import path
from share import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('upload/', views.upload_file, name='upload_file'),    
    path('files/', views.file_list, name='file_list'),
    path('files/<int:id>/', views.file_detail, name='file_detail'),
    path('files/<int:id>/delete/', views.file_delete, name='file_delete'),
    path('profile/', views.userProfile, name='user_profile'),
    
    
    path('password_reset_email/', views.password_reset_email, name='password_reset_email'),
    path('password_reset_code/', views.password_reset_code, name='password_reset_code'),
    path('password_reset_new_password/', views.password_reset_new_password, name='password_reset_new_password'),
       
] 

if settings.DEBUG:
    
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)