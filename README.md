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
