"""program constant, sql request to add products and tables necessary for use"""

#################################################################################################


TABLES = {}

TABLES["Categories"] = (
    "CREATE TABLE `Categories` ("
    "   `c_id` SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `name` VARCHAR(120)"
    ") ENGINE=InnoDB"
)

TABLES["Products"] = (
    "CREATE TABLE `Products` ("
    "   `p_id` SMALLINT NOT NULL AUTO_INCREMENT PRIMARY KEY,"
    "   `cat_id` SMALLINT NOT NULL, "
    "   `name` VARCHAR(210) NOT NULL,"
    "   `barcode` CHAR(14) NOT NULL,"
    "   `score` CHAR(1) NULL,"
    "   `url` TEXT NULL,"
    "   `market` VARCHAR(210) NULL,"
    "  CONSTRAINT `cat_id` FOREIGN KEY (`cat_id`) "
    "     REFERENCES `Categories` (`c_id`) ON DELETE CASCADE"
    ") ENGINE=InnoDB"
)

TABLES["Favorites"] = (
    "CREATE TABLE `Favorites` ("
    "   `fav_id` SMALLINT PRIMARY KEY, "
    "  CONSTRAINT `fav_id` FOREIGN KEY (`fav_id`) "
    "     REFERENCES `Products` (`p_id`) ON DELETE CASCADE,"
    "  UNIQUE KEY (`fav_id`)"
    ") ENGINE=InnoDB"
)

#################################################################################################
