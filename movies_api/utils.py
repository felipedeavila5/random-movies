import requests

def get_random_obj(instance):
    """
    Get a random object from any Model instance
    """
    return instance.objects.order_by("?").first()

def request_data(url, params=None):
    """
    Make a data request
    """
    r = requests.get(url, params=params)
    return r.json()
    

