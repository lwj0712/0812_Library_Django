from django.contrib import admin
from django.urls import path, include
from books.views import MainView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")), # books/로 시작하는 URL은 books 앱의 urls.py에서 처리
    path('', MainView.as_view(), name='main'), # 메인 화면을 보여줄 URL 지정
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),  # 로그아웃 후 홈 화면으로 리다이렉트
    path('signup/', SignUpView.as_view(), name='signup'),

    
]