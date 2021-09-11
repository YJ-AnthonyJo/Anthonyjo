# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
import inspect

class Introduction(models.Model):
    name = models.CharField(max_length=20,default='조용재')
    birthdate = models.DateField()
    hackingnickname = models.CharField(max_length=100, default='An4hoNYJ0')
    selfintroducteion = models.TextField(default=inspect.cleandoc(
        f'''
        Tony Stark가 되고싶은 컴공과생.🤩
        그래서 이름도 anThONY로 지었다는 소문이.. 있지만 사실은 아니라고 한다. 하핳
        '''))
    def __str__(self): 
        return self.name
    def dict__(self):
        return self.__dict__




# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text