from django.urls import path

from . import views

urlpatterns = [
    path('', views.index) # 웹에서 url 127.0.0.1:8000/pybo를 치면 config/urls.py에서 pybo/와 매칭 -> pybo/urls.py에서 pybo/views.index와 매칭, 결과값 리턴
]