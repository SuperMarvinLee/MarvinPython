#!/usr/bin/python3
# Filename      : cirrograph_test01.py
# Description   : Python3-CirroGraph-Client
# author        : Shangrila
# version       : cirrograph 1.3.1(hugegraph 12)
# date          : 2022/12/12
# -*- coding: UTF-8 -*-

'''
# 交互式环境使用
import sys
sys.path.append(r"/home/sophia/projects/python/cirrograph")
import cirrograph_client as cirrograph
'''

# python3 访问 CirroGraph rest-API
import cirrograph_client as cirroclient

# 没有开启Http Authentication credentials
# 新建一个CirroGraphClient对象
# cirrograph = cirroclient.CirroGraphClient("http://localhost:8080", "cirrograph")
# cirrograph = cirroclient.CirroGraphClient("http://localhost:8080", "cirrograph",headers={},auth={})

# 开启Http Authentication credentials
headers = {'Content-Type': 'application/json'}
auth = ('admin','cirrograph_admin')
# 新建一个CirroGraphClient对象
cirrograph = cirroclient.CirroGraphClient("http://localhost:8080", "cirrograph",headers=headers,auth=auth)

# 示例1：查找所有图信息
url = 'http://localhost:8080/graphs'
res = cirrograph.cirrograph_get(url)
print(res.status_code,res.response)

# 示例2：查找cirrograph图信息
url="http://localhost:8080/graphs/cirrograph"
res = cirrograph.cirrograph_get(url)
print(res.status_code,res.response)

# 示例3：查找cirrograph图schema信息
url="http://localhost:8080/graphs/cirrograph/schema"
res = cirrograph.cirrograph_get(url)
print(res.status_code,res.response)

# 测试Gremlin：遍历语句执行
# 示例4：发送gremlin语句（GET），同步执行
url='http://localhost:8080/gremlin?gremlin=cirrograph.traversal().'
gremlin = 'V()'
url = url + gremlin
res = cirrograph.cirrograph_get(url)
print(res.status_code,res.response)

# 示例5：发送gremlin语句（POST），同步执行
url='http://localhost:8080/gremlin'
data = {"gremlin": "cirrograph.traversal().V()" }
print(cirrograph.cirrograph_post(url,data))

# 示例6：发送gremlin语句（POST），异步执行,返回异步任务ID，根据异步任务ID查找结果
url='http://localhost:8080/graphs/cirrograph/jobs/gremlin'
data = { "gremlin": "cirrograph.traversal().V()" }
print(cirrograph.cirrograph_post(url,data))

# 示例7：异步执行后通过任务查询结果：示例中6是前述异步查询的任务号：
url='http://localhost:8080/graphs/cirrograph/tasks/3'
res = cirrograph.cirrograph_get(url)
print(res.status_code,res.response)

# 综合示例08：以下示例通过CirroGraph的rest服务来实现TinkerPop Modern图
# 步骤1：增加4个属性
url='http://localhost:8080/graphs/cirrograph/schema/propertykeys'

data = {"name": "name","data_type": "TEXT","cardinality": "SINGLE" }
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

data = {"name": "age","data_type": "INT","cardinality": "SINGLE" }
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

data = {"name": "weight","data_type": "DOUBLE","cardinality": "SINGLE" }
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

data = {"name": "lang","data_type": "TEXT","cardinality": "SINGLE" }
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

# 步骤2：增加2个VertexLabel
url='http://localhost:8080/graphs/cirrograph/schema/vertexlabels'
data = {
    "name": "person",
    "id_strategy": "CUSTOMIZE_NUMBER",
    "properties": ["name","age"],
    "nullable_keys": ["age"]
}

res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

data = {
    "name": "software",
    "id_strategy": "CUSTOMIZE_NUMBER",
    "properties": ["name","lang"],
    "nullable_keys": ["lang"]
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

# 步骤3：增加2个EdgeLabel
url='http://localhost:8080/graphs/cirrograph/schema/edgelabels'
data = {
    "name": "knows",
    "source_label": "person",
    "target_label": "person",
    "frequency": "MULTIPLE",
    "properties": ["weight"],
    "sort_keys": ["weight"],
    "user_data": {}
}
res = cirrograph.cirrograph_post(url,data)
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
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

# 步骤4：增加2个IndexLabel
url='http://localhost:8080/graphs/cirrograph/schema/indexlabels'
data = {
    "name": "personByName",
    "base_type": "VERTEX_LABEL",
    "base_value": "person",
    "index_type": "SECONDARY",
    "fields": ["name"]
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

data = {
    "name": "softwareByName",
    "base_type": "VERTEX_LABEL",
    "base_value": "software",
    "index_type": "SECONDARY",
    "fields": ["name"]
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

# 步骤5：增加顶点数据
url='http://localhost:8080/graphs/cirrograph/graph/vertices'
data = {
    "label": "person",
    "id":1,
    "properties": {
        "name": "marko",
        "age": 29
    }
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)
data = {
    "label": "person",
    "id":2,
    "properties": {
        "name": "vadas",
        "age": 27
    }
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)
data = {
    "label": "person",
    "id":4,
    "properties": {
        "name": "josh",
        "age": 32
    }
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)
data = {
    "label": "person",
    "id":6,
    "properties": {
        "name": "peter",
        "age": 28
    }
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)
data = {
    "label": "software",
    "id":5,
    "properties": {
        "name": "ripple",
        "lang": "java"
    }
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)
data = {
    "label": "software",
    "id":3,
    "properties": {
        "name": "lop",
        "lang": "java"
    }
}
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

# 步骤6：增加边数据
url='http://localhost:8080/graphs/cirrograph/graph/edges'
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
res = cirrograph.cirrograph_post(url,data)
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
res = cirrograph.cirrograph_post(url,data)
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
res = cirrograph.cirrograph_post(url,data)
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
res = cirrograph.cirrograph_post(url,data)
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
res = cirrograph.cirrograph_post(url,data)
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
res = cirrograph.cirrograph_post(url,data)
print(res.status_code,res.response)

# 综合示例9：删除图对象以及数据（要注意顺序）

# 步骤1：根据ID删除边数据
url='http://localhost:8080/graphs/cirrograph/graph/edges'
res = cirrograph.cirrograph_get(url)

url='http://localhost:8080/graphs/cirrograph/graph/edges/L1>6>B3~W00000000>L2'
res = cirrograph.cirrograph_delete(url)
print(res.status_code,res.response)

# 步骤2：根据ID删除点数据
url='http://localhost:8080/graphs/cirrograph/graph/vertices'
res = cirrograph.cirrograph_get(url)

url='http://localhost:8080/graphs/cirrograph/graph/vertices/6'
res = cirrograph.cirrograph_delete(url)
print(res.status_code,res.response)

# 步骤3：根据name删除边类型:    异步任务，相应数据也全部删除
url = 'http://localhost:8080/graphs/cirrograph/schema/edgelabels/knows'
res = cirrograph.cirrograph_delete(url)

url = 'http://localhost:8080/graphs/cirrograph/schema/edgelabels/created'
res = cirrograph.cirrograph_delete(url)
print(res.status_code,res.response)

# 步骤4：根据name删除点类型:没有关联的edgelabels才可以删除。异步任务，相应数据也全部删除
url = 'http://localhost:8080/graphs/cirrograph/schema/vertexlabels/person'
res = cirrograph.cirrograph_delete(url)

url = 'http://localhost:8080/graphs/cirrograph/schema/vertexlabels/software'
res = cirrograph.cirrograph_delete(url)
print(res.status_code,res.response)
# {"task_id":18}

# 异步执行后通过任务查询结果：示例中18是前述异步查询的任务号：
url='http://localhost:8080/graphs/cirrograph/tasks/18'
res = cirrograph.cirrograph_get(url)
print(res.status_code,res.response)

# 步骤5：删除属性：异步任务
url="http://localhost:8080/graphs/cirrograph/schema/propertykeys/age"
res = cirrograph.cirrograph_delete(url)
url="http://localhost:8080/graphs/cirrograph/schema/propertykeys/name"
res = cirrograph.cirrograph_delete(url)
url="http://localhost:8080/graphs/cirrograph/schema/propertykeys/weight"
res = cirrograph.cirrograph_delete(url)
url="http://localhost:8080/graphs/cirrograph/schema/propertykeys/lang"
res = cirrograph.cirrograph_delete(url)
print(res.status_code,res.response)

# 克隆图、清除图与删除图: 
# cirrograph_1为克隆新图名称，cirrograph为基准图
url='http://localhost:8080/graphs/cirrograph_1?clone_graph_name=cirrograph'
res = cirrograph.cirrograph_post(url,{})
print(res.status_code,res.response)

url='http://localhost:8080/graphs/cirrograph_1/clear?confirm_message=I%27m+sure+to+delete+all+data'
res = cirrograph.cirrograph_delete(url)
print(res.status_code,res.response)

url='http://localhost:8080/graphs/cirrograph_1?confirm_message=I%27m%20sure%20to%20drop%20the%20graph'
res = cirrograph.cirrograph_delete(url)
print(res.status_code,res.response)

# 测试Gremlin: schema语句
# 创建TinkerGraph Modern图：
# 注意  1、使用""" """来标识多行语句；
#      2、定义graph和schema变量：graph = cirrograph;schema = graph.schema(); 
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

url='http://localhost:8080/gremlin?gremlin='
url = url + gremlin
res = cirrograph.cirrograph_get(url)
print(res.status_code,res.response)

if __name__=="__main__":
    pass