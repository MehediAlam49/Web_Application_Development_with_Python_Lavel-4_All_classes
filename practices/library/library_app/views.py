from django.shortcuts import render,redirect,get_object_or_404
from library_app.models import *
from library_app.forms import *

# Create your views here.
def create_book(request):
    if request.method == "POST":
        form = LibraryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    
    else:
        form = LibraryForm()
    return render(request, 'create_book.html',{'form': form})

def book_list(request):
    book_data = LibraryModel.objects.all()
    return render(request, 'book_list.html',{'book_data': book_data})

def edit_book(request,id):
    books = get_object_or_404(LibraryModel, id=id)
    if request.method == "POST":
        form = LibraryForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    
    else:
        form = LibraryForm(instance=books)
    return render(request, 'edit_book.html',{'form':form})


def delete_book(request,id):
    get_object_or_404(LibraryModel,id=id).delete()
    return redirect('book_list')