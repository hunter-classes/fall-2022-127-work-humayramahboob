d = {}
d{2} = 12345
d{5} = "hello"
d['hello'] = 'world'
d['list'] = [2,3,4,5,6]
d[ (1,2) ] = 55
print(d)
d['list'] = 55.3
print(d)

person = {'first' : "John",
          'last'  : "Smith",
          'age'   :  50,
          'height':  60}
person['age'] = person['age'] + 1
print(person)

k= person.keys()
print(k)
for item in k:
  print('person[',item,'] = ',person[item])

# convert the dict_keys into a list:
klist = [x for x in person.keys()]
print(klist)

# convert the values and convert into a list
vlist = [x for x in person.values()]
print(vlist)

s1 = {'gender':'m','name':'barney', 'id':1111, 'scores':[100,90,85]}
s2 = {'gender':'f','name':'jen', 'id':4444, 'scores':[95,85]}
s3 = {'gender':'m','name':'marcel', 'id':3333, 'scores':[99,76,88,82]}
s4 = {'gender':'f','name':'sookie', 'id':2222, 'scores':[98]}
student_list = [s1,s2,s3,s4]
student_dict = {}
for item in student_list:
  student_dict[item['id']] = item
