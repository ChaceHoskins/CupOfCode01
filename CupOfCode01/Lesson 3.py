bit = 8
byte = int(bit/8)
old_pc = 32
new_pc = old_pc*2
print('the smallest unit of storage in pc is a bit')
print('''It takes ''', bit, 'bits to make', byte,'byte\n')
print('the old way was',old_pc, 'bit machines. this was the width of the cpu register')
print('the', old_pc, 'bit machines were limited to', bit/2, 'gigs')
print('those machines had a memory ceiling of', 2**32, 'bytes\n')
print('knowing that turns into', int(2**32/1000000000),'gigabytes\n')
print('right now I am working on a ', new_pc, 'bit machine')
print('letting me rock out', int(2**64/1000000000), 'gigs of memory ceiling')
print('yes thats over 18 BILLION gigs\n')
print('can your pc case hold that?')
print('I have', int(old_pc/4), 'gig ram sticks and rocking', int(bit/4), 'of them')
print('for a fairly standard', int(old_pc/2), 'gigs of ram')
print('but to max out what', new_pc,'can handle, I would need',int(round(2**64/1000000000)/(bit+bit)), '16 ram sticks')
print('print\n')
print('Yeahhhhhhhhh, I dont have a case for 1.1 billion 16 ram sticks')