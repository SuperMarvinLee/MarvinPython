import json
import cirrograph_client as cirroclient

auth = ('admin','2022131@CirroGraph')
traverser = cirroclient.CirroGraphTraverser("http://139.9.132.125:5000", "cirrograph",auth=auth)

val = traverser.kneighbor_get("3:taylor",1).response
print(type(val))

print(val)