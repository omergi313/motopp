from typing import Tuple
import re


class Source:
    name: str
    get_parts_args: Tuple[str, str]
    name_selector: str
    price_selector: str
    external_url_selector: str


class RevZillaSource(Source):
    name = "RevZilla"
    get_parts_args = ('div', 'product-index-results__product-tile-wrapper')
    name_selector = 'div', 'product-tile__name'
    price_selector = 'div', 'product-details__price-retail'
    external_url_selector = 'a'

    def name(self, x):
        return x.find(*self.name_selector).text

    def price(self, x):
        price = x.find(*self.price_selector).text
        return re.search(r'\d+\.\d+', price).group(0)

    def external_url(self, x):
        return x.find(*self.external_url_selector).find('meta', itemprop='image').get('content')


class MotoSparePartsSource(Source):
    name = "MotoSpareParts"
    get_parts_args = ('div', 'product-index-results__product-tile-wrapper')
    name_selector = 'div', 'product-tile__name'
    price_selector = 'div', 'product-details__price-retail'
    external_url_selector = 'a'

    def name(self, x):
        return x.find(*self.name_selector).text

    def price(self, x):
        price = x.find(*self.price_selector).text
        return re.search(r'\d+\.\d+', price).group(0)

    def external_url(self, x):
        return x.find(*self.external_url_selector).find('meta', itemprop='image').get('content')
