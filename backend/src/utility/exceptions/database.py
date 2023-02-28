from sqlalchemy import exc as sqlalchemy_error


class DatabaseError(sqlalchemy_error.DatabaseError):
    """
    Throw an exception when there is an error in the database.
    """
