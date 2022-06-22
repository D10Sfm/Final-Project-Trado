import allure
import pytest
# from Db.Utilitis.preConditions import UsersCollection
# import Db.trado_qa_db.collections as collections
import requests
from Server.Constants.loginConstants import ApiLoginConst

@allure.description("This class is set of functional tests for login feature[chrome]")
@allure.severity(allure.severity_level.CRITICAL)
# @pytest.mark.usefixtures('setUpUsersCollection')
@pytest.mark.server
@pytest.mark.serverlogin
class TestLogin(ApiLoginConst):
    @pytest.mark.sanity
    def test_valid_phone_login(self):
        url= self.base_url
        mydata = self.mydata
        response = requests.post(url, json=mydata)
        res_data = response.json()
        print(res_data)
        if response.elapsed.total_seconds() > 10:
           assert res_data['message'] == self.operation_err_msg
        else:
            assert res_data['status'] == 200
            assert response.elapsed.total_seconds() < 5


    def test_invalid_phone_login_non_existent(self):
        url= self.base_url
        mydata = self.mydata
        invalid_phone = "0545477821"
        mydata['phone'] = invalid_phone
        respone = requests.post(url, json=mydata)
        res_data = respone.json()
        assert res_data['status'] == 400
        if respone.elapsed.total_seconds() > 10:
           assert res_data['message'] == self.operation_err_msg
        else:
            assert self.non_exist_user_err_msg == res_data['message']
            assert respone.elapsed.total_seconds() < 5


    def test_invalid_phone_login_over(self):
        url = self.base_url
        mydata = self.mydata
        invalid_phone = "0585621541455"
        mydata['phone'] = invalid_phone
        respone = requests.post(url, json=mydata)
        res_data = respone.json()
        assert res_data['status'] == 400
        if respone.elapsed.total_seconds() > 10:
           assert res_data['message'] == self.operation_err_msg
        else:
            assert "no such user please register" == res_data['err']
            assert respone.elapsed.total_seconds() < 5
    @pytest.mark.xfail
    def test_facebook_api_link(self):
        url = self.facebook_api
        respone = requests.get(url)
        print(respone.json())
        assert 200 == respone.status_code


    def test_twitter_api_link(self):
        url = self.twitter_api
        respone = requests.get(url)
        assert 401 == respone.status_code

