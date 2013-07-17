import sys
import os
sys.path.insert(0, os.path.abspath('..'))
from jinja2 import Environment, PackageLoader

def render(name_of_template, **kwargs):
    env = Environment(loader=PackageLoader('terrikon', 'templates'))
    template = env.get_template(name_of_template)
    return template.render(**args)
