import json

def get_patient_record():

	jsonstring = """{
	"Diagnoses": [
		{
			"date": "1/5/2005",
			"diagnosis_code": "5245",
			"medication_code": "0056"
		},
		{
			"date": "10/12/2007",
			"diagnosis_code": "6545",
			"medication_code": "0025"
		}
	]
	}"""

	data  = json.loads(jsonstring)
	return json.dumps(data['Diagnoses'])

def get_patient_details(patient_id, field):

	array = """{
	"Patients": [
		{
			"Surname": "Kostas",
			"Name": "Kosta",
			"Code": "A001",
			"Telephone": "1234567890",
			"Birthdate": "25/03/1995",
			"Sex": "M",
			"Address": {
				"Street": "Georgiou Evagorou",
				"Number": 23,
				"PCode": 5568,
				"City": "Limassol"
			}
		},
		{
			"Surname": "Ioannou",
			"Name": "Marios",
			"Code": "A002",
			"Telephone": "1234567898",
			"Birthdate": "5/11/1983",
			"Sex": "M",
			"Address": {
				"Street": "Athinwn",
				"Number": 3,
				"PCode": 4168,
				"City": "Limassol"
			}
		}
	]
	}"""
	
	data  = json.loads(array)
	
	return data['Patients'][patient_id][field]

def get_patient_id(searchkey, keyvalue):

	array = """{
	"Patients": [
		{
			"Surname": "Kostas",
			"Name": "Kosta",
			"Code": "A001",
			"Telephone": "1234567890",
			"Birthdate": "25/03/1995",
			"Sex": "M",
			"Address": {
				"Street": "Georgiou Evagorou",
				"Number": 23,
				"PCode": 5568,
				"City": "Limassol"
			}
		},
		{
			"Surname": "Ioannou",
			"Name": "Marios",
			"Code": "A002",
			"Telephone": "1234567898",
			"Birthdate": "5/11/1983",
			"Sex": "M",
			"Address": {
				"Street": "Athinwn",
				"Number": 3,
				"PCode": 4168,
				"City": "Limassol"
			}
		}
	]
	}"""
	
	data  = json.loads(array)

	for x in range(len(data['Patients'])):
		if data['Patients'][x][searchkey]==keyvalue:
			return x



	return -1

def get_patients(searchkey):

	array = """{
	"Patients": [
		{
			"Surname": "Kostas",
			"Name": "Kosta",
			"Code": "A001",
			"Telephone": "1234567890",
			"Birthdate": "25/03/1995",
			"Sex": "M",
			"Address": {
				"Street": "Georgiou Evagorou",
				"Number": 23,
				"PCode": 5568,
				"City": "Limassol"
			}
		},
		{
			"Surname": "Ioannou",
			"Name": "Marios",
			"Code": "A002",
			"Telephone": "1234567898",
			"Birthdate": "5/11/1983",
			"Sex": "M",
			"Address": {
				"Street": "Athinwn",
				"Number": 3,
				"PCode": 4168,
				"City": "Limassol"
			}
		}
	]
	}"""
	
	data  = json.loads(array)
	rlist = []

	for x in range(len(data['Patients'])):
		rlist.append(data['Patients'][x][searchkey])

	return rlist

def get_medicines(searchkey):

	array = """{
	"Medicines": [
		{
			"Company": "Bayer",
			"Brand": "Ominaxil",
			"Code": "0025",
			"Supplier": "MJ Medicines Ltd",
			"key_ingredient": "Paracetamol",
			"Contraindications": [
				"0001",
				"0012",
				"1245"
			]
		},
		{
			"Company": "Novartis",
			"Brand": "Parasorilax",
			"Code": "3350",
			"Supplier": "Medicines Ltd",
			"key_ingredient": "Aspirin",
			"Contraindications": [
				"0052",
				"5245"
			]
		}
	]
	}"""
	
	data  = json.loads(array)
	rlist = []

	for x in range(len(data['Medicines'])):
		rlist.append(data['Medicines'][x][searchkey])

	return rlist


def get_Contraindications(searchkey, keyvalue):

	array = """{
	"Medicines": [
		{
			"Company": "Bayer",
			"Brand": "Ominaxil",
			"Code": "0025",
			"Supplier": "MJ Medicines Ltd",
			"key_ingredient": "Paracetamol",
			"Contraindications": [
				"5245",
				"0012",
				"1245"
			]
		},
		{
			"Company": "Novartis",
			"Brand": "Parasorilax",
			"Code": "3350",
			"Supplier": "Medicines Ltd",
			"key_ingredient": "Aspirin",
			"Contraindications": [
				"0052",
				"0012"
			]
		}
	]
	}"""
	
	data  = json.loads(array)

	for x in range(len(data['Medicines'])):
		if data['Medicines'][x][searchkey]==keyvalue:
			return data['Medicines'][x]['Contraindications']


def get_medicine_id(searchkey, keyvalue):

	array = """{
	"Medicines": [
		{
			"Company": "Bayer",
			"Brand": "Ominaxil",
			"Code": "0025",
			"Supplier": "MJ Medicines Ltd",
			"key_ingredient": "Paracetamol",
			"Contraindications": [
				"5245",
				"0012",
				"1245"
			]
		},
		{
			"Company": "Novartis",
			"Brand": "Parasorilax",
			"Code": "3350",
			"Supplier": "Medicines Ltd",
			"key_ingredient": "Aspirin",
			"Contraindications": [
				"0052",
				"0012"
			]
		}
	]
	}"""
	
	data  = json.loads(array)

	for x in range(len(data['Medicines'])):
		if data['Medicines'][x][searchkey]==keyvalue:
			return x

def get_medicine_details(medicine_id, field):

	array = """{
	"Medicines": [
		{
			"Company": "Bayer",
			"Brand": "Ominaxil",
			"Code": "0025",
			"Supplier": "MJ Medicines Ltd",
			"key_ingredient": "Paracetamol",
			"Contraindications": [
				"5245",
				"0012",
				"1245"
			]
		},
		{
			"Company": "Novartis",
			"Brand": "Parasorilax",
			"Code": "3350",
			"Supplier": "Medicines Ltd",
			"key_ingredient": "Aspirin",
			"Contraindications": [
				"0052",
				"0012"
			]
		}
	]
	}"""
	
	data  = json.loads(array)
	
	return data['Medicines'][medicine_id][field]