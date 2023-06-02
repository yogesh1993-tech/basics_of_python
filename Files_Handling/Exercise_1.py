''' poem.txt contains famous poem "Road not taken" by poet Robert Frost.
You have to read
this file in your python program and
find out words with maximum occurance.'''

''' 
file reading format 

f=open("C:\\Users\\yogesh.mohite.1\\OneDrive - Cotiviti\\Desktop\\Road not taken.txt","r")

for lines in f:
    print(lines)
     f.close()
     '''
''' File Reading with (With Function) = No Need to close file automatic distructure '''


''' with open("C:\\Users\\yogesh.mohite.1\\OneDrive - Cotiviti\\Desktop\\Road not taken.txt","r") as f:

    for lines in f:
        print(lines) '''


''' Creating and Writing Files '''

''' with open("C:\\Users\\yogesh.mohite.1\\OneDrive - Cotiviti\\Desktop\\NewFile.txt","w") as f:

    f.write("Love You Mrun") '''
'''  Appending file content in existing file '''

'''with open("C:\\Users\\yogesh.mohite.1\\OneDrive - Cotiviti\\Desktop\\NewFile.txt","a") as f:

    f.write("\n \n Will You Marry Me")'''



''' making empty dict  '''

word_stats = {}
with open("C:\\Users\\yogesh.mohite.1\\OneDrive - Cotiviti\\Desktop\\NewFile.txt","r") as f:

 for line in f:
    words = line.split(' ')
    for word in words:
        if word in word_stats:
            word_stats[word]+=1
        else:
            word_stats[word] = 1
print(word_stats)

word_occurance = list(word_stats.values())
max_count = max(word_occurance)
print("Max occurances of any word is:",max_count)


print("Words with max occurances are: ")
for word,count in word_stats.items():
    if count == max_count:
        print(word)





