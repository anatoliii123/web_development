# from django.shortcuts import render (not using this right now)
from django.http import JsonResponse

def api_home(request, *args, **kwargs)
return JsonResponse({"message": "Hi there this is your django api response"})

#views here
