# =============================================================================
# Copyright (c) 2020 Tom Kralidis
#
# Author: Tom Kralidis <tomkralidis@gmail.com>
#
# Contact email: tomkralidis@gmail.com
# =============================================================================

import logging

from owslib.ogcapi import API

LOGGER = logging.getLogger(__name__)


class Features(API):
    """Abstraction for OGC API - Features"""

    def __init__(self, url, json_=None, timeout=30, headers=None, auth=None):
        __doc__ = API.__doc__  # noqa
        super().__init__(url, json_, timeout, headers, auth)

    def collection_items(self, collection_id, **kwargs):
        """
        implements /collection/{collectionId}/items

        @type collection_id: string
        @param collection_id: id of collection
        @type bbox: list
        @param bbox: list of minx,miny,maxx,maxy
        @type datetime: string
        @param datetime: time extent or time instant
        @type limit: int
        @param limit: limit number of features
        @type startindex: int
        @param startindex: start position of results
        @type q: string
        @param q: full text search

        @returns: feature results
        """

        if 'bbox' in kwargs:
            kwargs['bbox'] = ','.join(kwargs['bbox'])

        path = 'collections/{}/items'.format(collection_id)
        return self._request(path, kwargs)

    def collection_item(self, collection_id, identifier):
        """
        implements /collections/{collectionId}/items/{featureId}

        @type collection_id: string
        @param collection_id: id of collection
        @type identifier: string
        @param identifier: feature identifier

        @returns: single feature result
        """

        path = 'collections/{}/items/{}'.format(collection_id, identifier)
        return self._request(path)
