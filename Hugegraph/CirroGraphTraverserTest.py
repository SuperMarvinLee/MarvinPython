import cirrograph_client as cirroclient
auth = ('admin','2022131@CirroGraph')
traverser = cirroclient.CirroGraphTraverser("http://localhost:8000", "cirrograph",auth=auth)
#request = KoutRequest.KoutRequest(1,EdgeStep.EdgeStep(),maxDepth=1,withVertex=True)
val = traverser.kout_get(1,2).response
# request = {
#   "source": 1,
#   "step": {
#     "direction": "BOTH",
#     "labels": ["knows", "created"],
#     "properties": {
#       "weight": "P.gt(0.1)"
#     },
#     "max_degree": 10000,
#     "skip_degree": 100000
#   },
#   "max_depth": 1,
#   "nearest": True,
#   "limit": 10000,
#   "with_vertex": True,
#   "with_path": True
# }

#val = traverser.kout_post(request).response
#val = traverser.kneighbor_get('10',2,max_degree=10).response
# request = {
#   "source": 1,
#   "step": {
#     "direction": "BOTH",
#     "labels": ["knows", "created"],
#     "properties": {
#       "weight": "P.gt(0.1)"
#     },
#     "max_degree": 10000,
#     "skip_degree": 100000
#   },
#   "max_depth": 3,
#   "limit": 10000,
#   "with_vertex": True,
#   "with_path": True
# }

# val = traverser.kneighbor_post(request).response
# val = traverser.sameneighbors(1,3).response
# val = traverser.jaccardsimilarity_get('10','12').response
# request = {
#   "vertex": 1,
#   "step": {
#     "direction": "BOTH",
#     "labels": [],
#     "max_degree": 10000,
#     "skip_degree": 100000
#   },
#   "top": 3
# }
# val = traverser.jaccardsimilarity_post(request).response
# val = traverser.shortestpath(2,5,5).response
# val = traverser.allshortestpaths(2,5,5).response
# val = traverser.weightedshortestpath(2,5,'weight',with_vertex=True).response
# val = traverser.singlesourceshortestpath(2,'weight',with_vertex=True).response
# request = {
#     "vertices": {
#         "ids": [2,5,6]
#     },
#     "step": {
#         "direction": "BOTH",
#         "properties": {
#         }
#     },
#     "max_depth": 10,
#     "capacity": 100000000,
#     "with_vertex": True
# }
# val = traverser.multinodeshortestpath(request).response
# val = traverser.paths_get(2,5,5).response
# request={
# "sources": {
#   "ids": [1]
# },
# "targets": {
#   "ids": [6]
# },
# "step": {
# "direction": "BOTH",
#   "properties": {
#     "weight": "P.gt(0.01)"
#   }
# },
# "max_depth": 10,
# "capacity": 100000000,
# "limit": 10000000,
# "with_vertex": False
# }
# val = traverser.paths_post(request).response
# request = {
#     "sources":{
#         "ids":[

#         ],
#         "label":"person",
#         "properties":{
#             "name":"marko"
#         }
#     },
#     "steps":[
#         {
#             "direction":"OUT",
#             "labels":[
#                 "knows"
#             ],
#             "weight_by":"weight",
#             "max_degree":-1
#         },
#         {
#             "direction":"OUT",
#             "labels":[
#                 "created"
#             ],
#             "default_weight":8,
#             "max_degree":-1,
#             "sample":1
#         }
#     ],
#     "sort_by":"INCR",
#     "with_vertex":True,
#     "capacity":-1,
#     "limit":-1
# }
# val = traverser.customizedpaths(request).response
# request = {
#   "sources": {
#     "ids": [],
#     "label": "person",
#     "properties": {
#       "name": "vadas"
#     }
#   },
#   "targets": {
#     "ids": [],
#     "label": "software",
#     "properties": {
#       "name": "ripple"
#     }
#   },
#   "steps": [
#     {
#       "direction": "IN",
#       "labels": ["knows"],
#       "properties": {
#       },
#       "max_degree": 10000,
#       "skip_degree": 100000
#     },
#     {
#       "direction": "OUT",
#       "labels": ["created"],
#       "properties": {
#       },
#       "max_degree": 10000,
#       "skip_degree": 100000
#     },
#     {
#       "direction": "IN",
#       "labels": ["created"],
#       "properties": {
#       },
#       "max_degree": 10000,
#       "skip_degree": 100000
#     },
#     {
#       "direction": "OUT",
#       "labels": ["created"],
#       "properties": {
#       },
#       "max_degree": 10000,
#       "skip_degree": 100000
#     }
#   ],
#   "capacity": 10000,
#   "limit": 10,
#   "with_vertex": False
# }

# val = traverser.templatepaths(request).response
# val = traverser.crosspoints(2,5,5).response
# request = {
#     "sources":{
#         "ids":[
#             3,
#             5
#         ]
#     },
#     "path_patterns":[
#         {
#             "steps":[
#                 {
#                     "direction":"IN",
#                     "labels":[
#                         "created"
#                     ],
#                     "max_degree":-1
#                 }
#             ]
#         }
#     ],
#     "with_path":True,
#     "with_vertex":True,
#     "capacity":-1,
#     "limit":-1
# }
# val = traverser.customizedcrosspoints(request).response
# val = traverser.rings(1,3).response
# val = traverser.rays(1,2).response
# request = {
#     "sources":{
#         "ids":[],
#         "label": "person",
#         "properties": {
#             "name":"marko"
#         }
#     },
#     "label":"knows",
#     "direction":"BOTH",
#     "min_neighbors":1,
#     "alpha":0.75,
#     "min_similars":1,
#     "top":0,
#     "group_property":"city",
#     "min_groups":2,
#     "max_degree": 10000,
#     "capacity": -1,
#     "limit": -1,
#     "with_intermediary": False,
#     "with_vertex":True
# }

# val = traverser.fusiformsimilarity(request).response
# val = traverser.verticesByIds([1,2,3,'10']).response
# val = traverser.verticesShard(1048576).response
# val = traverser.verticesByShard('CAE=','gTEyAA==').response
# val = traverser.edgesByIds(['L1>1>>L2','S11>3>>S12']).response
# val = traverser.edgesShard(1048576).response
# val = traverser.edgesByShard('CAGCCAEACAI=','gTExgggDAIExMgA=').response
# request = {
#     "source": 1,
#     "label": "created",
#     "alpha": 0.6,
#     "max_depth": 15,
#     "with_label": "OTHER_LABEL",
#     "sorted": True,
#     "limit": 10
# }

# val = traverser.personalrank(request).response
# request = {
#     "source":1,
#     "steps":[
#         {
#             "direction":"OUT",
#             "labels":[
#                 "knows"
#             ],
#             "max_degree":-1,
#             "top":100
#         },
#         {
#             "direction":"OUT",
#             "labels":[
#                 "created",
#             ],
#             "max_degree":-1,
#             "top":100
#         },
#         {
#             "direction":"OUT",
#             "labels":[
#                 "stredge"
#             ],
#             "max_degree":-1,
#             "top":100
#         }
#     ],
#     "alpha":0.9,
#     "capacity":-1
# }
# val = traverser.neighborrank(request).response
print(val)