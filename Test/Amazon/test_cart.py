from Page.amazon_searchresults import AmazonSearchResult
from Base import baseelement
from Util.logs import getLogger
from Page.amazon_header import AmazonHeader
from Page.amazon_cart import AmazonCart

log = getLogger()


class CartTests:

    def test_empty_cart(self, browser, amazonpage_url):
        page = AmazonHeader(browser, amazonpage_url)
        page.go()
        page.go_to_cart()
        page3 = AmazonCart(browser, amazonpage_url)
        text = page3.empty_cart_text()
        assert text == 'Your Amazon Cart is empty'

    def test_cart_not_empty(self, browser, amazonpage_url):
        page = AmazonHeader(browser, amazonpage_url)
        page.search_item("Fountain Pen")
        page2 = AmazonSearchResult(browser, amazonpage_url)
        page2.add_to_cart()
        page.go_to_cart()
        page3 = AmazonCart(browser, amazonpage_url)
        assert page3.verify_cart_not_empty()

    def test_cart_total(self, browser, amazonpage_url):
        page = AmazonHeader(browser, amazonpage_url)
        page.go()
        page.search_item("Lunch Box")

        page2 = AmazonSearchResult(browser, amazonpage_url)
        page2.add_to_cart()
        page.search_item("Flower Vase")
        page2.add_to_cart()
        page.go_to_cart()
        page3 = AmazonCart(browser, amazonpage_url)
        price_list = page3.cart_item_price_list()
        cart_sum = 0
        for item in price_list:
            cart_sum = cart_sum + item
        assert cart_sum == page3.cart_total_amt()

