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

* FBV 사용 예시
```python
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})
```
* CBV 사용 예시
```python
from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book  # 사용할 모델 지정
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
```
흔히 사용하는 get_object_or_404()가 DetailView에 이미 포함되어 있어, 따로 적지 않아도 됩니다.

## CreateView
CreateView*는 Django의 제네릭 뷰 중 하나로, 새로운 객체를 생성하기 위한 폼을 제공하고, 이 폼의 제출을 처리하는 데 사용됩니다. CreateView는 특정 모델과 연동된 폼을 자동으로 생성하고, 폼의 유효성 검사 및 객체 저장 로직을 처리하여 개발자가 일일이 이를 작성할 필요가 없도록 합니다.

* FBV 사용 예시
```python
from django.shortcuts import render, redirect
from .forms import BookForm

def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST) # 폼 생성
        if form.is_valid():    # 유효성 검사
            form.save()    # 객체 저장
            return redirect('books:book_list')    # 성공 시 도서 목록으로 리다이렉션
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
```

* CBV 사용 예시
```python
from django.views.generic import CreateView
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy

class BookCreateView(CreateView):
    model = Book    # 모델 지정
    form_class = BookForm    # 폼 클래스 지정
    template_name = 'books/book_form.html'    # 템플릿 파일 지정
    success_url = reverse_lazy('books:book_list') # 성공 시 리다이렉션할 URL 지정
```
CreateView를 사용하면, 폼 생성, 유효성 검사, 객체 저장, 리다이렉션 등의 작업이 자동으로 처리됩니다.

## UpdateView

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
## DeleteView

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
