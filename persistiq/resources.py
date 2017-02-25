from __future__ import unicode_literals

from client import api
from map import Map


class Resource(object):
    endpoint = None
    data_key = None

    @classmethod
    def wrap(cls, obj):
        if isinstance(obj, list):
            return map(Map, obj)
        return Map(obj)

    @classmethod
    def generator_wrap(cls, generator):
        for obj in generator:
            yield cls.wrap(obj)


class ListMixin(object):
    paginate = False

    @classmethod
    def list(cls):
        if cls.paginate:
            paginator = api.paginate(cls.endpoint, data_key=cls.data_key)
            return cls.generator_wrap(paginator)
        return cls.wrap(api.get(cls.endpoint)[cls.data_key])


class RetrieveMixin(object):
    single_data_key = None

    @classmethod
    def get(cls, resource_id):
        data_key = cls.single_data_key or cls.data_key
        response = api.get('{}/{}'.format(cls.endpoint, resource_id))
        return cls.wrap(response[data_key])


class User(ListMixin, Resource):
    endpoint = 'users'
    data_key = 'users'


class Lead(ListMixin, RetrieveMixin, Resource):
    endpoint = 'leads'
    data_key = 'leads'
    single_data_key = 'lead'
    paginate = True
