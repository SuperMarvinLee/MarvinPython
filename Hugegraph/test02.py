import cirrograph_client as cirroclient
auth = ('admin','2022131@CirroGraph')
traverser = cirroclient.CirroGraphTraverser("http://139.9.132.125:5000", "cirrograph",auth=auth)
#request2 = KoutRequest.KoutRequest(1,EdgeStep.EdgeStep(),maxDepth=1,withVertex=True)
val = traverser.kout_get(1,2).response
print(val)