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
        self.write_log_file(yaml.dump(yaml_data))
        self.base_url = yaml_data['base_url']

    def write_log_file(self, *args, **kwargs):
        for arg in args:
            str_format = ''
            str_format += arg
            with open('log.log', 'a') as f:
                f.write(f"[@@@] {str_format}")
        for key, value in kwargs.items():
            str_format = ''
            str_format += f"{key}: {value}"
            with open('log.log', 'a') as f:
                f.write(f"[@@@] {str_format}")

app = CustomFlaskApp(__name__)
GET = 'GET'
POST = 'POST'
@app.route("/", methods = [GET, POST])
def root():
    app.write_log_file(f"base_url: {app.base_url}")
    return render_template('index.html')
