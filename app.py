from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
from keras.models import load_model
model = load_model('model_ann2048_dp.h5')
scaler_data = pickle.load(open('scaler_data.pkl','rb'))


def preprocessing(input):
    input_data = pd.DataFrame(input,columns=['input'],
                              index=['batting_team','bowling_team','run_scored','curr_run_rate',
                                'target','wickets_left', 'Req_run_rate','runs_left'])
    input_data = ((input_data['input'].values - scaler_data['Mean'].values)/scaler_data['SD'].values).tolist()
    return [input_data]   

teams = {
    1: 'Chennai Super Kings',
    2: 'Delhi Capitals',
    3: 'Kings XI Punjab',
    4: 'Kolkata Knight Riders',
    5: 'Mumbai Indians',
    6: 'Rajasthan Royals',
    7: 'Royal Challengers Bangalore',
    8: 'Sunrisers Hyderabad'
}

#  'batting_team','bowling_team','run_scored','curr_run_rate',
#               'target','wickets_left', 'Req_run_rate','runs_left'
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/prediction',methods = ['POST'])
def predict():
    
    batting_team = int(request.form['batting_team'])
    bowling_team = int(request.form['bowling_team'])
    target = float(request.form['target'])
    runs_left = float(request.form['runs_left'])
    wickets_left = float(request.form['wickets_left'])
    balls_left = int(request.form['balls_left'])#to add to form
    Req_run_rate = (runs_left* 6)/balls_left
    run_scored = target - runs_left
    curr_run_rate = (run_scored*6)/(120 - balls_left)

    input = [batting_team,bowling_team,run_scored,curr_run_rate,target,wickets_left,Req_run_rate,runs_left]
    input = preprocessing(input)
    predictions = round(model.predict(input)[0][0])

    if predictions == 1:
        predictions = teams.get(batting_team, 'Invalid Team Number')  # batting team won
    elif predictions == 0:
        predictions = teams.get(bowling_team, 'Invalid Team Number')  # bowling team won
    else:
        predictions = 'Invalid Prediction'
    return render_template('index.html',predictions = predictions)


if __name__ == '__main__':
    app.run(debug=True)