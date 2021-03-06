from intelex import _expand_format, get_sdk_version, get_endpoint, get_apikey, _select_format, _count_format, _paginate_top_format, _paginate_skip_format, _generate_query_string, _filter_format, _sort_format, get_sdk_author
import os

def test_get_version():
    assert get_sdk_version() == '0.0.30'

def test_get_endpoint():
    assert get_endpoint() == os.environ['ilx_endpoint']

def test_get_aoikey():
    assert get_apikey() == os.environ['ilx_apikey']

def test_select_format():
    select_list = ['Hello', 'World', 'List']
    assert _select_format(select_list) == '$select=Hello, World, List'

def test_count_format_true():
    assert _count_format(True) == '$count=true'

def test_count_format_false():
    assert _count_format(False) == '$count=false'

def test_count_format_blank():
    assert _count_format() == '$count=false'

def test_paginate_top_format():
    assert _paginate_top_format(50) == '$top=50'

def test_paginate_skip_format():
    assert _paginate_skip_format(100) == '$skip=100'

def test_paginate_filter_format():
    filter_expression = 'TaskType eq \'Question\''
    assert _filter_format(filter_expression) == '$filter=TaskType eq \'Question\''

def test_sort_format():
    sort_list = ['DateCreated asc']
    assert _sort_format(sort_list) == '$orderby=DateCreated asc'


def test_generate_query_string_all():
    query_string = {
        'select': ['RecordNumber', 'Id'],
        'count': True,
        'paginate_top': 50,
        'paginate_skip': 100,
        'sort': ['DateCreated asc'],
        'filter': 'TaskType eq \'Question\'',
        'expand': {
            'CreatedBy': {
                'select': ['Email'],
                'sort': ['DateCreated'],
                'filter': 'Id eq c5b31e68-ad67-4c70-9701-dcbad68088ed'
            },
            'ModifiedBy': {
                'select': ['Email'],
                'sort': ['DateCreated'],
                'filter': 'Id eq c5b31e68-ad67-4c70-9701-dcbad68088ed'
            },
            'PersonResponsible': {}
        }
    }
    
    assert _generate_query_string(query_string) == '$select=RecordNumber, Id&$count=true&$top=50&$skip=100&$orderby=DateCreated asc&$filter=TaskType eq \'Question\'&$expand=CreatedBy($select=Email, $orderby=DateCreated, $filter=Id eq c5b31e68-ad67-4c70-9701-dcbad68088ed),ModifiedBy($select=Email, $orderby=DateCreated, $filter=Id eq c5b31e68-ad67-4c70-9701-dcbad68088ed),PersonResponsible'


def test_generate_query_string_select():
    query_string = {
        'select': ['RecordNumber', 'Id']
    }
    assert _generate_query_string(query_string) == '$select=RecordNumber, Id'


def test_generate_query_string_sort():
    query_string = {
        'sort': ['DateCreated asc', 'DateModified']
    }
    assert _generate_query_string(query_string) == '$orderby=DateCreated asc, DateModified'


def test_generate_query_string_count():
    query_string = {
        'count': True
    }
    assert _generate_query_string(query_string) == '$count=true'


def test_generate_query_string_top():
    query_string = {
        'paginate_top': 50
    }
    assert _generate_query_string(query_string) == '$top=50'


def test_generate_query_string_skip():
    query_string = {
        'paginate_skip': 100
    }
    assert _generate_query_string(query_string) == '$skip=100'


def test_generate_query_string_filter():
    query_string = {
        'filter': 'TaskType eq \'Question\''
    }
    assert _generate_query_string(query_string) == '$filter=TaskType eq \'Question\''


def test_get_author():
    assert get_sdk_author() == 'Thomas Sampson - sampsont91@gmail.com'

def test_expand_format():
    params = {
        'filter': 'PolbyAutomation eq false',
        'expand': {
            'CreatedBy': {
                'select': ['Email'],
            },
            'TargetSite': {
                'select': ['TenantName']
            },
            'TargEnvironment': {
                'select': ['EnvironmentName']
            },
            'TaskType': {}
        }
    }

    assert _expand_format(params) == '$expand=CreatedBy($select=Email),TargetSite($select=TenantName),TargEnvironment($select=EnvironmentName),TaskType' 
    
