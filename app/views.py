from django.shortcuts import render

from django.http import JsonResponse

def dowelltest(request):
    return JsonResponse({'message': 'Hello Dowell Test'})