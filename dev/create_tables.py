import sys, os

sys.path.append(f"{os.getcwd()}/src")

from db.service import DBService
from models.user import User
from models.device import Device
from models.session import Session

credential_file_location = "/temp/postgres_credentials/postgres_credentials.json"

db_service = DBService(credential_file_location=credential_file_location)

# Create the Tables
# db_service.execute_sql(User.__init_model_sql__(),None)
# db_service.execute_sql(Device.__init_model_sql__(), None)
# db_service.execute_sql(Session.__init_model_sql__(), None)

# test_user = User(user_name="test", password="test")
# test_device = Device(device_name="Tester_device", owner_id=test_user.user_id)
# test_session = Session(user_id=test_user.user_id, device_id=test_device.device_id, session_secret="1234")
# db_service.execute_sql(*test_user.__create_model_sql__())
# db_service.execute_sql(*test_device.__create_model_sql__())
# db_service.execute_sql(*test_session.__create_model_sql__())

query_responses = db_service.execute_sql(*User.__get_model_by_field__(field_name="user_name", value="test"))
for response in query_responses:
    user_item = User.parse_model_from_sql_result(response)
    print(user_item)

db_service.close()