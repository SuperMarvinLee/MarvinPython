
import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
output = open('static/data.pkl', 'wb')
pickle.dump(data1, output)
output.close()
input = open('static/data.pkl','rb')
data2 = pickle.load(input)
print(data2)
input.close()