# For loops loop through a list, performing an action for each list element

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#for i in l:
#    print(i)
#    print(i*i)
#    print()


# Can also use with ranges
# using f"{}" allows to format the printed result, i will use 2 spaces, i*i will use 4 spaces

for i in range(10):
    print(f"{i:2} {i*i:4}")

print ("That's the whole list!")