from flask import Flask, request, render_template
import requests
import yaml

class CustomFlaskApp(Flask):
    def __init__(self, *args, **kwargs):
        super(CustomFlaskApp, self).__init__(*args, **kwargs)
        self.base_url = None
        self.get_yaml_data()

    def load_yaml(self):
        with open('application.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data

    def get_yaml_data(self):
        yaml_data = self.load_yaml()
        self.base_url = yaml_data['base_url']

app = CustomFlaskApp(__name__)
GET = 'GET'
POST = 'POST'
@app.route("/", methods = [GET, POST])
def root():
    print(f"base_url: {app.base_url}")
    return render_template('index.html')
    