# In web development
# Hash tables are good for caching/memorizing data instead of making the server do some work

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url) # Simple example of how hash tables are use for caching
        cache[url] = data
        return data