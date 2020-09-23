from django.db import models

# Create your models here.
# var names below become column names in db
class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE) # fk indicates a 1:m relationship
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)