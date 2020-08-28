import json
#from collections import OrderedDict

with open('raw_solvera_user_data-20200828_1102.json', 'r',encoding="utf8") as f:
    result = ""
#Added to your saved items
#1:00
    users = json.loads(f.read())
#1:00
    i=0
    for uniq in users:
        for value in uniq:
            #print(value)
            #print (uniq[value])
            result = result + str(uniq[value]) + ";"
        result = result + "\n"
        #result = result + users
    text_file = open("solvera1102.csv", "w")
    n = text_file.write(result)
    text_file.close()
