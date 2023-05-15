dictionaries = {"Name" : "Tabriz", "Age" : 24, "Email" : "xyz@gmail.com"}
print(dictionaries) # {'Name': 'Tabriz', 'Age': 24, 'Email': 'xyz@gmail.com'}

dictionaries["Email"] = "pqr@gmail.com"
print(dictionaries) # {'Name': 'Tabriz', 'Age': 24, 'Email': 'pqr@gmail.com'}

dictionaries["Marks"] = 95
print(dictionaries) # {'Name': 'Tabriz', 'Age': 24, 'Email': 'pqr@gmail.com', 'Marks': 95}

del dictionaries["Email"]
print(dictionaries) # {'Name': 'Tabriz', 'Age': 24, 'Marks': 95}

print(dictionaries.keys()) # dict_keys(['Name', 'Age', 'Marks'])
print(dictionaries.values()) # dict_values(['Tabriz', 24, 95])
print(dictionaries.items()) # dict_items([('Name', 'Tabriz'), ('Age', 24), ('Marks', 95)])

dictionaries.clear()
print(dictionaries) # {}
