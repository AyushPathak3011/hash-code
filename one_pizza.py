#one pizza problem
inputfile = 'c_coarse.in.txt'
likes = []
dislikes = []
with open(inputfile,'r') as p:
    data=p.readlines()

for i in range(0,len(data)):
    word=data[i].split()
    #print(word)

    if i%2!=0 :
        likes = likes + word[1:]
    if i%2==0 and i!=0:
        dislikes = dislikes + word[1:]
print(likes)
print(dislikes)
A = set(likes)
B = set(dislikes)
C = list( A -  B)
C = [str(len(C))] + C



# 4 vxglq tfeej dlust luncl
dict_likes={}
dict_dislikes={}
for i in A:
    #print(i,likes.count(i))
    dict_likes[i]=likes.count(i)

for i in B:
    #print(i,likes.count(i))
    dict_dislikes[i]=dislikes.count(i)


dict_likes = dict( sorted(dict_likes.items(),key=lambda item: item[1],reverse=True))
dict_dislikes = dict( sorted(dict_dislikes.items(),key=lambda item: item[1],reverse=True))
print(dict_likes)
print(dict_dislikes)

print(" ".join(C))