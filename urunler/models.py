from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim=models.CharField(max_length=100)
    def __str__(self):
        return self.isim



class Urun(models.Model):
    kategori= models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
    isim=models.CharField(max_length=100, null=True)
    marka=models.CharField(max_length=100, null=True)
    aciklama=models.TextField(max_length=1000)
    fiyat=models.FloatField()
    resim=models.FileField(upload_to='urunler/', null=True)
    def __str__(self):
        return self.marka