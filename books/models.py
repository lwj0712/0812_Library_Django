from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    author = models.CharField(max_length=100, verbose_name='저자')
    publication_date = models.DateField(verbose_name='출판일')
    genre = models.CharField(max_length=100, verbose_name='장르') # 책 장르, 최대 100자 문자열
    summary = models.TextField(verbose_name='요약') # 책 요약, 문자열 길이 제한 없음
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)  # 이미지 필드 추가

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '도서' # 모델의 단수 표현
        verbose_name_plural = '도서들' # 모델의 복수 표현

class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='대여 도서')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='대여자')
    rental_date = models.DateField(auto_now_add=True, verbose_name='대여일')
    return_date = models.DateField(verbose_name='반납일', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user}님이 {self.book}을 대여함"