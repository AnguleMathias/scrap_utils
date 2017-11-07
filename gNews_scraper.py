#
# Script for scrapping products from Google News
#


import requests
import traceback
from bs4 import BeautifulSoup
from utils import sleep_scrapper, get_request_headers


class GoogleNewsScraper:

    def __init__(self):
        pass

    def run(self):
        try:

            url = 'https://news.google.com/news/headlines/section/topic' \
                  '/NATION.en_in/India?ned=in&hl=en-IN&gl=IN'

            print '[GoogleNewsScraper] :: fetching data from url: ', url
            r = requests.get(url, headers=get_request_headers())
            if not r.status_code == 200:
                print "[GoogleNewsScraper] :: Failed to get " \
                        "content of url: %s" % url
                return
            html_doc = r.content

            soup = BeautifulSoup(html_doc, 'html.parser')
            # print '------soup', soup
            for div in soup.find_all('div', class_='v4IxVd'):
                # print '-----div', div
                self.scrap_result_row(div)
            sleep_scrapper('GoogleNewsScraper')
        except Exception as exp:
            print '[GoogleNewsScraper] :: run() :: Got exception: %s'\
                  % exp
            print(traceback.format_exc())

    def scrap_result_row(self, div):

        try:
            c_wiz = div.find('c-wiz', class_='M1Uqc kWyHVd')
            a = c_wiz.find('a', class_='nuEeue hzdq5d ME7ew').text.strip()
            print '[GoogleNewsScraper] :: HeadLines: ', a
            div = div.find('div', class_='alVsqf')
            sub = div.find('div', class_='jJzAOb')
            c_wiz = sub.find('c-wiz', class_='M1Uqc MLSuAf')
            a = c_wiz.find('a', class_='nuEeue hzdq5d ME7ew').text.strip()
            print '[GoogleNewsScraper] :: SubheadLines: ', a
        except Exception as exp:
            print '[GoogleNewsScraper] :: scrap_result_row() :: ' \
                  'Got exception : %s' % exp
            print(traceback.format_exc())


if __name__ == '__main__':

    googlenews = GoogleNewsScraper()
    googlenews.run()
