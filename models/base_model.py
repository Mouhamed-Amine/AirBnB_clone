#!/usr/bin/python3

"""
This file represente the basemodel class

"""

from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self,*args,**kwargs):


        if kwargs== {}:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return

        if 'id' not in kwargs:
            kwargs['id'] =str(uuid4())
        self.id = kwargs['id']
    
        for Key,val in kwargs.items():
            if Key == "__class_":
                continue
        if "created_at" in kwargs:
            self.created_at =datetime.strptime(
                    kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if "updated_at" in kwargs:
            self.updated_at = datetime.strptime(
                    kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        
        form = "[{}] ({}) {}"
        return form.format(
                type(self).__name__,
                self.id,
                self.__dict__)
     def save(self):
        self.updated_at = datetime.now()
     def to_dict(self):
       
        dictionary = {**self.__dict__}
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dictionary['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dictionary 
