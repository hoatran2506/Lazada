#########################################################################
# Test cases
# The file provides the test cases to cover User handler
# __author__ = 'Hoa Tran'
#########################################################################

import test_lib
import test_variables
import logging

def test01_get_all_users():
    try:
        logging.info("Running Test01_Get_All_Users...")
        #Retrieve user data
        url = test_variables.url_all
        r = test_lib.get_data(url)
        data = r.json()
        #Check null data
        if not data:
            raise Exception("List of users is empty!")
        #Check if all users are retrieved
        count = 0
        for user in data:
            for user_element in user:
                if user_element == test_variables.user_id_element:
                    count += 1
        if count != test_variables.number_of_all_user:
            logging.error("Number of retrieved user: "+str(count))
            raise Exception("All users are not fully retrieved!")
        #Check if all user's info are retrieved
        for user1 in data:
            if test_lib.verify_element(user1,test_variables.list_user_elements) != True:
                logging.error("Missing user's info: " + str(user1))
                raise Exception("All user's info is not fully retrieved!")
    except Exception as e:
        logging.error(e)
        raise

def test02_get_one_user():
    try:
        logging.info("Running Test02_Get_One_User...")
        #Get one random user id
        random_user_id = test_lib.issue_random(test_variables.user_id_min, test_variables.user_id_max)
        # Retrieve user data
        url = test_variables.url_all + str(random_user_id)
        r = test_lib.get_data(url)
        data = r.json()
        # Check null data
        if not data:
            raise Exception("List of user's info is empty!")
        # Check if number of retrieved user is correct (=1)
        count = 0
        for user_element in data:
            if user_element == test_variables.user_id_element:
                count += 1
        if count != test_variables.number_of_one_user:
            logging.error("Number of retrieved user: " + str(count))
            raise Exception("Number of retrieved user is incorrect!")
        # Check if user id is correct
        if data[test_variables.user_id_element] != random_user_id:
            logging.error("User's id is incorrect: " + str(data[test_variables.list_user_elements]))
            raise Exception("User's id is incorrect!")
        # Check if all user's info is retrieved
        if test_lib.verify_element(data, test_variables.list_user_elements) != True:
            logging.error("Missing user's info: " + str(user1))
            raise Exception("User's info is not fully retrieved!")
    except Exception as e:
        logging.error(e)
        raise

def test03_get_invalid_user():
    try:
        logging.info("Running Test03_Get_Invalid_User...")
        # Get one random user with invalid boundary bottom id
        random_user_id = test_lib.issue_random(test_variables.user_id_min-10, test_variables.user_id_min-1)
        url = test_variables.url_all + str(random_user_id)
        # Retrieve invalid user data
        r = test_lib.get_data(url)
        data = r.json()
        # Check null data
        if data:
            raise Exception("List of user's info is NOT empty!")
        # Get one random user with invalid boundary top id
        random_user_id = test_lib.issue_random(test_variables.user_id_max +1, test_variables.user_id_max + 10)
        url = test_variables.url_all + str(random_user_id)
        # Retrieve invalid user data
        r = test_lib.get_data(url)
        data = r.json()
        # Check null data
        if data:
            raise Exception("List of user's info is NOT empty!")
    except Exception as e:
        logging.error(e)
        raise

def test20_search_by_name():
    try:
        logging.info("Running Test20_Search_User_By_Name...")
        # Get one random name of user
        random_int = test_lib.issue_random(0, len(test_variables.list_user_names)-1)
        random_name = str(test_variables.list_user_names[random_int])
        # Search user data by name
        url = test_variables.url_search + "name="
        url += random_name
        r = test_lib.get_data(url)
        data = r.json()
        # Check null data
        if not data:
            raise Exception("List of user's info is empty!")
        # Check if number of retrieved user is correct (=1)
        count = 0
        for user in data:
            for user_element in user:
                if user_element == test_variables.user_id_element:
                    count += 1
        if count != test_variables.number_of_one_user:
            logging.error("Number of retrieved user: " + str(count))
            raise Exception("Number of retrieved user is incorrect!")
        # Check if user name is correct
        if data[0][test_variables.user_name_element] != random_name:
            logging.error("User's name is incorrect: " + str(data[test_variables.list_user_elements]))
            raise Exception("User's name is incorrect!")
        # Check if all user's info is retrieved
        for user1 in data:
            if test_lib.verify_element(user1,test_variables.list_user_elements) != True:
                logging.error("Missing user's info: " + str(user1))
                raise Exception("All user's info is not fully retrieved!")
    except Exception as e:
        logging.error(e)
        raise

def test21_search_by_name_username():
    try:
        logging.info("Running Test21_Search_User_By_Name_And_Username...")
        # Get one random name of user
        random_int = test_lib.issue_random(0, len(test_variables.list_user_names)-1)
        random_name = str(test_variables.list_user_names[random_int])
        random_username = str(test_variables.list_usernames[random_int])
        # Search user data by name and username
        url = test_variables.url_search + "name="
        url += random_name
        url += "&username="
        url += random_username
        r = test_lib.get_data(url)
        data = r.json()
        # Check null data
        if not data:
            raise Exception("List of user's info is empty!")
        # Check if number of retrieved user is correct (=1)
        count = 0
        for user in data:
            for user_element in user:
                if user_element == test_variables.user_id_element:
                    count += 1
        if count != test_variables.number_of_one_user:
            logging.error("Number of retrieved user: " + str(count))
            raise Exception("Number of retrieved user is incorrect!")
        # Check if user name and username are correct
        if data[0][test_variables.user_name_element] != random_name or data[0][test_variables.username_element] != random_username:
            logging.error("User's name or username is incorrect: " + str(data[test_variables.list_user_elements]))
            raise Exception("User's name or username is incorrect!")
        # Check if all user's info is retrieved
        for user1 in data:
            if test_lib.verify_element(user1,test_variables.list_user_elements) != True:
                logging.error("Missing user's info: " + str(user1))
                raise Exception("All user's info is not fully retrieved!")
    except Exception as e:
        logging.error(e)
        raise

def test22_search_by_invalid_data():
    try:
        logging.info("Running Test22_Search_By_Invalid_Data...")
        # Search user by invalid name
        invalid_name = "INVALID"
        url = test_variables.url_search + "name="
        url += invalid_name
        r = test_lib.get_data(url)
        data = r.json()
        # Check null data
        if data:
            raise Exception("List of user's info is NOT empty!")
        # Search user by invalid name and username
        invalid_username = "INVALID"
        url = test_variables.url_search + "name="
        url += invalid_name
        url += "&username="
        url += invalid_username
        r = test_lib.get_data(url)
        data = r.json()
        # Check null data
        if data:
            raise Exception("List of user's info is NOT empty!")
    except Exception as e:
        logging.error(e)
        raise

def test30_create_user():
    try:
        logging.info("Running Test30_Create_User...")
        # Prepare user data
        payload = test_variables.list_payload
        # Create user
        url = test_variables.url_all
        r = test_lib.post_data(url, payload)
        data = r.json()
        # Check null data
        if not data:
            raise Exception("List of user's info is empty!")
        # Check if number of created user is correct (=1)
        count = 0
        for user_element in data:
            if user_element == test_variables.user_id_element:
                count += 1
        if count != test_variables.number_of_one_user:
            logging.error("Number of created user: " + str(count))
            raise Exception("Number of created user is incorrect!")
        # Check if all user's info is created
        if test_lib.verify_element(data, test_variables.list_user_elements) != True:
            logging.error("Missing user's info: " + str(user1))
            raise Exception("User's info is not fully retrieved!")
    except Exception as e:
        logging.error(e)
        raise
