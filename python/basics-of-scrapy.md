# The basics of scrapy - a Python based web scraping and crawling framework

1. Install Scrapy:

    ```
    pip install Scrapy

    ```

    Upgrade Scrapy:

    ```
    pip install --upgrade scrapy
    ```

2. Start a new project:

    ```
    scrapy startproject <name>
    ```

3. Basic Structure:

    ```
    - scrapy.cfg: the project configuration file
    - <name>/: the project’s python module, you’ll later import your code from here.
    - <name>/items.py: the project’s items file.
    - <name>/pipelines.py: the project’s pipelines file.
    - <name>/settings.py: the project’s settings file.
    - <name>/spiders/: a directory where you’ll later put your spiders.
    ```

4. Create a spider **<name>/spiders/<name>_spider.py**:

    ```
    import scrapy

    class DmozSpider(scrapy.Spider):
        name = "dmoz"
    	allowed_domains = ["dmoz.org"]
        start_urls = [
           "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
           "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    	    ]

    	    def parse(self, response):
            filename = response.url.split("/")[-2]
            with open(filename, 'wb') as f:
              f.write(response.body)
    ```

5. Run the crawl

    ```
    scrapy crawl dmoz
    ```

6. Using the Selectors in the shell:

    ```
    scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
    ```
