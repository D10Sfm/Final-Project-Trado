import requests
import pytest
from Server.Constants.registerConstants import ApiRegisterConst
from Db.trado_dbs.collections import UsersCollections
from Db.Utilitis.preConditions import UsersCollection


@pytest.mark.server
class TestRegistration(ApiRegisterConst):
    @pytest.mark.sanity
    def test_valid_register(self):
        url = self.base_url
        mydata = self.mydata
        response = requests.post(url, json=mydata)
        res_data = response.json()
        if response.elapsed.total_seconds() > 10:
           assert res_data['message'] == self.operation_err_msg
        else:
            assert res_data['status'] == 200
            assert response.elapsed.total_seconds() < 5
            return mydata['phone']


    def test_invalid_register_exist_user(self):
        url = self.base_url
        mydata = self.mydata
        mydata['phone'] = '0525086651'
        response = requests.post(url, json=mydata)
        res_data = response.json()
        if response.elapsed.total_seconds() > 10:
           assert res_data['message'] == self.operation_err_msg
        else:
            assert response.status_code == 200
            assert res_data['err']['message'] == "not unique"
            assert response.elapsed.total_seconds() < 5




    def test_invalid_register_unmarked_policy(self):
        url = self.base_url
        mydata = self.mydata
        mydata["policy"] = 'false'
        response = requests.post(url, json=mydata)
        res_data = response.json()
        if response.elapsed.total_seconds() > 10:
           assert res_data['message'] == self.operation_err_msg
        else:
            assert res_data['message'] == "please approve owr policy"
            assert res_data['status'] == 400
            assert response.elapsed.total_seconds() < 5


@pytest.mark.db
@pytest.mark.usefixtures('setUpUsersCollection')
class TestDbValidation(TestRegistration,UsersCollection):

    def test_valid_register_validation(self):
        collection = self.collection
        users = UsersCollections(collection)
        register_phone = self.test_valid_register()
        phone = users.getPhone('phone',register_phone)
        assert register_phone == phone


