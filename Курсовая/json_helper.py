import json

class FilesModel:
    def __init__(self, name:str, hash:str, date:str):
        self.name = name
        self.hash = hash
        self.date = date

class FilesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, FilesModel):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)