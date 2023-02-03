'''
Get all the post paths
'''
import pathlib
from bs4 import BeautifulSoup

here = pathlib.Path(__file__).parent.resolve()

site = here / 'site'

sitemap = site / 'sitemap.xml'

with open(sitemap, 'r') as file_:
    contents = file_.read()
    soup = BeautifulSoup(contents, "xml")
    locations = soup.find_all('loc')
    for location in locations:
        loc = location.text.removeprefix('https://fixes.co.za')
        print(f'"{loc}",')
