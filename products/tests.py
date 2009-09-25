
from foa.common.tests import CommonTestCase
from foa.products.models import Product

class TestCreation(CommonTestCase):
    """ Tests the creation of FOA products to the database
    """

    def setUp(self):
        CommonTestCase.setUp(self)

    def test_productCreation(self):
        """ Tests the creation of a product object to the foa line
        """
        # First tests the null case for an assertion error
        product = Product()
        self.failUnless(AssertionError)
        # Second creates a product with the required fields only
        product = Product(title="test", description="test_description", price=19.99)
        self.failUnlessEqual(product.title, "test")
        self.failUnlessEqual(product.description, "test_description")
        self.failUnlessEqual(product.price, 19.99)


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
