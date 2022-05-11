import json

info = 'raw/data.json'
with open(info, 'r') as data:
    res = json.load(data)




class Output:
    
    def get_adress(self, search):
        adresses = []
        for adress in res.keys():
            if search in adress:
                adresses.append(adress)
                
        return adresses, len(adresses)
        
    def get_key(self, written):
        key = ""
        for adress in res.keys():
            if written == adress:
                key = res.get(adress)
        return key
  
class Input:
    def raw_source(self, adress, key):
        comb = {}
        comb[adress] = key
        res.update(comb)
        with open(info, 'w') as data:
            json.dump(res, data)
        return res




tour = Output()
new_adresses = Input()


print("What do u want?")
print("Press \"T\"- to type in or \"S\" - to seach:")
choice = input()
if choice == "S":
    print("Type any letter to find adress:")
    letters = input()
    x, y = tour.get_adress(letters)
    print(x)
    if y == 0:
        print("Sorry, we do not have one like this")
    elif y == 1:
        print("The key is:")
        print(tour.get_key(x[0]))
    else:
        print(f"Select adress from 0 to {y-1}")
        adress = x[int(input())]
        print("The key is:")
        print(tour.get_key(adress))
if choice == "T":
    print("Print adress:")
    new_ad = input()
    print("Print key:")
    new_key = input()
    much = new_adresses.raw_source(new_ad, new_key)
    print("Now our list is by 1 adress bigger and it looks like this:", much)
    



