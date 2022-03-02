from importlib.resources import path
import json
import requests
url=requests.get("https://api.merakilearn.org/courses").json()
with open("courses.json","w") as file:
    json.dump(url , file , indent=4)
r = open("courses.json","r").read()
data = json.loads(r)
print()
print("<<<<< Welcome to Navgurukul and learn basic promming language >>>>>")
print()
i = 0
while i < len(data):
    print(str(i+1)+".",data[i]["name"],data[i]["id"])
    i+=1
user=int(input("<<<< enter the program number  >>>>:"))
print(data[user-1]["name"],data[user-1]["id"])
print()
data_file=data[user-1]["name"]+"_ "+data[user-1]["id"]+".json" 
url_file="http://api.merakilearn.org/courses/"+data[user-1]["id"]+"/exercises"
new_url=requests.get(url_file).json()
with open(data_file,"w") as f:
    json.dump(new_url,f,indent=4)
read_file= open(data_file,"r").read()
deta = json.loads(read_file)



i = 0
while i < len(deta["course"]["exercises"]):
    print(str(i+1)+".",deta["course"]["exercises"][i]["name"])
    i+=1
topic=int(input("enter the topic no:- "))
topic = topic-1
i = 0
while i < len(deta["course"]["exercises"][topic]["content"]):
    print(deta["course"]["exercises"][topic]["content"][i]["value"])
    print()
    i+=1
while topic <= len(deta["course"]["exercises"]):



    
    a = input("previous or next(p&n):")
    if a == "p" and a!= "n":
        topic-=1
        if a == "p" and topic >1:
            print(deta["course"]["exercises"][topic]["name"],"\n")
            i = 0 
            while i < len(deta["course"]["exercises"][topic]["content"]):
                print(deta["course"]["exercises"][topic]["content"][i]["value"])
                i+=1
        else :
            i = 0
            while i < len(deta):
                print(str(i+1),deta["course"]["exercises"][i]["name"])
                i+=1
    elif a == "n" and a!="p":
        topic+=1
        if a == "n" and topic < len(deta["course"]["exercises"]):
                print(deta["course"]["exercises"][topic]["name"],"\n")
                i = 0 
                while i < len(deta["course"]["exercises"][topic]["content"]):
                    print(deta["course"]["exercises"][topic]["content"][i]["value"])
                    i+=1
        if topic+1 == len(deta["course"]["exercises"]):
            print("topic is completed.")
            break
    else:
        print("wrong user_input ")
        break


# if (not True and False or False and True and True and False):
#     print('2')
# else:
#     print('6')