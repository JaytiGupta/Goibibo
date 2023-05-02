from Page.Goibibo.homepage import HomePage
from pytest import mark


class GoibiboHomeTests:

    def test_page_header(self, browser, picture, homepage_url):
        page = HomePage(browser, homepage_url)
        page.go()
        try:
            page.popupclose().click_element()
        except:
            pass
        page.from_location().click_element()
        assert page.page_header_text() == 'Domestic and International Flights'
        picture.capture()


    def test_title(self, browser, picture, homepage_url):
        page = HomePage(browser, homepage_url)
        page.go()
        try:
            page.popupclose().click_element()
        except:
            pass
        page.set_from_location("Delhi")
        page.set_to_location("Goa")
        page.departure_date("23,February 2023")
        picture.capture()
        page.calendar_done_btn().click_element()
        page.set_traveller(2, 1, 1)
        page.search_flight_btn()
        picture.capture()
        assert page.get_title() == "Book Cheap Flights, Air Tickets, Hotels, Bus & Holiday Package at Goibibo"
        browser.save_screenshot("C:\\Users\\jayti.gupta\\Documents\\Automation Screenshots\\Folder1\\page_title.png")
        picture.capture()
