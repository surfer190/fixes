'''
Create front matter for posts

1. Get all files in `_posts`
2. Remove the date part of the title
3. Copy the front matter into variable
4. write out the file with new front matter as exmplae below
'''

MD_DIR = './root/_posts/.'
OUTPUT_DIR = './root/output/'

import datetime
import os
import yaml


def create_file(name, path):
    '''
    1. Read the file
    '''
    with open(path, 'r') as file_stream:
        yaml_part = ''
        content = ''

        for count, line in enumerate(file_stream):
            if count < 5:
                yaml_part += line
            if count > 6:
                content += line

        try:
            yaml_doc = yaml.load(
                yaml_part,
                Loader=yaml.SafeLoader
            )
        except yaml.YAMLError as exc:
            print(exc)

        layout = yaml_doc.get('layout')
        title = yaml_doc.get('title')
        date = yaml_doc.get('date')
        category = yaml_doc.get('category')

        my_datetime = datetime.datetime.strptime(date[:10], '%Y-%m-%d')
        date = str(my_datetime.date())
            
        real_name = name[11:]
        summary = ''

        info = {
            'title':  title,
            'summary': '',
            'author': '',
            'date': date,
            'category': category
        }

        path = OUTPUT_DIR + category.lower()
        os.makedirs(path, exist_ok=True)

        with open(os.path.join(path, real_name), 'w') as f:
            info_dump = yaml.dump(info)
            f.write('---\n')
            f.write(info_dump)
            f.write('---\n')
            f.write(content)


if __name__ == '__main__':
    with os.scandir(MD_DIR) as it:
        for entry in it:
            if entry.name.endswith(".md") and entry.is_file():
                create_file(entry.name, entry.path)

'''
---
title: My Document
summary: A brief description of my document.
authors:
    - Waylan Limberg
    - Tom Christie
date: 2018-07-10
some_url: https://example.com
---
'''