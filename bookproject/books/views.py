from django.views.generic import ListView, TemplateView
from .models import Book

class BookListView(ListView):
    model = Book  # 사용할 모델 지정
    template_name = 'books/book_list.html'  # 사용할 템플릿 지정
    context_object_name = 'books'  # 템플릿에서 사용할 컨텍스트 객체 이름 지정 (옵션)
    ordering = ['-publication_date'] # 출판일 기준 내림차순으로 정렬

class MainView(TemplateView):
    template_name = 'main.html' # 랜더링할 템플릿 파일