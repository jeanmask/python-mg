#-*- coding:utf-8 -*-

from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse_lazy
from django.conf import settings

urlpatterns = patterns(
    'apps.contribuicoes.views',
    url(r'^$', 'contribuicao', name='apps.contribuicoes:contribuicao-add'),
)
