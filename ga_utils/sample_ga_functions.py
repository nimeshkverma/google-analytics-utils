import utils


def get_device_data():
    device_query_config = {
        'start_date': '2016-01-01',
        'end_date': '2016-01-02',
        'metrics': 'ga:users',
        'dimensions': 'ga:deviceCategory',
    }
    data = utils.query_ga(device_query_config)
    return data


def get_user_data():
    user_query_config = {
        'start_date': '2016-01-01',
        'end_date': '2016-01-02',
        'metrics': 'ga:users',
        'dimensions': 'ga:deviceCategory'
    }
    data = utils.query_ga(user_query_config)
    return data


def get_session_data():
    session_query_config = {
        'start_date': '2016-01-01',
        'end_date': '2016-01-02',
        'metrics': 'ga:sessions',
        'dimensions': 'ga:deviceCategory'
    }
    data = utils.query_ga(session_query_config)
    return data


def get_bounce_data():
    bounce_query_config = {
        'start_date': '2016-01-01',
        'end_date': '2016-01-02',
        'metrics': 'ga:bounceRate',
        'dimensions': 'ga:deviceCategory'}
    data = utils.query_ga(bounce_query_config)
    return data


def get_pagePerSession_data():
    pagePerSession_query_config = {
        'start_date': '2016-01-01',
        'end_date': '2016-01-02',
        'metrics': 'ga:pageviewsPerSession',
        'dimensions': 'ga:deviceCategory'
    }
    data = utils.query_ga(pagePerSession_query_config)
    return data


def get_returningUser_data():
    returningUser_query_config = {
        'start_date': '2016-01-01',
        'end_date': '2016-01-02',
        'metrics': 'ga:userType',
        'dimensions': 'ga:deviceCategory'}
    data = utils.query_ga(returningUser_query_config)
    return data


if __name__ == '__main__':
    print get_device_data()
