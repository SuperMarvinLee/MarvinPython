import cirrograph_client as cirroclient
auth = ('admin','2022131@CirroGraph')
client = cirroclient.CirroGraphClient("http://localhost:8000", "cirrograph",auth=auth)
'''schema API'''
# val = client.get_schema().response
'''PropertyKey API'''
# request = {
#     "name": "class",
#     "data_type": "TEXT",
#     "cardinality": "SINGLE"
# }
# val = client.create_propertykey(request).response
# request = {
#     "min": 0,
#     "max": 20
# }
# val = client.add_propertykey_userdata('myage',request).response
# request = {
#     "min":0
# }
# val = client.delete_propertykey_userdata('myage',request).response
# val = client.get_propertykeys().response
# val = client.get_propertykey_name('myage').response
# val = client.delete_propertykey_name('myage').response
'''VertexLabel API'''
# request = {
#     "name": "DaJun",
#     "id_strategy": "DEFAULT",
#     "properties": [
#         "name",
#         "age",
#         "num"
#     ],
#     "primary_keys": [
#         "name"
#     ],
#     "nullable_keys": [],
#     "enable_label_index": True
# }

# val = client.create_vertexlabel(request).response
# val = client.add_vertexlabel_properties('DaJun',['length'],['length']).response
# request = {
#     "class" : "the fifth class"
# }
# val = client.add_vertexlabel_userdata('DaJun',request).response
# val = client.get_vertexlabels().response
# val = client.get_vertexlabel_name('DaJun').response
# val = client.delete_vertexlabel_name('test').response
'''EdgeLabel API'''
# request = {
#     "name": "belongs",
#     "source_label": "person",
#     "target_label": "DaJun",
#     "frequency": "SINGLE",
#     "properties": [
#         "weight"
#     ],
#     "sort_keys": [],
#     "nullable_keys": [],
#     "enable_label_index": True
# }

# val = client.create_edgelabel(request).response
# val = client.add_edgelabel_properties('belongs',['name'],['name']).response
# request = {
#     'test':'test',
#     'meaning':'the relationship between person and DaJun'
# }
# val = client.add_edgelabel_userdata('belongs',request).response
# request = {
#     "test":"test"
# }
# val = client.delete_edgelabel_userdata("belongs",request).response
# val = client.get_edgelabels().response
# val = client.get_edgelabel_name('belongs').response
# val = client.delete_edgelabel_name('test').response
'''IndexLabel API'''
# request = {
#     "name": "personByAge",
#     "base_type": "VERTEX_LABEL",
#     "base_value": "person",
#     "index_type": "SECONDARY",
#     "fields": [
#         "age"
#     ]
# }
# val = client.create_indexlabel(request).response
# val = client.get_indexlabels().response
# val = client.get_indexLabel_name('personByName').response
'''Rebuild API'''
# val = client.rebuild_indexlabel('personByName').response
# val = client.rebuild_edgelabel('belongs').response
# val = client.rebuild_vertexlabel('DaJun').response
'''Vertex API'''
# request = {
#     "label": "DaJun",
#     "properties": {
#         "name": "逍遥",
#         "age": 24,
#         "num":18
#     }
# }
# val = client.create_vertex(request).response
# request = [
#     {
#         "label": "DaJun",
#         "properties": {
#             "name": "marko",
#             "age": 29,
#             "num":16
#         }
#     },
#     {
#         "label": "DaJun",
#         "properties": {
#             "name": "marvin",
#             "age": 28,
#             "num":17
#         }
#     }
    
# ]
# val = client.create_vertex_batch(request).response
# val = client.update_vertex_properties('4:marvin','DaJun',{'length':20}).response
# request = {
#     "vertices":[
#         {
#             "label":"DaJun",
#             "type":"vertex",
#             "properties":{
#                 "name": "marvin",
#                 "age": 26,
#                 "num":20
#             }
#         },
#         {
#             "label":"DaJun",
#             "type":"vertex",
#             "properties":{
#                 "name": "marko",
#                 "age": 28,
#                 "num":18
#             }
#         }
#     ],
#     "update_strategies":{
#         "name":"OVERRIDE",
#         "age":"OVERRIDE",
#         "num":"BIGGER",
#     },
#     "create_if_not_exist":True
# }

# val = client.update_vertex_properties_batch(request).response
# val = client.delete_vertex_properties('4:marvin','DaJun',{'length':20}).response
# val = client.get_vertexs_condition('DaJun',{'num':18}).response
# val = client.get_vertex_page(10).response
# val = client.get_vertex_page(10,'AghoAAAAAAAAAAo=').response
# val = client.get_vertex_id('4:marvin').response
# val = client.delete_vertex_id('4:dajun','DaJun').response
'''Edge API'''
# request = {
#     "label": "belongs",
#     "outV": 999,
#     "inV": "4:marvin",
#     "outVLabel": "person",
#     "inVLabel": "DaJun",
#     "properties": {
#         "weight": 0.2
#     }
# }
# val = client.create_edge(request).response
# request = [
#     {
#     "label": "belongs",
#     "outV": 999,
#     "inV": "4:marko1",
#     "outVLabel": "person",
#     "inVLabel": "DaJun",
#     "properties": {
#         "weight": 0.2
#     }
#     },
#     {
#     "label": "belongs",
#     "outV": 999,
#     "inV": "4:逍遥1",
#     "outVLabel": "person",
#     "inVLabel": "DaJun",
#     "properties": {
#         "weight": 0.2
#     }
#     }
# ]
# val = client.create_edge_batch(request,False).response
# val = client.update_edge_properties('L999>4>>S4:逍遥',{ "weight": 1.0 }).response
# request = {
#     "edges":[
#         {
#             "label": "belongs",
#             "outV": 999,
#             "inV": "4:marko",
#             "outVLabel": "person",
#             "inVLabel": "DaJun",
#             "properties":{
#                 "weight":0.1
#             }
#         },
#         {
#             "label": "belongs",
#             "outV": 999,
#             "inV": "4:marvin",
#             "outVLabel": "person",
#             "inVLabel": "DaJun",
#             "properties":{
#                 "weight":0.2
#             }
#         }
#     ],
#     "update_strategies":{
#         "weight":"SUM"
#     },
#     "check_vertex": False,
#     "create_if_not_exist":True
# }
# val = client.update_edge_properties_batch(request).response
# val = client.delete_edge_properties('L999>4>>S4:三木',{'name':'三木君'}).response
# val = client.get_edges_condition(999).response
# val = client.get_edges_page(2,'CAgBgggBAAgEAAAAAAAAAAE=').response
# val = client.get_edge_id('L1>1>>L4').response
# val = client.delete_edge_id('S11>3>>S12').response

'''Variable API'''
# val = client.create_variables('graph','cirrograph').response
# val = client.update_variables('graph','cirrograph').response
# val = client.get_variables().response
# val = client.get_variable_key('111').response
# val = client.delete_variable_key('1111').response
'''Graphs API'''
# val = client.get_graphs().response
# val = client.get_graph().response
# val = client.create_graph('cirrograph2').response
# val = client.clear_graph().response
# val = client.drop_graph().response
# val = client.get_graph_config().response
# val = client.get_graph_mode().response
# val = client.set_graph_mode('NONE').response
# val = client.get_graph_read_mode().response
# val = client.set_graph_read_mode('ALL').response
# val = client.graph_snapshot_create().response
# val = client.graph_snapshot_resume().response
# val = client.graph_compact().response
'''Task API'''
# val = client.get_tasks(status='SUCCESS').response
# val = client.get_task(1).response
# val = client.delete_task('3').response
# val = client.cancel_task('8').response
'''Gremlin API'''
# val = client.execute_germlin_get('cirrograph.traversal().V(1)').response
# request = {
# 	"gremlin": "cirrograph.traversal().V(1)",
# 	"bindings": {},
# 	"language": "gremlin-groovy",
# 	"aliases": {}
#     }

# val = client.execute_germlin_post(request).response
# gremlin = """
#     for (int i = 0; i < 10; i++) {
#         cirrograph.addVertex(T.label,'person',T.id,i+200,'name','person'+i);
#         cirrograph.tx().commit();
#         try {
#             sleep(1000);
#         } catch (InterruptedException e) {
#         break;
#         }
#     }
# """
# val = client.execute_germlin_post_job(gremlin).response
# val = client.execute_cypherql('match ()-[e]-() return e').response
'''用户认证与权限'''
# request={
#             "user_name": "bowen",
#             "user_password": "123456",
#             "user_phone": "155****9088",
#             "user_email": "123456@xx.com"
#         }
# val = client.add_user(request).response
# val = client.delete_user("-63:bowen").response
# request={
#             "user_password": "12345678",
#             "user_phone": "12345678",
#             "user_email": "12345678@xx.com"
#         }
# val = client.update_user('-63:bowen',request).response
# val = client.get_users().response
# val = client.get_user('-63:bowen').response
# val = client.get_user_role('-63:admin').response
# request = {
#         "group_name": "all",
#         "group_description": "group can do anything"
#     }
# val = client.add_group(request).response
# val = client.delete_group('-69:all').response
# request = {
#             "group_name": "all",
#             "group_description": "group can do anything,just like admin"
#     }
# val = client.update_group('-69:all',request).response
# val = client.get_groups().response
# val = client.get_group('-69:all').response
# request= {
#         "target_name": "all",
#         "target_graph": "cirrograph",
#         "target_url": "139.9.132.125:5000",
#         "target_resources": [
#             {
#                 "type": "ALL"
#             }
#             ]
#         }
# val = client.add_target(request).response
# val = client.delete_target('-77:all').response
# request = {
#             "target_name": "all",
#             "target_graph": "cirrograph",
#             "target_url": "139.9.132.125:5000",
#             "target_resources": [
#                 {
#                     "type": "ALL"
#                 }
#             ]
#         }
# val = client.update_target('-77:all',request).response
# val = client.get_targets().response
# val = client.get_target('-77:all').response
# request = {
#             "user": "-63:bowen",
#             "group": "-69:all"
#         }
# val = client.add_belong(request).response
# val = client.delete_belong('S-63:bowen>-82>>S-69:all').response
# request = {
#         "belong_description": "update test"
#     }
# val = client.update_belong('S-63:bowen>-82>>S-69:all',request).response
# val = client.get_belongs(2).response
# val = client.get_belong('S-63:bowen>-82>>S-69:all').response
# request = {
#     "group": "-69:all",
#     "target": "-77:all",
#     "access_permission": "READ"
# }
# val = client.add_accesses(request).response
# request = {
#     "group": "-69:all",
#     "target": "-77:all",
#     "access_permission": "READ"
# }
# val = client.add_accesses(request).response
# val = client.delete_accesses('S-69:all>-88>11>S-77:all').response
# val = client.update_accesses('S-69:all>-88>11>S-77:all',request).response
# val = client.get_accessess().response
# val = client.get_accesses('S-69:all>-88>11>S-77:all').response
# request = {
#         "access_description": "update test 2"
#     }
'''其他'''
val = client.get_version().response
print(val)