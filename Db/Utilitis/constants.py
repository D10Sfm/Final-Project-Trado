"""The Class Of all the constants of the connection to Trado Cluster ***the host variable is static and the db,
collection are for specific db and collection for other collection/db connectio just need to assign the db/collection
name_xpath to new variable inside the class and set him a class and 'setup_chrome' method in the
.trado_qa_db/collections.py(for new collection connect inside this db for different db you need to open new package
with db name_xpath and create collection.py file) """


class TradoQaDbUserConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'users'  # the collection name_xpath


class TradoQaDbAdminUsersConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'adminusers'  # the collection name_xpath


class TradoQaDbCartsConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'carts'  # the collection name_xpath


class TradoQaDbCategoriesConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'categories'  # the collection name_xpath


class TradoQaDbInfoPagesConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'infopages'  # the collection name_xpath


class TradoQaDbOrdersConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'orders'  # the collection name_xpath


class TradoQaDbProductsConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'products'  # the collection name_xpath


class TradoQaDbSalesConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'sales'  # the collection name_xpath


class TradoQaDbStoresConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name_xpath
    collectionTradoQaUsers = 'stores'  # the collection name_xpath
