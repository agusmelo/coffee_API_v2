from flask import Flask, render_template, jsonify, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__) # hace referencia al nombre del archivo

@app.route('/')
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio')
def show_home():
    return render_template('index.html')

@app.route('/<string:country>/<string:variety>/<float:aroma>/<float:aftertaste>/<float:acidity>/<float:body>/<float:balance>/<float:moisture>')
def result(country, variety, aroma, aftertaste, acidity, body, balance, moisture):
    cols = ['country_of_origin', 'variety', 'aroma','aftertaste','acidity','body','balance','moisture']
    data = [country, variety, aroma,aftertaste,acidity,body,balance,moisture]
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
    loaded_model = pickle.load(open('coffee_model.pkl','rb'))
    result = loaded_model.predict(posted)
    test_result = result.tolist()[0]
    if test_result == 'Yes':
        return jsonify(message = 'Si es un cafe de primera'), 200
    else:
        return jsonify(message = 'No es un cafe de primera'), 200



#@app.route('/url_variables/<string:name>/<int:age>')
#def url_variables(name, age):
#    if age < 18:
#        return jsonify(message='Lo siento ' + name + ' no estas autorizado'), 401
#    else:
#        return jsonify(message = ' Bienvenido ' + name ), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)


#probar
# No Other/Other/7.42/7.33/7.42/7.25/7.33/0.0
# Yes Guatemala/Bourbon/7.83/7.67/7.33/7.67/7.67/0.11