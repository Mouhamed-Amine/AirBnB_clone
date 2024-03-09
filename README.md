# AirBnB clone project
#1 At the beginning we have created BaseModel.py file that has an attribut,methods we are going to use in the project later
those attribut are id,created at and updated_at.//

we've learned new concept which is uuid to initialize id attribut with and then the created and updated attribut get initilized using datetime module.

The goal of building BaseModel like that is to create a persistent storage engine that we can rely on when we move on later.

The next step is to use fileStorage to save the data that we already converted to JSON format for a consistent system.

we have initialize it in __init__.py file,made a file called fileStorage.py within package engine in which i used dump and load to serialize and deserialize the data, and then the methods created will be used in BaseModel.py file 
