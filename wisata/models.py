from django.db import models

# Create your models here.

class Tipe(models.Model):
    tipe = models.CharField(max_length=50)

    def __str__(self):
        return self.tipe

class Wisata(models.Model):
    nama = models.CharField(max_length=100)
    harga_tiket = models.CharField(max_length=100)
    penginapan = models.TextField(max_length=300)
    tipe_id = models.ForeignKey(Tipe, on_delete=models.CASCADE, null=True)
    keterangan = models.TextField(max_length=200)
    
    def __str__(self):
        return self.nama

class Peta(models.Model):
    nama_id = models.ForeignKey(Wisata, on_delete=models.CASCADE, null=True)
    koordinat = models.CharField(max_length=150)
    alamat = models.CharField(max_length=200)
