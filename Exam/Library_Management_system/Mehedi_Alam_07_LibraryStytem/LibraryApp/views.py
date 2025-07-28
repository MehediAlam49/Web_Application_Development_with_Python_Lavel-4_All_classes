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
    bookData = BookModel.objects.all()
    return render(request, 'home.html',{'bookData':bookData})
@login_required
def profile(request):
    return render(request, 'profile.html')
@login_required
def editProfile(request):
    user = request.user
    student = StudentProfileModel.objects.filter(student_id=user)
    librarian = LibrarianProfileModel.objects.filter(employee_id=user)
    context={
        'student':student,
        'librarian':librarian
    }
    if request.user.user_type == 'Librarian':
        librarian_data = LibrarianProfileModel.objects.get(employee_id=user)
        if request.method == 'POST':
            librarian_data.designation = request.POST.get('designation')
            librarian_data.phone = request.POST.get('phone')
            librarian_data.address = request.POST.get('address')
            librarian_data.profile = request.FILES.get('profile')
            librarian_data.save()
            return redirect('profile')
        
    elif request.user.user_type == 'Student':
        student_data = LibrarianProfileModel.objects.get(student_id=user)
        if request.method == 'POST':
            student_data.department = request.POST.get('department')
            student_data.contact_number = request.POST.get('contact_number')
            student_data.address = request.POST.get('address')
            student_data.profile = request.FILES.get('profile')
            student_data.save()
            return redirect('profile')

    return render(request, 'editProfile.html',context)
@login_required
def addBook(request):
    if request.method == 'POST':
        book_form = BookModelForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('bookListPage')
    else:
        book_form = BookModelForm()
        
    return render(request, 'addBook.html',{'book_form':book_form})

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

