enterfile = open("W01 Ponder Weekly Reflection.txt", "r") 
print ("Enter file: ",enterfile.name)
lines = 0
words = 0
for line in enterfile:
  lines = lines +1
for word in line:
  words_list = line.split()
  words += len(words_list)
    
print("The file contains {} lines and {} words.".format(lines, words))