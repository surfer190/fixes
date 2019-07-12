# Print a python dict nicely

You could use pprint but `json.dumps` is much better

    my_dict = {'hello': [{'chops': 'chaps', 'trash': 4456}, {'chats': 'chops'}, True]}
    
    import json
    print(json.dumps(my_dict, indent=4, sort_keys=True))  
    
    {
        "hello": [
            {
                "chops": "chaps",
                "trash": 4456
            },
            {
                "chats": "chops"
            },
            true
        ]
    }

## Source

* [Stackoverflow print a dict nicely](https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python)