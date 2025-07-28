from django.shortcuts import render,redirect
from LibraryApp.models import *
from LibraryApp.form import *
from django.contrib.auth import authenticate, login, logout,hashers,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = CustomUserModel.objects.create_user(
                username=username,
                email=email,
                user_type=user_type,
                password=confirm_password,
            )
            if user_type == 'Student':
                StudentProfileModel.objects.create(
                    student_id=user,
                )
            elif user_type == 'Librarian':
                LibrarianProfileModel.objects.create(
                    employee_id=user,
                )
            return redirect('loginPage')
    
    return render(request, 'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')
def logoutPage(request):
    logout(request)
    return redirect('loginPage')

@login_required
def changePasswordPage(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user

        if not user.check_password(old_password):
            messages.error(request, 'Current password is incorrect.')
            return render(request, 'changePassword.html')

        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            return render(request, 'changePassword.html')

        user.set_password(new_password1)
        user.save()

        update_session_auth_hash(request, user)

        messages.success(request, 'Your password has been updated successfully.')
        return redirect('home') 
    return render(request, 'changePassword.html')
@login_required
def home(request):
    user = request.user
    if user.user_type == 'Librarian':
        bookData = BookModel.objects.filter(added_by=user)
    elif user.user_type == 'Student':
        bookData = BookModel.objects.all()
    else:
        bookData = BookModel.objects.none()  

    return render(request, 'home.html', {'bookData': bookData})


@login_required
def profile(request):
    user = request.user
    student = StudentProfileModel.objects.filter(student_id=user).first()
    librarian = LibrarianProfileModel.objects.filter(employee_id=user).first()

    context = {
        'student': student,
        'librarian': librarian,
    }
    return render(request, 'profile.html',context)

@login_required
def editProfile(request):
    user = request.user
    student = StudentProfileModel.objects.filter(student_id=user).first()
    librarian = LibrarianProfileModel.objects.filter(employee_id=user).first()

    if user.user_type == 'Librarian' and librarian:
        if request.method == 'POST':
            librarian.designation = request.POST.get('designation')
            librarian.phone = request.POST.get('phone')
            librarian.address = request.POST.get('address')
            if request.FILES.get('profile'):
                librarian.profile = request.FILES.get('profile')
            librarian.save()
            return redirect('profile')
    elif user.user_type == 'Student' and student:
        if request.method == 'POST':
            student.department = request.POST.get('department')
            student.contact_number = request.POST.get('contact_number')
            student.address = request.POST.get('address')
            if request.FILES.get('profile'):
                student.profile = request.FILES.get('profile')
            student.save()
            return redirect('profile')

    context = {
        'student': student,
        'librarian': librarian
    }
    return render(request, 'editProfile.html', context)


@login_required
def addBook(request):
    if request.method == 'POST':
        book_form = BookModelForm(request.POST)
        if book_form.is_valid():
            book = book_form.save(commit=False)
            book.added_by = request.user
            book.save()
            return redirect('home')
    else:
        book_form = BookModelForm()
        
    return render(request, 'addBook.html',{'book_form':book_form})

def editBook(request,id):
    user = request.user
    book = BookModel.objects.filter(id=id,added_by=user).first()
    if not book:
        return HttpResponseNotFound("Book not found")

    if request.method == 'POST':
        form = BookModelForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookModelForm(instance=book)

    return render(request, 'editBook.html', {'book_form': form})


@login_required
def viewBook(request,id):
    bookData = BookModel.objects.get(id=id)
    return render(request, 'viewBook.html',{'bookData':bookData})
    
@login_required
def deleteBook(request,id):
    books = BookModel.objects.get(id=id).delete()
    return redirect('home')

@login_required

def bookListPage(request):
    bookData = BookModel.objects.all()
    return render(request, 'bookList.html',{'bookData':bookData})

