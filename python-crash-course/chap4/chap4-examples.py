# Chapter 4 examples

magicians = ['alice','david','carolina']

for magician in magicians:
    print(magician.title() + ', you nailed it.')
print('Thanks for the show.')

for i in range(1,6):
    print(i)

numbers = list(range(0,11,2))
print(numbers)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

squares2 = [j ** 2 for j in range(1,11)]
print(squares2)

cubes = [k ** 3 for k in range(1,11)]
print(cubes)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:2])
print(players[2:])
print(players[-4:])

print("First 3 players:")
for player in players[:3]:
    print(player.title())

scores = [99, 88, 77, 87, 94, 88, 91, 98]
print(sorted(scores)) #temporary sorting
scores.sort(reverse=True)   #'permanent' sorting w/ reverse
print(scores)
print("Top 3 scores:")
for score in scores[:3]:
    print(score)


foods = ['pizza','tacos','sandwiches','sushi','buns']
your_foods = foods[:] #copy list using a slice

foods.append('smoothie')
foods.append('cereal')
your_foods.append('soup')
your_foods.append('salad')

print("My foods: " , foods)
print("Your foods: " , your_foods)

# copy a list, but both point to the same
friend_foods = foods
foods.append('yogurt')
friend_foods.append('spaghetti')

print("Foods: ", foods)
print("Friend Foods: ", friend_foods) 
#These will both have the same list. Both append to the same list, don't cha know how that works?

#Tuples. Immutable (unchangeable) list.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

