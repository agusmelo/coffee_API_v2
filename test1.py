import pickle
import pandas as pd
import numpy as np

# Contenido ficticio para poner en el model
# Modelo recibe 8 variables

country='Colombia'
variety='Caturra'
aroma = 7.83
aftertaste = 7.77
acidity = 7.33
body=7.67
balance=7.77
moisture=0.11


# Usamos un pipeline entonces tenemos que ponerlo en un df

# cabecera de objeto pandas
cols = ['country_of_origin', 'variety', 'aroma', 'aftertaste', 'acidity', 'body', 'balance', 'moisture']

# contenido de objeto pandas
data = [country, variety, aroma, aftertaste, acidity, body, balance, moisture]

# df
posted = pd.DataFrame(np.array(data).reshape(1,8), columns=cols)
#print(posted)


# Cargamos modelo entrenado

loaded_model = pickle.load(open('../models/coffee_model.pkl', 'rb')) # rb: read binary


# Pasar los datos al modelo

result = loaded_model.predict(posted) # devuelve archivo np, necesito llevarlo a texto

text_result = result.tolist()[0]

print(text_result)