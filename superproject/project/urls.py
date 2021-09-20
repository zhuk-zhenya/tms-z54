
from django.contrib import admin
from django.http import HttpResponse, HttpRequest
from django.urls import path


def hello_world(request: HttpRequest):

    return HttpResponse('Hello World!')


from task4.views import view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', hello_world),
    path('task4/', view),
]
