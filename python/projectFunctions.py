#function to return the results of a webpage request
#adopted from https://realpython.com/python-web-scraping-practical-introduction/
def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during request to {0} : {1}'.format(url, str(e)))
        return None

#returns True if the reponse code is positive and the responses seems to be html
def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return( resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

#function to log an error message
def log_error_simple(e):
    print(e)