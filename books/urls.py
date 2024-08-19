from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, RentalInfoView, BookRentalView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'books' # URL 네임스페이스를 설정하여 프로젝트 내에서 URL 이름이 겹치는 것을 방지합니다.

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'), # books/로 접속하면 BookListView가 실행되도록 설정
    path('<int:pk>', BookDetailView.as_view(), name = 'book_detail'),path('new/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('rental-info/', RentalInfoView.as_view(), name='rental_info'),
    path('rental/', BookRentalView.as_view(), name='book_rental'),
    path('rental/success/', TemplateView.as_view(template_name='books/rental_success.html'), name='rental_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)