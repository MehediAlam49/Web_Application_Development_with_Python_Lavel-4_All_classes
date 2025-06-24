student_name = ['mehedi', 'Raida', 'Tonny', 'Riju']
for name in student_name:
    print(name)



stu_name = 'Mehedi'
for name in stu_name:
    print(name)


print('-----Loop through a Dictionary Key')
marks ={
    'Bangla' : 80,
    'Math' : 70,
    'Physics' : 95,
}
for key in marks:
    print(key)
print('-----Loop through a Dictionary value')
for value in marks.values():
    print(value)
print('-----Loop through a Dictionary key and value')
for key,value in marks.items():
    print(key, '=' , value)




print('-----Loop through a Range')
for i in range(5):
    print(i)

for i in range(5):
    print('python')

for i in range(5,10):
    print(i)

for i in range(5,20,2):
    print(i)


print('-----Loop through a Brake statement')
employee = ['Mehedi', 'Aowlad', 'yeadul', 'Saika', 'Rayhan']
for name in employee:
    if name == 'yeadul':
        break
    print(name)

print('-----Loop through a continue statement')
for name in employee:
    if name == 'yeadul':
        continue
    print(name)