Djangoをインストールし、"Hello"と表示するシンプルなDjangoアプリケーションを作成する手順を説明します。以下の手順に従ってください：

1. 新しいフォルダを作成し、その中に移動します:

```
mkdir django_hello
cd django_hello
```

2. 仮想環境を作成し、有効化します:

```
python -m venv venv
source venv/bin/activate  # Linuxの場合
# または
venv\Scripts\activate  # Windowsの場合
```

3. Djangoをインストールします:

```
pip install django
```

4. Djangoプロジェクトを作成します:

```
django-admin startproject hello_project .
```

5. アプリケーションを作成します:

```
python manage.py startapp hello_app
```

6. `hello_project/settings.py`を開き、`INSTALLED_APPS`リストに`'hello_app'`を追加します:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello_app',
]
```

7. `hello_app/views.py`を開き、以下のコードを追加します:

```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django!")
```

8. `hello_project/urls.py`を開き、以下のように編集します:

```python
from django.contrib import admin
from django.urls import path
from hello_app.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello, name='hello'),
]
```

9. 開発サーバーを起動します:

```
python manage.py runserver
```

10. ブラウザで`http://localhost:8000`にアクセスすると、"Hello, Django!"というメッセージが表示されます。

これらの手順で、Djangoをインストールし、"Hello"メッセージを表示する基本的なDjangoアプリケーションを作成できます。何か質問や追加の説明が必要な部分はありますか？