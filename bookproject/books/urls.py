from django.urls import path
from .views import BookListView

app_name = 'books' # URL 네임스페이스를 설정하여 프로젝트 내에서 URL 이름이 겹치는 것을 방지합니다.

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
] # books/로 접속하면 BookListView가 실행되도록 설정