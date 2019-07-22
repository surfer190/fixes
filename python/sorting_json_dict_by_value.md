# How to sort a json Dict by the value of a key

For example a list of domains:

    domains = [
        {'mkey': 'apple.co.za', 'is_association': True},
        {'mkey': 'banana.org', 'is_association': True},
        {'mkey': 'beans.com', 'is_association': True},
        {'mkey': 'zulu.co.za', 'is_association': True},
        {'mkey': 'maakebos.com', 'is_association': True},
        {'mkey': 'thule.co.za', 'is_association': True},
        {'mkey': 'pollock.com', 'is_association': True},
        {'mkey': 'queen.co.za', 'is_association': True},
        {'mkey': 'zebra.co.uk', 'is_association': True},
    ]

To sort the items by the `mkey`:

    sorted_domains_atoz = sorted( 
        domains, 
        key = lambda i: i['mkey'] 
    )

    [{'mkey': 'apple.co.za', 'is_association': True},
    {'mkey': 'banana.org', 'is_association': True},
    {'mkey': 'beans.com', 'is_association': True},
    {'mkey': 'maakebos.com', 'is_association': True},
    {'mkey': 'pollock.com', 'is_association': True},
    {'mkey': 'queen.co.za', 'is_association': True},
    {'mkey': 'thule.co.za', 'is_association': True},
    {'mkey': 'zebra.co.uk', 'is_association': True},
    {'mkey': 'zulu.co.za', 'is_association': True}]

To sort the reverse order, use the `reverse=True` keyword argument

    sorted_domains_ztoa = sorted( 
        domains, 
        key = lambda i: i['mkey'], 
        reverse=True 
    )
    
    [{'mkey': 'zulu.co.za', 'is_association': True},
    {'mkey': 'zebra.co.uk', 'is_association': True},
    {'mkey': 'thule.co.za', 'is_association': True},
    {'mkey': 'queen.co.za', 'is_association': True},
    {'mkey': 'pollock.com', 'is_association': True},
    {'mkey': 'maakebos.com', 'is_association': True},
    {'mkey': 'beans.com', 'is_association': True},
    {'mkey': 'banana.org', 'is_association': True},
    {'mkey': 'apple.co.za', 'is_association': True}]

## Sources

* [Sort a list of dictionary values in python](https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/)
* [Python sorting](https://docs.python.org/3.3/howto/sorting.html)
