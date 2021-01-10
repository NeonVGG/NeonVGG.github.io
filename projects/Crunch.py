#Shesh Crunch 
alphabets='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
file=open("wordlist.txt",'w')
# here max length = 4
for i in alphabets:
      for j in alphabets:
            for k in alphabets:
                  for l in alphabets:
                        string=i+j+k+l
                        #print(i+j+k+l)
                        file.write(string+'\n')
file.close()
