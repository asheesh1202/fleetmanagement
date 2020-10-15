class FlaskConfig():
    debug = True
    env = 'development'

class DevelopmentConfig():
    MONGODBURI = 'mongodb://127.0.0.1:27017/'