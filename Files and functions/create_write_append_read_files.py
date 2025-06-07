#creating a new file and writing into it
f = open('story.txt','w')
f.write("The woods are lovely, dark and deep,\n")
f.write("But I have promises to keep,\n")
f.close()

#append new text into the existing file
f = open('story.txt','a')
f.write("And miles to go before I sleep.\n")
f.write("— Robert Frost\n")
f.close()

#read the file and display to the console
f = open('story.txt','r')
print(f.read())
f.close()