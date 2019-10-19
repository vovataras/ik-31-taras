from django.shortcuts import render
from django.http import JsonResponse
import os
from datetime import datetime
import platform


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    response = {'date': datetime.now(), 'current_page': request.path, 'server_info': {'system': platform.system(), 'node': platform.node(), 'release': platform.release(), 'version': platform.version(), 'machine': platform.machine(), 'processor': platform.processor()}, 'client_info': request.headers.get('User-Agent')}
    return JsonResponse(response)
