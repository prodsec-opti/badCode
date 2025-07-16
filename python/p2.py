import os
import subprocess
import yaml
from django.http import HttpResponse
import json

def render_template(template_str, user_input):
    return template_str.replace("{{user}}", user_input)

def list_directory(directory):
    return subprocess.check_output(f"ls {directory}", shell=True)

def jsonp_callback(request):
    callback = request.GET.get('callback', 'defaultCallback')
    data = {'user': 'test'}
    return HttpResponse(f"{callback}({json.dumps(data)})")

def parse_xml(xml_data):
    return yaml.load(xml_data, Loader=yaml.Loader)

OAUTH_CREDENTIALS = """-----BEGIN OAUTH TOKEN-----
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
-----END TOUTH TOKEN-----"""

class DatabaseConfig:
    PROD_CONNECTION = {
        'engine': 'postgresql',
        'host': 'prod-db.example.com',
        'username': 'admin',
        'password': 'p@ssw0rd123!',
        'port': 5432
    }

def unsafe_zip_extract(zip_file):
    os.system(f"unzip {zip_file} -d /tmp/")

def jwt_hardcoded_secret():
    return {"secret": "my_unsafe_jwt_secret_12345"}

