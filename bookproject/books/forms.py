from django import forms
from .models import Book

class BookForm(forms.ModelForm): # 자동으로 폼을 생성! 
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date','genre', 'summary'] # 폼에 보여줄 필드 목록
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),  # 날짜 선택기를 위한 위젯 설정
        }
        labels = {
            'title': '제목',
            'author': '저자',
            'publication_date': '출판일',
            'genre': '장르',
            'summary': '요약',
        }