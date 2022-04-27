from django.shortcuts import render , redirect
from.models import *

def home(request):
    book_obj        = Book.objects.all()
    context = {
        "book_obj":book_obj
    }
    return render(request,'home.html',context)

def create_book(request):
    if request.method == "POST":
        book_name       = request.POST.get("book_name")
        author_name     = request.POST.get("author_name")
        price           = request.POST.get("price")
        description     = request.POST.get("description")

        book_obj = Book.objects.create(
            book_name = book_name,
            price      = price ,
            author = author_name,
            description = description
        )
        return redirect("/")

    return render(request,'create_book.html')

def delete_book(request,id):
    book_obj = Book.objects.get(id = id).delete()
    return redirect("/")


def update_book(request , id):
    book_obj = Book.objects.get(id = id)
    if request.method == "POST":
        book_name       = request.POST.get("book_name")
        author_name     = request.POST.get("author_name")
        price           = request.POST.get("price")
        description     = request.POST.get("description")

        book_obj = Book.objects.filter(id = id).update(
            book_name = book_name,
            price      = price ,
            author = author_name,
            description = description
        )
        return redirect("/")

    context = {
        "book_obj":book_obj
    }
    return render(request,'update_book.html',context)