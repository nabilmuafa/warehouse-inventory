# [Warehouse Inventory]()

Proyek Django untuk Tugas 2 mata kuliah Pemrograman Berbasis Platform Ganjil 2023/2024. Dibuat oleh Muhammad Nabil Mu'afa - 2206024972

### Bagaimana cara saya mengimplementasi checklist yang ada?

<details>
<summary>Membuat proyek Django</summary>
Langkah pertama, saya membuat sebuah repository kosong di GitHub yang saya beri nama `warehouse-inventory`. Repository kosong ini kemudian saya clone ke local saya. Saya menggunakan environment Linux (menggunakan WSL) untuk mendevelop proyek ini.

Setelah repository saya clone ke local, saya menjalankan command:

```
python3 -m venv env
```

untuk membuat virtual environment. Hal ini diperlukan untuk memisahkan/mengisolasi dependency dari proyek-proyek berbeda. Kemudian saya mengaktifkannya dengan menjalankan command:

```
source env/bin/activate
```

Menggunakan terminal Linux, saya membuat file `requirements.txt` menggunakan command `nano requirements.txt`, dan meng-copy-paste requirements yang dibutuhkan untuk proyek ini dari tutorial. Setelah itu, saya menginstall dependencies yang dibutuhkan dengan menjalankan:

```
pip3 install -r requirements.txt
```

Command ini sekaligus menginstall module Django di virtual environment.

Untuk membuat sebuah proyek Django pada repository ini, saya menjalankan command

```
django-admin startproject warehouse_inventory .
```

Command ini membuat suatu folder bernama `warehouse_inventory` yang isinya file-file yang diperlukan dalam skala proyek.

Setelah itu, saya mengubah `ALLOWED_HOSTS` di file `settings.py` dengan menambahkan `"*"` agar proyek ini bisa dijalankan di host/domain apapun.

Setelah itu saya menguji deploy di localhost dengan menjalankan:

```
python3 manage.py migrate && python3 manage.py runserver
```

di root folder proyek. Deploy berhasil.

</details>
<details>
<summary>Membuat Aplikasi Main</summary>

Setelah proyek berhasil dijalankan, saya membuat aplikasi `main` dengan menjalankan:

```
python3 manage.py startapp main
```

Terbentuk folder baru bernama `main` di root repository proyek. Saya kemudian menambahkan nama aplikasi ini ke list `INSTALLED_APPS` yang dapat ditemukan di file `settings.py` pada folder `warehouse_inventory`.

</details>
<details>
<summary>Melakukan routing pada proyek</summary>

Agar proyek dapat menjalankan aplikasi `main`, route proyek perlu dikonfigurasi. Untuk ini, saya menambahkan beberapa hal pada `urls.py` di folder proyek (`warehouse_inventory`). Yang saya tambahkan adalah `include` pada baris

```
from django.urls import path, include
```

agar file routing ini dapat mengimpor route yang sudah didefinisikan oleh aplikasi lain. Kemudian, pada variabel `urlpatterns`, saya menambahkan:

```python
path('', include(main.urls))
```

Yang baris ini lakukan adalah menjadikan path URL utama dari proyek ini langsung mengarah ke route yang akan didefinisikan pada file rute tingkat aplikasi (`urls.py` di direktori `main`). Pada tutorial, path yang digunakan adalah `/main`, namun saya ingin ketika aplikasi saya dibuka, halaman aplikasi `main` langsung muncul tanpa user perlu menambahkan rute `/main` di address bar, sehingga saya gunakan path `''`.

</details>
<details>
<summary>Membuat model pada aplikasi main</summary>

Untuk membuat model, saya memodifikasi file `models.py` yang terdapat pada folder `main`. Berikut adalah kode yang saya tambahkan:

```python
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```

Model ini saya beri nama Item. Model ini memiliki atribut `name` yang berupa CharField dengan panjang maksimal 255, `amount` yang berupa IntegerField, dan `description` yang berupa TextField. Ketiga atribut tersebut digunakan untuk mendefinisikan sebuah Item yang nanti akan ada pada aplikasi, yaitu nama item, jumlah item di inventory, dan deskripsi item.

Setelah membuat model ini, agar Django dapat menyesuaikan struktur basis data dengan model yang baru dibuat, saya melakukan migrate dengan menjalankan dua command ini:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Dengan ini, penambahan model sudah 'tertanam' pada aplikasi dan basis data sudah disesuaikan.

</details>
<details>
<summary>Membuat fungsi pada views.py</summary>

Setelah mendefinisikan model, saya membuat file `main.html` sebagai template HTML terlebih dahulu, yang akan digunakan untuk men-display halaman app saya. Menggunakan fitur dari Visual Studio Code, saya sekaligus menambahkan beberapa header yang biasanya digunakan di dalam sebuah file HTML:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Warehouse Inventory</title>
  </head>
</html>
```

Pada bagian ini, saya mengatur agar bahasa yang diterima oleh website adalah bahasa Inggris. Kemudian saya mengatur character set yang akan digunakan website yaitu UTF-8, serta mengatur skala konten dan lebar halaman yang ditampilkan sesuai dengan device yang digunakan.

Karena instruksi pada tugas adalah untuk menampilkan nama aplikasi, nama, dan kelas saya, maka saya menambahkan bagian ini pada `main.html`:

```html
<body>
    <h1>{{app_name}}</h1>
    <h5>{{name}}</h5>
    <h5>{{class}}</h5>
</body>
</html>
```

Pada bagian ini, saya langsung menggunakan sintaks Django pada elemen HTML, agar ketika template di-render oleh `views.py`, data yang ditampilkan akan sesuai dengan data yang terdapat di `views.py`, bukan hanya suatu data statik.

Setelah mendefinisikan template, saatnya mengintegrasikan template dengan view. Untuk melakukan hal ini, saya perlu menambahkan fungsi yang akan menampilkan data saya di file `views.py` yang ada di aplikasi `main`. Pada file `views.py`, saya menambahkan kode berikut:

```python
from django.shortcuts import render

def show_main(request):
  context = {
    "app_name": "Warehouse Inventory",
    "name": "Muhammad Nabil Mu'afa",
    "class": "PBP C"
  }

  return render(request, "main.html", context)
```

Pertama, saya mengimpor method `render` dari module `django.shortcuts` agar bisa melakukan render pada template HTML dengan data yang saya punya. Kemudian, saya mendefinisikan fungsi bernama `show_main`. Pada fungsi ini, saya mendefinisikan sebuah dictionary yang isinya adalah data yang ingin saya tampilkan pada app saya dalam bentuk dictionary. Perlu diperhatikan bahwa key dari dictionary ini harus sama dengan variabel yang sudah didefinisikan pada `main.html` di bagian yang memuat sintaks Django, agar value yang berkaitan dapat dirender pada bagian yang sesuai di HTML. Kemudian, saya mengembalikan `render(request, "main.html", context)`, dimana fungsi `render()` inilah yang secara spesifik me-render data pada `context` ke template `main.html` agar ditampilkan sebagai data yang dinamis.

</details>
<details>
<summary>Melakukan routing pada aplikasi main</summary>

Agar aplikasi `main` dapat dijalankan pada proyek, saya perlu konfigurasi routing pada aplikasi `main` itu sendiri. Hal ini saya lakukan dengan menambahkan file `urls.py` di folder `main`. File tersebut diisi dengan:

```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main')
]
```

Dari kode ini, kita memberi nama aplikasi ini dengan `main` pada variabel `app_name`. Untuk mendefinisikan pola URL aplikasi `main`, kita menggunakan `path` dari `django.urls` dan memanggil `path('', show_main, name="show_main")`. Fungsi tersebut mendefinisikan fungsi `show_main` dari `main.views` sebagai tampilan yang akan dimunculkan ketika URL aplikasi diakses.

</details>
