#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


import requests
import json
from rest_framework import serializers
from house.models import HouseMetrics
from django.contrib.auth.models import User
from server.settings import FLUENT_URL, FLUENT_HEADERS


class HouseMetricsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tempertime = serializers.DateTimeField(input_formats=('%Y/%m/%d %H:%M', ))

    def save(self, **kwargs):
        super().save(**kwargs)
        # fluentd serverにPOST
        r = requests.post(url=FLUENT_URL, data=json.dumps(self.context['request'].DATA), headers=FLUENT_HEADERS)

    class Meta:
        model = HouseMetrics
        fields = (
            'owner',
            'place',
            'temperature',
            'tempertime',
            'memo',
            'lon',
            'lat'
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    house_metrics = serializers.HyperlinkedRelatedField(
        queryset=HouseMetrics.objects.all(), view_name='metrics-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'house_metrics')
