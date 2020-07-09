

class Product:
    """class representing the product object"""

    def __init__(self, nutriscore, barcode, name,  url, market):
        """Builder Product"""
        self.nutriscore = nutriscore
        self.barcode = barcode
        self.name = name
        self.url = url
        self.market = market
