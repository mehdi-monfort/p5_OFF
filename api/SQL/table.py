"""sql request to add products and tables necessary for use"""

##############################################################################


TABLES = {}

TABLES["Categories"] = (
    "CREATE TABLE `Categories` ("
    "  cat_id SMALLINT AUTO_INCREMENT PRIMARY KEY,"
    "  categorie VARCHAR(210) NOT NULL"
    ") ENGINE=InnoDB"
)

TABLES["Products"] = (
    "CREATE TABLE `Products` ("
    "  score CHAR(1) NOT NULL,"
    "  barcode VARCHAR(14) NOT NULL PRIMARY KEY,"
    "  name VARCHAR(210) NOT NULL,"
    "  url TEXT NULL,"
    "  market VARCHAR(210) NULL"
    ") ENGINE=InnoDB"
)

TABLES["Relations"] = (
    "CREATE TABLE `Relations` ("
    "  cat_id SMALLINT NOT NULL, "
    "  barcode VARCHAR(14) NOT NULL,"
    "  CONSTRAINT cat_id FOREIGN KEY (cat_id) "
    "     REFERENCES Categories (cat_id) ON DELETE CASCADE,"
    "  CONSTRAINT barcode FOREIGN KEY (barcode) "
    "     REFERENCES Products (barcode) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

TABLES["Favorites"] = (
    "CREATE TABLE `Favorites` ("
    "  code VARCHAR(14) PRIMARY KEY, "
    "  CONSTRAINT code FOREIGN KEY (code) "
    "     REFERENCES Relations (barcode) ON DELETE CASCADE,"
    "  UNIQUE KEY (code)"
    ") ENGINE=InnoDB"
)

###############################################################################
