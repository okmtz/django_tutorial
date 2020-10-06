from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # djangoがマッチする正規表現を見つけるとdjangoは指定されたビュー関数を呼び出す。
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
