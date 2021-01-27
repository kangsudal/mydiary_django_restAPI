from django.contrib import admin
from .models import Corpus

# Register your models here.
admin.site.register(Corpus)#관리자 페이지에 Corpus 모델을 register하여 관리할 수 있도록