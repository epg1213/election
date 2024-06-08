import json
import os.path

class Parti:
    partis={}
    def list(values=True):
        if values:
            return list(Parti.partis.values())
        return list(Parti.partis.keys())

    def get(name):
        if name in Parti.partis:
            return Parti.partis[name]
        return None

    def __init__(self, name: str):
        if not os.path.isfile(f"programmes/{name}.json"):
            return None
        with open(f"programmes/{name}.json", "r") as file:
            self.programme=json.load(file)
        self.name=name
        Parti.partis[name]=self
    
    def __str__(self):
        return self.name

    def get_proposition(self, sujet: str):
        if sujet in self.programme and self.programme[sujet]!='':
            return self.programme[sujet]
        return "Ce parti n'a rien proposé"
    