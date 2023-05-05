from django.shortcuts import render
from django.conf import settings
from django.db import models
from importlib import import_module
from .models import UserSession
from requests import Request, Session

class MyMiddleware(models.Model):
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not hasattr(request, 'session'):
            engine = import_module(settings.SESSION_ENGINE)
            session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME, None)

#        if not request.session.session_key:
            request.session = engine.SessionStore(session_key)
        response = self.get_response(request)
        return response