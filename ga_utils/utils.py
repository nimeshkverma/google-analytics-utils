import argparse

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools

from config import GA_CONFIG, PROFILE_ID


def get_service():
    """
        Takes params from config,
        Returns a service that is connected to the specified API.

    """
    secret_file = open(GA_CONFIG.get('key_file_location'), 'rb')
    key = secret_file.read()
    secret_file.close()
    credentials = SignedJwtAssertionCredentials(GA_CONFIG.get(
        'service_account_email'), key, scope=GA_CONFIG.get('scope'))
    http = credentials.authorize(httplib2.Http())
    service = build(
        GA_CONFIG.get('api_name'), GA_CONFIG.get('api_version'), http=http)
    return service


def query_ga(query_config):
    ids = PROFILE_ID
    start_date = query_config.get('start_date', 'yesterday')
    end_date = query_config.get('end_date', 'yesterday')
    metrics = query_config.get('metrics')
    dimensions = query_config.get('dimensions')
    sort = query_config.get('sort', None)
    filters = query_config.get('filters', None)
    start_index = query_config.get('start_index', None)
    max_results = query_config.get('max_results', None)
    service = get_service()
    query = service.data().ga().get(
        ids=ids,
        start_date=start_date,
        end_date=end_date,
        metrics=metrics,
        dimensions=dimensions,
        sort=sort,
        filters=filters,
        start_index=start_index,
        max_results=max_results)
    results = query.execute()
    return results
