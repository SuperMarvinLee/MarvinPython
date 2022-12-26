#!/usr/bin/python3
# Filename      : cirrograph_test02.py
# Description   : Python3-CirroGraph-Client
# author        : Shangrila
# version       : cirrograph 1.3.1(hugegraph 12)
# date          : 2022/12/12
# -*- coding: UTF-8 -*-

import cirrograph_client as cirroclient

# Client 测试:使用cirrograph.CirroGraphClient定义的方法
# access CirroGraphClient Class

# 新建一个CirroGraphClient对象
# 不开启Http Authentication credentials
# cirrograph.= cirroclient.CirroGraphClient("http://localhost:8080", "cirrograph")
# cirrograph = cirroclient.CirroGraphClient("http://localhost:8080", "cirrograph",headers={},auth={})

# 开启Http Authentication credentials
headers = {'Content-Type': 'application/json'}
auth = ('admin','cirrograph_admin')
cirrograph = cirroclient.CirroGraphClient("http://localhost:8080", "cirrograph",headers=headers,auth=auth)

# 查询CirroGraph对象
print(cirrograph.get_graphs().response)
print(cirrograph.get_graph().response)
print(cirrograph.get_schema().response)
print(cirrograph.get_propertykeys().response)
print(cirrograph.get_vertexlabels().response)
print(cirrograph.get_edgelabels().response)
print(cirrograph.get_indexlabels().response)

# 执行gremlin遍历: 
print(cirrograph.execute_germlin_traversal('V()').response)
print(cirrograph.execute_germlin_get('cirrograph.traversal().V()').response)
res = cirrograph.execute_germlin_post('cirrograph.traversal().V()')
print(res.status_code,res.response)

# 删除图对象以及数据(要注意顺序)
# 1、删除点数据会把该点的关联边数据也删除;
# 2、删除VertexLabel、EdgeLabel会把相应的数据和索引都删除。
# 根据ID删除边数据、根据ID删除点数据
res = cirrograph.delete_edge_id('L1>6>B3~W00000000>L2')
res = cirrograph.delete_vertex_id(1)

# 依次删除EdgeLabel、VertexLabel、PropertyKey
cirrograph.delete_edgelabel_name("knows")
cirrograph.delete_edgelabel_name("created")
cirrograph.delete_vertexlabel_name("person")
cirrograph.delete_vertexlabel_name("software")
cirrograph.delete_propertykey_name('age')
cirrograph.delete_propertykey_name('name')
cirrograph.delete_propertykey_name('lang')
cirrograph.delete_propertykey_name('weight')

# 克隆图、清除图与删除图: 
# 克隆图: cirrograph.要连接被克隆的图
print(cirrograph.clone_graph("cirrograph_2","cirrograph").status_code)
# 清除图与删除图: cirrograph.要连接被清除图与删除的图
print(cirrograph.clear_graph("cirrograph_2").status_code)
print(cirrograph.drop_graph("cirrograph_2").status_code)

# 综合示例:以下示例通过CirroGraphCLient的方法来实现TinkerPop Modern图
# 依次新增PropertyKey、VertexLabel、EdgeLabel
# 步骤1:增加4个属性
# 新增PropertyKey:两种方式新增属性(前一种可以扩展属性,后一种固定了3种参数)
cirrograph.create_propertykey({"name": "name","data_type": "TEXT","cardinality": "SINGLE" })
cirrograph.create_propertykey({"name": "lang","data_type": "TEXT","cardinality": "SINGLE" })
cirrograph.create_property_key("age","INT","SINGLE")
cirrograph.create_property_key("weight","FLOAT","SINGLE")

# 步骤2:增加2个VertexLabel
data = {
    "name": "person",
    "id_strategy": "CUSTOMIZE_NUMBER",
    "properties": [ "name","age" ],
    "nullable_keys": ["age"]
}
cirrograph.create_vertexlabel(data)
data = {
    "name": "software",
    "id_strategy": "CUSTOMIZE_NUMBER",
    "properties": ["name","lang" ],
    "nullable_keys": ["lang"]
}
res = cirrograph.create_vertexlabel(data)
print(res.response)

# 步骤3:增加2个EdgeLabel
data = {
    "name": "knows",
    "source_label": "person",
    "target_label": "person",
    "frequency": "MULTIPLE",
    "properties": ["weight"],
    "sort_keys": ["weight" ],
    "user_data": {}
}
res = cirrograph.create_edgelabel(data)
print(res.status_code,res.response)

data = {
    "name": "created",
    "source_label": "person",
    "target_label": "software",
    "frequency": "SINGLE",
    "properties": ["weight"],
    "sort_keys": [],
    "nullable_keys": ["weight"],
    "user_data": {}
}
res = cirrograph.create_edgelabel(data)
print(res.status_code,res.response)

# 步骤4:增加2个IndexLabel
data = {
    "name": "personByName",
    "base_type": "VERTEX_LABEL",
    "base_value": "person",
    "index_type": "SECONDARY",
    "fields": ["name"]
}
res = cirrograph.create_indexlabel(data)
print(res.status_code,res.response)

data = {
    "name": "softwareByName",
    "base_type": "VERTEX_LABEL",
    "base_value": "software",
    "index_type": "SECONDARY",
    "fields": ["name"]
}
res = cirrograph.create_indexlabel(data)
print(res.status_code,res.response)

# 步骤5:增加顶点数据
data = {
    "label": "person",
    "id":1,
    "properties": {
        "name": "marko",
        "age": 29
    }
}
res = cirrograph.create_vertex(data)
print(res.status_code,res.response)

data = {
    "label": "person",
    "id":2,
    "properties": {
        "name": "vadas",
        "age": 27
    }
}
res = cirrograph.create_vertex(data)
print(res.status_code,res.response)
data = {
    "label": "person",
    "id":4,
    "properties": {
        "name": "josh",
        "age": 32
    }
}
res = cirrograph.create_vertex(data)
print(res.status_code,res.response)
data = {
    "label": "person",
    "id":6,
    "properties": {
        "name": "peter",
        "age": 28
    }
}
res = cirrograph.create_vertex(data)
print(res.status_code,res.response)
data = {
    "label": "software",
    "id":5,
    "properties": {
        "name": "ripple",
        "lang": "java"
    }
}
res = cirrograph.create_vertex(data)
print(res.status_code,res.response)
data = {
    "label": "software",
    "id":3,
    "properties": {
        "name": "lop",
        "lang": "java"
    }
}
res = cirrograph.create_vertex(data)
print(res.status_code,res.response)


# 步骤6:增加边数据
data = {
    "label": "knows",
    "outV": 1,
    "inV": 2,
    "outVLabel": "person",
    "inVLabel": "person",
    "properties": {
        "weight": 0.5
    }
}
res = cirrograph.create_edge(data)
print(res.status_code,res.response)
data = {
    "label": "knows",
    "outV": 1,
    "inV": 4,
    "outVLabel": "person",
    "inVLabel": "person",
    "properties": {
        "weight": 1.0
    }
}
res = cirrograph.create_edge(data)
print(res.status_code,res.response)
data = {
    "label": "created",
    "outV": 1,
    "inV": 3,
    "outVLabel": "person",
    "inVLabel": "software",
    "properties": {
        "weight": 0.4
    }
}
res = cirrograph.create_edge(data)
print(res.status_code,res.response)

data = {
    "label": "created",
    "outV": 4,
    "inV": 3,
    "outVLabel": "person",
    "inVLabel": "software",
    "properties": {
        "weight": 0.4
    }
}
res = cirrograph.create_edge(data)
print(res.status_code,res.response)
data = {
    "label": "created",
    "outV": 4,
    "inV": 5,
    "outVLabel": "person",
    "inVLabel": "software",
    "properties": {
        "weight": 1.0
    }
}
res = cirrograph.create_edge(data)
print(res.status_code,res.response)
data = {
    "label": "created",
    "outV": 6,
    "inV": 3,
    "outVLabel": "person",
    "inVLabel": "software",
    "properties": {
        "weight": 0.2
    }
}
res = cirrograph.create_edge(data)
print(res.status_code,res.response)

# 测试Gremlin: schema语句
# 创建TinkerGraph Modern图:
# 注意  1、使用""" """来标识多行语句;
#      2、定义graph和schema变量:graph = cirrograph;schema = graph.schema(); 
#      3、cirrograph是后台配置的图名称

# gremlin语句开始
gremlin = """
graph = cirrograph;
schema = graph.schema(); 
schema.propertyKey("name").asText().ifNotExist().create();
// PropertyKey
schema.propertyKey("name").asText().ifNotExist().create();
schema.propertyKey("age").asInt().ifNotExist().create();
schema.propertyKey("weight").asDouble().ifNotExist().create();
schema.propertyKey("lang").asText().ifNotExist().create();

// VertexLabel
schema.vertexLabel("person").useCustomizeNumberId().properties("name","age").nullableKeys("age").ifNotExist().create();
schema.vertexLabel("software").useCustomizeNumberId().properties("name","lang").nullableKeys("lang").ifNotExist().create();

// EdgeLabel
//EdgeLabel must contain sortKeys when the cardinality property is multiple
schema.edgeLabel("knows").sourceLabel("person").targetLabel("person").properties("weight").nullableKeys("weight").ifNotExist().create();
schema.edgeLabel("created").sourceLabel("person").targetLabel("software").properties("weight").nullableKeys("weight").ifNotExist().create();

// IndexLabel
schema.indexLabel("personByName").onV("person").by("name").secondary().ifNotExist().create();
schema.indexLabel("softwareByName").onV("software").by("name").secondary().ifNotExist().create();

// Graph Data: Vertex
marko = graph.addVertex(T.label, "person", T.id, 1, "name", "marko", "age", 29);
vadas = graph.addVertex(T.label, "person", T.id, 2, "name", "vadas", "age", 27);
josh = graph.addVertex(T.label, "person", T.id, 4, "name", "josh", "age", 32);
peter = graph.addVertex(T.label, "person", T.id, 6, "name", "peter", "age",28);
ripple = graph.addVertex(T.label, "software", T.id, 5, "name", "ripple", "lang", "java");
lop = graph.addVertex(T.label, "software", T.id, 3, "name", "lop", "lang", "java");

// Graph Data: Edge
marko.addEdge("knows", vadas, "weight", 0.5);
marko.addEdge("knows", josh,  "weight", 1.0);
marko.addEdge("created", lop, "weight", 0.4);
josh.addEdge("created", lop, "weight", 0.4);
josh.addEdge("created", ripple, "weight", 1.0);
peter.addEdge("created", lop, "weight", 0.2);
"""
# gremlin语句结束

url='http://172.26.167.216:8080/gremlin?gremlin='
url = url + gremlin
res = cirrograph.execute_germlin_get(url)
print(res.status_code,res.response)

# 执行cypher查询
cypherql = "MATCH (v) return v"
res = cirrograph.execute_cypherql(cypherql)
print(res.status_code,res.response) 

if __name__=="__main__":
    pass

