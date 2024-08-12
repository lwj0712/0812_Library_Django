from django.contrib import admin
from .models import Book  # Book 모델을 임포트

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'genre')  # 관리자 페이지에서 표시할 필드
    list_display_links = ('author',)  # 링크로 사용할 필드를 'author'로 지정
    search_fields = ('title', 'author', 'genre' )  # 검색 가능한 필드
    list_filter = ('publication_date', 'genre')  # 필터링 가능한 필드
    ordering = ('-publication_date',)  # 출판일을 기준으로 내림차순 정렬
    readonly_fields = ('author',)  # 저자 필드를 읽기 전용으로 설정
    list_editable = ('title',)  # 제목을 목록에서 바로 수정 가능하도록 설정