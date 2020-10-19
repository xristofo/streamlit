import json
import boto3

def get_patient_record(patient_code):

	jsonfile = patient_code+'.json'

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = jsonfile
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)

	return json.dumps(data['Diagnoses'])

def get_patient_details(patient_id, field):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'patients.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)
	
	return data['Patients'][patient_id][field]

def get_patient_id(searchkey, keyvalue):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'patients.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)

	for x in range(len(data['Patients'])):
		if data['Patients'][x][searchkey]==keyvalue:
			return x

	return -1

def get_patients(searchkey):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'patients.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)

	rlist = []

	for x in range(len(data['Patients'])):
		rlist.append(data['Patients'][x][searchkey])

	return rlist

def get_medicines(searchkey):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'medicines.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)

	rlist = []

	for x in range(len(data['Medicines'])):
		rlist.append(data['Medicines'][x][searchkey])

	return rlist


def get_Contraindications(searchkey, keyvalue):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'medicines.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)


	for x in range(len(data['Medicines'])):
		if data['Medicines'][x][searchkey]==keyvalue:
			return data['Medicines'][x]['Contraindications']


def get_medicine_id(searchkey, keyvalue):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'medicines.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)

	for x in range(len(data['Medicines'])):
		if data['Medicines'][x][searchkey]==keyvalue:
			return x

def get_medicine_details(medicine_id, field):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'medicines.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)
	
	return data['Medicines'][medicine_id][field]

def get_alternative_medicine(key_ingredient, rejected_medicine):

	s3 = boto3.client('s3',aws_access_key_id='AKIAI47GTGZHLJKN6WLQ',
                      aws_secret_access_key='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')

	bucket = 'cei521'
	key = 'medicines.json'
	obj = s3.get_object(Bucket=bucket, Key=key)    

	jsonstring = obj['Body'].read()

	data  = json.loads(jsonstring)
	#array = medicines
	#data  = json.loads(array)

	for x in range(len(data['Medicines'])):
		if (data['Medicines'][x]['key_ingredient']==key_ingredient) and (data['Medicines'][x]['Brand']!=rejected_medicine):
			return data['Medicines'][x]['Brand']

	return ""