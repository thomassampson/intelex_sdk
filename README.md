[![Build Status](https://travis-ci.org/thomassampson/intelex_sdk.svg?branch=v0.0.29)](https://travis-ci.org/thomassampson/intelex_sdk) [![PyPI version](https://badge.fury.io/py/intelex.svg)](https://badge.fury.io/py/intelex)

# Intelex Python SDK

## INSTALLATION

```python
pip install intelex
```

## PREREQUISITES

You must set the following environment variables in order to use the SDK:

1. **ilx_endpoint**: The endpoint of your intelex tenant. Example for if tenant/site is called 'Python': https://clients.intelex.com/Login3/Python
2. **ilx_apikey**: The api key for your intelex tenant. Example: dgH67SHvhGhsb7Jsbwe3HnsN6

## USAGE

### Basic Functions

Results are returned as a string.

```python
import intelex as ilx

# Get current SDK version
ilx.get_sdk_version()

# Get Api Key from environment variables
ilx.get_apikey()

# Get Endpoint from environment variables
ilx.get_endpoint()

# Get SDK Author Contact Details
ilx.get_sdk_author()
```

### Object Functions

Results as returned as a dictionary.

```python
import intelex as ilx

object_name = 'IncidentsObject'
record_id = 'd0bf1ab9-6ff8-4362-8620-11cd74adb30a'
related_record_name = 'SubIncidents'
related_record_id = '3883f898-f6a3-40c8-be7e-8be000c596c6'

# Returns all records from an Intelex object that the user is authorized to view
ilx.get_records(object_name)

# Returns records from an Intelex object that the user is authorized to view based on input parameters in a dictionary
# Currently supports select, count, sort, filter, expand and pagination (You can add one or many)
# Expand supports select, sort and filter, you can also expand all fields in the related record by using {} to define an empty dictionary

    params = {
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
            'ModifiedBy': {}
    }

ilx.get_records(object_name, params)

# Returns an individual record from an object by referencing the UID of the record
ilx.get_record(object_name, record_id)

# Navigating to related records allows clients to request only the relational data belonging to a parent record.
ilx.get_related_records(object_name, record_id, related_record_name):

# Navigating to related records allows clients to request only specific relational data belonging to a parent record. 
ilx.get_related_record(object_name, record_id, related_record_name, related_record_id)

# Update an individual record from an object by passing in a dictionary with updated data

data = {
    'CompletionNotes': 'Risk as been corrected by our contractors'
}

ilx.update_record(object, id, data)
```