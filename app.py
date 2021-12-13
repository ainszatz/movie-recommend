from flask import Flask, render_template, request, redirect  
import joblib
import numpy as np
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])

def index():
 if request.method == 'POST':

        Umur = float(request.form['Umur'])
        Jenis_Kelamin = float(request.form['Jenis Kelamin'])
        Status = float(request.form['Status'])

        file = open('movie-recommender.joblib', 'rb')
        model = joblib.load(file)

        prediction = model.predict([[Umur, Jenis_Kelamin, Status]])
        prediction = np.array(prediction)
        print(prediction)
        result = prediction[0]

        return render_template('hasil.html', result = result)
                
#        # joblib.load
#         with open('movie-recommender.joblib') as r:
#                 model = joblib.load(r)       


#         datas = np.array((Umur,Jenis_Kelamin,Status))

#         # movrec = model.predict(datas)#

 else:
        return render_template('index.html')

if __name__ == "__main__":
        app.run(debug=True)
