from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Corpus(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #글쓴이
    title = models.CharField(max_length=200) #제목
    created_date = models.DateTimeField(default=timezone.now); #작성일
    published_date = models.DateTimeField(blank=True, null=True) #게시일
    ticker = models.CharField(max_length=20); #아이콘, 카테고리
    content = models.TextField(); #내용

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title