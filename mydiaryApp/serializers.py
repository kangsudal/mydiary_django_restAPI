from rest_framework import serializers
from .models import Corpus

class CorpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corpus
        fields = ('author','title', 'created_date','published_date','ticker','content')