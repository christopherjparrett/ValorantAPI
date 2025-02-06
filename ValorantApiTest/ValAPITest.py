import requests
import time


APIKEY = 'HDEV-73876480-ff0d-46cf-af3c-89ad95cafa6b'
URL = 'https://api.henrikdev.xyz/valorant/v2/mmr/NA/'

def CallAPI(website):
    time.sleep(2)
    response = requests.get(
        website,
        headers={"Authorization": APIKEY},
    )
    return response

def GetRank(username,tag):
    response = CallAPI(f"https://api.henrikdev.xyz/valorant/v2/mmr/na/{username}/{tag}")
    data = response.json()
    rank = data['data']['current_data']['currenttier']
    return(rank)

# response = CallAPI("https://api.henrikdev.xyz/valorant/v2/mmr/na/ButterCreep/NA1")
# data = response.json()
# print(data)

# print("\n\n\n\
# GetRank("ButterCreep","NA1")
# GetRank("Nipican","7474")

#make dictionary full of stuff we want
PlayerList = []
x=0
with open('C:/Users/butte/Desktop/1CSProjects/ValorantProjects/ValorantApiTest/ValAccounts.txt', 'r') as file:
    line = file.readline()  # Read one line at a time
    while line:
        split = line.strip().split("#")
        tag = split[1].split(" ")[0]
        response = CallAPI(f"https://api.henrikdev.xyz/valorant/v2/mmr/na/{split[0]}/{tag}")
        data = response.json()
        # print(data)
        if('errors' in data):
            PlayerList.append({"User":split[0], "Tag":tag,"RankNum":0,"Rank":"Unknown","NumInRank":0})
        else:
            PlayerList.append({"User":split[0], "Tag":tag,"RankNum":data['data']['current_data']['currenttier'],"Rank":data['data']['current_data']['currenttierpatched'],"NumInRank":data['data']['current_data']['ranking_in_tier']})
        if("Un" in PlayerList[x]['Rank']):
            print(data)
            print(f"{split[0]}#{tag}")
            print("\n\n\n\n\n\n")
        x+=1
        line = file.readline()
        # print(PlayerList)

#now we must sort the list
SortedAccounts = sorted(PlayerList, key=lambda account: (account["RankNum"], account["NumInRank"]))
#print off the accounts in a readable manner
print("Printing accounts from lowest to highest rank:\n")
with open('ValAccounts.txt', 'w') as file:
    x=0
    for account in SortedAccounts:
        x+=1
        print(f"{x}. {(account['User'] + "#" + account['Tag']):<30} -- {account["Rank"]:<9} : {account["NumInRank"]}")
        file.write(f"{(account['User'] + "#" + account['Tag']):<30} -- {account["Rank"]:<9} : {account["NumInRank"]}\n")