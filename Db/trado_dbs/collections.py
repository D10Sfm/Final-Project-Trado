"""
This file purpose is contain all the classes(collections) of trado_qa DB
each class have the methods for pulling data from the collection and some
methods are configur to manipulate and extract specific data for the tests
interest
"""

from Db.Utilitis.constants import TradoQaDbUserConstants
from pymongo.collection import Collection  # Importing the Collection class from pymongo for defined the 'noneType'
# constructor of the class with the collection type for extenuate the using of pymongo collection methods
import pprint
import pytest
from bson.objectid import ObjectId


class UsersCollections(TradoQaDbUserConstants):  # create the user collection class
    def __init__(self, collection: Collection):  # setting the constructor param type to Collection type
        self.collection = collection  # create the constructor

    def getAllRecord(self):  # define the all collection records method
        collection = self.collection.find()  # assigned the return value of find method to variable
        for record in collection:  # looping throw the return records
            pprint.pprint(record)  # printing each record with pprint method for beautify

    def getSpecificRecord(self, key, value):  # define the specific record method with key, value args
        record = self.collection.find_one({key: value})  # assigned the return value of find_one method to variable
        pretty_record = pprint.pprint(record)  # assigned the return value of pprint method on the record
        return pretty_record  # return the record variable

    def getSmsCode(self, key, value):  # define this method for extract login code
        record = self.collection.find_one({key: value})  # assigned the return value of find_one method to variable
        sms_code = record['loginCode']  # assigned the return value of the login key to variable
        return sms_code  # return the login code

    def getEmail(self, key, value):
        record = self.collection.find_one({key: value})
        email = record['email']
        return email

    def getPhone(self, key, value):  # define this method for extract phone number
        record = self.collection.find_one({key: value})  # assigned the return value of find_one method to variable
        phone = record['phone']  # assigned the return value of the login key to variable
        return phone  # return the phone number

    def delete_record(self, key, value):
        collection = self.collection
        collection.delete_one({key: value})
