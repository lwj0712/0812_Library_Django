from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='제목')
    author = models.CharField(max_length=100, verbose_name='저자')
    publication_date = models.DateField(verbose_name='출판일')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '도서' # 모델의 단수 표현
        verbose_name_plural = '도서들' # 모델의 복수 표현
