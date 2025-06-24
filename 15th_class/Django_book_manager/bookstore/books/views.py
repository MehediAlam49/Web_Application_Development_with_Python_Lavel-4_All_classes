from django.shortcuts import render,redirect
from books.models import *

# Create your views here.
def book_list(request):
    bookData = bookModel.objects.all()
    return render(request, 'book_list.html', {'book': bookData})
def book_form(request):
    if request.method == 'POST':
        books =bookModel(
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            category = request.POST.get('category'),
            publish_date = request.POST.get('publish_date'),
            description = request.POST.get('description'),
            cover_photo = request.FILES.get('cover_photo'),
        )
        books.save()
        return redirect('book_list')
    return render(request, 'book_form.html')

def delete_book(request,id):
    book = bookModel.objects.get(id=id).delete()
    return redirect('book_list')

def edit_book(request,id):
    bookData =bookModel.objects.get(id=id)
    if request.method == 'POST':
        books =bookModel(
            id =id,
            title = request.POST.get('title'),
            author = request.POST.get('author'),
            category = request.POST.get('category'),
            publish_date = request.POST.get('publish_date'),
            description = request.POST.get('description'),

        )

        picture = request.FILES.get('cover_photo')
        if picture is not None:
            bookData.cover_photo =picture
        books.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': bookData})