---
author: ''
category: Python
date: '2019-06-13'
summary: ''
title: Convert Json To Yaml
---
# Convert Json to Yaml

    import yaml

    abc = '{"all": {"hosts": ["1.1.1.1"], "vars": {}}, ...}'

    print(yaml.dump(yaml.load(abc)))

## Source

* [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation)