from suds.client import Client
url = "http://calculator-webservice.mybluemix.net/calculator?wsdl"
client = Client(url)
print(client) # This returns the details regarding the webservice.
print(client.service.add(2,3))