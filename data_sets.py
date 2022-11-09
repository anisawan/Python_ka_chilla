d1 = {"Apple":200, "Banana":100, "orange":50, "pears":250}
print(type(d1))
print(d1)
#getting data from dictionaries
# printing the dictionary keys
print(d1.keys())
#storing to variable
dic_keys=d1.keys()
print(dic_keys)
# printing the dictionary values
print(d1.values())
#storing to dic values to variable
dic_val=d1.values()
print(dic_val)
# adding new key and value to dic
d1["Samoosa"]=20
#print(d1)
#updating the existing values
d1["Samoosa"]=35
#print(d1)
d2 = {"rooti":15, "dates":150}
# concatenate the two dicts
d1.update(d2)
#printing a specific value of dict
print(d1["Samoosa"])
print(d1.get('rooti')) #Specify the key as the first argument. The corresponding value is returned if the key exists,
                        # and None is returned if the key does not exist.

# printing a key against a key
keys = [k for k, v in d1.items() if v == 150]
print(keys)
