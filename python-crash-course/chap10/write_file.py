filename = 'files/message.txt'

while True:
    message = input("What is your message? ")
    if message == 'quit':
        break
    elif message == 'print':
        with open(filename, 'r') as fo:
            lines = fo.readlines()
        for line in lines:
            print(line.rstrip())
    else:
        with open(filename, 'a') as fo:
            fo.write(message + "\n")
        print("Message added")