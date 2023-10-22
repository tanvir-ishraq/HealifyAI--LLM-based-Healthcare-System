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

ui_symptoms_sorted = sorted(columns_encoding.keys())

# Flask
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    predictions = {} #health condition predictions
    LLM_output = []
    LLM_answer = ''
    
    if request.method == "POST":
        print('Log ==============================')
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
        
            predictions = {model.classes_[idx].title() : int(probs[0][idx] *100)    for idx in top_5_indices}
            return render_template('index.html', 
                                   predictions=predictions,
                                   symptoms_collection=columns_encoding.keys(),
                                   LLM_output = LLM_output
                                   )

        elif 'LLM_button' in request.form:
            #print('LLM_button submitted')
            input_text = request.form['text'] #request.form.get('text_area_name')

            output = predict_question(input_text)[0]['confidences']
            print(output)
            print()
            if output[0]['confidence'] > 0.5 : 
                print('generating answer for {}'.format(output[0]['label']) )

                LLM_answer = df.loc[df['label'] == output[0]['label'], 'answer'].values[0]
                #format the answer for HTML:
                LLM_answer = LLM_answer.replace('�', '\'')
                LLM_answer = f'''{LLM_answer}'''
                LLM_answer = ''.join( line+'<br>'    for line in LLM_answer.split('\n'))
                output[0]['LLM_answer'] = LLM_answer
            else:
                output[0]['LLM_answer'] = LLM_answer
                
            LLM_output = output
            print(LLM_output)

            return render_template("index.html", 
                                   input_text=input_text, 
                                   LLM_output=output,
                                   symptoms_collection=columns_encoding.keys() )   
    
    else:
        return render_template("index.html", 
                               symptoms_collection=columns_encoding.keys(),
                               predictions=predictions,
                               LLM_output=LLM_output)


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
