'''
File that generates the config for navigation and the index page
'''
import os
import yaml

DOCS_DIR = './docs'


def get_entry(path):
    with open(path, 'r') as file_stream:
        yaml_part = ''

        for count, line in enumerate(file_stream):
            if count < 6:
                yaml_part += line
            if count > 5:
                break

        try:
            yaml_doc = yaml.load(
                yaml_part,
                Loader=yaml.SafeLoader
            )
        except yaml.YAMLError as exc:
            print(exc)

        return yaml_doc

if __name__ == '__main__':


    categories = {}
    all_entries = []

    for root, dirs, files in os.walk(DOCS_DIR):
        for dir_ in dirs:
            categories[dir_] = []
            with os.scandir(os.path.join(DOCS_DIR, dir_)) as it:
                for entry in it:
                    if entry.name.endswith(".md") and entry.is_file():
                        #print(entry.name, dir_)
                        rec  = get_entry(entry.path)
                        date = rec.get('date')
                        title = rec.get('title')
                        summary = rec.get('summary')
                        category = rec.get('category')

                        record = {
                            'date': date,
                            'title': title,
                            'summary': summary,
                            'category': category,
                            'file': entry.path
                        }

                        categories[dir_].append(record)
                        all_entries.append(record)
                        # print(date, title, summary, category)


    newlist = sorted(all_entries, key=lambda k: k['date'], reverse=True)

    category_keys = list(categories.keys())

    category_keys = sorted(category_keys)

    the_10_most_recent = newlist[0:20]

    print('# Home\n')

    print('A repo of documentation, notes, summaries, fixes and solutions on software development and related topics\n')

    print('## Most Recent Posts\n\n')

    for item in the_10_most_recent:
        print(f'- { item["date"] }: _{ item["category"] }_ [{ item["title"] }]({ item["file"][7:] })')

    print('## Table of Contents\n')
    print('[TOC]\n')

    for key in category_keys:
        records = categories[key]

        # sort records by date
        records = sorted(records, key=lambda k: k['date'], reverse=True)

        print(f'## { key.title() }\n')

        for item in records:
            print(f'- { item["date"] }: [{ item["title"] }]({ item["file"][7:] })')

        print()
