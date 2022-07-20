import builtwith 
u= raw_input("Enter The Web Site:")
r= builtwith.builtwith(u)
print("\n")
for i in r:
	print (i,"i",r[i][0] )