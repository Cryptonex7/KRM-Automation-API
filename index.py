# Imports
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.contrib.fixers import ProxyFix
from werkzeug.utils import cached_property
from flask_restplus import Resource, Api, fields
from flask_cors import CORS
from flask import Flask
import pandas as pd
import json

# Supress Warnings
import warnings
warnings.simplefilter('ignore')

# import variables
import services.student as st
import services.company as cp

app = Flask(__name__)
### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "covid19analytics"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
          version='0.1',
          title='Our sample API',
          description='This is our sample API'
          )

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


@app.route('/analyse')
def update():
    print("Welcome to KRM!")

    data = {
        'student': {
            'stud_hired_per_year_bar': st.stud_hired_per_year_bar,
            'stud_hired_per_year_pie': st.stud_hired_per_year_pie,
            'stud_gender_pie': st.stud_gender_pie,
            'stud_branch_pie': st.stud_branch_pie,
            'stud_package_hbar': st.stud_package_hbar,
            'stud_cgpa_line': st.stud_cgpa_line,
            'stud_profile_hbar': st.stud_profile_hbar,
        },
        'company': {
            'comp_profile_pie': cp.comp_profile_pie,
            'comp_cgpa_hbar': cp.comp_cgpa_hbar,
            'comp_branch_pie': cp.comp_branch_pie,
            'comp_gender_pie': cp.comp_gender_pie,
        }
    }
    return json.dumps(data)


if __name__ == "__main__":
    app.run(debug=True)  # for deployment turn it off(False)
