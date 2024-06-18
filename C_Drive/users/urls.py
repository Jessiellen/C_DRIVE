from django.urls import path
from .views import custom_login_view, custom_logout_view, SignupView, staff_dashboard, user_dashboard

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('staff/dashboard/', staff_dashboard, name='staff_dashboard'),
    path('user/dashboard/', user_dashboard, name='user_dashboard'),
]