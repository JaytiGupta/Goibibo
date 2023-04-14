from Page.amazon_searchresults import AmazonSearchResult
from Util.logs import getLogger
from Page.amazon_home import AmazonHome


log = getLogger()


class CartTests:

    def test_s(self, browser, amazonpage_url):
        page = AmazonHome(browser, amazonpage_url)
        page.go()
        page.search_item("Light Bulb")

        page2 = AmazonSearchResult(browser, amazonpage_url)
        page2.add_to_cart()
