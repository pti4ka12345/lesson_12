# В данном задании вам предстоит инициализировать 
# Flask-приложение, а также создать 3 view-функции, которые:
#
# 1. При переходе в бразузере на по адресу 127.0.0.1:5000 
#    отображает надпись "Главная страничка".
#
# 2. При переходе в бразузере на по адресу 127.0.0.1:5000/catalog/ 
#    отображает надпись "Страничка каталога".
#
# 3. При переходе в бразузере на по адресу 127.0.0.1:5000/settings/ 
#    отображает надпись "Страничка настроек".
#
# P.S. В данном задании каждую надпись необходимо отобразить.
#      на странице как заголовок первого уровня, 
#      (используя язык html разметки).
#
#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def page_index():
   return "<h1>Главная страничка</h1>"

@app.route("/catalog/")
def page_catalog():
   return "<h1>Страничка каталога</h1>"

@app.route("/settings/")
def page_settings():
   return "<h1>Страничка настроек</h1>"

app.run()