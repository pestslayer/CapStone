from flask import Blueprint, request, jsonify, render_template
from models import db, User, Ticket, ticket_schema, tickets_schema

api = Blueprint('api',__name__, url_prefix='/api')
@api.route('/ticket', methods = ["POST", "PUT" ])
def create_ticket():
    customerName = request.json['customerName']
    custAddress = request.json['custAddress']
    custNo = request.json['custNo']
    invoiceNo = request.json['invoiceNo']
    serArea = request.json['serArea']
    instruct = request.json['instruct']
    service = request.json['service']
    appDate = request.json['appDate']
    timeIn = request.json['timeIn']
    timeOut = request.json['timeOut']
    temp = request.json['temp']
    windDir = request.json['windDir']
    windSpeed = request.json['windSpeed']
    lic = request.json['lic']
    sqft = request.json['sqft']
    sprayer = request.json['sprayer']
    rate = request.json['rate']
    target = request.json['target']
    product = request.json['product']
    print(customerName)

    ticket = Ticket(customerName,custAddress,custNo,invoiceNo,serArea, instruct, service, appDate, timeIn, timeOut, temp,
                     windDir, windSpeed, lic, sqft, sprayer, rate, target, product)
    
    db.session.add(ticket)
    db.session.commit()

    response = ticket_schema.dump(ticket)
    return jsonify(response)

@api.route('/ticket', methods = ['GET'])
def get_ticket():
    ticket = Ticket.query.filter_by().all()
    response = tickets_schema.dump(ticket)
    return jsonify(response)

@api.route('/ticket/<id>', methods = ['GET'])
def get_single_ticket(id):
    ticket = Ticket.query.get(id)
    response = ticket_schema.dump(ticket)
    return jsonify(response)

@api.route('/ticket/<id>', methods = ['POST', 'PUT'])
def update_ticket(id):
    ticket = Ticket.query.get(id)
    ticket.customerName = request.json['customerName']
    ticket.custAddress = request.json['custAddress']
    ticket.custNo = request.json['custNo']
    ticket.invoiceNo = request.json['invoiceNo']
    ticket.serArea = request.json['serArea']
    ticket.instruct = request.json['instruct']
    ticket.service = request.json['service']
    ticket.appDate = request.json['appDate']
    ticket.timeIn = request.json['timeIn']
    ticket.timeOut = request.json['timeOut']
    ticket.temp = request.json['temp']
    ticket.windDir = request.json['windDir']
    ticket.windSpeed = request.json['windSpeed']
    ticket.lic = request.json['lic']
    ticket.sqft = request.json['sqft']
    ticket.sprayer = request.json['sprayer']
    ticket.rate = request.json['rate']
    ticket.target = request.json['target']
    ticket.product = request.json['product']

    db.session.commit()
    response = ticket_schema.dump(ticket)
    return jsonify(response)

@api.route('/ticket/<id>', methods = ['DELETE'])
def delete_ticket(id):
    ticket = Ticket.query.get(id)
    db.session.delete(ticket)
    db.session.commit()
    response = ticket_schema.dump(ticket)
    return(response)


