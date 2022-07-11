"""
This file purpose is to contain all the classes that each of them represent a collection.
inside each class(collection) will be a 'setup_chrome' method for connection to the mongo db and
yield(everything after the yield statement wil be our 'tear down' action
in this case we close the connection with the db for security measures)
 the chosen collection this will be used for a precondition at tests that will be need makes
queries and pull  data from the collection for assertion and validation in the tests.
for use this method as "precondition" of tests we use the fixture method of pytest lib.
and for the connection itself we use the pymongo lib
"""

import pytest  # import of pytest lib
import pymongo  # import of pymongo lib
from Db.Utilitis.constants import *  # import the class of the constants that contain all the data connection


class UsersCollection(TradoQaDbUserConstants):
    # create the class for the user collection that inside trado_qa DB

    @pytest.fixture(autouse=True)
    # using a decorator for using the fixture method as args*
    def setUpUsersCollection(self):  # define the 'setup_chrome' method for initiate the connection to mongo&collection
        print('Initiating the users collection')
        self.connect = pymongo.MongoClient(self.host)  # create an instance of the connection
        self.db = self.connect[self.dbTradoQa]  # assign the DB to variable **dict style
        self.collection = self.db[self.collectionTradoQaUsers]  # assign the collection from the db
        # to variable **dict style
        yield self.collection  # yielding the collection
        print("-----------------------------------------")
        print("Tests is finished")
        if self.connect is not None:  # if the connection instance is none so is already closed
            self.connect.close()  # else I will close it with the close method


class AdminUsersCollection(TradoQaDbAdminUsersConstants):
    # create the class for the admin users collection that inside trado_qa DB

    @pytest.fixture(autouse=True)
    # using a decorator for using the fixture method as args*
    def setUpAdminUsersCollection(self):  # define the 'setup_chrome' method for initiate the connection to mongo&collection
        print('Initiating the admin users collection')
        self.connect = pymongo.MongoClient(self.host)  # create an instance of the connection
        self.db = self.connect[self.dbTradoQa]  # assign the DB to variable **dict style
        self.collection = self.db[self.collectionTradoQaUsers]  # assign the collection from the db
        # to variable **dict style
        yield self.collection  # yielding the collection
        print("-----------------------------------------")
        print("Tests is finished")
        if self.connect is not None:  # if the connection instance is none so is already closed
            self.connect.close()  # else I will close it with the close method

