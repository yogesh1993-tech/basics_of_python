"""
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

"""

heros=['spider man','thor','hulk','iron man','captain america']

# lenth of the list

l = len(heros)
print(f"Length of the list is : {l}" )

print("printing length without using len function")

count = 0
for i in heros:
    count +=1
print(f"lennth is without using len function {count}")

#  Add 'black panther' at the end of this list

heros.append("black panther")
print(heros)

"""
You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
"""
heros.remove("black panther")
print(heros)

heros[3] = "black panther"
print(heros)

"""
. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
"""

heros[1:3] =['Doctor Strange']
print(heros)

"""
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

"""
heros.sort(reverse=True)
print(heros)
