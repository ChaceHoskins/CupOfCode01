#lists can be changed by calling and modifying
#tuples can not-fixed

x = 5,6,7,8
y = (5,6,7,3)

x = [5,6,7,]
y = [5,6,7,3]

#tuples are great for sequence of unpacking
#or having a list you never change

def function():
    return 12,6,8
q,r,s = function()
#when called this function will always have 12,6,8

print(q,r,s)
print(s,r,q)

def second():
    return [3,5,8]

b,i,g = second()

sample = ['today','tomorrow','yesterday','another day']
print(sample)
print(len(sample))
print(sample.count('tomorrow'))
print(sample[2])

sample.insert(1, 'huge')
print(sample)

sample.insert(3, 'huger')
print(sample)

sample.remove('huge')
print(sample)

sample.reverse()
print(sample)

sample.pop(0)
print(sample)

sample.append('this will always be put in the last indexed position)
print(sample,'\n')
sample.sort()
print(sample)

print(sample[:2])
print(sample)

print(sample[2:4],'\n')

