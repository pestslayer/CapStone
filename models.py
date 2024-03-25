from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import uuid
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import secrets

db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(150), nullable=True, default='')
    last_name = db.Column(db.String(150), nullable=True, default='')
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=True, default='')
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, first_name="", last_name="", password=""):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'


class Ticket(db.Model):
    id = db.Column(db.String, primary_key=True)
    customerName = db.Column(db.String(150), nullable=False)
    custAddress = db.Column(db.String(150))
    custNo = db.Column(db.String(150))
    invoiceNo = db.Column(db.String(150))
    serArea = db.Column(db.String(150))
    instruct = db.Column(db.String(150))
    service = db.Column(db.String(150))
    appDate = db.Column(db.String(150))
    timeIn = db.Column(db.String(150))
    timeOut = db.Column(db.String(150))
    temp = db.Column(db.String(150))
    windDir = db.Column(db.String(150))
    windSpeed = db.Column(db.String(150))
    lic = db.Column(db.String(150))
    sqft = db.Column(db.String(150))
    sprayer = db.Column(db.String(150))
    rate = db.Column(db.String(150))
    target = db.Column(db.String(150))
    product = db.Column(db.String(150))

    def __init__(self, customerName, custAddress, custNo, invoiceNo, serArea, instruct, service, appDate, timeIn,
                 timeOut, temp, windDir, WindSpeed, lic, sqft, sprayer, rate, target, product, id=""):
        self.id = self.set_id()
        self.customerName = customerName
        self.custAddress = custAddress
        self.custNo = custNo
        self.invoiceNo = invoiceNo
        self.serArea = serArea
        self.instruct = instruct
        self.service = service
        self.appDate = appDate
        self.timeIn = timeIn
        self.timeOut = timeOut
        self.temp = temp
        self.windDir = windDir
        self.windSpeed = WindSpeed
        self.lic = lic
        self.sqft = sqft
        self.sprayer = sprayer
        self.rate = rate
        self.target = target
        self.product = product

    def __repr__(self):
        return f'The Following contact has been added to the database: {self.name}'

    def set_id(self):
        return secrets.token_urlsafe()


class TicketSchema(ma.Schema):
    class Meta:
        fields = ['id', 'customerName', 'custAddress', 'custNo', 'invoiceNo', 'serArea', 'instruct', 'service',
                  'appDate', 'timeIn', 'timeOut', 'temp', 'windDir', 'windSpeed', 'lic', 'sqft', 'sprayer',
                  'rate', 'target', 'product']


ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
