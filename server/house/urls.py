#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'

from house import views
from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'metrics', views.MetricsViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
