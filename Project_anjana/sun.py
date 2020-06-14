import random, string

def randomword(length):
   
   letters = ["a","c","t","g"]
   word=''.join(random.choice(letters) for i in range(length))
   with open("dna-sequence.txt","a") as file_txt:
   	file_txt.write(word)
   with open("dna-sequence2.txt","a") as file_txt:
   	file_txt.write(''.join(random.choice(letters) for i in range(length)))

def lcs(X, Y, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]
 
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    
    index = L[m][n]
 
    
    lcs = [""] * (index+1)
    lcs[index] = ""
 
    
    i = m
    j = n
    while i > 0 and j > 0:
 
        
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
 
        
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
 
    print ("LCS of " + X + " and " + Y + " is " + "".join(lcs) )
    if(len(lcs)>500):
    	print("Matching")
    else:
    	print("Not matching")

 

randomword(1000) 
X = (open("sun1.txt","r").read())
Y = (open("sun2.txt","r").read())
m = len(X)
n = len(Y)
lcs(X, Y, m, n)
