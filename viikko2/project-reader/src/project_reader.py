from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
      
        toml_dict = toml.loads(content)['tool']['poetry']

        return Project(
            toml_dict['name'],
            toml_dict['description'],
            toml_dict['dependencies'], 
            toml_dict['dev-dependencies']
            )