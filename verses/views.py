from django.shortcuts import render
from verses.models import Verse

from verses.serializers import VerseSerializer
from .selectors import get_random_verse
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.





#@authentication_classes([authentication.TokenAuthentication])
#@permission_classes([permissions.IsAuthenticated])
class get_random_verse(APIView):
    def get(self, request, format=None):
        response = get_random_verse(request)
        return response

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import random
from random import seed
from random import randint
@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_random_verse2(request):
    #tutorial_data = JSONParser().parse(request)
    queryset_dict = {}
    print("count: ", Verse.objects.all().count())
    table_rows_count = Verse.objects.all().count()
    n = randint(1, table_rows_count)
    print("n: ", n)

    tutorial_data = Verse.objects.get(pk=n)
    #for item in tutorial_data:
    queryset_dict["part_one"] = tutorial_data.part_one
    queryset_dict["part_two"] = tutorial_data.part_two
    queryset_dict["poet"] = tutorial_data.poet

    print("PART ONE")
    #print(tutorial_data.part_one)
    
    #serializer = VerseSerializer(data=tutorial_data)
    serializer = VerseSerializer(data=queryset_dict)
    print("HOHO")
    
    if serializer.is_valid():
        print("valid")
        #create_loan_service(serializer.validated_data,request)
        #serializer.save(user=request.user)
    else:
        print(serializer.errors)
    return Response(serializer.data)
