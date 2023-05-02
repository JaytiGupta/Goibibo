from Util.logs import getLogger
from Page.Amazon.amazon_header import AmazonHeader
from Page.Amazon.amazon_searchresults import AmazonSearchResult

log = getLogger()


class AmazonPriceRangeTests:

    def test_search_result_text(self, browser, amazonpage_url):
        page = AmazonHeader(browser, amazonpage_url)
        page.go()
        # page.search_dropbox("Furniture")
        item = 'Flower Vase'
        page.search_item(item)
        searchpage = AmazonSearchResult(browser, amazonpage_url)
        log.info("Asserting if the text contains the searched item name")
        assert item in searchpage.search_result_text()

    def test_pricerange(self, browser, amazonpage_url):
        searchpage = AmazonSearchResult(browser, amazonpage_url)
        min_price = 1500
        max_price = 3000
        searchpage.set_price_range(min_price, max_price)
        price_list = searchpage.all_item_price_list()
        log.info("Verifying the items listed fall in the set price range")
        assert price_list[0] >= min_price and price_list[-1] <= max_price
