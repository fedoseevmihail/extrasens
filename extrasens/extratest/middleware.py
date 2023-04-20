from django.shortcuts import render
from django.conf import settings
from django.db import models

class MyMiddleware(models.Model):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.session_key:
            request.session.save()
        response = self.get_response(request)
        return response