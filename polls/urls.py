from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # djangoがマッチする正規表現を見つけるとdjangoは指定されたビュー関数を呼び出す。
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
