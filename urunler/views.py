from django.shortcuts import render
from .models import *
from django.db.models import Q
# Create your views here.

def index(request):
    urunler=Urun.objects.all()
    Kategoriler=Kategori.objects.all()
    search=''
    if request.GET.get('search'):
        search=request.GET.get('search')
        urunler=Urun.objects.filter(
            Q(aciklama__icontains=search) | 
            Q(kategori__isim__icontains=search)
         )
    context={
        'urunler':urunler,
        'search':search,
        'kategoriler':Kategoriler
    }
    return render(request,'index.html',context)

def urunDetay(request,urunId):
    urun=Urun.objects.get(id=urunId)
    context={
        'urun':urun
    }
    return render(request,'urun.html',context)