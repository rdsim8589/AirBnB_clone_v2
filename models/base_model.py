#!/usr/bin/python3
import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
        for k in kwargs:
            print("kwargs: {}: {}".format(k, kwargs[k]))

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe