ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there is not ten things in the list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff =["Day", "Night", "Frisbee", "Banana", "Corn", "Girl","Boy"]


while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now." %len(stuff))


print("There we go : ", stuff)

print("Lets do somethings with stuff")

print(stuff[-2])
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) # What? cool
print('#'.join(stuff[3:5]))
print(stuff)

