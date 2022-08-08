from flask import Flask, render_template, jsonify, request 

app = Flask(__name__) # hacer ref al nombre del archivo

@app.route('/')
def hello_flask():
    return 'Hello Flask'

@app.route('/inicio')
def show_home():
    return "Hello world"

# @app.route('/url_variables/<string: name>/<int: age>')
# def url_variables(name,age):
#     if age < 18:
#         return jsonify(message = 'Lo siento' + name + 'no estas autorizado'), 401
#     else:
#         return jsonify(message = 'Bienvenido' + name), 200 # por default es 200
    

@app.route('/<string:country>/<string:variety><float:aroma>/<float:aftertaste>/<float:acidity>/<float:body>/<float:balance>/<float:moisture>')
def result(country, variety, aroma, aftertaste, acidity, body, balance, moisture):
    cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']

    # contenido de objeto pandas
    data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]

    # df
    posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
    #print(posted)


    # Cargamos modelo entrenado

    loaded_model = pickle.load(open('coffee_model.pkl', 'rb')) # rb: read binary


    # Pasar los datos al modelo

    result = loaded_model.predict(posted) # devuelve archivo np, necesito llevarlo a texto
    text_result = result.tolist()[0]

    if(text_result == 'Yes'):
        return jsonify(message='Es un cafe de primeras'), 200
    else:
        return jsonify(message='No es un cafe de primeras'), 200




if __name__ == '__main__':
    app.run(debug= True, host='127.0.0.1', port=5000) 

