from django.urls import path

from account.views import EditProfile, ChangePassword, Login, Join, UserDetail, Logout

urlpatterns = [
    path('users/edit-profile/', EditProfile.as_view(), name='edit_profile'),
    path('users/change-password/', ChangePassword.as_view(), name='change_password'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('join/', Join.as_view(), name='join'),
    path('users/<int:id>/', UserDetail.as_view(), name='user_detail'),
]
