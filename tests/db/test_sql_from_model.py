from pydantic import BaseModel
from typing import Union

from db import sql_from_model

def test_sql_create_object():
    # Setup
    class Test(BaseModel):
        test_id: Union[str, None] = None
        test_name: str
        test_length: int
        test_result: str

    test_1 = Test(test_name="Test1", test_length=10, test_result="Good")

    expected_sql_template = "INSERT INTO %s (test_name,test_length,test_result) VALUES (%s,%s,%s)"
    expected_values = ("tests","Test1", 10, "Good")
    # Run
    resulted_sql_template, resulted_values = sql_from_model.create_sql_insert_to_object(test_1)

    # ASSERT
    assert expected_sql_template == resulted_sql_template
    for index, item in enumerate(expected_values):
        assert resulted_values[index] == item