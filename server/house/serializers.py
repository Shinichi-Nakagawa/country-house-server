#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


from rest_framework import serializers
from house.models import HouseMetrics
from django.contrib.auth.models import User


class HouseMetricsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    tempertime = serializers.DateTimeField(input_formats=('%Y/%m/%d %H:%M', ))

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
