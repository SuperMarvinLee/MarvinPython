import cirrograph_client as cirroclient
auth = ('admin','2022131@CirroGraph')
traverser = cirroclient.CirroGraphTraverser("http://139.9.132.125:5000", "cirrograph",auth=auth)

request = {
  "source": 1,
  "step": {
    "direction": "BOTH",
    "labels": ["knows", "created"],
    "properties": {
      "weight": "P.gt(0.1)"
    },
    "max_degree": 10000,
    "skip_degree": 100000
  },
  "max_depth": 3,
  "limit": 10000,
  "with_vertex": True,
  "with_path": True
}

#request2 = KoutRequest.KoutRequest(1,EdgeStep.EdgeStep(),maxDepth=1,withVertex=True)

val = traverser.kneighbor_post(request).response
print(type(val))

print(val)