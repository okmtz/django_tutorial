from django.urls import path

from . import views

urlpatterns = [
    # djangoがマッチする正規表現を見つけるとdjangoは指定されたビュー関数を呼び出す。
    path('', views.index, name='index'),
]
