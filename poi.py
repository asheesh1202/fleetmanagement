from ..app import app
from ..app import db

poi =  db.poi

@app.route('/poi/add/', mehtods=['POST'])
def add_poi():
    #check if the form is valid 
    if request.method == 'POST':
        id = 
        name = 
        lat = 
        lng = 
        region = 
        Address = 
        category = 
        point = {
            "name":name,
            "lat" : lat,
            "lng" : lng,
            "region":region,
            "Address":Address
        }
        poi.insert_one(school)

@app.route('poi/get_all/', methods = ['GET'])
def get_allPOI():
    allPois  = poi.find()
    res={}
    i = 0
    for poi in allPois: 
        res[i] = poi
        i+=i
        
    response = json.dumps(res, indent = 4)
    return response

@app.route('poi/get/', method=['GET'])
def getPoi( ):
    searchRes = poi.find_one({'id':request.form['id'], 'name':request.form['name']})
    response = {
    'id' = searchRes['id']
    'name' = searchRes['name']
    'lat' = searchRes['lat']
    'lng' = searchRes['lng']
    'region' = searchRes['region']
    'Address' = searchRes['Address']
    'category' = searchRes['category']
    }
    return response
    
@app.route('poi/update/', method=['Update'])
def getPoi( ):
    searchRes = poi.find_one({'id':request.form['id'], 'name':request.form['name']})
    #things to update
    #opens update form 
    
    if searchRes:
        users_drivers.find_one_and_update({ 'id':request.form['id'], 'name':request.form['name']}  },
                                      { '$set': {'name': request.form['lat'],
                                                  'lat': request.form['lng'] 
                                                  'lng': request.form['lng']
                                                  'category': request.form['category']
                                                  'region': request.form['region']
                                                  'Address': request.form['Address']}
                                      }, 
                                      upsert=False)
    return 'true/successful'
    
@app.route('poi/delete' mehtod = ['DELETE'])
def deletePoi(  ):
    delete = poi.delete ({'id': request.form['id'], 'name:'request.form['name']})
    