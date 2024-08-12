from django.contrib import admin
from django.urls import path, include
from books.views import MainView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", include("books.urls")), # books/로 시작하는 URL은 books 앱의 urls.py에서 처리
    path('', MainView.as_view(), name='main'), # 메인 화면을 보여줄 URL 지정
]