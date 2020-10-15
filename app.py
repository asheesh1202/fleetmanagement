from flask import Flask, request, make_response, g
from . import config
import pymongo
import os 
import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

app = Flask(__name__)

client  = pymongo.MongoClient(config.DevelopmentConfig.MONGODBURI)
db = client.db
users_drivers = db.users_drivers 
users_operators = db.users_operators

g['GEOFENCE_REGION1'] = [ [1,1],[1,2], [2,2,], [2,1] ]
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
@app.route("/")
def home():
    return 'home page url'
    
@app.route("/add_user", methods=['POST'])
def addUser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        category = request.form['category']
        
        if category == 'driver':
            user = {
                    "username":username,
                    "password" : password,
                    "catergory" : category,
                    "lat":0,
                    "lng":0
                    }
            users_drivers.insert_one(user)
            
        if category == 'driver':
            user = {
                    "username":username,
                    "password" :password,
                    "catergory" :category,
                    "lat":0,
                    "lng":0
                    }
            users_drivers.insert_one(user)
            
        return 'successful'    
        
        
@app.route("/update_current_location/<username>/", methods=['POST'])
def update_current_location(username):
    if request.method == 'POST':
        if users_drivers.find_one({'username':username})!=None:
            id = users_drivers.find_one({'username':username})['_id']
            print(id)
            users_drivers.find_one_and_update({ 'username': username },
                                      { '$set': {'lat': request.form['lat'],
                                                  'lng': request.form['lng'] }
                                       }, 
                                       upsert=False)
            return 'request successfull'
        else:
            return 'user not found'
            
    
@app.route("/get_current_location/<username>/", methods=['GET'])
def get_current_location(username):
    if request.method =='GET':
        if users_drivers.find_one({'username':username})!=None:
            lat  = users_drivers.find_one({'username':username})['lat']
            lng  = users_drivers.find_one({'username':username})['lng']
            if lat != 0 and lng != 0:   
                res = {
                        'lat':lat,
                        'lng':lng,
                        'username':username
                      
                        }
                return make_response(res, 200) 
            else:
                return 'invalid lat lng'
        else: 
            return 'invalid user'
            
                
@app.route("/check_geofencing/<user>/<region>", mehtod=['GET'])
def check_geofencing():
    if request.method=='GET':
        lat = request.form['lat']
        lng = request.form['lng']
        point = Point(double(lat), double(lng))
        if(polygon.contains(point)):
            return True
        else:
            return False    
                