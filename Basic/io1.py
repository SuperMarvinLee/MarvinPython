
import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
output = open('static/data.pkl', 'ab+')
pickle.dump(data1, output)
data2 = pickle.load(output)
print(data2)
output.close()