
class ApiWeb():
    """
    Has methods generic to handle with
    web apis requests
    """

    def add_filters_url(self, url, filters):
        """
        Add query parameters/filters to a URL
        """

        url += '?'
        for f in filters:
            if not filters[f]: continue
            url+=str(f)+'='+str(filters[f])+'&'
        return url[:-1]