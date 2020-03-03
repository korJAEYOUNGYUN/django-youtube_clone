from django.urls import path

from account import views


urlpatterns = [
    path('users/edit-profile/', views.EditProfile.as_view(), name='edit_profile'),
    path('users/change-password/', views.ChangePassword.as_view(), name='change_password'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('join/', views.Join.as_view(), name='join'),
    path('users/<int:id>/', views.UserDetail.as_view(), name='user_detail'),
]
