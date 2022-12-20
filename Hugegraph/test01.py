import json
import cirrograph_client as cirroclient

auth = ('admin','2022131@CirroGraph')
cirrograph = cirroclient.CirroGraphClient("http://172.26.167.216:8080", "cirrograph",auth=auth)

val = cirrograph.get_graph().response
print(type(val))

print(type(json.load(val)))