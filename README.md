Django의 CBV를 활용하여 도서관 앱을 만들어 보았습니다.

## CBV(Class Based View)
* FBV: 모든 재료를 직접 준비하고 요리하는 것과 같습니다. 각 재료의 양과 순서를 자유롭게 조절할 수 있지만, 모든 것을 직접 해야 하므로 시간이 더 걸릴 수 있습니다.
* CBV: 미리 준비된 요리 레시피를 사용하는 것과 같습니다. 이미 검증된 레시피를 활용하되, 필요할 때는 레시피의 일부를 수정하거나 재료를 추가할 수 있습니다. 기본적인 준비 작업을 줄여주기 때문에 빠르고 효율적으로 요리를 완성할 수 있습니다.

## ListView
* ListView는 Django의 제네릭 뷰 중 하나로, 특정 모델의 객체 리스트를 쉽게 보여줄 수 있도록 도와줍니다.<br>
반복적인 목록 페이지를 구현 할 때는 CBV의 ListView를 활용하는 것이 효율적입니다.

* FBV 사용 예시
```python
from django.shortcuts import render
from .models import Book, Author

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})
```
* CBV 사용 예시
```python
from django.views.generic import ListView
from .models import Book, Author

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class AuthorListView(ListView):
    model = Author
    template_name = 'authors/author_list.html'
    context_object_name = 'authors'
```

## DetailView

## CreateView

## UpdateView

## DeleteView
