"""定义users的URL模式"""

from django.urls.conf import path
# from django.contrib.auth.views import login （原书代码）
from django.contrib.auth.views import LoginView

from . import views
app_name = 'users'

urlpatterns = [
    # 登录页面
    # path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
