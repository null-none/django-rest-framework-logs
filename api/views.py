from django.http import HttpResponse
from django.conf import settings

import json

from rest_framework import authentication, permissions
from rest_framework import generics
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from mixins import LoggingMixin


response_data = {}
response_data['status'] = 'success'
response_data['text_error'] = ''


class TestApiView(LoggingMixin, generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        self.log(request, response_data, kwargs)
        return HttpResponse(json.dumps(response_data), content_type="application/json")
