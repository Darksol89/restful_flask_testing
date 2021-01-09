"""API methods for testing"""
import requests


class APIClient:

    def __init__(self, base_url):
        """Initializing base url"""
        self.base_url = base_url

    def headers_data(self):
        """Getting headers"""
        headers = {"Content-type": "application/json; charset=UTF-8"}

        return headers

    def get_method(self, method, request_data=None, **params):
        """GET method for API request"""
        get_method_response = requests.get(self.base_url + method,
                                           json=request_data,
                                           params=params,
                                           headers=self.headers_data())

        return get_method_response


    def post_method(self, method, request_data=None, **params):
        """POST method for API request"""
        post_method_response = requests.post(self.base_url + method,
                                             json=request_data,
                                             headers=self.headers_data())

        return post_method_response

    def put_method(self, method, request_data=None, **params):
        """PUT method for API request"""
        put_method_response = requests.put(self.base_url + method,
                                           json=request_data,
                                           headers=self.headers_data())

        return put_method_response

    def delete_method(self, method):
        """DELETE method for API request"""
        delete_method_response = requests.delete(self.base_url + method,
                                                 headers=self.headers_data())

        return delete_method_response