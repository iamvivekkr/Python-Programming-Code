#Dictionary and its Functions

d1 = {}
print(type(d1))
d2 = {"vivek":"toffee", "Abhi": "egg"}
print(d2)
print(d2["Abhi"])
d2["Ankit"] = "Junkfood"
d2[420] = "kabab"
print(d2)
del d2[420]
print(d2)

#Function 

d3=d2.copy()          #if we write d3=d2 & delete vivek then from both d2&d3 vivek deleted
del d3["vivek"]       #if we use d3=d2.copy then delete after only vivek, delete from d3 not d2

print(d2.get("vivek"))  #add dictionary in d2
d2.update({"Sanvi": "tea"})
print(d2)

print(d2.keys()) #print only keys point

print(d2.items()) #print iteams under keys