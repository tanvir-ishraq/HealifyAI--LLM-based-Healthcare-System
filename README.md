<div align="center">
<h1 align="center">HealifyAI - LLM based Healthcare System</h1>
</div> 
https://healifyai-llm.onrender.com/ <br>
(Project complete. documentation is work in progress) 

## About The Project
This project aims to develop a comprehensive healthcare system to aid healthcare professionals. While also providing knowledge to patients. It uses a LLM plus traditional Machine Learning (ML) to provide in-depth answers to medical health condition queries and can predict diseases based on patient symptoms.<br>
The system consists of two main modules:
* Disease Prediction Model
* HealifyLLM QA Language Model
<!-- GETTING STARTED <br> -->

## training Data Collection





<h4 align="center">HealifyLLM QA Language Model</h4>
The Bio_ClinicalBERT model was trained on a kaggle dataset from from MIMIC III, a database containing electronic health records from ICU patients at the Beth Israel Hospital in Boston, MA. For more details on MIMIC, see here. All notes from the NOTEEVENTS table were included (~880M words).<br> <br>

<div align="center">HealifyLLM QA Language Model </div>
The Bio_ClinicalBERT model was trained on a kaggle dataset from from MIMIC III, a database containing electronic health records from ICU patients at the Beth Israel Hospital in Boston, MA. For more details on MIMIC, see here. All notes from the NOTEEVENTS table were included (~880M words).<br>

**HealifyLLM QA Language Model:** <br>
The Bio_ClinicalBERT model was trained on a kaggle dataset from from MIMIC III, a database containing electronic health records from ICU patients at the Beth Israel Hospital in Boston, MA. For more details on MIMIC, see here. All notes from the NOTEEVENTS table were included (~880M words).<br><br>
**Disease Model:** <br>
The Bio_ClinicalBERT model was trained on a kaggle dataset from from MIMIC III, a database containing electronic health records from ICU patients at the Beth Israel Hospital in Boston, MA. For more details on MIMIC, see here. All notes from the NOTEEVENTS table were included (~880M words).<br>

<!--
Disease Prediction Model: This component uses traditional ML algorithm to predict potential diseases based on the symptoms input by the user. Covering a total of 135 categories of common and as well as rare yet important health conditions, diseases, psychology disorders such as diabetes, dehydration, depression, bipolar disorder, HIV, breast cancer, stroke, pneumonia, flu, asthma, obesity and so on. The model is trained on a large dataset of hundreds to thousands of patient records (denoted by frequency in dataset) to ensure reliable predictions based on NY Hospital based [Disease-Symptom Knowledge Database](https://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/). 

QA Language Model: This component uses a Language Model (LLM) to answer medical queries from users. The LLM is trained on my from-scratch scraped then enhanced corpus dataset of medical queries & professional solutions, enabling it to provide detailed and accurate answers to a wide range of medical questions. Sample addition was done to enhance the dataset for user experience. Covering urgent topics of diagnosis, treatment, prevention, causes, risks, complications, details of symptoms, disease description.

The combination of these two components allows for a robust interactive healthcare system that can assist both patients and healthcare professionals in diagnosing diseases, finding relevant medical information and diseases relation potentially. The system is designed to be user-friendly, with an intuitive interface that makes it easy for anyone to use. 

## Future work and limitations
Please note that while this system can provide valuable insights and information, it is not intended to replace professional medical advice. Always consult with a healthcare professional for medical concerns.-->

