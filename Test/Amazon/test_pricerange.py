from Util.logs import getLogger
from Util.screenshot import take_screenshot
from Page.Amazon.amazon_header import AmazonHeader
from Page.Amazon.amazon_searchresults import AmazonSearchResult
from pytest import mark


@mark.pricerange
class AmazonPriceRangeTests:

    log = getLogger()

    @mark.smoke
    def test_search_result_text(self, browser, amazonpage_url):
        page = AmazonHeader(browser, amazonpage_url)
        page.go()
        # page.search_dropbox("Furniture")
        item = 'Flower Vase'
        page.search_item(item)
        search_page = AmazonSearchResult(browser, amazonpage_url)
        self.log.info("Asserting if the text contains the searched item name")
        assert item in search_page.search_result_text()
        take_screenshot(browser)

    def test_pricerange(self, browser, amazonpage_url):
        search_page = AmazonSearchResult(browser, amazonpage_url)
        min_price = 1500
        max_price = 3000
        search_page.set_price_range(min_price, max_price)
        price_list = search_page.all_item_price_list()
        self.log.info("Verifying the items listed fall in the set price range")
        assert price_list[0] >= min_price and price_list[-1] <= max_price
        take_screenshot(browser, search_page.first_search_elm())
