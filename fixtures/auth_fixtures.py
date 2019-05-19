login_user_valid_data = {
    'email': 'suzan.nice@hoc.com',
    'password': 'somecrazeypassword'
}

login_admin_valid_data = {
    'email': 'gregory.best@hoc.com',
    'password': 'somecrazeypassword'
}

login_user_invalid_password = {
    'email': 'suzan.nice@hoc.com',
    'password': 'somepassword'
}

login_user_invalid_email = {
    'email': 'suzan.nissse@hoc.com',
    'password': 'somecrazeypassword'
}

login_user_invalid_detail_expected_response = {
    'error': 'Invalid email or password'
}

login_user_no_json_data_expected_response = {
    'msg': 'Missing JSON in request'
}
