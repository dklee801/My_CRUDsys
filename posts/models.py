from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    author = models.CharField('작성자',max_length= 20)
    contents = models.TextField('내용',max_length=1000)

    def __str__(self):
        return self.contents

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
