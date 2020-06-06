# Imports
import json
# Supress Warnings
import warnings

import pandas as pd
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.contrib.fixers import ProxyFix
from werkzeug.utils import cached_property

import services.company as cp
# import variables
import services.student as st

warnings.simplefilter('ignore')


app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testUser:12345@localhost/krmdata'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iisvqvdsyxlvgy:f4a9d2df20edbddd173a0283fdaaa96b7c5657c5a9e52b65b4ba4534422dca79@ec2-34-194-198-176.compute-1.amazonaws.com:5432/d3fk9q73hl4l9t'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


### Swagger Config ###
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "KIIT KRM API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### End Swagger Config ###

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app,
          version='0.1',
          title='Welcom to KRM Automation API',
          description='The Power of Analytics to Korporate Relationship Management!'
          )

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Student db schema


class StudentData(db.Model):
    __tablename__ = 'studentdata'
    rollno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(200), nullable=False)
    cgpa = db.Column(db.Float, nullable=False)
    company = db.Column(db.String(200), nullable=False)
    profile = db.Column(db.String(200), nullable=False)
    ctc = db.Column(db.Float, nullable=False)

    def __init__(self, rollno, name, gender, branch, cgpa, company, profile, ctc):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.branch = branch
        self.cgpa = cgpa
        self.company = company
        self.profile = profile
        self.ctc = ctc

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Student form


@app.route('/studentform')
def studentform():
    return render_template('studentform.html')

# Get all student details


@app.route('/student/getall')
def get_student_data():
    try:
        return jsonify(student_list=[i.as_dict() for i in db.session.query(StudentData).all()])
    except:
        response = app.response_class(
            response=json.dumps(
                'Student data not found, try enterning some data using /students/add'),
            status=404,
            mimetype='application/json'
        )
        return response

# Add new students to the db


@app.route('/student/add', methods=['POST'])
def submit_student_data():
    if request.method == 'POST':
        rollno = request.form['rollno']
        name = request.form['studName']
        gender = request.form['gender']
        branch = request.form['branch']
        cgpa = request.form['cgpa']
        company = request.form['company']
        profile = request.form['profile']
        ctc = request.form['ctc']

        if gender == 'M' or gender == 'Male':
            gender = 'M'
        elif gender == 'F' or gender == 'Female':
            gender = 'F'
        else:
            gender = 'O'

        if db.session.query(StudentData).filter(StudentData.rollno == rollno).count() == 0:
            data = StudentData(rollno, name, gender, branch,
                               cgpa, company, profile, ctc)
            db.session.add(data)
            db.session.commit()
            print(rollno, name, gender, branch, cgpa, company, profile, ctc)
            print("Data added")

            return jsonify(student_list=[i.as_dict() for i in db.session.query(StudentData).all()])

        response = app.response_class(
            response=json.dumps(
                'Could not add new student, check for duplicate roll number'),
            status=400,
            mimetype='application/json'
        )
        return response


# company db schema
class CompanyData(db.Model):
    __tablename__ = 'companydata'
    name = db.Column(db.String(200), nullable=False)
    compid = db.Column(db.String(250), primary_key=True)
    hired15 = db.Column(db.Integer, nullable=False)
    hired16 = db.Column(db.Integer, nullable=False)
    hired17 = db.Column(db.Integer, nullable=False)
    hired18 = db.Column(db.Integer, nullable=False)
    hired19 = db.Column(db.Integer, nullable=False)

    def __init__(self, name, compid, hired15, hired16, hired17, hired18, hired19):
        self.name = name
        self.compid = compid
        self.hired15 = hired15
        self.hired16 = hired16
        self.hired17 = hired17
        self.hired18 = hired18
        self.hired19 = hired19

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Company form


@app.route('/companyform')
def compnayform():
    return render_template('companyform.html')

# Get all company details


@app.route('/company/getall')
def get_company_data():
    try:
        return jsonify(company_list=[i.as_dict() for i in db.session.query(CompanyData).all()])
    except:
        response = app.response_class(
            response=json.dumps(
                'company data not found, try enterning some data using /companys/add'),
            status=404,
            mimetype='application/json'
        )
        return response

# Add new company to the db


@app.route('/company/add', methods=['POST'])
def submit_company_data():
    if request.method == 'POST':
        name = request.form['name']
        compid = request.form['compid']
        hired15 = request.form['hired15']
        hired16 = request.form['hired16']
        hired17 = request.form['hired17']
        hired18 = request.form['hired18']
        hired19 = request.form['hired19']

        if db.session.query(CompanyData).filter(CompanyData.compid == compid).count() == 0:
            data = CompanyData(name, compid, hired15,
                               hired16, hired17, hired18, hired19)
            db.session.add(data)
            db.session.commit()
            print(name, compid, hired15, hired16, hired17, hired18, hired19)
            print("Data added")

            return jsonify(company_list=[i.as_dict() for i in db.session.query(CompanyData).all()])

        response = app.response_class(
            response=json.dumps(
                'Could not add new company, check for duplicate company id'),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/analyse')
def get_all():
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
    return data


@app.route('/company_list')
def get_company_list():
    print("Welcome to KRM!")

    data = {'company_list': cp.company_list}
    return data


if __name__ == "__main__":
    app.run()
