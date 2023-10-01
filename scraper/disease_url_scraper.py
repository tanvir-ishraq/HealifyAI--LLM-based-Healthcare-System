from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
import time
import random
import re
import csv

def initialize_csv():
    ''' writes header columns of csv '''
    with open("disease_urls.csv", "a", newline="" , encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["disease_label", "url", "heading"])

if __name__ == "__main__":

    # initialize_csv()

    disease_list = [ 'diabetes',
    'depression mental / depressive disorder',
    'coronary arteriosclerosis / coronary heart disease',
    'pneumonia',
    'asthma',
    'myocardial infarction',
    'anemia',
    'dementia',
    'hypothyroidism',
    'malignant neoplasms / primary malignant neoplasm',
    'acquired immuno-deficiency syndrome / HIV / hiv infections',
    'cellulitis',
    'gastroesophageal reflux disease',
    'septicemia / systemic infection / sepsis (invertebrate)',
    'deep vein thrombosis',
    'dehydration',
    'neoplasm',
    'embolism pulmonary',
    'epilepsy',
    'cardiomyopathy',
    'chronic kidney failure',
    'carcinoma',
    'hepatitis C',
    'peripheral vascular disease',
    'psychotic disorder',
    'hyperlipidemia',
    'bipolar disorder',
    'obesity',
    'ischemia',
    'cirrhosis',
    'benign prostatic hypertrophy',
    'arthritis',
    'bronchitis',
    'osteoporosis',
    'transient ischemic attack',
    'adenocarcinoma',
    'pancreatitis',
    'incontinence',
    'hernia',
    'malignant neoplasm of prostate / carcinoma prostate',
    'malignant neoplasm of breast / carcinoma breast',
    'diverticulitis',
    'osteomyelitis',
    'gastritis',
    'bacteremia',
    'sickle cell anemia',
    'upper respiratory infection',
    'hepatitis',
    'gout',
    'thrombocytopaenia',
    'hypoglycemia',
    'pneumonia aspiration',
    'colitis',
    'diverticulosis',
    'suicide attempt',
    'hepatitis B',
    'parkinson disease',
    'lymphoma',
    'hyperglycemia',
    'encephalopathy',
    'tricuspid valve insufficiency',
    "Alzheimer's disease",
    'candidiasis / oral candidiasis',
    'neuropathy',
    'kidney disease',
    'fibroid tumor',
    'glaucoma',
    'neoplasm metastasis',
    'malignant tumor of colon / carcinoma colon',
    'ketoacidosis diabetic',
    'tonic-clonic epilepsy / tonic-clonic seizures',
    'respiratory failure',
    'melanoma',
    'gastroenteritis',
    'malignant neoplasm of lung / carcinoma of lung',
    'manic disorder',
    'personality disorder',
    'primary carcinoma of the liver cells',
    'emphysema pulmonary',
    'hemorrhoids',
    'aphasia',
    'obesity morbid',
    'pyelonephritis',
    'endocarditis',
    'pneumothorax',
    'delirium',
    'neutropenia',
    'hyperbilirubinemia',
    'influenza',
    'dependence',
    'thrombus',
    'cholecystitis',
    'hernia hiatal',
    'migraine disorders',
    'pancytopenia',
    'cholelithiasis / biliary calculus',
    'tachycardia sinus',
    'ileus',
    'adhesion',
    'delusion',
    'hypertension',
    'coronary artery disease',
    'congestive heart failure',
    'stroke',
    'high cholesterol',
    'infectious disease',
    'UTI',
    'COPD',
    'kidney failure',
    'dementia',
    'osteoarthritis',
    'anxiety disorder',
    'cancer',
    'HIV infection',
    'sepsis',
    'rash',
    'acute kidney injury',
    'mitral valve prolapse',
    'partial paralysis',
    'paranoid personality disorder',
    'paroxysmal nocturnal dyspnea',
    'pulmonary edema',
    'lymphedema',
    'aortic valve stenosis',
    'schizophrenia spectrum disorder',
    'fluid overload',
    'peptic ulcer',
    'kidney failure',
    'heart failure',
    'pulmonary hypertension',
    'dysphagia',
    'Pneumocystis pneumonia',
    'pericardial effusion',
    'alcohol use disorder',
    'bronchospasm',
    'emotional lability',
    'bedsore']
    disease_list = [ disease.replace('/','or')      for disease in disease_list ]

    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled") #Remove Navigator.Webdriver Flag in Selenium
    chrome_options.add_argument("--incognito") # so that they can't track with cookie , session

    chrome_options.add_argument('--blink-settings=imagesEnabled=false') #data save, time save
    chrome_options.add_experimental_option("detach", True) #just to obsereve

    #user agent for : linux, macos, win 7 ,8, 8.1, avoiding 10 cos mine, try 11 too
    ua_list = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36", #win <8.1 doesnt officialy support chrome 116
                "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"]


    for disease in tqdm(disease_list):
        
        ua_choice = random.choice(ua_list)
        chrome_options.add_argument(f'--user-agent={ua_choice}')
        driver = webdriver.Chrome(options=chrome_options)
        actions = ActionChains(driver)
        
        driver.get('https://www.google.com/')
        time.sleep(random.uniform(1.7,5))
        actions.move_by_offset(random.randint(150, 250), random.randint(150, 250)).perform()
        while(random.randint(0,1)): 
            driver.maximize_window() 
            break        

        search_box = driver.find_element(By.TAG_NAME, "textarea")
        search_box.send_keys(f'healthline.com Symptoms {disease}')
        time.sleep(random.uniform(1.7, 6))
        actions.move_by_offset(random.randint(150, 250), random.randint(150, 250)).perform()
        
        #actions.move_to_element(search_button).perform()#.click().perform()
        search_box.send_keys(Keys.RETURN) 
        time.sleep(random.uniform(1.7,5))
        actions.move_by_offset(random.randint(150, 250), random.randint(150, 250)).perform()
        while(random.randint(0,1)): 
            driver.maximize_window()
            break
        
        pattern = r':.*symptoms'
        div_iterator = 1
        heading = driver.find_element(By.XPATH, f'//*[@id="rso"]/div[{div_iterator}]').find_element(By.TAG_NAME, "h3").text
        #actions.move_to_element(webelement).perform() #stale element reference: stale element not found
        
        #checks through google result divs to scrap required match:
        while(True): 

            if re.search(r':.*symptoms', heading, re.IGNORECASE): break #pattern found. break from loop. iteration is not needed.

            div_iterator += 1
            try:
                heading = driver.find_element(By.XPATH, f'//*[@id="rso"]/div[{div_iterator}]').find_element(By.TAG_NAME, "h3").text
            except:
                div_iterator = 1
                heading = driver.find_element(By.XPATH, f'//*[@id="rso"]/div[{div_iterator}]').find_element(By.TAG_NAME, "h3").text
                break 


        url = driver.find_element(By.XPATH, f'//*[@id="rso"]/div[{div_iterator}]').find_element(By.TAG_NAME, "a").get_attribute('href') #(By.CLASS_NAME, 'MjjYud')
    
        with open("disease_urls.csv", "a", newline="" , encoding="UTF8") as file: #must newline="" else enters extra newlines
            writer = csv.writer(file)
            writer.writerow([disease, url, heading])
        
        #actions.move_to_element(move_mouse).perform()
        #actions.move_to_element_with_offset(driver.find_element(By.TAG_NAME, 'body'), 0, 0).perform()
        time.sleep(random.uniform(1.7,5))
        actions.move_by_offset(random.randint(150, 250), random.randint(150, 250)).perform()
        driver.quit()

