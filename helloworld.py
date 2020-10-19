import streamlit as st
from PIL import Image
import myfunctions as mf
import pandas as pd

col1, col2, col3 = st.beta_columns(3)

with col1:
	st.header("")
	st.image("https://www.cut.ac.cy/digitalAssets/17/17780_1CUT-LOGO-EN-WEB.png", use_column_width=True)

with col2:
	st.header("")
	st.image("https://www.cut.ac.cy/digitalAssets/17/17780_1logo-eut.png", use_column_width=True)

with col3:
	st.header("")
	st.image("http://seiis.cut.ac.cy/images/seiislogo.png", use_column_width=True)

st.title("CEI 521 (463)")
st.header("Advanced Topics in Software Engineering")
st.subheader("Autumn 2020 - Project")

# x = st.slider('x')
# st.write(x, 'squared is', x * x)
#st.write(str(myfunctions.get_patients())
searchkey = st.radio("Search key:",('Surname', 'Name', 'Code', 'Telephone'))

selected_patient = st.selectbox(label="Please select patient's name:", options=['Select:']+mf.get_patients(searchkey))


if selected_patient != 'Select:':
	st.write("Patient's details:")
	patiend_id = mf.get_patient_id(searchkey, selected_patient)

	st.text("*"*91)
	st.write('Surname:', mf.get_patient_details(patiend_id, "Surname"))
	st.write('Name:', mf.get_patient_details(patiend_id, "Name"))
	st.write('Birthdate:', mf.get_patient_details(patiend_id, "Birthdate"))
	st.write('Telephone:', mf.get_patient_details(patiend_id, "Telephone"))
	st.text("*"*91)

	patient_code = mf.get_patient_details(patiend_id, "Code")
	df = pd.read_json (mf.get_patient_record(patient_code))

	st.write("Visits")
	st.write(df)
	st.text("*"*91)

	#if st.button('Add new visit'):
	selected_medicine = st.selectbox(label="Please select Medication:", options=['Select:']+mf.get_medicines("Brand"))

	if selected_medicine != 'Select:':
		cilist = mf.get_Contraindications("Brand", selected_medicine)
		cidf = pd.DataFrame(cilist, columns =['Contraindications'])
		st.write("Contraindications")
		st.write(cidf)
	
		notok = False

		for index, row in df.iterrows():
			for indexci, rowci in cidf.iterrows():
				if (str(row['diagnosis_code'])==str(rowci['Contraindications'])):
					notok = True

		if notok:
			st.error('Medicine '+selected_medicine+' is not indicated for patient '+mf.get_patient_details(patiend_id, "Name"))
			
			medicine_id = mf.get_medicine_id("Brand", selected_medicine)
			key_ingredient = mf.get_medicine_details(medicine_id, "key_ingredient")
			rejected_medicine = selected_medicine
			suggested_medicine = mf.get_alternative_medicine(key_ingredient, rejected_medicine)
			
			if not suggested_medicine:
				st.error('No Alternative... Sorry!')
			else:	
				st.success('Please consider '+suggested_medicine+ ' as alternative medication!')
		else: 
			#st.balloons()
			st.success('Ok')