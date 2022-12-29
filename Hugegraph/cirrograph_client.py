#!/usr/bin/python3
# Filename      : cirrograph_client.py
# Description   : Python3-CirroGraph-Client
# author        : Shangrila Shell
# version       : cirrograph 1.3.1(hugegraph 12)
# date          : 2022/12/12
# -*- coding: UTF-8 -*-

import json,requests

# response of reuqest
class CirroGraphResponse(object):
    """
    获得响应状态码和内容
    """
    def __init__(self, response):
        self.status_code = response.status_code
        if(response.text != ''):
            self.response = response.text
        else:
            self.response = response.status_code

# CirroGraphClient Class
class CirroGraphClient(object):
    """
    CirroGraph Client API
    """

    def __init__(self,host,graph,headers={},auth=()):
        #auth = ('admin','2022131@CirroGraph')
        self.host = host
        self.graph = graph
        self.auth = auth
        
        if headers=={}:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Content-Type': 'application/json'
            }
        else:
            self.headers = headers
    
    # Common Request Methods
    # -----------------------------------------------------------------------------------------
    # get
    def cirrograph_get(self,url): 
        """
        CirroGraph restful API: GET
        """     
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    # post
    def cirrograph_post(self,url,data):   
        """
        CirroGraph restful API: POST
        """     
        return CirroGraphResponse(requests.post(url,data=json.dumps(data),headers=self.headers,auth=self.auth))

    # delete
    def cirrograph_delete(self,url):   
        """
        CirroGraph restful API: DELETE
        """    
        return CirroGraphResponse(requests.delete(url,headers=self.headers,auth=self.auth))

    # patch
    def cirrograph_patch(self,url,data): 
        """
        CirroGraph restful API: PATCH
        """     
        return CirroGraphResponse(requests.patch(url,data,headers=self.headers,auth=self.auth))

    # put
    def cirrograph_put(self,url,data):  
        """
        CirroGraph restful API: PUT
        """ 
        return CirroGraphResponse(requests.put(url,data,headers=self.headers,auth=self.auth))
    
    # CirroGraphClient API
    # ---------------------------------------------------------------------------------
    def get_graphs(self):
        """
        列出全部的图(图类似关系数据库中的数据库)
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs"

        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def get_version(self):
        """
        查看CirroGraph的版本信息
        :return: CirroGraphResponse
        """
        url = self.host + "/versions"

        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def get_graph(self):
        """
        查看当前连接的图信息
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph  

        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_schema(self):
        """
        查看当前图的schema信息
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_graph_config(self,graph):
        """
        查看某个图的配置,该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/conf"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_graph_mode(self,graph):
        """
        查看某个图的模式
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/mode"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def set_graph_mode(self,graph,modename):
        """
        设置某个图的模式. 该操作需要管理员权限 
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/mode"
        
        return CirroGraphResponse(requests.put(url,data=json.dumps(modename),headers=self.headers,auth=self.auth))

    def get_graph_read_mode(self,graph):
        """
        查看某个图的读模式
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/graph_read_mode"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def set_graph_read_mode(self,graph,modename):
        """
        设置某个图的读模式. 该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/graph_read_mode"
        
        return CirroGraphResponse(requests.put(url,data=json.dumps(modename),headers=self.headers,auth=self.auth))

    def graph_snapshot_create(self,graph):
        """
        创建快照
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/snapshot_create"
        
        return CirroGraphResponse(requests.put(url,headers=self.headers,auth=self.auth))

    #有bug
    def graph_snapshot_resume(self,graph):
        """
        快照恢复
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/snapshot_resume"
        
        return CirroGraphResponse(requests.put(url,headers=self.headers,auth=self.auth))

    def graph_compact(self,graph):
        """
        手动压缩图，该操作需要管理员权限 
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph +"/compact"
        
        return CirroGraphResponse(requests.put(url,headers=self.headers,auth=self.auth))

    # def clone_graph(self,new_graph,cloned_graph):
    #     """
    #     基于当前图进行图克隆。该操作需要管理员权限
    #     :param new_graph: 新克隆的图
    #     :param cloned_graph: 被克隆的图
    #     :return: CirroGraphResponse
    #     """
    #     url = self.host + "/graphs" + "/" + new_graph + "?clone_graph_name=" + \
    #           cloned_graph + "&token=" + self.token 
        
    #     return CirroGraphResponse(requests.post(url, headers=self.headers,auth=self.auth))

    def clear_graph(self,graph):
        """
        清空某个图的全部数据,包括schema、vertex、edge和索引等,该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph + "/clear?confirm_message=I%27m+sure+to+delete+all+data"
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def drop_graph(self,graph):
        """
        删除某个图,包含配置文件以及存储的全部数据,包括schema、vertex、edge和索引等,该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph + "/?confirm_message=I%27m%20sure%20to%20drop%20the%20graph"
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))
    
    def create_graph(self,graph):
        """
        创建一个图，该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs/"+ graph +"/create"
        return CirroGraphResponse(requests.post(url, headers=self.headers,auth=self.auth))

    def create_propertykey(self, propertykeys):
        """
        创建一个propertykey
        :param propertykeys: {}
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(propertykeys), headers=self.headers,auth=self.auth))

    def create_property_key(self, propertykey_name, dataType, cardinality):
        """
        创建一个propertykey
        :param property_name:
        :param dataType: INT TEXT
        :param cardinality:  SINGLE
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys"
        propertykeys = {
            "name": propertykey_name,
            "data_type": dataType,
            "cardinality": cardinality
        }
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(propertykeys), headers=self.headers,auth=self.auth))

    def add_propertykey_userdata(self, property_name, user_data):
        """
        为已存在的 PropertyKey 添加userdata
        :param property_name:
        :param user_data:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys" \
              + "/" + property_name + "?action=append"
        data = {
            "name": property_name,
            "user_data": user_data
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def delete_propertykey_userdata(self, property_name, user_data):
        """
        为已存在的 PropertyKey 移除 userdata
        :param property_name:
        :param user_data:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys" \
              + "/" + property_name + "?action=eliminate"
        data = {
            "name": property_name,
            "user_data": user_data
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def get_propertykeys(self):
        """
        获取所有的 PropertyKey
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys"
        
        return CirroGraphResponse(requests.get(url))

    def get_propertykey_name(self, property_name):
        """
        根据name获取PropertyKey
        :param property_name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/propertykeys" \
              + "/" + property_name
        
        return CirroGraphResponse(requests.get(url))

    def delete_propertykey_name(self, property_name):
        """
        根据name删除PropertyKey
        :param property_name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/schema/propertykeys" + "/" + property_name
        
        return CirroGraphResponse(requests.delete(url))

    def create_vertexlabel(self, data):
        """
        创建一个VertexLabel
        9 known properties for data:
            "check_exist", "primary_keys","nullable_keys",
            "properties","id_strategy", "id",
            "user_data", "name", "enable_label_index"
        :param data:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def add_vertexlabel_properties(self, name, properties, nullable=''):
        """
        为一个VertexLabel添加properties属性
        :param name:
        :param properties:
        :param nullable:give a list
        :return: CirroGraphResponse
        """
        if nullable == '':
            nullable = []
        url = self.host + "/graphs" + "/" + self.graph \
              + "/schema/vertexlabels" + "/" + name + "?action=append"
        data = {
            "name": name,
            "properties": properties,
            "nullable_keys": nullable
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def add_vertexlabel_userdata(self, name, userdata):
        """
        为一个VertexLabel添加userdata属性
        :param name:
        :param userdata:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" \
              + "/" + name + "?action=append"
        data = {
            "name": name,
            "user_data": userdata
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def delete_vertexlabel_userdata(self, name, userdata):
        """
        为一个VertexLabel删除userdata属性
        :param name:
        :param userdata:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" \
              + "/" + name + "?action=eliminate"
        data = {
            "name": name,
            "user_data": userdata
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def get_vertexlabels(self):
        """
        获取所有的VertexLabel
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_vertexlabel_name(self, name):
        """
        根据name获取VertexLabel
        :param name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_vertexlabel_name(self, name):
        """
        根据name删除VertexLabel
        :param name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/vertexlabels" + "/" + name
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def create_edgelabel(self, data):
        """
        创建一个EdgeLabel
        11 known properties for data:
                "source_label", "nullable_keys", "properties",
                "sort_keys", "target_label", "id",
                "frequency", "user_data", "check_exist",
                "name", "enable_label_index"
        :param data:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def add_edgelabel_properties(self, name, properties, nullable=''):
        """
        为一个EdgeLabel添加properties
        :param name:
        :param properties:
        :param nullable:give a list
        :return: CirroGraphResponse
        """
        if nullable == '':
            nullable = []
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" \
              + "/" + name + "?action=append"
        data = {
            "name": name,
            "properties": properties,
            "nullable_keys": nullable
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def add_edgelabel_userdata(self, name, userdata):
        """
        为一个EdgeLabel添加userdata
        :param name:
        :param userdata:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" \
              + "/" + name + "?action=append"
        data = {
            "name": name,
            "user_data": userdata
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def delete_edgelabel_userdata(self, name, userdata):
        """
        为一个EdgeLabel删除userdata
        :param name:
        :param userdata:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" \
              + "/" + name + "?action=eliminate"
        data = {
            "name": name,
            "user_data": userdata
        }
        
        return CirroGraphResponse(requests.put(url, headers=self.headers,auth=self.auth))

    def get_edgelabels(self):
        """
        获取所有的EdgeLabels
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_edgelabel_name(self, name):
        """
        根据name获取EdgeLabel
        :param name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" + "/" + name
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_edgelabel_name(self, name):
        """
        根据name删除EdgeLabel
        :param name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/edgelabels" + "/" + name
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def create_indexlabel(self, data):
        """
        创建一个IndexLabel
         7 known properties for data:
                "check_exist", "base_value", "index_type",
                "base_type", "fields", "id", "name"
        :param data:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def get_indexlabels(self):
        """
        获取所有的indexlabel
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_indexLabel_name(self, name):
        """
        根据name获取indexlabel
        :param name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels" + "/" + name
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_indexlabel_name(self, name):
        """
        根据name删除indexlabel
        :param name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/schema/indexlabels" + "/" + name
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def create_vertex(self, data):
        """
        创建一个顶点
        :param label:
        :param data:
                {
                    "label": label,
                    "properties": properties
                }
        :param properties:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def create_vertex_batch(self, data):
        """
        创建多个顶点
        :param data:
                    [
                        {
                            "label": "person",
                            "properties": {
                                "name": "marko",
                                "age": 29
                            }
                        },
                        {
                            "label": "software",
                            "properties": {
                                "name": "ripple",
                                "lang": "java",
                                "price": 199
                            }
                        }
                    ]
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" \
              + self.graph + "/graph/vertices/batch"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def update_vertex_properties(self, vertex_id, label, properties):
        """
        更新顶点属性
        :param vertex_id:
        :param label:
        :param properties:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/graph/vertices/" + vertex_id + "?action=append"
        data = {
            "label": label,
            "properties": properties
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    #批量更新顶点属性

    def delete_vertex_properties(self, vertex_id, label, properties):
        """
        删除顶点属性
        :param vertex_id:
        :param label:
        :param properties:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/graph/vertices/" + vertex_id + "?action=eliminate"
        data = {
            "label": label,
            "properties": properties
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def get_vertexs_condition(self, label="", properties='', limit=0):
        """
        获取符合条件的顶点
        :param label:
        :param properties:give a dict
        :param limit:
        :param page:
        :return: CirroGraphResponse
        """
        if properties == '':
            properties = {}
        # 以上参数都是可选的,如果提供page参数,必须提供limit参数,不允许带其他参数。"/graphs" + "/" + self.graph + "/graph/vertices?"
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices?"
        para = ""
        if label != "":
            para = para + "&label=" + label
        if properties != {}:
            para = para + "&properties=" + properties
        if limit > 0:
            para = para + "&limit=" + limit
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_vertex_page(self, limit, page=""):
        """
        获取符合条件的顶点 ,如果提供page参数,必须提供limit参数,不允许带其他参数
        :param page:
        :param limit:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices?"
        if page == "":
            if limit <= 0:
                res = CirroGraphResponse(400, "parameter:limit can not be empty ")
            else:
                url = url + "page&limit=" + str(limit)
        else:
            url = url + "page=" + str(page) + "&limit=" + str(limit)
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_vertex_id(self, vertex_id):
        """
        根据ID 获取顶点
        :param vertex_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices/\"" + vertex_id + "\""
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_vertex_id(self, vertex_id):
        """
        根据ID 删除顶点
        :param vertex_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices/" + str(vertex_id)
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def create_edge(self, data):
        """
         create an edge
        :param data: {
            outv:
            inv:
            outv_label:
            inv_label:
            properties:
        }
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def create_edge6(self, edge_label, outv, inv, outv_label, inv_label, properties):
        """
         create an edge
        :param edge_label:
        :param outv:
        :param inv:
        :param outv_label:
        :param inv_label:
        :param properties:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges"
        data = {
            "label": edge_label,
            "outV": outv,
            "inV": inv,
            "outVLabel": outv_label,
            "inVLabel": inv_label,
            "properties": properties
        }
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def create_edge_batch(self, data):
        """
        创建多条边
        :param data:
            [
                {
                    "label": "created",
                    "outV": "1:peter",
                    "inV": "2:lop",
                    "outVLabel": "person",
                    "inVLabel": "software",
                    "properties": {
                        "date": "2017-5-18",
                        "weight": 0.2
                    }
                },
                {
                    "label": "knows",
                    "outV": "1:marko",
                    "inV": "1:vadas",
                    "outVLabel": "person",
                    "inVLabel": "person",
                    "properties": {
                        "date": "2016-01-10",
                        "weight": 0.5
                    }
                }
            ]
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/batch"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def update_edge_properties(self, edge_id, properties):
        """
        更新边的属性
        :param properties:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/graph/edges/" + edge_id + "?action=append"
        data = {
            "properties": properties
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    #批量更新边属性

    def delete_edge_properties(self, edge_id, properties):
        """
        删除边的属性
        :param properties:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/graph/edges/" + edge_id + "?action=eliminate"
        data = {
            "properties": properties
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def get_edges_condition(self, vertex_id="", direction="", label="", properties='', limit=0):
        """
        根据条件查询获取边
        :param vertex_id: vertex_id为可选参数,如果提供参数vertex_id则必须同时提供参数direction。
        :param direction: (IN | OUT | BOTH)
        :param label:
        :param properties:give a dict
        :param limit:
        :return: CirroGraphResponse
        """
        if properties == '':
            properties = {}
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges?"
        para = ""
        if vertex_id != "":
            if direction != "":
                para = para + "&vertex_id=" + vertex_id + "&direction=" + direction
            else:
                return CirroGraphResponse(400, "direction can not be empty")
        if label != "":
            para = para + "&label=" + label
        if properties != {}:
            para = para + "&properties=" + properties
        if limit > 0:
            para = para + "&limit=" + limit
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_edges_page(self, limit, page=""):
        """
        获取符合条件的边 ,如果提供page参数,必须提供limit参数,不允许带其他参数
        :param limit:
        :param page:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges?"
        if page == "":
            if limit <= 0:
                res = CirroGraphResponse(400, "parameter:limit can not be empty ")
            else:
                url = url + "page&limit=" + str(limit)
        else:
            url = url + "page=" + str(page) + "&limit=" + str(limit)
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_edge_id(self, edge_id):
        """
        根据Id 获取边
        :param edge_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/" + edge_id
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_edge_id(self, edge_id):
        """
        根据Id 删除边
        :param edge_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges/" + edge_id
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def create_variables(self, key, value):
        """
        创建某个键值对
        :param key:
        :param value:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/" + key
        data = {
            "data": value
        }
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def update_variables(self, key, value):
        """
        更新某个键值对
        :param key:
        :param value:
        :return: CirroGraphResponse
        """
        return self.create_variables(key, value)

    def get_variables(self):
        """
        列出全部键值对
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/"
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_variable_key(self, key):
        """
        列出某个键值对
        :param key:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/" + key
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_variable_key(self, key):
        """
        删除某个键值对
        :param key:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/" + key
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def get_tasks(self, status="", limit=""):
        """
        列出某个图中全部的异步任务
        :param status: 异步任务的状态(success,failed)
        :param limit: 返回异步任务数目上限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks?"
        para = ''
        if status != '':
            para = f'{para}&status={status}' 
        if limit != "":
            para = f'{para}&limit={limit}'

        url += para[1:]
        print(url)

        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_task(self, task_id):
        """
        查看某个异步任务的信息
        :param task_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks/" + task_id
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_task(self, task_id):
        """
        删除某个异步任务信息,不删除异步任务本身
        :param task_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks/" + task_id
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))
    
    def cancel_task(self, task_id):
        """
        取消某个异步任务，该异步任务必须具有处理中断的能力 
        :param task_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks/" + task_id + '?action=cancel'
        
        return CirroGraphResponse(requests.put(url, headers=self.headers,auth=self.auth))

    def rebuild_indexlabel(self, indexlabel_name):
        """
        重建IndexLabel
        :param indexlabel_name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/jobs/rebuild/indexlabels/" + indexlabel_name
        
        return CirroGraphResponse(requests.put(url, headers=self.headers,auth=self.auth))

    def rebuild_vertexlabel(self, vertexlabel_name):
        """
        重建vertexlabel
        :param vertexlabel_name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/jobs/rebuild/vertexlabels/" + vertexlabel_name
        
        return CirroGraphResponse(requests.put(url, headers=self.headers,auth=self.auth))

    def rebuild_edgelabel(self, edgelabel_name):
        """
        重建edgelabel
        :param edgelabel_name:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph \
              + "/jobs/rebuild/edgelabels/" + edgelabel_name
        
        return CirroGraphResponse(requests.put(url, headers=self.headers,auth=self.auth))

    def execute_germlin_get(self, gremlin, bindings='', language="gremlin-groovy", aliases=""):
        """
        向CirroGraphServer发送gremlin语句(GET),同步执行
        :param gremlin: 要发送给CirroGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型,默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return: CirroGraphResponse
        """
        if bindings == '':
            bindings = {}
        url = self.host + "/gremlin?gremlin=" + gremlin
        if bindings != {}:
            url = url + "&bindings=" + bindings
        if language != "gremlin-groovy":
            url = url + "&language=" + language
        if aliases != "":
            url = url + "&aliases=" + aliases
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def execute_germlin_post(self, gremlin, bindings='', language="gremlin-groovy", aliases={}):
        """
        向CirroGraphServer发送gremlin语句(post),同步执行
        :param gremlin: 要发送给CirroGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型,默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return: CirroGraphResponse
        """
        if bindings == '':
            bindings = {}
        url = self.host + "/gremlin"

        return CirroGraphResponse(requests.post(url, data=json.dumps(gremlin), headers=self.headers,auth=self.auth))

    def execute_germlin_post_job(self, gremlin, bindings='', language="gremlin-groovy"):
        """
        向CirroGraphServer发送gremlin语句(post),异步执行
        异步执行Gremlin语句暂不支持aliases,可以使用 graph 代表要操作的图,也可以直接使用图的名字, 例如 CirroGraph; 另外g代表 traversal,等价于 graph.traversal() 或者 CirroGraph.traversal()
        :param gremlin: 要发送给CirroGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型,默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return: CirroGraphResponse
        """
        if bindings == '':
            bindings = {}
        url = self.host + "/graphs" + "/" + self.graph + "/jobs/gremlin"
        data = {
            "gremlin": gremlin,
            "bindings": bindings,
            "language": language,
            "aliases": {}
        }
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def execute_cypherql(self, cypherql):
        """
        向CirroGraphServer发送cypher语句(post)        
        :param data: { 要发送给CirroGraphServer执行的cypher语句 }
        data = {
            "cypher": "MATCH (v) return v"
        }
        :return: CirroGraphResponse
        """
        url = self.host + "/gremlin" + "/" + self.graph + "/cypher"
        data = {
            "cypher": cypherql
        }
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))
    
    def add_user(self, request):
        """
        创建用户   
        Params:
            user_name: 用户名称,必填
            user_password: 用户密码,必填
            user_phone: 用户手机号
            user_email: 用户邮箱
        request:
            {
                "user_name": "bowen",
                "user_password": "123456",
                "user_phone": "155****9088",
                "user_email": "123456@xx.com"
            }

        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/users"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def delete_user(self, userid):
        """
        删除用户   
        Params:
            id: 需要删除的用户Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/users/"+userid
        
        return CirroGraphResponse(requests.delete(url,headers=self.headers,auth=self.auth))

    def update_user(self,userid,request):
        """
        修改用户   
        Params:
            id: 需要修改的用户Id
        request:
            {
                "user_name": "bowen",
                "user_password": "12345678",
                "user_phone": "12345678,
                "user_email": "12345678@xx.com"
            }

        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/users/"+userid
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def get_users(self,limit=''):
        """
        查询用户列表   
        Params:
            id: 需要删除的用户Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/users"

        if limit != '':
            url += f'?limit={limit}'
        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def get_user(self,id):
        """
        查询用户列表   
        Params:
            id: 需要查询的用户Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/users/"+id        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def get_user_role(self,id):
        """
        查询某个用户的角色   
        Params:
            id: 需要查询的用户Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/users/"+id+'/role'        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))
    
    def add_group(self, request):
        """
        用户组会赋予相应的资源权限，用户会被分配不同的用户组，即可拥有不同的资源权限。
        用户组接口包括：创建用户组，删除用户组，修改用户组，和查询用户组相关信息接口。
        创建用户组
        Params:
            group_name: 用户组名称
            group_description: 用户组描述
        request:
            {
                "group_name": "all",
                "group_description": "group can do anything"
            }

        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/groups"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def delete_group(self, groupid):
        """
        删除用户组
        Params:
            id: 需要删除的用户组Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/groups/"+groupid
        
        return CirroGraphResponse(requests.delete(url,headers=self.headers,auth=self.auth))

    def update_group(self,groupid,request):
        """
        修改用户   
        Params:
            id: 需要修改的用户组Id
        request:
            {
                "group_name": "all",
                "group_description": "group can do anything,just like admin"
            }

        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/groups/"+groupid
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def get_groups(self,limit=''):
        """
        查询用户组列表   
        Params:
            limit: 返回结果条数的上限
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/groups"

        if limit != '':
            url += f'?limit={limit}'
        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def get_group(self,id):
        """
        查询某个用户组   
        Params:
            id: 需要查询的用户组Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/groups/"+id        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def add_target(self, request):
        """
        资源描述了图数据库中的数据，比如符合某一类条件的顶点，每一个资源包括type、label、properties三个要素，
        共有18种type、 任意label、任意properties的组合形成的资源，一个资源的内部条件是且关系，多个资源之间的条件是或关系。
        资源接口包括：资源的创建、删除、修改和查询。
        创建用户组
        Params:
            target_name: 资源名称
            target_graph: 资源图
            target_url: 资源地址
            target_resources: 资源定义(列表)
            target_resources可以包括多个target_resource，以列表的形式存储。
                每个target_resource包含：
                    type：可选值 VERTEX, EDGE等, 可填ALL，则表示可以是顶点或边；
                    label：可选值，⼀个顶点或边类型的名称，可填*，则表示任意类型；
                    properties：map类型，可包含多个属性的键值对，必须匹配所有属性值，属性值⽀持填条件范围（age: P.gte(18)），
                    properties如果为null表示任意属性均可，如果属性名和属性值均为‘*ʼ也表示任意属性均可。
                如精细资源：“target_resources”: [{“type”:“VERTEX”,“label”:“person”,“properties”:{“city”:“Beijing”,“age”:“P.gte(20)”}}]**
                资源定义含义：类型是’person’的顶点，且城市属性是’Beijing’，年龄属性大于等于20。
        request:
            {
            "target_name": "all",
            "target_graph": "cirrograph",
            "target_url": "139.9.132.125:5000",
            "target_resources": [
                {
                    "type": "ALL"
                }
                ]
            }
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/targets"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def delete_target(self, targetid):
        """
        删除资源
        Params:
            id: 需要删除的资源Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/targets/"+targetid
        
        return CirroGraphResponse(requests.delete(url,headers=self.headers,auth=self.auth))

    def update_target(self,targetid,request):
        """
        修改资源   
        Params:
            id: 需要修改的资源Id
        request:
            {
                "target_name": "all",
                "target_graph": "cirrograph",
                "target_url": "139.9.132.125:5000",
                "target_resources": [
                    {
                        "type": "NONE"
                    }
                ]
            }
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/targets/"+targetid
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def get_targets(self,limit=''):
        """
        查询资源列表   
        Params:
            limit: 返回结果条数的上限
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/targets"

        if limit != '':
            url += f'?limit={limit}'
        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def get_target(self,id):
        """
        查询某个资源   
        Params:
            id: 需要查询的资源Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/targets/"+id        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def add_belong(self, request):
        """
        关联用户和用户组的关系，一个用户可以关联一个或者多个用户组。
        用户组拥有相关资源的权限，不同用户组的资源权限可以理解为不同的角色。即给用户关联角色。
        关联角色接口包括：用户关联角色的创建、删除、修改和查询。
        创建用户的关联角色
        Params:
            user: 用户 Id
            group: 用户组 Id
            belong_description: 描述
        request:
            {
                "user": "-63:bowen",
                "group": "-69:all"
            }

        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/belongs"
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def delete_belong(self, belongid):
        """
        删除关联角色
        Params:
            id: 需要删除的关联角色Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/belongs/"+belongid
        
        return CirroGraphResponse(requests.delete(url,headers=self.headers,auth=self.auth))

    def update_belong(self,belongid,request):
        """
        关联角色只能修改描述，不能修改 user 和 group 属性，如果需要修改关联角色，需要删除原来关联关系，新增关联角色。
        Params:
            id: 需要修改的关联角色Id
        request:
            {
                "belong_description": "update test"
            }
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/belongs/"+belongid
        
        return CirroGraphResponse(requests.put(url, data=json.dumps(request), headers=self.headers,auth=self.auth))

    def get_targets(self,limit=''):
        """
        查询资源列表   
        Params:
            limit: 返回结果条数的上限
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/targets"

        if limit != '':
            url += f'?limit={limit}'
        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))

    def get_target(self,id):
        """
        查询某个资源   
        Params:
            id: 需要查询的资源Id
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/auth/targets/"+id        
        return CirroGraphResponse(requests.get(url,headers=self.headers,auth=self.auth))


class CirroGraphTraverser():
    """
    CirroGraph Traverser API
    """

    def __init__(self,host,graph,headers={},auth=()):
        #auth = ('admin','2022131@CirroGraph')
        self.host = host
        self.graph = graph
        self.auth = auth
        
        if headers=={}:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Content-Type': 'application/json'
            }
        else:
            self.headers = headers
    
    def kout_get(self, source,max_depth,direction="",label="",nearest="",max_degree="",capacity="",limit=""):
        """
        根据起始顶点、方向、边的类型(可选)和深度depth,查找从起始顶点出发恰好depth步可达的顶点
        Params:
            source:起始顶点id,必填项
            direction:起始顶点向外发散的方向(OUT,IN,BOTH),选填项,默认是BOTH
            max_depth:步数,必填项
            label:边的类型,选填项,默认代表所有edge label
            nearest:nearest为true时,代表起始顶点到达结果顶点的最短路径长度为depth,不存在更短的路径;nearest为false时,代表起始顶点到结果顶点有一条长度为depth的路径(未必最短且可以有环),选填项,默认为true
            max_degree:查询过程中,单个顶点遍历的最大邻接边数目,选填项,默认为10000
            capacity:遍历过程中最大的访问的顶点数目,选填项,默认为10000000
            limit:返回的顶点的最大数目,选填项,默认为10000000
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kout?"
        para = ""
        if type(source) is int:
                para = f'{para}&source={source}'
        else:
            if source.isnumeric():
                para = f'{para}&source={source}'
            else:
                para = f'{para}&source="{source}"'
        if max_depth != "":
            para = para + "&max_depth=" + str(max_depth)
        if direction != "":
            para = para + "&direction=" + direction
        if label != "":
            para = para + "&label=" + label
        if nearest != "":
            para = para + "&nearest=" + nearest
        if max_degree != "":
            para = para + "&max_degree=" + max_degree
        if capacity != "":
            para = para + "&capacity=" + capacity
        if limit != "":
            para = para + "&limit=" + limit    

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def kout_post(self,request):
        '''
        根据起始顶点、步骤（包括方向、边类型和过滤属性）和深度depth，查找从起始顶点出发恰好depth步可达的顶点。
        Params:
            source：起始顶点id，必填项
            从起始点出发的Step，必填项，结构如下：
                direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                labels：边的类型列表
                properties：通过属性的值过滤边
                max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            max_depth：步数，必填项
            nearest：nearest为true时，代表起始顶点到达结果顶点的最短路径长度为depth，不存在更短的路径；nearest为false时，代表起始顶点到结果顶点有一条长度为depth的路径（未必最短且可以有环），选填项，默认为true
            count_only：Boolean值，true表示只统计结果的数目，不返回具体结果；false表示返回具体的结果，默认为false
            with_path：true表示返回起始点到每个邻居的最短路径，false表示不返回起始点到每个邻居的最短路径，选填项，默认为false
            with_vertex，选填项，默认为false：
                true表示返回结果包含完整的顶点信息（路径中的全部顶点）
                    with_path为true时，返回所有路径中的顶点的完整信息
                    with_path为false时，返回所有邻居的完整信息
                false时表示只返回顶点id
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的顶点的最大数目，选填项，默认为10000000
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
            "max_depth": 1,
            "nearest": True,
            "limit": 10000,
            "with_vertex": True,
            "with_path": True
        }
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kout"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))

    def kneighbor_get(self, source, max_depth, direction="",label="",max_degree="",limit=""):
        """
        根据起始顶点、方向、边的类型(可选)和深度depth,查找包括起始顶点在内、depth步之内可达的所有顶点
        Params:
            source: 起始顶点id，必填项
            direction：起始顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            max_depth：步数，必填项
            label：边的类型，选填项，默认代表所有edge label
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            limit：返回的顶点的最大数目，也即遍历过程中最大的访问的顶点数目，选填项，默认为10000000
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kneighbor?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_depth != "":
            para = f'{para}&max_depth={max_depth}'
        if label != "":
            para = f'{para}&label={label}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if limit != "":
            para = f'{para}&limit={limit}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))    

    def kneighbor_post(self,request):
        '''
        根据起始顶点、步骤（包括方向、边类型和过滤属性）和深度depth，查找从起始顶点出发depth步内可达的所有顶点。
        Params:
            source：起始顶点id，必填项
            从起始点出发的Step，必填项，结构如下：
                direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                labels：边的类型列表
                properties：通过属性的值过滤边
                max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            max_depth：步数，必填项
            count_only：Boolean值，true表示只统计结果的数目，不返回具体结果；false表示返回具体的结果，默认为false
            with_path：true表示返回起始点到每个邻居的最短路径，false表示不返回起始点到每个邻居的最短路径，选填项，默认为false
            with_vertex，选填项，默认为false：
                true表示返回结果包含完整的顶点信息（路径中的全部顶点）
                    with_path为true时，返回所有路径中的顶点的完整信息
                    with_path为false时，返回所有邻居的完整信息
                false时表示只返回顶点id
            limit：返回的顶点的最大数目，选填项，默认为10000000
        request:{
            "source": "1:marko",
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
            "with_vertex": true,
            "with_path": true
        }
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kneighbor"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))

    def sameneighbors(self,vertex,other,direction="",label="",max_degree="",limit=""):
        '''
        查询两个点的共同邻居
        Params:
            vertex：一个顶点id，必填项
            other：另一个顶点id，必填项
            direction：顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            limit：返回的共同邻居的最大数目，选填项，默认为10000000
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/sameneighbors?"
        para = ""
        if type(vertex) is int:
            para = f'{para}&vertex={vertex}'
        else:
            para = f'{para}&vertex="{vertex}"'
        if type(other) is int:
            para = f'{para}&other={other}'
        else:
            para = f'{para}&other="{other}"'
        if direction != "":
            para = para + "&direction=" + direction
        if label != "":
            para = para + "&label=" + label
        if max_degree != "":
            para = para + "&max_degree=" + max_degree
        if limit != "":
            para = para + "&limit=" + limit    

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    
    def jaccardsimilarity_get(self,vertex,other,direction="",label="",max_degree="",limit=""):
        '''
        计算两个顶点的jaccard similarity（两个顶点邻居的交集比上两个顶点邻居的并集）
        Params:
            vertex：一个顶点id，必填项
            other：另一个顶点id，必填项
            direction：顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/jaccardsimilarity?"
        para = ""
        if type(vertex) is int:
            para = f'{para}&vertex={vertex}'
        else:
            para = f'{para}&vertex="{vertex}"'
        if type(other) is int:
            para = f'{para}&other={other}'
        else:
            para = f'{para}&other="{other}"'
        if direction != "":
            para = f'{para}&direction="{direction}"'
        if label != "":
            para = f'{para}&label="{label}"'
        if max_degree != "":
            para = f'{para}&max_degree="{max_degree}"'
        if limit != "":
            para = f'{para}&limit="{limit}"'
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    
    def jaccardsimilarity_post(self,request):
        '''
        计算与指定顶点的jaccard similarity最大的N个点
        jaccard similarity的计算方式为：两个顶点邻居的交集比上两个顶点邻居的并集
        Params:
            vertex：一个顶点id，必填项
            从起始点出发的Step，必填项，结构如下：
                direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                labels：边的类型列表
                properties：通过属性的值过滤边
                max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            top：返回一个起点的jaccard similarity中最大的top个，选填项，默认为100
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/jaccardsimilarity"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))
    
    def shortestpath(self, source, target,max_depth,direction="",label="",max_degree="",skip_degree="",capacity=""):
        """
        根据起始顶点、目的顶点、方向、边的类型(可选)和最大深度,查找一条最短路径
        Params:
            source：起始顶点id，必填项
            target：目的顶点id，必填项
            direction：起始顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            max_depth：最大步数，必填项
            label：边的类型，选填项，默认代表所有edge label
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/shortestpath?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if type(target) is int:
            para = f'{para}&target={target}'
        else:
            para = f'{para}&target="{target}"'
        if max_depth != "":
            para = f'{para}&max_depth={max_depth}'
        if label != "":
            para = f'{para}&label={label}'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if skip_degree != "":
            para = f'{para}&skip_degree={skip_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    
    def allshortestpaths(self, source, target,max_depth,direction="",label="",max_degree="",skip_degree="",capacity=""):
        """
        根据起始顶点、目的顶点、方向、边的类型（可选）和最大深度，查找两点间所有的最短路径
        Params:
            source：起始顶点id，必填项
            target：目的顶点id，必填项
            direction：起始顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            max_depth：最大步数，必填项
            label：边的类型，选填项，默认代表所有edge label
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/allshortestpaths?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if type(target) is int:
            para = f'{para}&target={target}'
        else:
            para = f'{para}&target="{target}"'
        if max_depth != "":
            para = f'{para}&max_depth={max_depth}'
        if label != "":
            para = f'{para}&label={label}'
        if direction != "":
            para = f'{para}&direction={direction}' 
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if skip_degree != "":
            para = f'{para}&skip_degree={skip_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    
    def weightedshortestpath(self, source, target,weight,direction="",label="",max_degree="",skip_degree="",capacity="",with_vertex=""):
        """
        根据起始顶点、目的顶点、方向、边的类型（可选）和最大深度，查找一条带权最短路径
        Params:
            source：起始顶点id，必填项
            target：目的顶点id，必填项
            direction：起始顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            weight：边的权重属性，必填项，必须是数字类型的属性
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            with_vertex：true表示返回结果包含完整的顶点信息（路径中的全部顶点），false时表示只返回顶点id，选填项，默认为false
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/weightedshortestpath?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if type(target) is int:
            para = f'{para}&target={target}'
        else:
            para = f'{para}&target="{target}"'
        if weight != "":
            para = f'{para}&weight={weight}'
        if label != "":
            para = f'{para}&label={label}'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if skip_degree != "":
            para = f'{para}&skip_degree={skip_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'
        if with_vertex != "":
            para = f'{para}&with_vertex={with_vertex}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def singlesourceshortestpath(self, source,weight="",direction="",label="",max_degree="",skip_degree="",capacity="",limit="",with_vertex=""):
        """
        从一个顶点出发，查找该点到图中其他顶点的最短路径（可选是否带权重）
        Params：
            source：起始顶点id，必填项
            direction：起始顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            weight：边的权重属性，选填项，必须是数字类型的属性，如果不填或者虽然填了但是边没有该属性，则权重为1.0
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：查询到的目标顶点个数，也是返回的最短路径的条数，选填项，默认为10
            with_vertex：true表示返回结果包含完整的顶点信息（路径中的全部顶点），false时表示只返回顶点id，选填项，默认为false
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/singlesourceshortestpath?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if weight != "":
            para = f'{para}&weight={weight}'
        if label != "":
            para = f'{para}&label={label}'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if skip_degree != "":
            para = f'{para}&skip_degree={skip_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'
        if limit != "":
            para = f'{para}&limit={limit}'
        if with_vertex != "":
            para = f'{para}&with_vertex={with_vertex}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def multinodeshortestpath(self,request):
        '''
        查找指定顶点集两两之间的最短路径
        Params:
            vertices：定义起始顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供起始顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询起始顶点
                    label：顶点的类型
                    properties：通过属性的值查询起始顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            step：表示从起始顶点到终止顶点走过的路径，必填项，Step的结构如下：
                direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                labels：边的类型列表
                properties：通过属性的值过滤边
                max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            max_depth：步数，必填项
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            with_vertex：true表示返回结果包含完整的顶点信息（路径中的全部顶点），false时表示只返回顶点id，选填项，默认为false
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/multinodeshortestpath"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))
    
    def paths_get(self, source, target,max_depth,direction="",label="",max_degree="",capacity="",limit=""):
        """
        根据起始顶点、目的顶点、方向、边的类型（可选）和最大深度等条件查找所有路径
        Params:
            source：起始顶点id，必填项
            target：目的顶点id，必填项
            direction：起始顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            max_depth：步数，必填项
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的路径的最大数目，选填项，默认为10
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/paths?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if type(target) is int:
            para = f'{para}&target={target}'
        else:
            para = f'{para}&target="{target}"'
        if max_depth != "":
            para = f'{para}&max_depth={max_depth}'
        if label != "":
            para = f'{para}&label={label}'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'
        if limit != "":
            para = f'{para}&limit={limit}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def paths_post(self,request):
        '''
        根据起始顶点、目的顶点、步骤（step）和最大深度等条件查找所有路径
        Params:
            sources：定义起始顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供起始顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询起始顶点
                    label：顶点的类型
                    properties：通过属性的值查询起始顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            targets：定义终止顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供终止顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询终止顶点
                    label：顶点的类型
                    properties：通过属性的值查询终止顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            step：表示从起始顶点到终止顶点走过的路径，必填项，Step的结构如下：
                direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                labels：边的类型列表
                properties：通过属性的值过滤边
                max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            max_depth：步数，必填项
            nearest：nearest为true时，代表起始顶点到达结果顶点的最短路径长度为depth，不存在更短的路径；nearest为false时，代表起始顶点到结果顶点有一条长度为depth的路径（未必最短且可以有环），选填项，默认为true
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的路径的最大数目，选填项，默认为10
            with_vertex：true表示返回结果包含完整的顶点信息（路径中的全部顶点），false时表示只返回顶点id，选填项，默认为false
        request:{
            "sources": {
            "ids": ["1:marko"]
            },
            "targets": {
            "ids": ["1:peter"]
            },
            "step": {
            "direction": "BOTH",
            "properties": {
                "weight": "P.gt(0.01)"
            }
            },
            "max_depth": 10,
            "capacity": 100000000,
            "limit": 10000000,
            "with_vertex": false
        }
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/paths"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))
    
    def customizedpaths(self,request):
        '''
        根据一批起始顶点、边规则（包括方向、边的类型和属性过滤）和最大深度等条件查找符合条件的所有的路径
        Params：
            sources：定义起始顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供起始顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询起始顶点
                    label：顶点的类型
                    properties：通过属性的值查询起始顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            steps：表示从起始顶点走过的路径规则，是一组Step的列表。必填项。每个Step的结构如下：
                direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                labels：边的类型列表
                properties：通过属性的值过滤边
                weight_by：根据指定的属性计算边的权重，sort_by不为NONE时有效，与default_weight互斥
                default_weight：当边没有属性作为权重计算值时，采取的默认权重，sort_by不为NONE时有效，与weight_by互斥
                max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                sample：当需要对某个step的符合条件的边进行采样时设置，-1表示不采样，默认为采样100
            sort_by：根据路径的权重排序，选填项，默认为NONE：
                NONE表示不排序，默认值
                INCR表示按照路径权重的升序排序
                DECR表示按照路径权重的降序排序
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的路径的最大数目，选填项，默认为10
            with_vertex：true表示返回结果包含完整的顶点信息（路径中的全部顶点），false时表示只返回顶点id，选填项，默认为false
        request:{
            "sources":{
                "ids":[

                ],
                "label":"person",
                "properties":{
                    "name":"marko"
                }
            },
            "steps":[
                {
                    "direction":"OUT",
                    "labels":[
                        "knows"
                    ],
                    "weight_by":"weight",
                    "max_degree":-1
                },
                {
                    "direction":"OUT",
                    "labels":[
                        "created"
                    ],
                    "default_weight":8,
                    "max_degree":-1,
                    "sample":1
                }
            ],
            "sort_by":"INCR",
            "with_vertex":true,
            "capacity":-1,
            "limit":-1
        }
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/customizedpaths"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))

    def templatepaths(self,request):
        '''
        根据一批起始顶点、边规则（包括方向、边的类型和属性过滤）和最大深度等条件查找符合条件的所有的路径
        Params:
            sources：定义起始顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供起始顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询起始顶点
                    label：顶点的类型
                    properties：通过属性的值查询起始顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            targets：定义终止顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供终止顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询终止顶点
                    label：顶点的类型
                    properties：通过属性的值查询终止顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            steps：表示从起始顶点走过的路径规则，是一组Step的列表。必填项。每个Step的结构如下：
                direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                labels：边的类型列表
                properties：通过属性的值过滤边
                max_times：当前step可以重复的次数，当为N时，表示从起始顶点可以经过当前step 1-N 次
                max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)
            with_ring：Boolean值，true表示包含环路；false表示不包含环路，默认为false
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的路径的最大数目，选填项，默认为10
            with_vertex：true表示返回结果包含完整的顶点信息（路径中的全部顶点），false时表示只返回顶点id，选填项，默认为false
        request:{
            "sources": {
                    "ids": [],
                    "label": "person",
                    "properties": {
                        "name": "vadas"
                    }
                    },
                    "targets": {
                    "ids": [],
                    "label": "software",
                    "properties": {
                        "name": "ripple"
                    }
                    },
                    "steps": [
                    {
                        "direction": "IN",
                        "labels": ["knows"],
                        "properties": {
                        },
                        "max_degree": 10000,
                        "skip_degree": 100000
                    },
                    {
                        "direction": "OUT",
                        "labels": ["created"],
                        "properties": {
                        },
                        "max_degree": 10000,
                        "skip_degree": 100000
                    },
                    {
                        "direction": "IN",
                        "labels": ["created"],
                        "properties": {
                        },
                        "max_degree": 10000,
                        "skip_degree": 100000
                    },
                    {
                        "direction": "OUT",
                        "labels": ["created"],
                        "properties": {
                        },
                        "max_degree": 10000,
                        "skip_degree": 100000
                    }
                    ],
                    "capacity": 10000,
                    "limit": 10,
                    "with_vertex": true
                }
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/templatepaths"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))

    def crosspoints(self, source, target,max_depth,direction="",label="",max_degree="",capacity="",limit=""):
        """
        根据起始顶点、目的顶点、方向、边的类型（可选）和最大深度等条件查找相交点
        Params:
            source：起始顶点id，必填项
            target：目的顶点id，必填项
            direction：起始顶点到目的顶点的方向, 目的点到起始点是反方向，BOTH时不考虑方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            max_depth：步数，必填项
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的交点的最大数目，选填项，默认为10
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/crosspoints?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if type(target) is int:
            para = f'{para}&target={target}'
        else:
            para = f'{para}&target="{target}"'
        if max_depth != "":
            para = f'{para}&max_depth={max_depth}'
        if label != "":
            para = f'{para}&label={label}'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'
        if limit != "":
            para = f'{para}&limit={limit}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def customizedcrosspoints(self,request):
        '''
        根据一批起始顶点、多种边规则（包括方向、边的类型和属性过滤）和最大深度等条件查找符合条件的所有的路径终点的交集
        Params:
            sources：定义起始顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供起始顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询起始顶点
                    label：顶点的类型
                    properties：通过属性的值查询起始顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            path_patterns：表示从起始顶点走过的路径规则，是一组规则的列表。必填项。每个规则是一个PathPattern
                每个PathPattern是一组Step列表，每个Step结构如下：
                    direction：表示边的方向（OUT,IN,BOTH），默认是BOTH
                    labels：边的类型列表
                    properties：通过属性的值过滤边
                    max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                    skip_degree：用于设置查询过程中舍弃超级顶点的最小边数，即当某个顶点的邻接边数目大于 skip_degree 时，完全舍弃该顶点。选填项，如果开启时，需满足 skip_degree >= max_degree 约束，默认为0 (不启用)，表示不跳过任何点 (注意: 开启此配置后，遍历时会尝试访问一个顶点的 skip_degree 条边，而不仅仅是 max_degree 条边，这样有额外的遍历开销，对查询性能影响可能有较大影响，请确认理解后再开启)

            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000

            limit：返回的路径的最大数目，选填项，默认为10

            with_path：true表示返回交点所在的路径，false表示不返回交点所在的路径，选填项，默认为false

            with_vertex，选填项，默认为false：
                true表示返回结果包含完整的顶点信息（路径中的全部顶点）
                    with_path为true时，返回所有路径中的顶点的完整信息
                    with_path为false时，返回所有交点的完整信息
                false时表示只返回顶点id
        request:{
            "sources":{
                "ids":[
                    "2:lop",
                    "2:ripple"
                ]
            },
            "path_patterns":[
                {
                    "steps":[
                        {
                            "direction":"IN",
                            "labels":[
                                "created"
                            ],
                            "max_degree":-1
                        }
                    ]
                }
            ],
            "with_path":true,
            "with_vertex":true,
            "capacity":-1,
            "limit":-1
        }

        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/customizedcrosspoints"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))
    
    def rings(self, source,max_depth,direction="",label="",source_in_ring="",max_degree="",capacity="",limit=""):
        """
        根据起始顶点、方向、边的类型（可选）和最大深度等条件查找可达的环路
        Params:
            source：起始顶点id，必填项
            direction：起始顶点发出的边的方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            max_depth：步数，必填项
            source_in_ring：环路是否包含起点，选填项，默认为true
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的可达环路的最大数目，选填项，默认为10  
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/rings?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if max_depth != "":
            para = f'{para}&max_depth={max_depth}'
        if label != "":
            para = f'{para}&label={label}'
        if source_in_ring != "":
            para = f'{para}&source_in_ring={source_in_ring}'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'
        if limit != "":
            para = f'{para}&limit={limit}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    
    def rays(self, source,max_depth,direction="",label="",max_degree="",capacity="",limit=""):
        """
        根据起始顶点、方向、边的类型（可选）和最大深度等条件查找发散到边界顶点的路径
        Params:
            source：起始顶点id，必填项
            direction：起始顶点发出的边的方向（OUT,IN,BOTH），选填项，默认是BOTH
            label：边的类型，选填项，默认代表所有edge label
            max_depth：步数，必填项
            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000
            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            limit：返回的非环路的最大数目，选填项，默认为10
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/rays?"
        para = ""
        if type(source) is int:
            para = f'{para}&source={source}'
        else:
            para = f'{para}&source="{source}"'
        if max_depth != "":
            para = f'{para}&max_depth={max_depth}'
        if label != "":
            para = f'{para}&label={label}'
        if direction != "":
            para = f'{para}&direction={direction}'
        if max_degree != "":
            para = f'{para}&max_degree={max_degree}'
        if capacity != "":
            para = f'{para}&capacity={capacity}'
        if limit != "":
            para = f'{para}&limit={limit}'

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def fusiformsimilarity(self,request):
        '''
        按照条件查询一批顶点对应的"梭形相似点"。当两个顶点跟很多共同的顶点之间有某种关系的时候，我们认为这两个点为"梭形相似点"。
        举个例子说明"梭形相似点"：“读者A"读了100本书，可以定义读过这100本书中的80本以上的读者，是"读者A"的"梭形相似点”
        Params:
            sources：定义起始顶点，必填项，指定方式包括：
                ids：通过顶点id列表提供起始顶点
                label和properties：如果没有指定ids，则使用label和properties的联合条件查询起始顶点
                    label：顶点的类型
                    properties：通过属性的值查询起始顶点

                    注意：properties中的属性值可以是列表，表示只要key对应的value在列表中就可以

            label：边的类型，选填项，默认代表所有edge label

            direction：起始顶点向外发散的方向（OUT,IN,BOTH），选填项，默认是BOTH

            min_neighbors：最少邻居数目，邻居数目少于这个阈值时，认为起点不具备"梭形相似点"。比如想要找一个"读者A"读过的书的"梭形相似点"，那么min_neighbors为100时，表示"读者A"至少要读过100本书才可以有"梭形相似点"，必填项

            alpha：相似度，代表：起点与"梭形相似点"的共同邻居数目占起点的全部邻居数目的比例，必填项

            min_similars：“梭形相似点"的最少个数，只有当起点的"梭形相似点"数目大于或等于该值时，才会返回起点及其"梭形相似点”，选填项，默认值为1

            top：返回一个起点的"梭形相似点"中相似度最高的top个，必填项，0表示全部

            group_property：与min_groups一起使用，当起点跟其所有的"梭形相似点"某个属性的值有至少min_groups个不同值时，才会返回该起点及其"梭形相似点"。比如为"读者A"推荐"异地"书友时，需要设置group_property为读者的"城市"属性，min_group至少为2，选填项，不填代表不需要根据属性过滤

            min_groups：与group_property一起使用，只有group_property设置时才有意义

            max_degree：查询过程中，单个顶点遍历的最大邻接边数目，选填项，默认为10000

            capacity：遍历过程中最大的访问的顶点数目，选填项，默认为10000000

            limit：返回的结果数目上限（一个起点及其"梭形相似点"算一个结果），选填项，默认为10

            with_intermediary：是否返回起点及其"梭形相似点"共同关联的中间点，默认为false

            with_vertex，选填项，默认为false：
                true表示返回结果包含完整的顶点信息
                false时表示只返回顶点id
        request = {
            "sources":{
            "ids":[],
            "label": "person",
            "properties": {
                "name":"marko"
            }
            },
            "label":"created",
            "direction":"OUT",
            "min_neighbors":2,
            "alpha":0.75,
            "min_similars":1,
            "top":0,
            "group_property":"city",
            "min_groups":2,
            "max_degree": 10000,
            "capacity": -1,
            "limit": -1,
            "with_intermediary": False,
            "with_vertex":False
        }
        return: CirroGraphResponse
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/fusiformsimilarity"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))
    
    def verticesByIds(self,vertexIds):
        """
        根据顶点的id列表，批量查询顶点 s
        Params:
            ids：要查询的顶点id列表
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/vertices?"
        para = ''
        for id in vertexIds:
            if type(id) is int:
                para = f'{para}&ids={id}'
            else:
                para = f'{para}&ids="{id}"'
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def verticesShard(self,split_size):
        """
        通过指定的分片大小split_size，获取顶点分片信息
        Params:
            split_size：分片大小，必填项
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/vertices/shards?"
        para = f'&split_size={split_size}'
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def verticesByShard(self,start,end,page="",page_limit=""):
        """
        通过指定的分片信息批量查询顶点
        Params:
            start：分片起始位置，必填项
            end：分片结束位置，必填项
            page：分页位置，选填项，默认为null，不分页；当page为“”时表示分页的第一页，从start指示的位置开始
            page_limit：分页获取顶点时，一页中顶点数目的上限，选填项，默认为100000
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/vertices/scan?"
        para = ''
        if start != '':
            para = f'{para}&start={start}'
        if end != '':
            para = f'{para}&end={end}'
        if page != '':
            para = f'{para}&page={page}'
        if page_limit != '':
            para = f'{para}&page_limit={page_limit}'
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    
    def edgesByIds(self,edgesIds):
        """
        根据边的id列表，批量查询边
        Params:
            ids：要查询的边id列表
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/edges?"
        para = ''
        for id in edgesIds:
            para = f'{para}&ids={id}'
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def edgesShard(self,split_size):
        """
        通过指定的分片大小split_size，获取边分片信息
        Params:
            split_size：分片大小，必填项
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/edges/shards?"
        if split_size != '':
            para = f'&split_size={split_size}'
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def edgesByShard(self,start,end,page="",page_limit=""):
        """
        通过指定的分片信息批量查询边
        Params:
            start：分片起始位置，必填项
            end：分片结束位置，必填项
            page：分页位置，选填项，默认为null，不分页；当page为“”时表示分页的第一页，从start指示的位置开始
            page_limit：分页获取边时，一页中边数目的上限，选填项，默认为100000
        return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/edges/scan?"
        para = ''
        if start != '':
            para = f'{para}&start={start}'
        if end != '':
            para = f'{para}&end={end}'
        if page != '':
            para = f'{para}&page={page}'
        if page_limit != '':
            para = f'{para}&page_limit={page_limit}'
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    
    def personalrank(self,request):
        """
            Personal Rank 算法典型场景是用于推荐应用中, 根据某个点现有的出边, 推荐具有相近 / 相同关系的其他点
            Params:
                必填项:

                    source: 源顶点 id
                    label: 源点出发的某类边 label，须连接两类不同顶点
                选填项:
                    alpha：每轮迭代时从某个点往外走的概率，与 PageRank 算法中的 alpha 类似，取值区间为 (0, 1], 默认值 0.85
                    max_degree: 查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000
                    max_depth: 迭代次数，取值区间为 [2, 50], 默认值 5
                    with_label：筛选结果中保留哪些结果，可选以下三类, 默认为 BOTH_LABEL
                        SAME_LABEL：仅保留与源顶点相同类别的顶点
                        OTHER_LABEL：仅保留与源顶点不同类别（二分图的另一端）的顶点
                        BOTH_LABEL：同时保留与源顶点相同和相反类别的顶点
                    limit: 返回的顶点的最大数目，默认为 100
                    max_diff: 提前收敛的精度差, 默认为 0.0001 (后续实现)
                    sorted：返回的结果是否根据 rank 排序，为 true 时降序排列，反之不排序，默认为 true
            return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/personalrank"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))
    
    def neighborrank(self,request):
        """
            在一般图结构中，找出每一层与给定起点相关性最高的前 N 个顶点及其相关度，用图的语义理解就是：从起点往外走， 走到各层各个顶点的概率。
            Params:
                source: 源顶点 id，必填项
                alpha：每轮迭代时从某个点往外走的概率，与 PageRank 算法中的 alpha 类似，必填项，取值区间为 (0, 1]
                steps: 表示从起始顶点走过的路径规则，是一组 Step 的列表，每个 Step 对应结果中的一层，必填项。每个 Step 的结构如下：
                    direction：表示边的方向（OUT, IN, BOTH），默认是 BOTH
                    labels：边的类型列表，多个边类型取并集
                    max_degree：查询过程中，单个顶点遍历的最大邻接边数目，默认为 10000 (注: 0.12版之前 step 内仅支持 degree 作为参数名, 0.12开始统一使用 max_degree, 并向下兼容 degree 写法)
                    top：在结果中每一层只保留权重最高的前 N 个结果，默认为 100，最大值为 1000
                capacity: 遍历过程中最大的访问的顶点数目，选填项，默认为10000000
            request:{
                "source":1,
                "steps":[
                    {
                        "direction":"OUT",
                        "labels":[
                            "knows"
                        ],
                        "max_degree":-1,
                        "top":100
                    },
                    {
                        "direction":"OUT",
                        "labels":[
                            "created",
                        ],
                        "max_degree":-1,
                        "top":100
                    },
                    {
                        "direction":"OUT",
                        "labels":[
                            "stredge"
                        ],
                        "max_degree":-1,
                        "top":100
                    }
                ],
                "alpha":0.9,
                "capacity":-1
            }
            return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/neighborrank"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))

if __name__=="__main__":
    pass