#!/usr/bin/python3

"""
This file represente the basemodel class

"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self,*args,**kwargs):
        
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    
    def __str__(self):
        
        form = "[{}] ({}) {}"
        return form.format(
                type(self).__name__,
                self.id,
                self.__dict__)
     def save(self):
        self.updated_at = datetime.now()
        models.storage.save(self)

     def to_dict(self):
       
        dictionary = {**self.__dict__}
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dictionary['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dictionary 
