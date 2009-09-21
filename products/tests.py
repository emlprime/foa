"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from foa.common.tests import CommonTestCase

class NavigationTestCase(CommonTestCase):
    """
    Tests the site's navigability.
    """

    def setUp(self):
        CommonTestCase.setUp(self)

    def test_clickThrough(self):
        """
        Alice visits the site.  She should be able to...
        """
        alice=self.alice
        # Arrive at the home page
        doc=alice.clicks_a_link('/', templates_used=["base.html", "index.html"])
        # See the links to the other pages
        alice.sees_a_link(doc=doc, href="/products/")
        alice.sees_a_link(doc=doc, href="/about/")
        # Click the links to the other pages
        alice.clicks_a_link("/products/", templates_used=["base.html", "products.html"])
        alice.clicks_a_link("/about/", templates_used=["base.html", "about.html"])
