import datetime

from django.db import models
from django.utils import timezone
# フィールドインスタンスの名前はデータベースも列の名前として使うことになる

class Question(models.Model):
    # 文字フィールド
    question_text = models.CharField(max_length=200)
    # 日時フィールド
    pub_date = models.DateTimeField('date published')

    # __str__()メソッドをモデルに追加する
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Create your models here.
