from flask import Flask, render_template, request #, redirect, url_for
import json, pickle, requests
import pandas as pd
from numpy import argsort

# laad required model and data
df = pd.read_csv('healifyLLM_answer_dataset_optimized.csv', encoding='utf-8', engine='python')

with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open("columns_encoded.json", "r") as f:
    columns_encoding = json.load(f) 

ui_symptoms_sorted = sorted([symptom.capitalize() for symptom in columns_encoding.keys()])

# Flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    predictions = {}
    LLM_answer = ''
    
    if request.method == "POST":
        print('==============================')
        if 'symptoms_button' in request.form:
            user_symptoms = request.form.getlist('symptoms')

            #prepare for prediction 
            symptoms_input = [0] * len(model.feature_names_in_)
            for name in user_symptoms:
                index = columns_encoding[name]
                symptoms_input[index] = 1

            symptoms_input = [symptoms_input]
            probs = model.predict_proba(symptoms_input)    
            top_5_indices = argsort(probs[0]) [-5:] 
            top_5_indices = top_5_indices[ : : -1]
        
            predictions = {model.classes_[idx] : int(probs[0][idx] *100)    for idx in top_5_indices}
            return render_template('index.html', 
                                   predictions=predictions,
                                   symptoms_collection = ui_symptoms_sorted,
                                   )

        elif 'LLM_button' in request.form:
            #print('LLM_button submitted')
            input_text = request.form['text'] #request.form.get('text_area_name')

            output = predict_question(input_text)[0]['confidences'][0] #(input_text)[0] 
            print(output)
            #if output['confidence'] > 0.5 : 
            print('generating answer for {}'.format(output['label']) )
            #selected_row = df[df['label'] == output['label'] ]#.idxmin()

            LLM_answer = df.loc[df['label'] == output['label'], 'answer'].item()
            print(type(LLM_answer), LLM_answer)
            LLM_answer = LLM_answer.replace('�', '\'')
            LLM_answer = f'''{LLM_answer}'''
            LLM_answer = '\n'.join( line+'<br>'    for line in LLM_answer.split('\n'))
            print(LLM_answer)

            return render_template("index.html", 
                                   input_text=input_text, 
                                   LLM_answer=LLM_answer,
                                   symptoms_collection = ui_symptoms_sorted)   
    
    else:
        return render_template("index.html", 
                               symptoms_collection = ui_symptoms_sorted,
                               predictions=predictions,
                               LLM_answer=LLM_answer)


# hugging face api 
def predict_question(input_text):
    response = requests.post("https://tanvir-ishraq-healifyllm-classifier.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    }).json()
    data = response["data"]
    return data

if __name__ == "__main__":
    app.run(debug=True)
