import pytest, yaml

with open('conf.yaml') as file:
	data = yaml.load(file, Loader = yaml.FullLoader)
	ip = data['ip']
	login, password = data['data']['login'], data['data']['password']
	testValue = data['stringg']

def testData():
	assert ip == '127.0.0.1'
	assert login == 'name'
	assert password == 'pass'
	assert type(testValue) == str