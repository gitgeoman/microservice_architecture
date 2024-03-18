import os, gridfs, pika, json

from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import utill

server = Flask(__name__)
server.config['MONGO_URI'] = 'mongodb://host.minikuve.internal:27017/videos'

mongo = PyMongo(server)
fs = gridfs.GridFS(mongo.db)
connection = pika.BlockingConnection(pika.ConnnectionParameters(
    host='localhost'
))
channel = connection.channel()
@server.route('/login', methods=['POST'])
def login():
    token, err = access.login(request)
