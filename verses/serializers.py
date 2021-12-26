from rest_framework import serializers


from .models import Verse

class VerseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verse
        fields = ['part_one','part_two', 'poet']
        
