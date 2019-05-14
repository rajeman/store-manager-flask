create_user_valid_data = {
    "name": "Brian Anoete",
    "email": "brian.anoete@andela.com"
}

create_user_expected_response = {
    "message": "account created for Brian Anoete"}

create_user_duplicate_email = {
    "email": "suzan.nice@hoc.com",
    "name": "Suzan Nice"
}

create_user_duplicate_email_response = {
    "error": "email in use"
}

create_user_invalid_name = {
    "name": "BA",
    "email": "brian.anoete@andela.com"
}

create_user_invalid_email = {
    "email": "brian.anoete.com",
    "name": "brian.anoete@andela.com"
}

create_user_invalid_detail_response = {
    "error": "Invalid input. Make sure email is valid and name is at least 3 characters"
}
