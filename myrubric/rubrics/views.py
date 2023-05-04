from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Class, Book

@login_required
def class_list(request):
    classes = Class.objects.filter(user=request.user)
    return render(request, 'class_list.html', {'classes': classes})

@login_required
def book_list(request, class_id):
    classroom = get_object_or_404(Class, id=class_id, user=request.user)
    books = Book.objects.filter(classroom=classroom)
    return render(request, 'book_list.html', {'classroom': classroom, 'books': books})

@login_required
def book_edit(request, book_id):
    book = get_object_or_404(Book, id=book_id, classroom__user=request.user)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
    
    return render(request, 'book_edit.html', {'book': book})

def home(request):
    # code to handle the request
    classes = Class.objects.all()
    return render(request, 'home.html', {classes: 'classes'})

def classes(request):
    class_list = Class.objects.all()
    return render(request, 'classes.html', {'class_list': class_list})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_detail.html', {'book': book})

from .forms import ClassForm

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.user = request.user # set the user field to the current user
            new_class.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'add_class.html', {'form': form})
