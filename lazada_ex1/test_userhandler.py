#########################################################################
# Test cases
# The file provides the test cases to cover User handler
# __author__ = 'Hoa Tran'
#########################################################################

import test_lib
import test_variables
import logging

def test_get_user():
    logging.info("Get All Users...")
    # Retrieve data of all users
    url_all_user = test_variables.url_all
    r = test_lib.get_data(url_all_user)
    data_all = r.json()
    # Check if all users are retrieved
    count = 0
    for user in data_all:
        for user_element in user:
            if user_element == test_variables.user_id_element:
                count += 1
    assert count == test_variables.number_of_all_user
    # Check if all user's info are retrieved
    for user1 in data_all:
        assert test_lib.verify_element(user1, test_variables.list_user_elements) == True

    logging.info("Get One Random User...")
    # Get one random user id
    random_user_id = test_lib.issue_random(test_variables.user_id_min, test_variables.user_id_max)
    # Retrieve user data
    url_by_one = test_variables.url_all + str(random_user_id)
    r = test_lib.get_data(url_by_one)
    data_one = r.json()
    # Check if number of retrieved user is correct (=1)
    count = 0
    for user_element in data_one:
        if user_element == test_variables.user_id_element:
            count += 1
    assert count == test_variables.number_of_one_user
    # Check if user id is correct
    assert data_one[test_variables.user_id_element] == random_user_id
    # Check if all user's info is retrieved
    assert test_lib.verify_element(data_one, test_variables.list_user_elements) == True

    logging.info("Get an user with invalid boundary id...")
    # Get one random user with invalid boundary bottom id
    random_invalid_id1 = test_lib.issue_random(test_variables.user_id_min - 10, test_variables.user_id_min - 1)
    invalid_url1 = test_variables.url_all + str(random_invalid_id1)
    # Retrieve invalid user data
    r = test_lib.get_data(invalid_url1)
    data_invalid1 = r.json()
    # Check null data is returned
    assert len(data_invalid1) == 0
    # Get one random user with invalid boundary top id
    random_invalid_id2 = test_lib.issue_random(test_variables.user_id_max + 1, test_variables.user_id_max + 10)
    invalid_url2 = test_variables.url_all + str(random_invalid_id2)
    # Retrieve invalid user data
    r = test_lib.get_data(invalid_url2)
    data_invalid2 = r.json()
    # Check null data is returned
    assert len(data_invalid2) == 0

def test_search_user():
    logging.info("Search User By Name...")
    # Get one random name of user
    random_int = test_lib.issue_random(0, len(test_variables.list_user_names) - 1)
    random_name = str(test_variables.list_user_names[random_int])
    # Search user data by name
    url_by_name = test_variables.url_search + "name="
    url_by_name += random_name
    r = test_lib.get_data(url_by_name)
    data_by_name = r.json()
    # Check if number of retrieved users is correct (=1)
    count = 0
    for user in data_by_name:
        for user_element in user:
            if user_element == test_variables.user_id_element:
                count += 1
    assert count == test_variables.number_of_one_user
    # Check if the returned name is correct
    assert data_by_name[0][test_variables.user_name_element] == random_name
    # Check if all user's info is retrieved
    for user1 in data_by_name:
        assert test_lib.verify_element(user1, test_variables.list_user_elements) == True

    logging.info("Search User By Name and Username...")
    # Get one random name of user
    random_int = test_lib.issue_random(0, len(test_variables.list_user_names) - 1)
    random_name = str(test_variables.list_user_names[random_int])
    random_username = str(test_variables.list_usernames[random_int])
    # Search user data by name and username
    url_multi = test_variables.url_search + "name="
    url_multi += random_name
    url_multi += "&username="
    url_multi += random_username
    r = test_lib.get_data(url_multi)
    data_multi = r.json()
    count = 0
    for user in data_multi:
        for user_element in user:
            if user_element == test_variables.user_id_element:
                count += 1
    assert count == test_variables.number_of_one_user
    # Check if user name and username are correct
    assert data_multi[0][test_variables.user_name_element] == random_name or data_multi[0][
        test_variables.username_element] == random_username
    # Check if all user's info is retrieved
    for user1 in data_multi:
        assert test_lib.verify_element(user1, test_variables.list_user_elements) == True

    logging.info("Search By Single Invalid data: invalid name' ")
    # Search user by invalid name
    invalid_name = "INVALID"
    url_single_invalid = test_variables.url_search + "name="
    url_single_invalid += invalid_name
    r = test_lib.get_data(url_single_invalid)
    data_single_invalid = r.json()
    # Check if null data is returned
    assert len(data_single_invalid) == 0

    # Search user by multiple invalid data: correct id, name and invalid username
    invalid_name = "INVALID"
    random_int = test_lib.issue_random(0, len(test_variables.list_user_names) - 1)
    random_name = str(test_variables.list_user_names[random_int])
    # Config multiple invalid data: correct id, name and invalid name
    url_multi_invalid = test_variables.url_search + "id="
    url_multi_invalid += str(random_int + 1)
    url_multi_invalid += "&name="
    url_multi_invalid += random_name
    url_multi_invalid += "&name="
    url_multi_invalid += invalid_name
    r = test_lib.get_data(url_multi_invalid)
    data_multi_invalid = r.json()
    # Check null data is returned
    assert  len(data_multi_invalid) == 0

def test_create_user():
    logging.info("Create User...")
    # Prepare user data
    payload = test_variables.list_payload
    # Create user
    url = test_variables.url_all
    r = test_lib.post_data(url, payload)
    data = r.json()
    # Check if number of created user is correct (=1)
    count = 0
    for user_element in data:
        if user_element == test_variables.user_id_element:
            count += 1
    assert count == test_variables.number_of_one_user
    # Check if all user's info is created
    assert test_lib.verify_element(data, test_variables.list_user_elements) == True
