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
        self.response = response.text

# CirroGraphClient Class
class CirroGraphClient(object):
    """
    CirroGraph Client API
    """

    def __init__(self,host,graph,headers={},auth=()):
        
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
        列出全部的图（图类似关系数据库中的数据库）
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

    def get_graph_config(self):
        """
        查看某个图的配置，该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "conf?token=" + self.token
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def clone_graph(self,new_graph,cloned_graph):
        """
        基于当前图进行图克隆。该操作需要管理员权限
        :param new_graph: 新克隆的图
        :param cloned_graph: 被克隆的图
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + new_graph + "?clone_graph_name=" + \
              cloned_graph + "&token=" + self.token 
        
        return CirroGraphResponse(requests.post(url, headers=self.headers,auth=self.auth))

    def clear_graph(self,graph):
        """
        清空某个图的全部数据，包括schema、vertex、edge和索引等，该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph + "/clear?token=" + \
              self.token + "&confirm_message=I%27m+sure+to+delete+all+data"
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

    def drop_graph(self,graph):
        """
        删除某个图，包含配置文件以及存储的全部数据，包括schema、vertex、edge和索引等，该操作需要管理员权限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + graph + "/?token=" + \
              self.token + "&confirm_message=I%27m%20sure%20to%20drop%20the%20graph"
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

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
        # 以上参数都是可选的，如果提供page参数，必须提供limit参数，不允许带其他参数。"/graphs" + "/" + self.graph + "/graph/vertices?"
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
        获取符合条件的顶点 ，如果提供page参数，必须提供limit参数，不允许带其他参数
        :param page:
        :param limit:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/vertices?"
        if page == "":
            if limit <= 0:
                res = CirroGraphResponse(400, "parameter：limit can not be empty ")
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
        :param vertex_id: vertex_id为可选参数，如果提供参数vertex_id则必须同时提供参数direction。
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
        获取符合条件的边 ，如果提供page参数，必须提供limit参数，不允许带其他参数
        :param limit:
        :param page:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/graph/edges?"
        if page == "":
            if limit <= 0:
                res = CirroGraphResponse(400, "parameter：limit can not be empty ")
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

    def traverser_shortest_path(self, source, target, direction, max_depth, label=""):
        """
        根据起始顶点、目的顶点、方向、边的类型（可选）和最大深度，查找一条最短路径
        :param source:
        :param target:
        :param direction: (IN | OUT | BOTH)
        :param max_depth:
        :param label:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/shortestpath?"
        para = ""
        if source == "":
            return CirroGraphResponse(400, "source can not be empty")
        else:
            para = para + "&source=\"" + source + "\""
        if target == "":
            return CirroGraphResponse(400, "target can not be empty")
        else:
            para = para + "&target=\"" + target + "\""
        if direction == "":
            return CirroGraphResponse(400, "direction can not be empty")
        else:
            para = para + "&direction=" + direction
        if max_depth == "":
            return CirroGraphResponse(400, "max_depth can not be empty")
        else:
            para = para + "&max_depth=" + str(max_depth)
        if label != "":
            para = para + "&label=" + label

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))
    def traverser_kout(self, source, direction, depth, label="", nearest="true"):
        """
        根据起始顶点、方向、边的类型（可选）和深度depth，查找从起始顶点出发恰好depth步可达的顶点
        :param source: 起始顶点id
        :param direction: 起始顶点向外发散的方向（OUT,IN,BOTH）
        :param depth: 步数
        :param label: 边的类型
        :param nearest: 默认为true，代表起始顶点到达结果顶点的最短路径长度为depth，不存在更短的路径；nearest为false时，
                        代表起始顶点到结果顶点有一条长度为depth的路径（未必最短且可以有环)
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kout?"
        para = ""
        if source == "":
            return CirroGraphResponse(400, "source can not be empty")
        else:
            para = para + "&source=\"" + source + "\""
        if direction == "":
            return CirroGraphResponse(400, "direction can not be empty")
        else:
            para = para + "&direction=" + direction
        if depth == "":
            return CirroGraphResponse(400, "depth can not be empty")
        else:
            para = para + "&depth=" + str(depth)
        if label != "":
            para = para + "&label=" + label
        if nearest != "":
            para = para + "&nearest=" + label

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))


    def traverser_vertices(self, vertex_ids):
        """
        根据顶点的id列表，批量查询顶点
        :param vertex_ids: 要查询的顶点id列表
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/vertices?"
        para = ""
        for id in vertex_ids:
            para = para + "&ids=\"" + id + "\""
        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

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
        return self.CreateVariables(key, value)

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
        requests.get(url, headers=self.headers,auth=self.auth)
        return CirroGraphResponse()

    def delete_variable(self, key):
        """
        删除某个键值对
        :param key:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/variables/" + key
        requests.delete(url, headers=self.headers,auth=self.auth)
        return CirroGraphResponse()

    def get_tasks(self, status="success", limit=""):
        """
        列出某个图中全部的异步任务
        :param status: 异步任务的状态(success,failed)
        :param limit: 返回异步任务数目上限
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks?status=" + status
        if limit != "":
            url = url + "&limit=" + limit
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def get_task(self, task_id):
        """
        查看某个任务的信息
        :param task_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks/" + task_id
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def delete_task(self, task_id):
        """
        删除某个异步任务信息，不删除异步任务本身
        :param task_id:
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/tasks/" + task_id
        
        return CirroGraphResponse(requests.delete(url, headers=self.headers,auth=self.auth))

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

    def execute_germlin_traversal(self, gremlin, bindings='', language="gremlin-groovy", aliases=""):
        """
        向CirroGraphServer发送gremlin语句（GET），同步执行
        :param gremlin: 要发送给CirroGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型，默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return: CirroGraphResponse
        """
        if bindings == '':
            bindings = {}
        url = self.host + "/gremlin?gremlin=" + self.graph + ".traversal()." + gremlin
        if bindings != {}:
            url = url + "&bindings=" + bindings
        if language != "gremlin-groovy":
            url = url + "&language=" + language
        if aliases != "":
            url = url + "&aliases=" + aliases
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def execute_germlin_get(self, gremlin, bindings='', language="gremlin-groovy", aliases=""):
        """
        向CirroGraphServer发送gremlin语句（GET），同步执行
        :param gremlin: 要发送给CirroGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型，默认为gremlin-groovy
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
        向CirroGraphServer发送gremlin语句（post），同步执行
        :param gremlin: 要发送给CirroGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型，默认为gremlin-groovy
        :param aliases: 为存在于图空间的已有变量添加别名
        :return: CirroGraphResponse
        """
        if bindings == '':
            bindings = {}
        url = self.host + "/gremlin"
        data = {
            "gremlin": gremlin,
            "bindings": bindings,
            "language": language,
            "aliases": aliases
        }
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

    def execute_germlin_post_job(self, gremlin, bindings='', language="gremlin-groovy"):
        """
        向CirroGraphServer发送gremlin语句（post），异步执行
        异步执行Gremlin语句暂不支持aliases，可以使用 graph 代表要操作的图，也可以直接使用图的名字， 例如 CirroGraph; 另外g代表 traversal，等价于 graph.traversal() 或者 CirroGraph.traversal()
        :param gremlin: 要发送给CirroGraphServer执行的gremlin语句
        :param bindings: 可以给gremlin语句中的变量绑定值
        :param language: 发送语句的语言类型，默认为gremlin-groovy
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
        向CirroGraphServer发送cypher语句（post）        
        :param data: { 要发送给CirroGraphServer执行的cypher语句 }
        data = {
            "cypher": "MATCH (v) return v"
        }
        :return: CirroGraphResponse
        """
        if bindings == '':
            bindings = {}
        url = self.host + "/gremlin" + "/" + self.graph + "/cypher"
        data = {
            "cypher": cypherql
        }
        
        return CirroGraphResponse(requests.post(url, data=json.dumps(data), headers=self.headers,auth=self.auth))

class CirroGraphTraverser():
    """
    CirroGraph Traverser API
    """

    def __init__(self,host,graph,headers={},auth=()):
        
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
    
    def kout_get(self, source,depth,direction="",max_degree="",capacity="",limit="",label="", nearest=""):
        """
        根据起始顶点、方向、边的类型（可选）和深度depth，查找从起始顶点出发恰好depth步可达的顶点
        :param source: 起始顶点id
        :param direction: 起始顶点向外发散的方向（OUT,IN,BOTH）
        :param depth: 步数
        :param label: 边的类型
        :param nearest: 默认为true，代表起始顶点到达结果顶点的最短路径长度为depth，不存在更短的路径；nearest为false时，
                        代表起始顶点到结果顶点有一条长度为depth的路径（未必最短且可以有环)
        :return: CirroGraphResponse
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
        if depth != "":
            para = para + "&max_depth=" + str(depth)
        if direction != "":
            para = para + "&direction=" + direction
        if label != "":
            para = para + "&label=" + label
        if nearest != "":
            para = para + "&nearest=" + label
        if max_degree != "":
            para = para + "&max_degree=" + label
        if capacity != "":
            para = para + "&capacity=" + label
        if limit != "":
            para = para + "&limit=" + label    

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))

    def kout_post(self,request):
        '''
        eg:
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
        '''
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kout"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))

    def kneighbor_get(self, source,  depth, direction="BOTH",label="",max_degree="10000",limit="10000000"):
        """
        根据起始顶点、方向、边的类型（可选）和深度depth，查找包括起始顶点在内、depth步之内可达的所有顶点
        :param source: 起始顶点id
        :param direction: 起始顶点向外发散的方向（OUT,IN,BOTH）
        :param depth: 步数
        :param label: 边的类型
        :return: CirroGraphResponse
        """
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kneighbor?"
        para = ""
        if type(source) is int:
                para = f'{para}&source={source}'
        else:
            if source.isnumeric():
                para = f'{para}&source={source}'
            else:
                para = f'{para}&source="{source}"'
        if direction != "":
            para = para + "&direction=" + direction
        if depth != "":
            para = para + "&max_depth=" + str(depth)
        if label != "":
            para = para + "&label=" + label
        if max_degree != "":
            para = para + "&max_degree=" + label
        if limit != "":
            para = para + "&limit=" + label

        url = url + para[1:]
        
        return CirroGraphResponse(requests.get(url, headers=self.headers,auth=self.auth))    

    def kneighbor_post(self,request):
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kneighbor"
        return CirroGraphResponse(requests.post(url,json.dumps(request),headers=self.headers,auth=self.auth))

    def sameneighbors(self,vertex,other,direction="BOTH",label="",max_degree="10000",limit="10000000"):
        url = self.host + "/graphs" + "/" + self.graph + "/traversers/kout?"
        para = ""
        if type(vertex) is int:
            para = f'{para}&source={vertex}'
        else:
            para = f'{para}&source="{vertex}"'
        if type(other) is int:
            para = f'{para}&source={other}'
        else:
            para = f'{para}&source="{other}"'
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

if __name__=="__main__":
    pass