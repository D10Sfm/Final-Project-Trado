"""The Class Of all the constants of the connection to Trado Cluster ***the host variable is static and the db,
collection are for specific db and collection for other collection/db connectio just need to assign the db/collection
name to new variable inside the class and set him a class and 'setup_chrome' method in the .trado_qa_db/collections.py(for
new collection connect inside this db for different db you need to open new package with db name and create
collection.py file) """


class TradoQaDbUserConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'users'  # the collection name




class TradoQaDbAdminUsersConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'adminusers'  # the collection name


class TradoQaDbCartsConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'carts'  # the collection name


class TradoQaDbCategoriesConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'categories'  # the collection name


class TradoQaDbInfoPagesConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'infopages'  # the collection name


class TradoQaDbOrdersConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'orders'  # the collection name


class TradoQaDbProductsConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'products'  # the collection name


class TradoQaDbSalesConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'sales'  # the collection name


class TradoQaDbStoresConstants:
    host = 'mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority'
    # the host URI
    dbTradoQa = 'trado_qa'  # db name
    collectionTradoQaUsers = 'stores'  # the collection name
