from flask import Flask, request,jsonify
import pickle
import pandas as pd
import numpy as np
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Api, Resource

app=Flask(__name__)



SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    }
)

app.register_blueprint(swaggerui_blueprint)


api = Api(app)
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome_page():
    return "Welcome."


#@app.route('/predict',methods=['GET'])
class PredictNoteAuthentication(Resource):
    def get(self):
      try:        
       variance = float(request.args['variance'])        
       skewness = float(request.args['skewness'])        
       curtosis = float(request.args['curtosis'])       
       entropy = float(request.args['entropy'])        
       prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
       return jsonify(prediction=str(prediction[0]))
      except Exception as e:
       return jsonify(error=str(e)), 400

api.add_resource(PredictNoteAuthentication, '/predict')


if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
