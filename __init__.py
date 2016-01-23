from magnet_url import MagnetUrl

def url(magnet_url):
    '''Short-cut function for easier manipulate with magnet urls.
    For given magnet_url function retuns MagnetUrl instance.
    i.e.
    >>> import magnet
    >>> data = magnet.url('?xt')'''
    return MagnetUrl(magnet_url)

