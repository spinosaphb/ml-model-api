from pymongo.results import InsertOneResult
from bson.objectid import ObjectId

def handle_create_result(result: InsertOneResult):
    """
    Handle result
    """
    return {'id': str(result.inserted_id)}


class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        """
        Valid Object Id
        """
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid object_id")
        return ObjectId(value)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
