# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:guest1
@file:urls.py
@time:2022/10/14
"""
from django.conf.urls import url
from book.views import LoginView
urlpatterns = [
    url(r'^login/$', LoginView.as_view())
]


if __name__ == '__main__':
    pass
