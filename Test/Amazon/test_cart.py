from Page.amazon_searchresults import AmazonSearchResult
from Util.logs import getLogger
from Page.amazon_header import AmazonHeader
from Page.amazon_cart import AmazonCart

log = getLogger()


class CartTests:

    def test_s(self, browser, amazonpage_url):
        page = AmazonHeader(browser, amazonpage_url)
        page.go()
        page.search_item("Light Bulb")

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

