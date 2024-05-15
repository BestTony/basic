"""Add an item to a shopping cart. Verify. Remove item. Verify."""
from .page_objects import Page
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class MyTestClass(BaseCase):
    def test_basics(self):
        self.open("https://www.saucedemo.com")
        self.type(Page.css_1, "standard_user")
        self.type(Page.css_2, "secret_sauce\n")
        self.assert_element(Page.css_3)
        self.assert_exact_text("Products", Page.css_4)
        self.click(Page.css_5)
        self.click(Page.css_6)
        self.assert_exact_text("Your Cart", Page.css_4)
        self.assert_text("Backpack", Page.css_7)
        self.click(Page.css_8)  # HTML innerText
        self.assert_text_not_visible("Backpack", "div.cart_item")
        self.js_click(Page.css_9)
        self.assert_element(Page.css_10)

