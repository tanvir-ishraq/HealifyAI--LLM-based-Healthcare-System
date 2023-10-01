import gradio as gr
from transformers import AutoTokenizer
import torch, json

from fastai.text.all import *
from blurr.text.modeling.all import *
#from blurr.text.data.all import *

# from blurr.modeling.core import Blearner
# learner = Blearner.load_learner('path/to/your/export.pkl')
# result = learner.blurr_predict('Your text here')

with open('question_labels.json', 'r') as f:
  question_dictionary = json.load(f)
que_classes = question_dictionary.key() list(labels.keys())

blurr_model = load_learner('healifyLLM-stage4.pkl')

def detect_question(text):
  # research tokenization requirement for blurr_predict()
  probs = blurr_model.blurr_predict(text)[0]['probs']
  return dict(zip(que_classes, map(float, probs))) 

label = gr.outputs.Label(num_top_classes=5)
#interface with i/o
iface = gr.Interface(fn=detect_question, inputs="text", outputs=label)
iface.launch(inline=False)
				