from Class.product import Product


class Favorite(Product):
    """class representing the favorite object"""

    def __init__(self, nutriscore, barcode, name,  url, market):
        """Builder Favorites"""
        Product.__init__(
            self, nutriscore, barcode, name, url, market
            )
