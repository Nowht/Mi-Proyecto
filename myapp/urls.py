from django.urls import path
from .views import LoginView, login_page, dashboard, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login-page/', login_page, name='login_page'),
    path('dashboard/', dashboard, name='dashboard'),
]
