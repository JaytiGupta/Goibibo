import time

from Page.guidewire.tab_bar import TabBar
from Page.guidewire.gwpc import GWPC


class HomeTests:

    def test_home(self, browser):
        page = GWPC(browser)
        page.go()
        page.login(username='su', password='gw')

        tab_bar = TabBar(browser)
        tab_bar.search_account(5653250347)
        time.sleep(3)
        tab_bar.search_submission('0000013128')
        time.sleep(3)
        tab_bar.search_policy(3408578567)
        time.sleep(3)
