# How 2 use django

## 1. python version 3.9.x
```
py --version
```

## 2. create venv (tentukan folder untuk menampung virtual environment)
```
virtualenv -p python3 .
```

## 3. mengaktifkan venv di command prompt

lokasi folder yang dibuka saat ini adalah folder virtual environment yang dibuat
```
Scripts/activate
```

## 4. install django in venv
```
pip install Django
```
catatan: Django yang terinstall hanya ada di dalam virtual environment tidak universal kayaknya...

## 5. clone git ini ke dalam venvnya (ini sama saja kayak django-admin startproject)
masuk ke folder yang ada manage.py di dalamnya lalu run command di command prompt:
```
py manage.py migrate
```

### catatan:
disarankan clone ke folder local kalian dan install github desktop jadi ketika ada update atau tambahan dari kalian cukup upload ke local folder lalu push dari aplikasi github desktopnya atau pull ketika ada yang update di github ini sehingga kalian tidak tertinggal codenya

catatan juga kalo mau push (publish ke github ini) pastikan sudah dicek, apakah sudah bagus untuk dipakai oleh teman-teman yang lain karena ketika sudah dipublish kemungkinan code yang lalu akan overwrite ketika kalian melakukan perubahan pada code yang sudah ada (update)
