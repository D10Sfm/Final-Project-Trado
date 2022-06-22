import requests
import pytest
from Server.Constants.footerConstants import ApiFooterConst

@pytest.mark.server
class Test_FooterAPI(ApiFooterConst):
    def test_(self):
        url = self.base_url
        mydb = {""}
        response = requests.post(url, json=mydb)
        res_data = response.json()
        assert res_data['status'] == 200
        assert response.elapsed.total_seconds() < 5