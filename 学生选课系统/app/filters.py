

import django_filters

from rest_framework import filters

from app.models import Student


class StudentFilter(filters.FilterSet):

    s_name = django_filters.CharFilter('s_name', lookup_expr='contains')
    s_chinese_min = django_filters.NumberFilter('s_chinese', lookup_expr='gte')
    s_chinese_max = django_filters.NumberFilter('s_chinese', lookup_expr='lte')

    class Meta:
        model = Student
        fields = ['s_name',]