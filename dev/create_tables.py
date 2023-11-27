import sys, os

sys.path.append(f"{os.getcwd()}/src")

from db.service import DBService
from models.user import UserDB
from models.device import Device
from models.session import Session

credential_file_location = "/temp/postgres_credentials/postgres_credentials.json"

db_service = DBService(credential_file_location=credential_file_location)

# Create the Tables
# print("Create Tables")
# db_service.create_table(User)
# db_service.create_table(Device)
# db_service.create_table(Session)


# print("Create Objects")
# test_user = db_service.insert(User, user_name="test2", password="test")
# test_device = db_service.insert(Device, device_name="Tester_device3", owner_id=test_user.user_id)
# test_device = db_service.insert(Device, device_name="Tester_device2", owner_id=test_user.user_id)
# test_session = db_service.insert(Session,user_id=test_user.user_id, device_id=test_device.device_id, session_secret="1234")

print("Get objects")
find_user = db_service.select(UserDB, user_name="test2")
find_session = db_service.select(Session, user_id=find_user.user_id)
find_devices = db_service.select(Device, owner_id=find_user.user_id)
print(f"Found User: {find_user}")
print(f"The user owns the following devices: {find_devices} ")
print(f"The user currently has the session {find_session}")
# query_responses = db_service.__execute_sql__(*User.__get_model_by_field__(field_name="user_name", value="test"))
# for response in query_responses:
#     user_item = User.parse_model_from_sql_result(response)
#     print(user_item)

db_service.close()