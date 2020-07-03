"""program constant, """
"""sql request to add products and tables necessary for use"""

##############################################################################


TABLES = {}

TABLES["Categories"] = (
    "CREATE TABLE `Categories` ("
    "  categorie VARCHAR(210) NOT NULL PRIMARY KEY"
    ") ENGINE=InnoDB"
)

TABLES["Products"] = (
    "CREATE TABLE `Products` ("
    "  barcode VARCHAR(14) NOT NULL PRIMARY KEY,"
    "  name VARCHAR(210) NOT NULL,"
    "  score CHAR(1) NULL,"
    "  url TEXT NULL,"
    "  market VARCHAR(210) NULL"
    ") ENGINE=InnoDB"
)

TABLES["Favorites"] = (
    "CREATE TABLE `Favorites` ("
    "  fav_id VARCHAR(14) PRIMARY KEY, "
    "  CONSTRAINT fav_id FOREIGN KEY (fav_id) "
    "     REFERENCES Products (barcode) ON DELETE CASCADE,"
    "  UNIQUE KEY (fav_id)"
    ") ENGINE=InnoDB"
)

TABLES["Relations"] = (
    "CREATE TABLE `Relations` ("
    "  categorie VARCHAR(210) NOT NULL, "
    "  barcode VARCHAR(14) NOT NULL,"
    "  CONSTRAINT categorie FOREIGN KEY (categorie) "
    "     REFERENCES Categories (categorie) ON DELETE CASCADE,"
    "  CONSTRAINT barcode FOREIGN KEY (barcode) "
    "     REFERENCES Products (barcode) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

###############################################################################
