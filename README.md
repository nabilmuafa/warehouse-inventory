# [Warehouse Inventory](https://warehouse-inventory.adaptable.app)

Proyek Django untuk tugas mata kuliah Pemrograman Berbasis Platform Ganjil 2023/2024. Dibuat oleh Muhammad Nabil Mu'afa - 2206024972

### Daftar Isi

- [README.md Tugas 2](#tugas-2)
  - [Implementasi Checklist Tugas 2](#implementasi-checklist-tugas-2)
  - [Bagan request client ke webapp berbasis Django](#buatlah-bagan-yang-berisi-request-client-ke-web-aplikasi-berbasis-django-beserta-responnya-dan-jelaskan-pada-bagan-tersebut-kaitan-antara-urlspy-viewspy-modelspy-dan-berkas-html)
  - [Mengapa kita menggunakan virtual environment?](#mengapa-kita-menggunakan-virtual-environment-apakah-kita-tetap-dapat-membuat-aplikasi-web-berbasis-django-tanpa-menggunakan-virtual-environment)
  - [MVC, MVT, MVVM](#apakah-itu-mvc-mvt-mvvm-apakah-perbedaan-dari-ketiganya)
- [README.md Tugas 3](#tugas-3)
  - [Implementasi Checklist Tugas 3](#implementasi-checklist-tugas-3)
  - [Perbedaan form POST dan form GET pada Django](#apa-perbedaan-antara-form-post-dan-form-get-pada-django)
  - [Perbedaan XML, JSON, dan HTML](#apa-perbedaan-utama-antara-xml-json-dan-html-dalam-konteks-pengiriman-data)
  - [Mengapa JSON lebih sering digunakan dalam pertukaran data?](#mengapa-json-sering-digunakan-dalam-pertukaran-data-antara-aplikasi-web-modern)
  - [Mengakses URL melalui Postman](#mengakses-url-melalui-postman)
- [README.md Tugas 4](#tugas-4)
  - [Implementasi Checklist Tugas 4](#implementasi-checklist-tugas-4)
  - [Apa itu Django UserCreationForm](#apa-itu-django-usercreationform-dan-jelaskan-apa-kelebihan-dan-kekurangannya)
  - [Perbedaan autentikasi dan otorisasi](#apa-perbedaan-antara-autentikasi-dan-otorisasi-dalam-konteks-django-dan-mengapa-keduanya-penting)
  - [Apa itu cookies dalam konteks aplikasi web](#apa-itu-cookies-dalam-konteks-aplikasi-web-dan-bagaimana-django-menggunakan-cookies-untuk-mengelola-data-sesi-pengguna)
  - [Apakah penggunaan cookies aman secara default](#apakah-penggunaan-cookies-aman-secara-default-dalam-pengembangan-web-atau-apakah-ada-risiko-potensial-yang-harus-diwaspadai)
- [README.md Tugas 5](#tugas-5)
  - [Implementasi Checklist Tugas 5](#implementasi-checklist-tugas-5)
  - [Manfaat dari tiap element selector dan kapan waktu yang tepat untuk menggunakannya](#manfaat-dari-tiap-element-selector)
  - [HTML5 Tag yang saya ketahui](#jelaskan-html5-tag-yang-kamu-ketahui)
  - [Perbedaan antara Margin dan Padding](#jelaskan-perbedaan-antara-margin-dan-padding)
  - [Perbedaan antara framework Tailwind dan Bootstrap](#jelaskan-perbedaan-antara-framework-css-tailwind-dan-bootstrap)

## Tugas 2

### Implementasi Checklist Tugas 2

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

```python
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
<details>
<summary>Melakukan deployment ke Adaptable</summary>

Sebelum melakukan deployment, saya kembali mencoba menjalankan aplikasi di localhost dengan command:

```
python3 manage.py runserver
```

dan aplikasi saya berjalan dengan baik, sehingga sudah bisa saya push ke repository dan saya deploy ke Adaptable. Saya hanya perlu menjalankan command untuk melakukan add, commit, dan push:

```
git fetch
git pull
git add .
git commit -m "create main app"
git push
```

Pada command ini, saya hanya menggunakan `git pull` dan `git push` tanpa perlu men-specify branch yang digunakan karena saya membuat repository di local dengan melakukan clone terhadap yang ada di GitHub, sehingga repository local saya sudah di-set untuk track remote repository yang terdapat di GitHub.

Setelah itu, seperti tutorial pertama, saya melakukan deploy di Adaptable. Saya menggunakan Python App Template dengan PostgreSQL dengan skema database yang digunakan. Command untuk menjalankan aplikasi yang saya gunakan adalah:

```
python manage.py migrate && gunicorn warehouse_inventory.wsgi
```

Setelah menunggu sekitar 5 menit, aplikasi saya sudah terdeploy dan bisa dilihat pada [website ini](https://warehouse-inventory.adaptable.app).

</details>

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.

![](https://cdn.discordapp.com/attachments/1133956580728127550/1151007158771654778/image.png)

Ketika user mengakses aplikasi, request akan dikirimkan ke `urls.py`. File `urls.py` mengolah request dan meneruskan request tersebut ke `views.py` yang bersangkutan, yaitu `views.py` dari halaman yang di-request oleh user.

`views.py` kemudian berkomunikasi dengan `models.py`, dimana `models.py` berkomunikasi dengan database untuk meminta dan menerima data apabila ada data yang dibutuhkan dari database berdasarkan request user.

Setelah data diterima, data akan diteruskan untuk dimasukkan oleh `views.py` ke template HTML yang sudah disediakan. Setelah template dengan data sudah di-render, halaman tersebut akan dikembalikan kepada user sebagai HTML response untuk diakses oleh user.

### Mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan agar dependency antar proyek-proyek yang berbeda dapat diisolasikan dan tidak terjadi konflik, terutama konflik versi. Selain itu, menggunakan virtual environment dapat mempermudah collaborative work. Apabila user lain ingin memodifikasi suatu aplikasi kemudian melakukan tes dengan menjalankannya, mereka hanya perlu membuat dan mengaktifkan virtual environment, kemudian menginstall requirements yang diperlukan untuk bisa menjalankan aplikasinya di komputer mereka. Apabila terdapat perbedaan versi dependency pada komputer berbeda, hal ini bisa diatasi dengan virtual environment.

Virtual environment bukan suatu hal yang wajib untuk membuat aplikasi Django, tetapi akan cukup sulit untuk memperbaiki apabila terdapat konflik versi antara dependency proyek dan dan versi yang terinstall di komputer.

### Apakah itu MVC, MVT, MVVM? Apakah perbedaan dari ketiganya?

#### MVC

MVC adalah salah satu pola desain arsitektur pada sebuah aplikasi. MVC memisahkan sebuah aplikasi menjadi tiga komponen, yaitu **Model**, **View**, dan **Controller**. Pada arsitektur MVC, komponen Model bertugas sebagai komponen yang mengelola segala macam logic terkait data yang dibutuhkan user. Sementara itu, komponen View bertugas sebagai komponen yang mengelola logic UI dari aplikasi. Terakhir, controller berfungsi sebagai perantara antara Model dan View. Komponen controller memproses request, memanipulasi data menggunakan Model dan berinteraksi dengan View untuk me-render halaman web yang bersesuaian dengan apa yang direquest user.

#### MVT

MVT adalah pola desain arsitektur software yang digunakan oleh framework Django. MVT adalah singkatan dari **Model**, **View**, **Template**, yang merupakan komponen-komponen pada arsitektur ini. Mirip dengan arsitektur MVC, Model pada arsitektur ini berfungsi sebagai komponen yang mengelola logic terkait data yang dibutuhkan user dari basis data. Akan tetapi, pada arsitektur ini, View berfungsi sebagai jembatan/perantara antara Model dan template. View mengelola request dari user, berkomunikasi dengan Model untuk mengambil data yang diperlukan dari database, kemudian merender data tersebut ke template untuk dikembalikan ke user. Sementara itu, template berfungsi sebagai komponen yang mengelola UI dari aplikasi, seperti komponen statisnya yang terdapat di dalam HTML.

#### MVVM

MVVM adalah pola desain arsitektur software lain yang diciptakan oleh arsitek software Microsoft. MVVM memisahkan aplikasi menjadi tiga komponen, yaitu **Model**, **View**, dan **ViewModel**. Pada arsitektur ini, Model berperan sebagai komponen yang mengelola data. Berbeda dengan arsitektur-arsitektur sebelumnya, pada arsitektur ini Model tidak berkomunikasi dengan View. Bahkan Model dianggap "tidak mengetahui" bahwa ada View. Begitu pula dengan View, pada arsitektur ini View hanya berfungsi sebagai user interface dan tidak memiliki logic aplikasi. Logic yang dimiliki oleh View hanyalah ketika user berinteraksi dengannya, View akan menotifikasi ViewModel. ViewModel pada arsitektur ini berperan sebagai link antara View dan ViewModel. ViewModel mengimplementasikan data binding dan berbagai macam instruksi kepada View, serta mengupdate Model apabila diketahui terdapat interaksi pada View. Apabila terdapat perubahan pada Model atau interaksi pada View, ViewModel akan mengirimkan notifikasi kepada View ataupun Model dengan event notifikasi.

#### Perbedaan di antara ketiganya

Hal mendasar yang membedakan MVT dengan arsitektur lain adalah adanya Template sebagai bagian yang penting dari arsitekturnya yang menyimpan struktur UI dan presentasinya. Arsitektur ini juga memisahkan Template dengan View. Pada arsitektur MVC, yang menjadi pembeda adalah adanya separation of concerns yang lebih jelas, yaitu View yang mengelola UI, Model yang mengelola data, dan Controller yang mengelola interaksi user. Terakhir, yang membedakan MVVM dengan arsitektur lainnya adalah sifatnya yang lebih data-driven dalam men-display UI. View dan Model terikat dengan ViewModel, dan setiap perubahan data yang terjadi atau interaksi user akan mengupdate Model dan View secara otomatis.

## Tugas 3

### Implementasi Checklist Tugas 3

<details>
<summary>Menambahkan input form</summary>

Sebelum menambahkan form, karena page utama dan page form akan memiliki bagian atas (`<head>`) yang sama, maka kita bisa menggunakan suatu template lain yang terpisah agar lebih mengefisienkan kode. Untuk itu, saya membuat directory `template/` baru di root project dan mengisinya dengan file `base.html`. Isi file tersebut sebagai berikut:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Warehouse Inventory</title>
    <link
      href="https://cdn.jsdelivr.net/npm/tailwindcss@3.3.3/tailwind.min.css"
      rel="stylesheet"
    />
    <script src="https://cdn.jsdelivr.net/npm/tailwindcss@3.3.3/lib/index.min.js"></script>
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

`base.html` ini menyimpan bagian atas dari suatu page, sehingga bisa kita gunakan untuk membuat page lain yang memiliki bagian atas yang sama dengan cara di-extend pada file template lain.

Sebelum `base.html` bisa digunakan sebagai template, kita perlu melakukan konfigurasi pada settings.py agar `base.html` terdeteksi sebagai template. Berikut adalah baris kode yang saya tambahkan:

```python
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        ...
    }
]
...
```

Setelah ini, `base.html` bisa digunakan sebagai template. Sebelum itu, saya mengubah `main.html` pada `main/templates` terlebih dahulu agar menggunakan `base.html` sebagai template dasarnya:

```html
{% extends 'base.html' %} {% block content %}
<h1 class="font-sans">{{ app_name }}</h1>
<h5>{{ name }}</h5>
<h5>{{ class }}</h5>
{% endblock content %}
```

`main.html` sudah menggunakan `base.html` sebagai template dasarnya. Kita bisa fokus ke form.

Untuk menambahkan form, diperlukan file baru yaitu `forms.py`. Form ini akan digunakan untuk memasukkan entry baru sesuai dengan model yang kita gunakan. Module `ModelForm` akan digunakan sebagai dasar dari form ini. Saya mengisi `forms.py` dengan code berikut:

```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description"]
```

Karena nama model yang saya gunakan adalah `Item`, maka yang saya import pada awal code adalah `Item`. Kemudian saya definisikan class `ItemForm` sebagai form yang akan saya gunakan. Di dalam class ini, terdapat class `Meta` yang memiliki atribut `model` yang isinya adalah model yang saya gunakan, kemudian `fields` yang berisi fields yang akan diinput pada form.

Setelah mendefinisikan `forms.py`, saya kembali memodifikasi `views.py` untuk bisa menampilkan form. Terdapat beberapa bagian yang saya modifikasi.

Pertama, menambahkan import:

```python
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ItemForm
from django.urls import reverse
```

- `HttpResponseRedirect` untuk redirect setelah submit form. `HttpResponse` akan digunakan ketika memroses data ke bentuk JSON dan XML, jadi saya tambahkan dari awal.
- `import ItemForm` mengimport form ke views agar bisa digunakan
- `reverse` mengambil detail url melalui file urls.py

Kedua, menambahkan fungsi:

```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        # stores the last item inserted to current session
        last_entry = Item.objects.latest('id')
        request.session['last_entry'] = {
            "name": last_entry.name,
            "amount": last_entry.amount
        }
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

Secara garis besar, fungsi ini akan menampilkan form dengan membuka page `create_item.html`. Apabila form disubmit (request methodnya POST) dan isinya valid, maka yang diinput akan disimpan ke database kemudian web app akan kembali redirect ke halaman utama. Sebelum kembali ke halaman utama, disini saya mengimplementasikan pesan submit (untuk skor bonus). Saya menyimpan objek terakhir yang disimpan pada form, kemudian saya simpan ke session dari request dengan key `last_entry` dan value berupa dictionary berisi nama barang dan jumlah barang.

Ketiga, saya mengubah fungsi `show_main()`:

```python
def show_main(request):
    items = Item.objects.all()

    context = {
        'app_name': "Warehouse Inventory",
        'name': "Muhammad Nabil Mu'afa",
        'class': "PBP C",
        'items': items,
        # adds the latest entry to parameter if there is one
        'last_entry': request.session.pop('last_entry', None)
    }

    return render(request, "main.html", context)
```

Saya mengambil seluruh objek `Item` yang ada di database, lalu menambahkannya ke `context` sebagai value untuk kemudian ditampilkan di HTML. Saya juga menambahkan key dan value lain, yaitu `last_entry` sebagai item yang terakhir diisi. Untuk mengambil valuenya, saya pop value yang disimpan di session (agar session menjadi kosong) dari request tadi. Sekarang `last_entry` berisi atribut `name` dan `amount` dari item yang terakhir diinput.

Setelah memodifikasi `views.py`, saya memodifikasi `urls.py` yang ada pada `main`. Saya menambahkan dua baris berikut:

```python
from main.views import show_main, create_item

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name="create_item"),
    ...
]
```

Intinya saya mengimport `create_item` dari `views.py` serta menambahkan path untuk page form.

Setelah itu, saya membuat file HTML baru untuk page form yang diberi nama `create_item.html` pada `main/templates`. File tersebut saya isi dengan:

```html
{% extends 'base.html' %} {% block content %}
<h1>Add New Item</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Item" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

Secara garis besar, HTML ini 'mengimpor' `base.html` sebagai template kode, kemudian mendefinisikan content untuk mengisi block content yang sudah didefinisikan pula pada `base.html`. HTML ini membuat page form, dan fields yang didefinisikan pada form di-display dengan mengubahnya menjadi tabel. Halaman ini memiliki CSRF token yang berfungsi sebagai security.

Terakhir, pada `main.html`, saya menambahkan kode berikut di bawah elemen yang sudah ada sebelumnya di dalam `content`:

```html
{% if last_entry %}
<div id="message">
  Kamu menyimpan {{last_entry.amount}} {{last_entry.name}} pada Warehouse
</div>
{% endif %}
<table>
  <tr>
    <th>Name</th>
    <th>Amount</th>
    <th>Description</th>
  </tr>
  {% for item in items %}
  <tr>
    <td>{{item.name}}</td>
    <td>{{item.amount}}</td>
    <td>{{item.description}}</td>
  </tr>
  {% endfor %}
</table>

<br />

<a href="{% url 'main:create_item' %}">
  <button>Add New Product</button>
</a>
```

Secara garis besar, bagian HTML ini menampilkan item yang ada pada database dengan menggunakan sistem tabel dan menambahkan tombol untuk menyimpan item baru pada bagian bawah. Item yang ditampilkan diambil dari value dengan key `items` yang diberikan oleh `views.py` ketika me-render, lalu di-iterasi dengan for loop.

Pada bagian atas, saya menambahkan sebuah if statement yang memeriksa `last_entry`. Apabila `last_entry` tidak kosong, artinya kita sedang di-redirect setelah baru saja menambahkan item (karena session dari request ada isinya), sehingga kode akan memunculkan pesan. Tetapi jika `last_entry` kosong, maka tidak ada item yang baru ditambahkan, sehingga kita tidak perlu menampilkan apa-apa.

</details>
<details>
<summary>Menambahkan fungsi views untuk melihat objek dalam JSON & XML</summary>

> Note: Instruksi pada checklist meminta membuat fungsi views untuk melihat dalam format HTML, tetapi saya asumsikan fungsi show_main() sudah memenuhi karena men-display data dalam bentuk tabel di HTML.

Sebelum bisa menampilkan data dalam kedua format tersebut, saya menambahkan satu module untuk di-import (karena `HttpResponse` sudah di-import di awal):

```python
from django.core import serializers
```

Serializer diperlukan untuk men-'translate' objek pada model menjadi bentuk lain. Dalam kasus ini dapat kita gunakan untuk mentranslate objek menjadi XML dan JSON.

Untuk menampilkan data dalam bentuk XML, saya membuat 2 fungsi pada `views.py`:

```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type="application/xml")
```

Fungsi yang pertama mengembalikan seluruh objek yang ada pada database dalam bentuk XML. Hal ini dilakukan dengan mengambil seluruh objek yang ada pada model, kemudian melakukan serializing terhadap data tersebut menjadi XML, dan diubah menjadi respon HTTP. Fungsi yang kedua pun sama, hanya saja objek yang diambil dilakukan filtering berdasarkan ID, sehingga hanya objek dengan ID yang sama yang akan diambil.

Untuk menampilkan data dalam bentuk JSON, saya membuat 2 fungsi juga pada `views.py`:

```python
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type="application/json")
```

Cara kerjanya sama persis dengan fungsi XML di atas, hanya saja objek di-serialize menjadi JSON.

</details>
<details>
<summary>Membuat routing URL untuk masing-masing views</summary>

Untuk menambahkan routing URL, saya mengimport fungsi-fungsi XML dan JSON yang telah saya buat ke `urls.py`:

```python
from main.views import show_main, create_item, show_xml, show_json, show_json_by_id, show_xml_by_id
```

Kemudian, saya hanya perlu menambahkan path untuk masing-masing fungsi:

```python
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('xml/<int:id>/', show_xml_by_id, name="show_xml_by_id"),
    path('json/<int:id>/', show_json_by_id, name="show_json_by_id")
]
```

Path yang pertama dan kedua adalah untuk menampilkan seluruh data pada database dalam format XML atau JSON, yang menggunakan fungsi `show_xml` dan `show_json` dari views. Path yang ketiga dan keempat adalah untuk menampilkan data berdasarkan id yang di-input pada path dalam format XML atau JSON menggunakan fungsi `show_xml_by_id` dan fungsi `show_json_by_id`. Misalnya, untuk melihat data dengan id 1 dalam bentuk JSON, maka kita dapat membuka url `http://localhost:8000/json/1`, dan seterusnya.

</details>

### Apa perbedaan antara form POST dan form GET pada Django?

| POST                                                                           | GET                                                                                     |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| Ketika disubmit, data dari form disimpan melalui body HTTP request             | Ketika disubmit, data dari form disimpan sebagai parameter query di address bar         |
| Tidak terlihat di URL, sehingga lebih secure untuk informasi sensitif          | Terlihat di URL, sehingga data apapun yang diproses dapat dilihat                       |
| Request POST tidak di-cache, sehingga data request tidak disimpan oleh browser | Request GET bisa di-cache, bisa menimbulkan masalah request berulang kali tanpa sengaja |
| Melakukan request yang sama berulang kali bisa memberikan hasil berbeda        | Melakukan request yang sama berulang kali tetap memberikan hasil yang sama              |

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

HTML digunakan untuk menampilkan data yang telah diproses. XML adalah bahasa markup dengan data yang terstruktur seperti pohon dari root, branch, hingga leaves dan menggunakan tag. JSON digunakan untuk menyimpan dan mengirimkan data dan menggunakan pasangan key-value. XML dan JSON keduanya sama-sama digunakan untuk menyimpan atau mengirimkan data.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON memiliki struktur yang jauh lebih simple, human-readable dan machine-readable karena menggunakan pasangan key-value, sehingga lebih mudah untuk membaca objek-objeknya (parse) atau menulis ke file JSON. Bahkan di bahasa seperti Python, file JSON dapat diubah menjadi dictionary Python karena adanya kesamaan struktur yang menggunakan pasangan key-value.

### Mengakses URL melalui Postman

#### GET / (HTML)

![](https://media.discordapp.net/attachments/1133956580728127550/1153757084467339294/image.png?width=954&height=595)

#### GET /json (JSON)

![](https://media.discordapp.net/attachments/1133956580728127550/1153757155351080970/image.png?width=954&height=595)

#### GET /json/1 (JSON)

![](https://media.discordapp.net/attachments/1133956580728127550/1153757201027043429/image.png?width=954&height=595)

#### GET /xml (XML)

![](https://media.discordapp.net/attachments/1133956580728127550/1153757245096591401/image.png?width=954&height=595)

#### GET /xml/1 (XML)

![](https://media.discordapp.net/attachments/1133956580728127550/1153757302176878603/image.png?width=954&height=595)

## Tugas 4

### Implementasi Checklist Tugas 4

<details>
<summary>Mengimplementasikan fungsi registrasi, login, dan logout</summary>

Untuk fungsi registrasi, saya menambahkan fungsi ini di `views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
...
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {"form": form}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return render(request, "register.html", context)
```

Fungsi ini membuat halaman form register. Apabila method request user adalah POST, form akan diperiksa validitasnya, kemudian jika valid data yang diinput akan disimpan ke database (sebagai user baru). Page akan redirect ke login.

Saya menambahkan logic baru di bagian bawah, dimana apabila user sedang terautentikasi dengan suatu akun, mereka akan ter-redirect ke main apabila mereka ingin mengakses halaman register. Jika tidak, halaman `register.html` akan dirender dengan form.

Karena file terlalu panjang, implementasi `register.html` yang berada di directory `main/templates` dapat dilihat pada [file ini](/main/templates/register.html). Pada tutorial, form diubah menjadi tabel dengan `form.as_table`. Akan tetapi, saya menjabarkan form tersebut dengan cara meng-copy source code dari form yang sudah dibentuk menjadi tabel sehingga tiap-tiap elemennya bisa diberikan styling. Saya menggunakan Tailwind CSS untuk styling.

Saya juga memberikan fungsionalitas menampilkan pesan error pada bagian berikut di `register.html`:

```html
{% if form.errors %}
<tr>
  <td>
    <ul class="pt-2">
      {% for _,error in form.errors.items %}
      <li class="text-red-500 text-sm text-center">{{ error }}</li>
      {% endfor %}
      <li class="text-red-500 text-sm text-center">Please try again.</li>
    </ul>
  </td>
</tr>
{% endif %}
```

Bagian ini akan menampilkan pesan error saat register apabila response dari form juga membawa error.

Untuk fungsi login, saya menambahkan fungsi ini di `views.py`:

```python
from django.contrib.auth import authenticate, login, logout
...
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:show_main'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:show_main'))
    else:
        return render(request, "login.html", context)
```

Fungsi ini membuat halaman login. Apabila request method dari user adalah POST, maka username dan password yang diinput oleh user akan diambil dari request untuk kemudian di authenticate. Apabila authentication berhasil, instance akun user akan diambil dari database kemudian dilakukan login. User akan di-redirect ke halaman utama dengan cookie yang di-set ke waktu terakhir login. Apabila authentication gagal, akan ada pesan username/password salah.

Sama seperti register, saya mengimplementasikan logic baru pada akhir kode, dimana user tidak bisa mengakses halaman login apabila dalam keadaan authenticated. User akan di redirect ke main. Jika user tidak authenticated, halaman `login.html` akan dirender.

Karena file terlalu panjang, implementasi `login.html` yang berada di directory `main/templates` dapat dilihat pada [file ini](/main/templates/login.html). Saya menggunakan Tailwind CSS untuk memberikan styling pada halaman ini. Sama seperti halaman register, saya menambahkan fungsionalitas menampilkan pesan error:

```html
{% if messages %}
<tr>
  {% for message in messages %}
  <td class="text-red-500 text-center pt-2">{{ message }}</td>
  {% endfor %}
</tr>
{% endif %}
```

Apabila terdapat `messages` di request, maka akan ditampilkan di halaman ini, baik sebagai pesan error maupun pesan sukses membuat akun.

Pada halaman login, saya menambahkan tombol untuk ke halaman register apabila user belum memiliki akun, begitupun sebaliknya pada halaman register.

Untuk fungsi logout, saya menambahkan fungsi ini di `views.py`:

```python
from django.contrib.auth import authenticate, login, logout
...
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Fungsi ini akan memanggil fungsi logout dari Django untuk melakukan logout pada user. Setelah logout, user akan di-redirect ke halaman login, dan cookie dari user akan dihapus.

Pada `main.html`, saya memberikan tombol logout dengan icon "keluar pintu" yang menandakan logout di sebelah kanan atas halaman. Implementasinya seperti ini:

```html
...
<a class="hover:text-blue-500 pb-1" href="{% url 'main:logout' %}">
  <svg
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    viewBox="0 0 24 24"
    stroke-width="1.5"
    stroke="currentColor"
    class="w-6 h-6"
  >
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      d="M15.75 9V5.25A2.25 2.25 0 0013.5 3h-6a2.25 2.25 0 00-2.25 2.25v13.5A2.25 2.25 0 007.5 21h6a2.25 2.25 0 002.25-2.25V15m3 0l3-3m0 0l-3-3m3 3H9"
    />
  </svg>
</a>
```

Saya menggunakan SVG yang saya temukan online untuk menampilkan icon. Tombol ini berada di block header yang juga saya fungsikan sebagai navigation bar.

Setelah membuat tiap fungsi dan halaman tersebut, saya menambahkan pathnya ke `urls.py`:

```python
from django.urls import path
from main.views import ..., register, login_user, logout_user, ...

urlpatterns = [
  ...
  path('register/', register, name="register"),
  path('login/', login_user, name="login"),
  path('logout/', logout_user, name="logout"),
  ...
]
```

Setiap halaman sekarang sudah bisa diakses dan sistem autentikasi sudah selesai. Sebagai tambahan, saya menambahkan bagian kode ini pada `views.py` untuk merestriksi akses user ke halaman utama (harus logged in):

```python
from django.contrib.auth.decorators import login_required
...
@login_required(login_url='/login')
def show_main(request):
  ...
```

Apabila user belum terautentikasi, maka user akan di-redirect ke page login jika mencoba untuk mengakses halaman utama.

</details>
<details>
<summary>Menampilkan detail informasi pengguna yang sedang logged in, menerapkan cookies</summary>

Pada fungsi `login_user` di `views.py` tadi, saya memiliki bagian berikut:

```python
import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
...
def login_user(request):
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse('main:show_main'))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
```

Pada bagian ini, apabila user berhasil login (akunnya sudah terautentikasi), maka akan ditambahkan cookie pada response yang valuenya berupa waktu kapan user terakhir kali login.

Pada fungsi `show_main` di `views.py`, saya menambahkan baris ini pada `context`:

```python
context = {
    ...
    'last_login': request.COOKIES['last_login'],
    }
```

Baris ini akan mengambil nilai cookie yang memiliki nama `last_login` lalu memberikannya kepada response yang akan ditampilkan pada halaman utama.

Pada fungsi `logout()` di `views.py` tadi, saya juga memiliki bagian ini:

```python
from django.contrib.auth import authenticate, login, logout
...
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Apabila user logout, maka cookie dari user yang terkait akan dihapus dari response.

Kemudian pada halaman utama, saya menambahkan bagian ini di dekat tombol logout, untuk menampilkan cookies berupa kapan terakhir user login:

```html
<div class="flex flex-col items-end">
  ...
  <p class="text-xs pt-2">Last login: {{last_login}}</p>
</div>
```

Sekarang cookie sudah dapat dilihat apabila user melakukan login.

</details>
<details>
<summary>Membuat dua akun pengguna & 3 dummy data</summary>

Saya membuat dua akun dengan username `nabilmuafa` dan `cicakbinkadal` _(matkul OS reference, saya sih bukan cbkadal)_. Untuk setiap akun, saya sudah menambahkan 3 data:
![](https://media.discordapp.net/attachments/1133956580728127550/1156405550410641458/image.png?ex=6514da18&is=65138898&hm=09b4cfa968932b524a9f0a3f0d0477b491062da9516683ffb90879a52f243b04&=&width=1241&height=434)
![](https://media.discordapp.net/attachments/1133956580728127550/1156405899884245082/image.png?ex=6514da6b&is=651388eb&hm=c7d61cee7612677e043930d8ca6ff9417667e8ea2fe266a92d9319f19e14f343&=&width=1241&height=392)

</details>
<details>
<summary>Menghubungkan model Item dengan User</summary>

Pada `models.py`, saya menambahkan bagian-bagian ini:

```python
from django.contrib.auth.models import User
...
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Saya menambahkan field `user` pada setiap model menggunakan `ForeignKey` sebagai relationship untuk meng-assign setiap objek dari model ke user yang membuat objeknya.

Kemudian pada `views.py` tepatnya di fungsi `create_product`, saya memodifikasi cara penyimpanan objeknya sebagai berikut:

```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        last_entry = Item.objects.latest('id')
        messages.info(request, f"Kamu telah menyimpan {last_entry.name} sebanyak {last_entry.amount} di Warehouse Inventory!")
        return HttpResponseRedirect(reverse('main:show_main'))
    ...
```

Pada bagian ini, setiap `item` yang dibuat akan disimpan terlebih dahulu ke suatu variabel tanpa langsung "commit" atau disimpan ke database. Pada variabel tersebut, field user akan di-assign dengan user yang melakukan POST request. Barulah item akan disimpan ke database.

Terdapat sedikit perubahan dari cara saya menampilkan pesan "telah menyimpan barang" dibanding pada tugas sebelumnya, yaitu sekarang saya menggunakan `messages.info()` untuk menambahkan pesan ke request. Ketika request redirect dari `create_item` didisplay ke halaman utama, maka pesan "telah menyimpan" tersebut akan muncul, tetapi akan hilang setelah di-refresh.

Kemudian, saya memodifikasi fungsi `show_main`:

```python
def show_main(request):
    items = Item.objects.filter(user=request.user)

    context = {
        'app_name': "Warehouse Inventory",
        'name': request.user.username,
        ...
    }
```

Melalui kode ini, objek `Item` yang akan ditampilkan hanyalah punya user yang terautentikasi (dengan mem-filter objek-objek `Item` berdasarkan field user yang disesuaikan dengan user pada request). Field `name` pada `context` juga nilainya saya ubah menjadi nama user yang sedang terautentikasi pada request.

Setelah perubahan ini, saya lakukan migrasi. Sama seperti di tutorial, muncul sebuah error yang meminta default value (saya tidak screenshot, tetapi messagenya sama persis). Saya masukkan 1 sebagai default value dan web app sudah berfungsi dengan selayaknya.

</details>
<details>
<summary>Bonus</summary>

Untuk mengimplementasikan tombol menambahkan dan mengurangi amount, saya membuat dua fungsi baru di `views.py`:

```python
def decrement(request, id):
    item = Item.objects.get(pk=id)
    if item.amount == 1:
        messages.info(request, "Jumlah item tidak boleh kurang dari 1!")
    else:
        item.amount -= 1
        item.save(update_fields=["amount"])
    return HttpResponseRedirect(reverse("main:show_main"))

def increment(request, id):
    item = Item.objects.get(pk=id)
    item.amount += 1
    item.save(update_fields=["amount"])
    return HttpResponseRedirect(reverse("main:show_main"))
```

Intinya, setiap fungsi akan mengambil objek sesuai id yang direquest, kemudian menambahkan atau mengurangi amountnya sesuai dengan fungsi yang digunakan. Pada fungsi `decrement`, ada logic yang membatasi bahwa setiap item jumlahnya tidak boleh kurang dari 1, sehingga jika user tetap memaksa menguranginya, akan dimunculkan pesan error dan jumlah tidak akan berkurang.

Pada `views.py`, saya juga membuat fungsi untuk menghapus sebuah item:

```python
def delete(request, id):
    Item.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse("main:show_main"))
```

Fungsi ini akan mengambil item sesuai id yang direquest kemudian menghapusnya dari database.

Setelah membuat fungsi-fungsi ini, saya melakukan routing pada `urls.py` agar fungsi-fungsi ini dapat diakses:

```python
from django.urls import path
from main.views import ..., decrement, increment, delete

urlpatterns = [
  ...
  path('dec/<int:id>/', decrement, name="dec"),
  path('inc/<int:id>/', increment, name="inc"),
  path('delete/<int:id>/', delete, name="delete"),
  ...
]
```

Kemudian saya menambahkan tombol-tombolnya pada `main.html` (pada for loop dalam iterasi setiap objek barang):

```html
<div class="h-80 bg-white border-2 border-gray-200 rounded-lg p-6">
  <p class="flex text-xl justify-between font-bold">
    {{item.name}}
    <a class="hover:text-red-500" href="delete/{{item.pk}}">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-6 h-6"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
        />
      </svg>
    </a>
  </p>
  <p class="flex items-center font-medium text-lg gap-3 py-4">
    <a class="rounded-full hover:bg-gray-300" href="dec/{{item.pk}}">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-6 h-6"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M18 12H6" />
      </svg>
    </a>
    {{item.amount}}
    <a class="rounded-full hover:bg-gray-300" href="inc/{{item.pk}}">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="w-6 h-6"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M12 6v12m6-6H6"
        />
      </svg>
    </a>
  </p>
  <p>{{item.description}}</p>
</div>
```

Menggunakan icon SVG yang dapat saya temukan online, kira-kira penampilannya seperti ini:

![](https://media.discordapp.net/attachments/1133956580728127550/1156433014537076786/image.png?ex=6514f3ac&is=6513a22c&hm=1cbeabb8b8c9290cde5faa9f04f9e0ae6e186e13a05c92526c3fb845996427ae&=)

</details>

### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

`UserCreationForm` adalah sebuah class dari Django yang dapat digunakan untuk membuat form registrasi user. Pada umumnya, `UserCreationForm` memiliki tiga field untuk diisi, yaitu `username`, `password1`, dan `password2` (untuk konfirmasi). Sebagai class milik Django, `UserCreationForm` memiliki kelebihan yaitu integrasinya terhadap database, sehingga kita tidak perlu membuat fungsionalitas registrasi dari awal dan secara manual menghubungkannya dengan database. Akan tetapi, `UserCreationForm` yang polos hanya memiliki 3 field secara default, sehingga apabila kita mau menambahkan field lain, ujung-ujungnya kita harus mendefinisikan class kita sendiri yang meng-inherit `UserCreationForm`. Singkatnya, `UserCreationForm` memiliki kelebihan yaitu integrasinya dengan database, serta kekurangan yaitu sedikitnya field-field yang tersedia by default.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi adalah proses memverifikasi identitas pengguna yang mencoba mengakses aplikasi Django (misalnya menggunakan username dan password), sementara otorisasi adalah proses memverifikasi dan mengendalikan konten apa saja yang bisa seorang pengguna akses sesuai dengan haknya setelah pengguna berhasil autentikasi (misalnya dengan membedakan user group). Keduanya saling melengkapi, autentikasi diperlukan agar kita bisa memastikan bahwa seseorang yang mengakses suatu akun memang "orang yang seharusnya", serta otorisasi diperlukan agar akses pengguna dapat dikendalikan dan pengguna tidak mengakses hal-hal yang tidak seharusnya mereka akses sesuai dengan haknya.

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

Cookies adalah sebuah data kecil yang dikirim oleh server kepada browser kemudian disimpan pada client-side, untuk kemudian dikirim kembali ke server ketika browser melakukan request ke server. Cookies digunakan untuk mengelola data sesi dari setiap pengguna sebagai bentuk 'identifikasi' bahwa suatu permintaan datang dari pengguna siapa dalam sesi mana.

Pada Django, ketika seorang user sudah terautentikasi, maka cookie dengan nama `sessionid` dan value yang terenkripsi akan terbentuk. Cookie tersebut mengidentifikasi sesi seorang pengguna sehingga server dapat mengetahui dari pengguna mana sebuah request datang. Ketika user tersebut logout, `sessionid` tersebut akan dihapus. Ketika user login lagi, `sessionid` akan berubah namun tetap dapat digunakan untuk mengidentifikasi sesi mana dan user siapa yang melakukan request.

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Dalam konteks Django, cookie yang dihasilkan sudah di-generate secara otomatis, sehingga seharusnya cenderung aman. Akan tetap, terdapat risiko yang harus diwaspadai apabila website dikembangkan tanpa framework. Apabila cookie yang menyimpan sesi seorang user tidak dienkripsi dengan baik, seorang pengguna bisa saja mengganti cookie-nya menjadi value dari sesi pengguna lain dengan mengenkripsi sebuah data, sehingga request dari pengguna tersebut seolah-olah datang dari pengguna lain yang bisa saja akunnya memiliki akses lebih tinggi.

Sebagai contoh, misalkan ada cookie yang bernama `is_admin` dengan nilai `ZmFsc2U=` yang mengidentifikasi apakah seorang user merupakan admin. Bila diperhatikan, nilai `ZmFsc2U=` merupakan string yang terenkripsi dalam Base64, dan apabila di-decipher, artinya adalah `false`. Seorang user bisa saja mengenkripsi `true` ke Base64 menjadi `dHJ1ZQ==` kemudian mengubah nilai cookienya menjadi string tersebut. Dengan begitu, nilai asli cookie `is_admin` akan bernilai `true` dan user bisa mendapatkan akses admin.

## Tugas 5

### Implementasi Checklist Tugas 5

<details>
<summary>Kustomisasi halaman login, register, dan tambah inventori</summary>

Dalam melakukan kustomisasi, saya menggunakan Tailwind CSS.
Berikut source code dari halaman login: [login.html](/main/templates/login.html)

![](https://media.discordapp.net/attachments/1133956580728127550/1158951033750433862/image.png?ex=651e1cc2&is=651ccb42&hm=59f19ec5184586a345efe1e85d44bc0c8db4d14fa42335483b490b9d4b5870a8&=&width=1179&height=566)
![](https://media.discordapp.net/attachments/1133956580728127550/1158951146132615178/image.png?ex=651e1cdd&is=651ccb5d&hm=0dafc33598e4d7e68c3f26d6dbc6a043eb1b5e50b56ef0038d191e8250c01f68&=&width=254&height=566)

Berikut source code dari halaman register: [register.html](/main/templates/register.html)

![](https://media.discordapp.net/attachments/1133956580728127550/1158951275891806329/image.png?ex=651e1cfc&is=651ccb7c&hm=ac9681baa24bd91cb0d84bd59fb13e62ae469b0c7d2583b6f2d73efdd1e1c23e&=&width=1183&height=566)
![](https://media.discordapp.net/attachments/1133956580728127550/1158952054631452773/image.png?ex=651e1db6&is=651ccc36&hm=1a3581e21cd852f789ed89748edd2b0ab516e78f87d12fc50a240b101df60a6c&=&width=251&height=565)

Berikut source code dari halaman tambah inventori: [create_item.html](/main/templates/create_item.html)

![](https://media.discordapp.net/attachments/1133956580728127550/1158953173772402768/image.png?ex=651e1ec0&is=651ccd40&hm=9df8a74d8c607970016c72969ec00e140c50b2820b907ef781f79307b1760a87&=&width=1179&height=566)
![](https://media.discordapp.net/attachments/1133956580728127550/1158953307927216308/image.png?ex=651e1ee0&is=651ccd60&hm=49a9af55456f5fccf5c401e5970dc5ca7886e5ef000e4a175d5b4bdd213278a0&=&width=257&height=566)

- Setiap label dan input box saya pisah menjadi setiap baris tabel. Seisi tabel tersebut diletakkan dalam satu card besar yang didalamnya diberikan padding.
- Untuk halaman yang menggunakan `{{form.as_table}}`, saya memecah tabel tersebut untuk bisa di-styling tiap bagiannya kemudian menjadikan setiap komponen setiap baris berbeda. Caranya dengan membukanya di browser, kemudian meng-copy source code dari tampilan yang terbentuk dari `{{form.as_table}}` dan hanya memodifikasi strukturnya tanpa memodifikasi atribut-atributnya.
- Untuk halaman login dan register, pesan error atau pesan sukses akan ditampilkan di bawah tombol login/register, masih didalam card besar.
- Halaman login dan register saling memiliki referensi ke masing-masing, pada halaman login terdapat link ke halaman register dan sebaliknya.
</details>
<details>
<summary>Kustomisasi halaman daftar inventori</summary>

Berikut source code dari halaman utama (daftar inventori): [main.html](/main/templates/main.html)

![](https://media.discordapp.net/attachments/1133956580728127550/1158949983341531226/image.png?ex=651e1bc8&is=651cca48&hm=8590c0e9453b08004a23eb23fac57b48fe41be84b1c652ffded985eff6beda26&=&width=1181&height=566)
![](https://media.discordapp.net/attachments/1133956580728127550/1158950070960537640/image.png?ex=651e1bdd&is=651cca5d&hm=e0111fe54d94431c008d34b0842533737ce6e914bb91b588b07c504598582929&=&width=255&height=566)

- Saya menambahkan navbar. Di sebelah paling kiri terdapat nama aplikasi yang juga link ke halaman utama. Di sebelah paling kanan, terdapat informasi user dan tombol logout. Pada mobile design, terdapat tombol add item di tengah navbar, serta tombol logout di kanan berada di sebuah dropdown yang muncul apabila icon user ditekan.
- Pada desktop design, tombol add new item berada tepat di bawah navbar, sebelum list dari tiap-tiap barang. Pada mobile design, tombol ini tidak ada dan digantikan dengan tombol yang ada pada tengah navbar.
- Setiap item ditampilkan sebagai suatu card (self-defined menggunakan Tailwind). Pada card tersebut terdapat nama item, jumlah yang bisa di-decrement atau increment, tombol hapus, dan deskripsi barang. Pada desktop design, setiap baris akan menampilkan 3 card/3 item, tetapi pada mobile design setiap baris hanya akan menampilkan 1 item.
</details>

### Manfaat dari tiap element selector

- Universal selector:

```css
* {
  ...;
}
```

Universal selector memilih semua elemen yang terdapat pada suatu halaman HTML dan meng-apply semua style yang didefinisikan didalamnya. Selector ini cocok digunakan apabila kita ingin meng-apply suatu style pada keseluruhan bagian website, misalnya font, warna background, dan sebagainya.

- Inline styles

```html
<h1 style="color: black"></h1>
```

Inline styles adalah selector yang digunakan langsung pada elemen spesifik yang ingin kita ubah penampilannya dalam bentuk atribut pada HTML tag. Dapat digunakan apabila kita ingin override style-style yang sudah didefinisikan, karena inline styles memiliki presedensi/prioritas tertinggi.

- ID selector

```css
#test {
  color: green;
}
```

ID selector hanya memilih elemen dengan ID tertentu untuk memberikan style yang lebih spesifik juga. Karena ID selector memiliki presedensi/prioritas tertinggi kedua setelah inline styles, ID selector dapat digunakan apabila kita ingin override style lain yang sudah didefinisikan SELAIN style yang ada pada inline styles. Karena ID bersifat unik untuk setiap elemen, maka ID selector bersifat cukup spesifik.

- Class selector

```css
.test {
  color: blue;
}
```

Class selector memilih elemen yang memiliki class-class yang sama untuk diberikan style. Tipe selector ini paling umum digunakan dalam CSS karena style yang diberikan dapat di-apply secara keseluruhan pada halaman web hanya dengan memberikan class-class yang sesuai pada elemen yang sesuai pula. Cocok digunakan apabila kita ingin memberikan style yang sama pada beberapa elemen dengan style yang sama.

- Element selector

```css
h1 {
  color: red;
}
```

Element selector memilih elemen-elemen HTML dan meng-apply efek tersebut ke seluruh elemen yang bertipe sama. Cocok digunakan apabila kita ingin memberikan style hanya pada elemen tertentu, misalnya font pada \<h1>, \<p>, dan elemen-elemen lainnya.

### Jelaskan HTML5 Tag yang kamu ketahui

- \<aside>: Digunakan untuk mendefinisikan konten yang tidak terlalu berkaitan dengan konten pada halaman website, misalnya side bar.
- \<header>: Digunakan untuk mendefinisikan bagian atas dari sebuah halaman web.
- \<footer>: Digunakan untuk mendefinisikan bagian bawah dari sebuah halaman web.
- \<section>: Digunakan untuk mendefinisikan section berbeda dari dokumen/halaman web.
- \<nav>: Digunakan untuk mendefinisikan navigation bar.
- \<article>: Digunakan untuk mendefinisikan sebuah bagian konten dari dokumen/halaman web, misalnya artikel koran atau blog.

### Jelaskan perbedaan antara margin dan padding.

Margin memberikan efek berupa memberi jarak antara objek dengan objek lain **di luar** objek tersebut, sementara padding memberikan efek berupa memberi jarak antara border objek dengan objek lain **di dalam** objek tersebut.

Sebagai contoh, kita bisa melihat pada card yang saya definisikan di halaman utama. Meskipun saya tidak menggunakan margin, margin dapat digunakan untuk memberikan jarak antar card. Sementara itu, padding digunakan untuk memberikan jarak antara border objek dengan teks yang ada di dalam card, sehingga teks tidak menempel pada border objek.

### Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap.

| Tailwind CSS                                                                                                         | Bootstrap                                                                                         |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Bersifat utility-first, menggabungkan class-class yang ada untuk membentuk style                                     | Bersifat component-first, menggunakan komponen yang telah didefinisikan                           |
| Pada production build, Tailwind hanya akan menghasilkan CSS yang digunakan (class yang tidak digunakan tidak dibuat) | Menyertakan banyak komponen yang belum tentu digunakan, dapat membuat ukuran halaman lebih besar  |
| Sangat fleksibel dalam kustomisasi, bisa menambahkan class sendiri dan sebagainya                                    | Kustomisasi lebih terbatas, namun sudah menyediakan style dan tema                                |
| Cocok digunakan apabila kita ingin punya kontrol luas terhadap desain, misalnya untuk website dengan desain unik.    | Cocok digunakan untuk proyek yang butuh pengembangan secara cepat dengan komponen yang sudah ada. |
