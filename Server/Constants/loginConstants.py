class ApiLoginConst:
    # urls
    base_url = 'https://qa.trado.co.il/api/user/logincode'
    twitter_api = 'https://cors.bridged.cc/https://api.twitter.com/oauth/request_token'

    #data
    mydata = {"phone": "0502659178", "type": "phone"}


    # err msg
    operation_err_msg = 'Operation `users.aggregate()` buffering timed out after 10000ms'
    non_exist_user_err_msg = "no such user please register"