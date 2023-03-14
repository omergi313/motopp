from typing import List
import requests
from bs4 import BeautifulSoup, Tag
import pandas as pd
from parts_scraper.sources import Source



class Scraper(object):
    def __init__(self, url: str):
        self.url = url

    def scrape(self, *parts_args) -> List[Tag]:
        page = self.get_page()
        return self.get_parts(page, *parts_args)

    def get_page(self) -> str:
        response = requests.get(self.url)
        return response.text

    def get_parts(self, page: str, *args) -> List:
        soup = BeautifulSoup(page, 'html.parser')
        parts = soup.find_all(*args)
        return parts

    def get_part(self, page: str):
        raise NotImplementedError


class PartsScraper(Scraper):
    def __init__(self, url: str, source: Source):
        super().__init__(url)
        self.source = source
        self.parts = self.scrape(*self.source.get_parts_args)
        self.df = self.parse_parts()

    def parse_parts(self) -> pd.DataFrame:
        df = pd.DataFrame({'soups': self.parts})
        df['name'] = df['soups'].apply(self.source.name)
        df['price'] = df['soups'].apply(self.source.price)
        df['external_url'] = df['soups'].apply(self.source.external_url)
        return df.drop('soups', axis=1)


