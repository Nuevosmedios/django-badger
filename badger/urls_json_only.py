"""
This is a simplified URLs list that omits any of the multiplayer features,
assuming that all badges will be managed from the admin interface, and most
badges will be awarded in badges.py
"""
from django.conf.urls import patterns, include, url

from django.conf import settings

from .feeds import (AwardsRecentFeed, AwardsByUserFeed, AwardsByBadgeFeed,
                    BadgesRecentFeed, BadgesByUserFeed)
from . import views


urlpatterns = patterns('badger.views',
    url(r'^badge/(?P<slug>[^/]+)/awards/(?P<id>[^\.]+)\.json$', 'award_detail',
        kwargs=dict(format="json"),
        name='badger.award_detail_json'),
    url(r'^badge/(?P<slug>[^\.]+)\.json$', 'detail',
        kwargs=dict(format="json"),
        name='badger.detail_json'),
    url(r'^issuer.json$', 'issuer', name='badger.detail_json'),
)
