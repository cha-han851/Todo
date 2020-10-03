from django.db import models
from datetime import date
# Create your models here.
class Todo(models.Model):

  title = models.CharField(max_length=50,null=False)
  text = models.CharField(max_length=200,null=False)
  added_date = models.DateField(null=False)
  time = models.PositiveIntegerField(null=False)
  IMPORTANCE_CHOICE = [
    ('最重要', '最重要'),
    ('重要', '重要'),
    ('急ぎでない', '急ぎでない'),
  ]
  importance = models.CharField(
    choices=IMPORTANCE_CHOICE,
    verbose_name="重要度", max_length= 10,null=False)

  def __str__(self):
        return self.text

  @property
  def is_today(self):
        if date.today() == self.added_date:
            return True
