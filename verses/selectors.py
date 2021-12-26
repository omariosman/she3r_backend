from .models import Verse
import json
from rest_framework import status
from rest_framework.response import Response


def get_random_verse(request):
    print("get random verse selector")
    random_verse = Verse.objects.get(pk=1)
    part_one = random_verse.part_one
    print(part_one)
    part_one_serialized= json.dumps(part_one)
    #response = serializers.serialize('json', [loan1], ensure_ascii=False)
    return Response(part_one_serialized, status=status.HTTP_200_OK)
