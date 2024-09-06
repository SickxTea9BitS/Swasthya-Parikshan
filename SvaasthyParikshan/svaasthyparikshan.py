import streamlit as st
import uuid
from streamlit_option_menu import option_menu
from fpdf import FPDF
from googletrans import Translator
import pickle
import numpy as np
# Set page config

svc = pickle.load(open('svc.npl', 'rb'))
symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}
diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}

def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        input_vector[symptoms_dict[item]] = 1
    return diseases_list[svc.predict([input_vector])[0]]

st.set_page_config(page_title="Svaasthy Parikshan", page_icon=":hospital:")

# Initialize the Translator
translator = Translator()

# Supported languages
LANGUAGES = {
    'English': 'en', 'Hindi': 'hi', 'Bengali': 'bn', 'Marathi': 'mr', 
    'Gujarati': 'gu', 'Telugu': 'te', 'Tamil': 'ta', 'Kannada': 'kn', 
    'Malayalam': 'ml', 'Odia': 'or'
}

# Select language
selected_language = st.sidebar.selectbox("Select Language", list(LANGUAGES.keys()))
target_language = LANGUAGES[selected_language]

# Function to translate text
def translate_text(text, target_lang):
    if target_lang == 'en':
        return text  # No translation needed for English
    return translator.translate(text, dest=target_lang).text

# CSS Styling
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: #f0f2f6;
    }}
    .main {{
        color: #2c3e50;
    }}
    .header {{
        background-color: #0552ed;
        padding: 20px;
        text-align: center;
        color: white;
        font-size: 32px;
        border-radius: 10px;
    }}
    .footer {{
        background-color: #2c3e50;
        padding: 10px;
        text-align: center;
        color: white;
        font-size: 14px;
        border-radius: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Function to generate a unique token
def generate_token(ward_no):
    return f"W-{ward_no}-{uuid.uuid4().hex[:8]}"

# Function to create PDF report
def create_pdf_report(patient_details, diagnosis_details, token):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(200, 10, txt=translate_text("Patient Report", target_language), ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"{translate_text('Token', target_language)}: {token}", ln=True, align='L')

    pdf.set_font("Arial", 'B', 10)
    pdf.cell(50, 10, txt=translate_text("Field", target_language), border=1, align='C')
    pdf.cell(140, 10, txt=translate_text("Value", target_language), border=1, align='C')
    pdf.ln()

    pdf.set_font("Arial", size=10)
    for key, value in patient_details.items():
        pdf.cell(50, 10, txt=translate_text(str(key), target_language), border=1, align='C')
        pdf.cell(140, 10, txt=translate_text(str(value), target_language), border=1, align='C')
        pdf.ln()

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt=translate_text("Diagnosis Details", target_language), ln=True, align='L')

    pdf.set_font("Arial", size=10)
    for key, value in diagnosis_details.items():
        pdf.cell(50, 10, txt=translate_text(str(key), target_language), border=1, align='C')
        pdf.cell(140, 10, txt=translate_text(str(value), target_language), border=1, align='C')
        pdf.ln()

    pdf_file_name = f"Patient_Report_{uuid.uuid4().hex[:8]}.pdf"
    pdf.output(pdf_file_name)
    return pdf_file_name

# Function to display the report on the web page
def display_report(patient_details, diagnosis_details, token):
    st.subheader(f"{translate_text('Token', target_language)}: {token}")
    
    st.subheader(translate_text("Patient Report", target_language))
    st.write(translate_text("### Patient Details", target_language))
    patient_table = f"| {translate_text('Field', target_language)} | {translate_text('Value', target_language)} |\n| --- | --- |\n"
    for key, value in patient_details.items():
        patient_table += f"| {translate_text(key, target_language)} | {translate_text(value, target_language)} |\n"
    st.markdown(patient_table)

    st.write(translate_text("### Diagnosis Details", target_language))
    diagnosis_table = f"| {translate_text('Field', target_language)} | {translate_text('Value', target_language)} |\n| --- | --- |\n"
    for key, value in diagnosis_details.items():
        diagnosis_table += f"| {translate_text(key, target_language)} | {translate_text(value, target_language)} |\n"
    st.markdown(diagnosis_table)

    pdf_file = create_pdf_report(patient_details, diagnosis_details, token)
    with open(pdf_file, "rb") as file:
        st.download_button(label=translate_text("Download PDF", target_language), data=file, file_name=pdf_file, mime="application/octet-stream")

# Patient Details Input
st.subheader(translate_text("Enter Patient Details", target_language))
patient_name = st.text_input(translate_text("Patient Name", target_language))
patient_age = st.number_input(translate_text("Age", target_language), min_value=0, max_value=120, step=1)
patient_gender = st.selectbox(translate_text("Gender", target_language), [translate_text("Male", target_language), translate_text("Female", target_language), translate_text("Other", target_language)])
patient_phone = st.text_input(translate_text("Phone No", target_language))
patient_address = st.text_area(translate_text("Address", target_language))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(translate_text('Select The Ward', target_language),
                           [translate_text('General Medicine', target_language)],#, translate_text('Pediatrics', target_language), translate_text('Gynecology ', target_language),translate_text('Orthopedics', target_language), translate_text('Dermatology', target_language), translate_text('Ophthalmology', target_language), translate_text('ENT', target_language), translate_text('Gastroenterology', target_language), translate_text('Endocrinology', target_language) ,translate_text('Urology', target_language),  translate_text('Allergy and Immunology', target_language)],
                           default_index=0)

patient_details = {
    translate_text("Name", target_language): patient_name,
    translate_text("Age", target_language): patient_age,
    translate_text("Gender", target_language): patient_gender,
    translate_text("Phone No", target_language): patient_phone,
    translate_text("Address", target_language): patient_address,
    translate_text("Ward No", target_language): selected
}

# General Medicine Ward
if selected == translate_text('General Medicine', target_language):
    st.title(translate_text('Welcome to General Medicine Ward', target_language))
    
    symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("itching", target_language), translate_text("skin_rash", target_language), translate_text("nodal_skin_eruptions", target_language), translate_text("continuous_sneezing", target_language), translate_text("shivering", target_language), translate_text("chills", target_language), translate_text("joint_pain", target_language), translate_text("stomach_pain", target_language), translate_text("acidity", target_language), translate_text("ulcers_on_tongue", target_language), translate_text("muscle_wasting", target_language), translate_text("vomiting", target_language), translate_text("burning_micturition", target_language), translate_text("spotting_ urination", target_language), translate_text("fatigue", target_language), translate_text("weight_gain", target_language), translate_text("anxiety", target_language), translate_text("cold_hands_and_feets", target_language), translate_text("mood_swings", target_language), translate_text("weight_loss", target_language), translate_text("restlessness", target_language), translate_text("lethargy", target_language), translate_text("patches_in_throat", target_language), translate_text("irregular_sugar_level", target_language), translate_text("cough", target_language), translate_text("high_fever", target_language), translate_text("sunken_eyes", target_language), translate_text("breathlessness", target_language), translate_text("sweating", target_language), translate_text("dehydration", target_language), translate_text("indigestion", target_language), translate_text("headache", target_language), translate_text("yellowish_skin", target_language), translate_text("dark_urine", target_language), translate_text("nausea", target_language), translate_text("loss_of_appetite", target_language), translate_text("pain_behind_the_eyes", target_language), translate_text("back_pain", target_language), translate_text("constipation", target_language), translate_text("abdominal_pain", target_language), translate_text("diarrhoea", target_language), translate_text("mild_fever", target_language), translate_text("yellow_urine", target_language), translate_text("yellowing_of_eyes", target_language), translate_text("acute_liver_failure", target_language), translate_text("fluid_overload", target_language), translate_text("swelling_of_stomach", target_language), translate_text("swelled_lymph_nodes", target_language), translate_text("malaise", target_language), translate_text("blurred_and_distorted_vision", target_language), translate_text("phlegm", target_language), translate_text("throat_irritation", target_language), translate_text("redness_of_eyes", target_language), translate_text("sinus_pressure", target_language), translate_text("runny_nose", target_language), translate_text("congestion", target_language), translate_text("chest_pain", target_language), translate_text("weakness_in_limbs", target_language), translate_text("fast_heart_rate", target_language), translate_text("pain_during_bowel_movements", target_language), translate_text("pain_in_anal_region", target_language), translate_text("bloody_stool", target_language), translate_text("irritation_in_anus", target_language), translate_text("neck_pain", target_language), translate_text("dizziness", target_language), translate_text("cramps", target_language), translate_text("bruising", target_language), translate_text("obesity", target_language), translate_text("swollen_legs", target_language), translate_text("swollen_blood_vessels", target_language), translate_text("puffy_face_and_eyes", target_language), translate_text("enlarged_thyroid", target_language), translate_text("brittle_nails", target_language), translate_text("swollen_extremeties", target_language), translate_text("excessive_hunger", target_language), translate_text("extra_marital_contacts", target_language), translate_text("drying_and_tingling_lips", target_language), translate_text("slurred_speech", target_language), translate_text("knee_pain", target_language), translate_text("hip_joint_pain", target_language), translate_text("muscle_weakness", target_language), translate_text("stiff_neck", target_language), translate_text("swelling_joints", target_language), translate_text("movement_stiffness", target_language), translate_text("spinning_movements", target_language), translate_text("loss_of_balance", target_language), translate_text("unsteadiness", target_language), translate_text("weakness_of_one_body_side", target_language), translate_text("loss_of_smell", target_language), translate_text("bladder_discomfort", target_language), translate_text("foul_smell_of urine", target_language), translate_text("continuous_feel_of_urine", target_language), translate_text("passage_of_gases", target_language), translate_text("internal_itching", target_language), translate_text("toxic_look_(typhos)", target_language), translate_text("depression", target_language), translate_text("irritability", target_language), translate_text("muscle_pain", target_language), translate_text("altered_sensorium", target_language), translate_text("red_spots_over_body", target_language), translate_text("belly_pain", target_language), translate_text("abnormal_menstruation", target_language), translate_text("dischromic _patches", target_language), translate_text("watering_from_eyes", target_language), translate_text("increased_appetite", target_language), translate_text("polyuria", target_language), translate_text("family_history", target_language), translate_text("mucoid_sputum", target_language), translate_text("rusty_sputum", target_language), translate_text("lack_of_concentration", target_language), translate_text("visual_disturbances", target_language), translate_text("receiving_blood_transfusion", target_language), translate_text("receiving_unsterile_injections", target_language), translate_text("coma", target_language), translate_text("stomach_bleeding", target_language), translate_text("distention_of_abdomen", target_language), translate_text("history_of_alcohol_consumption", target_language), translate_text("fluid_overload.1", target_language), translate_text("blood_in_sputum", target_language), translate_text("prominent_veins_on_calf", target_language), translate_text("palpitations", target_language), translate_text("painful_walking", target_language), translate_text("pus_filled_pimples", target_language), translate_text("blackheads", target_language), translate_text("scurring", target_language), translate_text("skin_peeling", target_language), translate_text("silver_like_dusting", target_language), translate_text("small_dents_in_nails", target_language), translate_text("inflammatory_nails", target_language), translate_text("blister", target_language), translate_text("red_sore_around_nose", target_language), translate_text("yellow_crust_ooze", target_language)






])
    # diagnosis_details = {
    #     translate_text("Diagnosis", target_language): translate_text(predicted_disease, target_language),
    #     translate_text("Symptoms", target_language): ", ".join(symptoms),
        # translate_text("Suggested Medication", target_language): translate_text("Paracetamol, Antihistamines, Cough Syrup", target_language),
        # translate_text("Precautions", target_language): translate_text("Rest, Stay Hydrated", target_language),
        # translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
        # translate_text("Duration of Treatment", target_language): translate_text("3-5 Days", target_language),
        # translate_text("Patient Instructions", target_language): translate_text("Take paracetamol every 6 hours, drink warm fluids", target_language),
        # translate_text("Potential Complications", target_language): translate_text("Fever persists > 5 days, worsening symptoms", target_language)
    # }
    
    if st.button(translate_text("Generate Report", target_language)):
        predicted_disease = get_predicted_value(symptoms)
        
        diagnosis_details = {
            translate_text("Diagnosis", target_language): translate_text(predicted_disease, target_language),
            translate_text("Symptoms", target_language): ", ".join(symptoms)
        }

        token = generate_token(patient_details[translate_text("Ward No", target_language)])
        display_report(patient_details, diagnosis_details, token)

# # Pediatrics Ward
# if selected == translate_text('Pediatrics', target_language):
#     st.title(translate_text('Welcome to Pediatrics Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Fever", target_language), translate_text("Irritability", target_language), translate_text("Cough", target_language), translate_text("Rashes", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Mild Viral Infection", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Paracetamol, Fluids", target_language),
#         translate_text("Precautions", target_language): translate_text("Keep the Child Hydrated, Monitor Fever", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("3-4 Days", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Give paracetamol every 6 hours, ensure rest", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Persistent fever or worsening symptoms", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Gynecology and Obstetrics Ward
# if selected == translate_text('Gynecology and Obstetrics', target_language):
#     st.title(translate_text('Welcome to Gynecology and Obstetrics Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Mild Abdominal Pain", target_language), translate_text("Fatigue", target_language), translate_text("Irregular Periods", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Mild Hormonal Imbalance", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Pain Relievers, Oral Contraceptives", target_language),
#         translate_text("Precautions", target_language): translate_text("Monitor Symptoms, Rest", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("Yes", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("1 Week", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Take pain relievers as prescribed, rest", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Worsening pain or irregularity", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Orthopedics Ward
# if selected == translate_text('Orthopedics', target_language):
#     st.title(translate_text('Welcome to Orthopedics Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Joint Pain", target_language), translate_text("Swelling", target_language), translate_text("Stiffness", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Mild Arthritis", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Anti-inflammatory Drugs, Pain Relievers", target_language),
#         translate_text("Precautions", target_language): translate_text("Avoid Stress on Joints", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("Yes", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("2 Weeks", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Take medication as prescribed, gentle exercise", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Severe pain or immobility", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Dermatology Ward
# if selected == translate_text('Dermatology', target_language):
#     st.title(translate_text('Welcome to Dermatology Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Itchy Skin", target_language), translate_text("Rashes", target_language), translate_text("Dry Skin", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Mild Eczema", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Moisturizers, Hydrocortisone Cream", target_language),
#         translate_text("Precautions", target_language): translate_text("Avoid Irritants", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("1-2 Weeks", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Apply cream twice daily, avoid hot showers", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Persistent itching or infection", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Ophthalmology Ward
# if selected == translate_text('Ophthalmology', target_language):
#     st.title(translate_text('Welcome to Ophthalmology Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Itchy Eyes", target_language), translate_text("Redness", target_language), translate_text("Watery Eyes", target_language), translate_text("Blurred Vision", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Conjunctivitis (Pink Eye)", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Eye Drops, Antihistamines", target_language),
#         translate_text("Precautions", target_language): translate_text("Avoid Touching Eyes, Maintain Hygiene", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("5-7 Days", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Use eye drops 3 times a day, wash hands frequently", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Persistent redness or vision issues", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # ENT (Ear, Nose, and Throat) Ward
# if selected == translate_text('ENT', target_language):
#     st.title(translate_text('Welcome to ENT Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Sore Throat", target_language), translate_text("Ear Pain", target_language), translate_text("Nasal Congestion", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Sinus Infection", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Decongestants, Pain Relievers", target_language),
#         translate_text("Precautions", target_language): translate_text("Steam Inhalation, Avoid Cold Air", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("1 Week", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Take medication as prescribed, drink warm fluids", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Persistent congestion or ear pain", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Gastroenterology Ward
# if selected == translate_text('Gastroenterology', target_language):
#     st.title(translate_text('Welcome to Gastroenterology Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Stomach Pain", target_language), translate_text("Bloating", target_language), translate_text("Nausea", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Indigestion", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Antacids, Digestive Enzymes", target_language),
#         translate_text("Precautions", target_language): translate_text("Avoid Spicy/Fatty Foods", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("2-3 Days", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Take antacids after meals, eat smaller meals", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Persistent nausea or worsening pain", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Endocrinology Ward
# if selected == translate_text('Endocrinology', target_language):
#     st.title(translate_text('Welcome to Endocrinology Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Fatigue", target_language), translate_text("Weight Gain", target_language), translate_text("Hair Loss", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Mild Hypothyroidism", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Thyroid Hormone Replacement", target_language),
#         translate_text("Precautions", target_language): translate_text("Regular Monitoring of Thyroid Levels", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("Yes", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("Ongoing", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Take medication daily, monitor weight changes", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Severe fatigue or irregular heartbeats", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Urology Ward
# if selected == translate_text('Urology', target_language):
#     st.title(translate_text('Welcome to Urology Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Frequent Urination", target_language), translate_text("Burning Sensation", target_language), translate_text("Lower Abdominal Pain", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Mild Urinary Tract Infection (UTI)", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Antibiotics, Pain Relievers", target_language),
#         translate_text("Precautions", target_language): translate_text("Drink Plenty of Water, Maintain Hygiene", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("3-5 Days", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Take antibiotics as prescribed, drink water frequently", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Worsening pain or blood in urine", target_language)
#     }

#     if st.button(translate_text("Generate Report", target_language)):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)

# # Allergy and Immunology Ward
# if selected == translate_text('Allergy and Immunology', target_language):
#     st.title(translate_text('Welcome to Allergy and Immunology Ward', target_language))
    
#     symptoms = st.multiselect(translate_text("Select Symptoms", target_language), [translate_text("Sneezing", target_language), translate_text("Runny Nose", target_language), translate_text("Itchy Eyes", target_language)])
#     diagnosis_details = {
#         translate_text("Diagnosis", target_language): translate_text("Seasonal Allergies", target_language),
#         translate_text("Symptoms", target_language): ", ".join(symptoms),
#         translate_text("Suggested Medication", target_language): translate_text("Antihistamines", target_language),
#         translate_text("Precautions", target_language): translate_text("Avoid Allergens (Pollen, Dust)", target_language),
#         translate_text("Follow-Up Required", target_language): translate_text("No", target_language),
#         translate_text("Duration of Treatment", target_language): translate_text("As Needed", target_language),
#         translate_text("Patient Instructions", target_language): translate_text("Take antihistamines when symptoms occur", target_language),
#         translate_text("Potential Complications", target_language): translate_text("Persistent or severe allergic reactions", target_language)
#      }

#     if st.button(translate_text("Generate Report", target_language), key=1):
#         token = generate_token(patient_details[translate_text("Ward No", target_language)])
#         display_report(patient_details, diagnosis_details, token)
