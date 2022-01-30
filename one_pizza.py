#one pizza problem
inputfile = 'c_coarse.in.txt'

with open('Test Cases/'+inputfile,'r') as p:
    inputdata=p.readlines()

class Customer:
    def __init__(self, likes, dislikes):
        self.likes = likes
        self.dislikes = dislikes
    
    def __str__ (self):
        return ("likes : " + " ".join(self.likes) + "\n" + "dislikes : " + " ".join(self.dislikes))

cust = {}

#creates objects for customers and assigns their preferences
for i in range(1,len(inputdata),2):
    line_list1 = inputdata[i].split()
    line_list2 = inputdata[i+1].split()
    """
    #displays 2 consecutive lines
    print(line_list1)
    print(line_list2)
    """
    cust[int(((i+1)/2)-1)] = Customer(line_list1[1:], line_list2[1:])

"""
#displays all the customers with their preferences
for i in range(0,len(cust)):
    print ("cust" + str(i)+ "\n",cust[i],"n")
"""

#finds the total no of people that will come to store
def IngScore(a):
    ingredients_list = a
    #ingredients_list = list(filter(None, ingredients_list))
    score = 0
    for i in range(0,len(cust)):
        if (not(set(cust[i].dislikes).issubset(set(ingredients_list)))) or (cust[i].dislikes == []):
            if (set(cust[i].likes).issubset(set(ingredients_list))):
                score += 1
                #print ("cust" + str(i) + "\n", cust[i], "\n")
    return score
#print(IngScore(input("enter ingredients list : ")))

#this is the actual procedural algorithm that adds ingredients that suits the majority of customers
ingredients_list = []
dislikes_list = []
for i in range(0,len(cust)):
    if ((not(set(cust[i].dislikes).issubset(set(ingredients_list)))) or cust[i].dislikes == []) and (set(cust[i].likes).isdisjoint(set(dislikes_list))):
        ingredients_list += cust[i].likes
        dislikes_list += cust[i].dislikes
    """
    else :
        if (cust[i].dislikes.count(i) > ingredients_list.count(i)):
            ingredients_list += cust[i].likes
    """

"""
print("Ingredients :", set(ingredients_list))
print("Customers interested list : ")
print("Total customer interested :", IngScore(ingredients_list))
"""

#this is the output
print(len(set(ingredients_list))," ".join(list(set(ingredients_list))))

output_str=str(len(set(ingredients_list)))+ " " + " ".join(list(set(ingredients_list)))

output_file=open('output.txt','w')
output_file.write(output_str)
output_file.close()
