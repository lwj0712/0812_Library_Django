Django의 CBV를 활용하여 도서관 앱을 만들어 보았습니다.<br>
ListView, DetailView, CreateView, UpdateView, DeleteView를 활용하였고, <br>
FBV와 CBV의 비교, 사용 된 CBV에 대한 간단한 설명과 어떤 상황에 사용하면 유용한지에 대해 알아보겠습니다.<br>

## CBV(Class Based View)
* FBV: 모든 재료를 직접 준비하고 요리하는 것과 같습니다. 각 재료의 양과 순서를 자유롭게 조절할 수 있지만, 모든 것을 직접 해야 하므로 시간이 더 걸릴 수 있습니다.
* CBV: 미리 준비된 요리 레시피를 사용하는 것과 같습니다. 이미 검증된 레시피를 활용하되, 필요할 때는 레시피의 일부를 수정하거나 재료를 추가할 수 있습니다. 기본적인 준비 작업을 줄여주기 때문에 빠르고 효율적으로 요리를 완성할 수 있습니다.

## ListView
ListView는 Django의 제네릭 뷰 중 하나로, 특정 모델의 객체 리스트를 쉽게 보여줄 수 있도록 도와줍니다.<br>
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
Django에서 상세 페이지를 구현할 때, FBV보다는 CBV의 DetailView를 사용하는 것이 훨씬 효율적이고 간결합니다. DetailView는 객체 조회, 예외 처리, 템플릿 렌더링을 자동으로 처리해주므로, 반복적인 코드를 줄이고 유지보수성을 높일 수 있습니다.
## CreateView

## UpdateView

## DeleteView
