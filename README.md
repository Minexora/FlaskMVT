# Flask MVC Model Yapısı

- Model: Veritabanı kodlarının yazıldığı kısımdır.

- View: Template ve Model ile bağlantılı çalışır. Fonksiyonlar view içerisine yazılır, fonksiyonlarda gerekli işlemler yapıldıktan sonra Template içerisinde bulunan HTML dosyalarına yönlendirilir.

- Template: Sayfaların tasarımlarının olduğu ve istemcilere sunulduğu kısımdır. HTML kodları burada yazılır.



## Çalıştırmak için;
```bash 
python -m venv venv # -> Venv oluşturmak için
source venv/(Scripts|bin)/active # -> Venv aktif etmek için
pip install -r req.txt # -> Gereksinimleri indirmek için
export FLASK_APP=main.py
export FLASK_ENV=development
flask initdb #-> Veritabanına tabloları oluşturmak için
flask run # -> Projeyi başlatmak için
```