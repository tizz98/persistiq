from __future__ import unicode_literals

import os

import requests

from constants import __str_version__


class Client(object):
    BASE_URL = 'https://api.persistiq.com'

    def __init__(self, api_key, version='v1'):
        self.api_key = api_key
        self.version = version

    @property
    def headers(self):
        return {
            'User-Agent': 'python/persistiq v{}'.format(
                __str_version__
            ),
            'x-api-key': self.api_key,
        }

    @property
    def api_url(self):
        return '{base_url}/{version}'.format(
            base_url=self.BASE_URL,
            version=self.version,
        )

    def _request(self, method, url, **kwargs):
        if not url.startswith(self.api_url):
            url = '{api_base}/{endpoint}'.format(
                api_base=self.api_url,
                endpoint=url
            )

        if 'headers' not in kwargs:
            kwargs['headers'] = {}

        kwargs['headers'].update(self.headers)
        return requests.request(method, url, **kwargs).json()

    def get(self, endpoint, params=None, **kwargs):
        return self._request('get', endpoint, params=params, **kwargs)

    def post(self, endpoint, data=None, json=None, **kwargs):
        return self._request('post', endpoint, data=data, json=json, **kwargs)

    def put(self, endpoint, data=None, json=None, **kwargs):
        return self._request('put', endpoint, data=data, json=json, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request('delete', endpoint, **kwargs)

    def paginate(self, endpoint, data_key=None, get_params=None, **get_kwargs):
        if data_key is None:
            data_key = endpoint.replace('/', '')

        response = self.get(endpoint, params=get_params, **get_kwargs)

        while response['has_more']:
            for obj in response[data_key]:
                yield obj

            response = self.get(
                response['next_page'],
                params=get_params,
                **get_kwargs
            )


api = Client(
    os.environ['PERSIST_IQ_API_KEY'],
    version=os.environ.get('PERSIST_IQ_API_VERSION', 'v1')
)
