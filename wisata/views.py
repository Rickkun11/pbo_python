from django.shortcuts import render
from .models import *
from .forms import *


# Create your views here.

def beranda(request):
    judul = "Trip"
    map = Peta.objects.all()
    trip = Wisata.objects.all()
    konteks = {
        "title" : judul,
        "map" : map,
        "trip" : trip
    }
    return render(request, 'beranda.html', konteks)

def tambah_peta(request):
    judul = "Tambah Data Peta"
    konteks = {
        "title" : judul,
    }
    return render(request, 'tambah_peta.html', konteks)

def update_peta(request):
    judul = "Update Data Peta"
    konteks = {
        "title" : judul,
    }
    return render(request, 'update_peta.html', konteks)

def delete_peta(request):
    judul = "Delete Data Peta"
    konteks = {
        "title" : judul,
    }
    return render(request, 'delete_peta.html', konteks)

def tambah_wisata(request):
    if request.POST:
        form = FormWisata(request.POST)
        if form.is_valid():
            form.save()
            form = FormWisata()
            pesan= "Data Tempat Wisata berhasil ditambahkan"
            data = {
                'Title' : "Tambah Data",
                'subtitle' : "Tambah Rekomendasi Tempat Wisata",
                'form' : form,
                'pesan' : pesan,
            }
        return render(request, 'tambah_wisata.html', data)
    
    else:
        form = FormWisata()
        konteks = {
            "form" : form,
        }
    return render(request, 'tambah_wisata.html', konteks)

def update_wisata(request):
    judul = "Update Data Wilayah"
    konteks = {
        "title" : judul,
        
    }
    return render(request, 'update_wisata.html', konteks)

def delete_wisata(request):
    judul = "Delete Data Wilayah"
    konteks = {
        "title" : judul,
    }
    return render(request, 'delete_wisata.html', konteks)

def login(request):
    judul = "Login"
    konteks = {
        "title" : judul,
    }
    return render(request, 'login.html', konteks)

def signup(request):
    judul = "Signup"
    konteks = {
        "title" : judul,
    }
    return render(request, 'signup.html', konteks)
