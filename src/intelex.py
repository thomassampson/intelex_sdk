import requests as r
import os
import json


# Private Functions

def _select_format(select_list):
    output = ', '
    output = output.join(select_list)
    return '{}'.format(output)


def _count_format(bool=False):
    if bool:
        return '$count=true'
    else:
        return '$count=false'


def _paginate_top_format(top):
    return '$top={}'.format(top)


def _paginate_skip_format(skip):
    return '$skip={}'.format(skip)


def _filter_format(filter_expression):
    return '$filter={}'.format(filter_expression)


def _sort_format(sort_list):
    output = ', '
    output = output.join(sort_list)
    return '$orderby={}'.format(output)


def _generate_query_string(query_string):
    
    result = []

    if 'select' in query_string:
        result.append('$select={}'.format(_select_format(query_string['select'])))

    if 'count' in query_string:      
        result.append('{}'.format(_count_format(query_string['count'])))

    if 'paginate_top' in query_string:
        result.append('{}'.format(_paginate_top_format(query_string['paginate_top'])))
    
    if 'paginate_skip' in query_string:
        result.append('{}'.format(_paginate_skip_format(query_string['paginate_skip'])))

    if 'sort' in query_string:
        result.append('{}'.format(_sort_format(query_string['sort'])))

    if 'filter' in query_string:
        result.append('{}'.format(_filter_format(query_string['filter'])))


    output = '&'
    output = output.join(result)
    
    return '{}'.format(output)


# Public Functions

def get_version():
    return '0.0.27'


def get_endpoint():
    ilx_endpoint = os.environ['ilx_endpoint']
    return ilx_endpoint


def get_apikey():
    ilx_apikey = os.environ['ilx_apikey']
    return ilx_apikey


def get_records(object, params=None):
    ilx_endpoint = os.environ['ilx_endpoint']
    ilx_apikey = os.environ['ilx_apikey']
    auth_header = 'Basic {}'.format(ilx_apikey)

    headers = {
        'Authorization': auth_header
    }

    if params != None:
        query = '{}/api/v2/object/{}?{}'.format(ilx_endpoint, object, _generate_query_string(params))
    else:
        query = '{}/api/v2/object/{}'.format(ilx_endpoint, object)
    
    response = r.get(query, headers=headers)
    
    return json.loads(response.text)


def get_record(object, id):
    ilx_endpoint = os.environ['ilx_endpoint']
    ilx_apikey = os.environ['ilx_apikey']
    auth_header = 'Basic {}'.format(ilx_apikey)

    headers = {
        'Authorization': auth_header
    }

    query = '{}/api/v2/object/{}({})'.format(ilx_endpoint, object, id)

    response = r.get(query, headers=headers)

    return json.loads(response.text)


def get_related_records(object, id, navigation_property):
    ilx_endpoint = os.environ['ilx_endpoint']
    ilx_apikey = os.environ['ilx_apikey']
    auth_header = 'Basic {}'.format(ilx_apikey)

    headers = {
        'Authorization': auth_header
    }

    query = '{}/api/v2/object/{}({})/{}'.format(ilx_endpoint, object, id, navigation_property)
    response = r.get(query, headers=headers)

    return json.loads(response.text)


def get_related_record(object, id, navigation_property, related_id):
    ilx_endpoint = os.environ['ilx_endpoint']
    ilx_apikey = os.environ['ilx_apikey']
    auth_header = 'Basic {}'.format(ilx_apikey)

    headers = {
        'Authorization': auth_header
    }

    query = '{}/api/v2/object/{}({})/{}({})'.format(ilx_endpoint, object, id, navigation_property, related_id)
    response = r.get(query, headers=headers)

    return json.loads(response.text)


if __name__ == '__main__':
    pass
