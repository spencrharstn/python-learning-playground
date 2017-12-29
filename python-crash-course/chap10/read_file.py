filename = 'files/pi1000000.txt'
with open(filename) as fo:
    lines = fo.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

birthday = '021591'
if birthday in pi_string:
    print('Your birthday is in the first million digits of pi')
else:
    print('Your birthday is not in the first million digits of pi')