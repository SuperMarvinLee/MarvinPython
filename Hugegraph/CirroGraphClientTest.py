import cirrograph_client as cirroclient
auth = ('admin','2022131@CirroGraph')
client = cirroclient.CirroGraphClient("http://139.9.132.125:5000", "cirrograph",auth=auth)
#val = client.create_variables('graph','cirrograph').response
#修改时调用的是创建的接口
#val = client.update_variables('graph','cirrograph').response
#val = client.get_variables().response
#val = client.get_variable_key('111').response
#val = client.delete_variable_key('1111').response
# val = client.get_graphs().response
# val = client.get_graph().response
#val = client.create_graph('cirrograph2').response
# val = client.clear_graph('cirrograph2').response
#val = client.drop_graph('cirrograph2').response
#val = client.get_graph_config('cirrograph').response
# val = client.get_graph_mode('cirrograph').response
# val = client.set_graph_mode('cirrograph','NONE').response
#val = client.get_graph_read_mode('cirrograph').response
# val = client.set_graph_read_mode('cirrograph','ALL').response
# val = client.graph_snapshot_create('cirrograph3').response
#val = client.graph_snapshot_resume('mysqlgraph').response
#val = client.graph_compact('cirrograph').response
#val = client.get_tasks(status='SUCCESS').response
# val = client.get_task().response
# val = client.delete_task('3').response
# val = client.cancel_task('8').response
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
# request={
#             "user_name": "bowen",
#             "user_password": "123456",
#             "user_phone": "155****9088",
#             "user_email": "123456@xx.com"
#         }
'''用户认证与权限'''
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
#                     "type": "NONE"
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
request = {
        "belong_description": "update test"
    }
val = client.update_belong('S-63:bowen>-82>>S-69:all',request).response
print(val)