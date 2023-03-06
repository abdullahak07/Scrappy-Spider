import scrapy
from scrapy.crawler import CrawlerProcess
import xml.etree.ElementTree as ET
import datetime


class Spider(scrapy.Spider):
    name = 'rwfj' # set the spider's name
    download_timeout = 120 # set the download timeout for the spider
    """
    Specify the format here:
    i.e 1) json
        2) csv
        3) xml
    """

    OUTPUT_FORMAT = "json"  # set the output format to JSON
    #OUTPUT_FORMAT = "csv" # set the output format to CSV (commented out)

    now = datetime.datetime.now() # get the current date and time
    formatted_date = now.strftime("%Y%m%d_%H%M%S") # format the date and time as a string

    # set the spider's custom settings
    custom_settings = {
        'ROBOTSTXT_OBEY': False, # ignore the robots.txt file
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',# set the user agent string
        'FEED_FORMAT': OUTPUT_FORMAT,# set the feed format to the specified output format
        'FEED_URI': f"{name}_{formatted_date}.{OUTPUT_FORMAT}"# set the feed URI to include the spider name and the formatted date/time string
    }

    # requesting all the urls from the website
    def start_requests(self):
        # define the headers to be used in the requests
        Headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://rewardsforjustice.net',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        #Defining the data to be sent in the post request
        Data = "action=jet_smart_filters&provider=jet-engine%2Frewards-grid&query%5B_tax_query_crime-category%5D%5B%5D=1070&query%5B_tax_query_crime-category%5D%5B%5D=1071&query%5B_tax_query_crime-category%5D%5B%5D=1073&query%5B_tax_query_crime-category%5D%5B%5D=1072&query%5B_tax_query_crime-category%5D%5B%5D=1074&defaults%5Bpost_status%5D%5B%5D=publish&defaults%5Bpost_type%5D%5B%5D=north-korea&defaults%5Bpost_type%5D%5B%5D=rewards&defaults%5Bposts_per_page%5D=200&defaults%5Bpaged%5D=1&defaults%5Bignore_sticky_posts%5D=1&settings%5Blisitng_id%5D=22078&settings%5Bcolumns%5D=3&settings%5Bcolumns_tablet%5D=1&settings%5Bcolumns_mobile%5D=1&settings%5Bpost_status%5D%5B%5D=publish&settings%5Buse_random_posts_num%5D=&settings%5Bposts_num%5D=9&settings%5Bmax_posts_num%5D=&settings%5Bnot_found_message%5D=No+data+was+found&settings%5Bis_masonry%5D=&settings%5Bequal_columns_height%5D=&settings%5Buse_load_more%5D=&settings%5Bload_more_id%5D=&settings%5Bload_more_type%5D=click&settings%5Bloader_text%5D=&settings%5Bloader_spinner%5D=&settings%5Buse_custom_post_types%5D=yes&settings%5Bcustom_post_types%5D%5B%5D=north-korea&settings%5Bcustom_post_types%5D%5B%5D=rewards&settings%5Bhide_widget_if%5D=&settings%5Bcarousel_enabled%5D=&settings%5Bslides_to_scroll%5D=3&settings%5Barrows%5D=true&settings%5Barrow_icon%5D=fa+fa-angle-left&settings%5Bdots%5D=&settings%5Bautoplay%5D=&settings%5Bautoplay_speed%5D=5000&settings%5Binfinite%5D=&settings%5Bcenter_mode%5D=&settings%5Beffect%5D=slide&settings%5Bspeed%5D=500&settings%5Binject_alternative_items%5D=&settings%5Binjection_items%5D%5B0%5D%5Bitem%5D=90086&settings%5Binjection_items%5D%5B0%5D%5B_id%5D=a4c8515&settings%5Binjection_items%5D%5B0%5D%5Bitem_num%5D=1&settings%5Binjection_items%5D%5B0%5D%5Binject_once%5D=yes&settings%5Binjection_items%5D%5B0%5D%5Bmeta_key%5D=dprk&settings%5Binjection_items%5D%5B0%5D%5Bitem_condition_type%5D=item_meta&settings%5Binjection_items%5D%5B0%5D%5Bstatic_item%5D=yes&settings%5Bscroll_slider_enabled%5D=&settings%5Bscroll_slider_on%5D%5B%5D=desktop&settings%5Bscroll_slider_on%5D%5B%5D=tablet&settings%5Bscroll_slider_on%5D%5B%5D=mobile&settings%5Bcustom_query%5D=&settings%5Bcustom_query_id%5D=&settings%5B_element_id%5D=rewards-grid&settings%5Bjet_cct_query%5D=&settings%5Bjet_rest_query%5D=&props%5Bfound_posts%5D=181&props%5Bmax_num_pages%5D=21&props%5Bpage%5D=1&paged=1&referrer%5Buri%5D=%2Findex%2F%3Fjsf%3Djet-engine%3Arewards-grid%26tax%3Dcrime-category%3A1070%252C1071%252C1073%252C1072%252C1074&referrer%5Binfo%5D=&referrer%5Bself%5D=%2Findex.php&indexing_filters=%5B41852%2C41851%5D"

        # Creating a request object to send a POST request to the given URL
        request = scrapy.Request(
            url='https://rewardsforjustice.net/wp-admin/admin-ajax.php',
            headers=Headers,
            method='POST',
            body=Data,
            callback=self.getAllURLS,

        )
        # Yielding the request object to pass it to Scrapy's engine
        yield request

    # Function to get all the links in the AJAX response
    def getAllURLS(self, response):
        Data = response.json() # Extracting the JSON content from the response
        HTML = Data["content"] # Extracting the HTML content from the JSON data
        HTML_PARSER = ET.fromstring(HTML) # Parsing the HTML content using ElementTree library
        Links = HTML_PARSER.findall(".//a") # Extracting all the links from the parsed HTML content

        for Link in Links: # Iterating over each link
            URL = Link.attrib["href"] # Extracting the URL from the link's attributes

            request = scrapy.Request(url=URL, callback=self.parse) # Creating a request object for each URL

            yield request # Yielding the request object to pass it to Scrapy's engine

    # Define the XPath expressions to extract information from the website
    def parse(self, response):
        DATE_OF_BIRTH = "//h2[contains(text(),'Date of Birth')]/../../following-sibling::div/div/text()"
        REWARD_AMOUNT = "//h2[contains(text(),'Up to')]/text()"
        TITLE = "//div[@id='hero-col']//h2[contains(@class,'elementor-size-default')]/text()"
        ABOUT = "//h2[contains(text(),'About')]/../../following-sibling::div/div/p"
        ASSOCIATE_ORGANIZATIONS = "//p[contains(text(),'Associated Organization')]//a"
        ASSOCIATE_LOCATION = "//*[contains(text(),'Associated Location')]/../../following-sibling::div//span/text()"
        IMAGES = "//*[@id='gallery-1']//img"

        # Extract data from the response object using the defined XPATH expressions
        DOB = str(response.xpath(DATE_OF_BIRTH).get()).replace("\n", "").replace("\t", "")
        RA = str(response.xpath(REWARD_AMOUNT).get()).replace("Up to ", "").replace("\n", "").replace("\t", "")
        Title = str(response.xpath(TITLE).get()).replace("\n", "").replace("\t", "")
        About = response.xpath(ABOUT)
        About_TEXT = "\n".join([i.xpath(".//text()").get() for i in About])
        AO = response.xpath(ASSOCIATE_ORGANIZATIONS)
        AO_TEXT = ";".join([i.xpath(".//text()").get() for i in AO])
        AL = str(response.xpath(ASSOCIATE_LOCATION).get()).replace("\n", "").replace("\t", "")
        Images = response.xpath(IMAGES)
        Images_TEXT = ";".join([i.xpath(".//@src").get() for i in Images])

        # Yield extracted data in a dictionary format
        yield {
            "URL": response.url,
            'DATE_OF_BIRTH': DOB,
            'REWARD_AMOUNT': RA,
            'TITLE': Title,
            'ABOUT': About_TEXT,
            'ASSOCIATE_ORGANIZATIONS': AO_TEXT,
            'ASSOCIATE_LOCATION': AL,
            'IMAGES': Images_TEXT
        }


if "__main__" == __name__:
    # Run the spider

    process = CrawlerProcess()
    process.crawl(Spider)
    process.start()






