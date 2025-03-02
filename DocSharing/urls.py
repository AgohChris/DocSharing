from django.contrib import admin
from django.urls import path
from share import views 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

#home, register, login_view, logout_view, upload_file, file_detail, file_delete, file_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout_view'),
    path('upload/', views.upload_file, name='upload_file'),    
    path('files/', views.file_list, name='file_list'),
    path('files/<int:id>/', views.file_detail, name='file_detail'),
    path('files/<int:id>/delete/', views.file_delete, name='file_delete'),
    path('profile/', views.userProfile, name='user_profile'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)