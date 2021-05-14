from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings

from .models import Book

# Create your views here.

# def homepage(request):
#     return HttpResponse('<ul><h1>Welcome to the world of Books</h1><strong>Here you can search for all engineering books</strong></ul>')

def homepage(request):
    all_books = Book.active_objects.all()
    return render(request,template_name='home.html',context={"books":all_books})


def save_book(request):
    if request.method == "POST":
        if request.POST.get('bid'):
            book = Book.objects.get(id=request.POST.get('bid'))
            book.name = request.POST['bnm']
            book.author = request.POST['bauth']
            book.price = request.POST['bprice']
            book.pub = request.POST['bpub']
            book.save()
            messages.success(request, f"{book.name} book updated successfully..!!")

        else:
            nm = request.POST['bnm']
            auth = request.POST['bauth']
            prc = request.POST['bprice']
            pub = request.POST['bpub']
            b1 =Book(name=nm,author=auth,price=prc,pub=pub)
            b1.save()
            messages.success(request, "Book saved successfully..!!")
        return redirect("/Home/")
        # return HttpResponse("Book saved successfully....!!")
        
    else:
        return HttpResponse("Wrong method invoked...!!")

SUCCESS = 25
def del_book(request,id):
    book_obj = Book.objects.get(id=id)
    book_obj.is_deleted = 1
    book_obj.save()
    # book_obj.delete()
    messages.add_message(request, SUCCESS, 'Book Deleted Successfully...!!!')
    return redirect("/Home/")
  
def edit_book(request,id):
    all_books = Book.active_objects.all()
    book_obj = Book.objects.get(id=id)
    return render(request,template_name='home.html',context={"book":book_obj, "books":all_books})

def show_deleted_books(request):
    delete_books = Book.inactive_objects.all()
    return render(request,template_name='home.html',context={'deleted':'yes',"books":delete_books})

def restore_book(request,id):
    book = Book.objects.get(id=id)
    book.is_deleted=0
    book.save()
    return redirect("/Home/")

