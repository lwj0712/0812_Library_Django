from django.contrib import admin
from .models import Book  # Book 모델을 임포트

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  # 관리자 페이지에서 표시할 필드
    search_fields = ('title', 'author')  # 검색 가능한 필드
    list_filter = ('publication_date',)  # 필터링 가능한 필드