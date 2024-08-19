from django import forms
from .models import Book, Rental
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm): # 자동으로 폼을 생성! 
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date','genre', 'summary', 'image'] # 폼에 보여줄 필드 목록
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),  # 날짜 선택기를 위한 위젯 설정
        }
        labels = {
            'title': '제목',
            'author': '저자',
            'publication_date': '출판일',
            'genre': '장르',
            'summary': '요약',
            'image': '이미지'
        }

class CustomUserCreationForm(UserCreationForm):
    # 현재 원하는 필드가 모델에 없을 경우, 직접 필드를 추가할 수 있음
    email = forms.EmailField(label='이메일', required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    
class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['book', 'return_date']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }