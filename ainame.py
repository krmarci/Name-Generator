import random

no = int(input("# of names: "))

print("Starting...")

# read namelist

print("Reading list...")

wordcount = 0
totallength = 0
longest = 0

f = open("NevekSzazAngolFerfi.txt", "r", encoding="utf-8")
namelistb = f.read()
namelistb = namelistb.lower()
namelist = namelistb.splitlines()

print("Processing data...")

for i in range(len(namelist)):
    namelist[i] = ";" + namelist[i] + ";"
    wordcount = wordcount + 1
    totallength = totallength + len(namelist[i])
    if len(namelist[i]) > longest:
        longest = len(namelist[i])

averagewordlength = totallength / wordcount

# find list and probabilities of all substrings

comblist = []
combfreq = []
combprob = []

for i in range(longest):
    comb = []
    comb2 = []
    comb3 = []
    for j in range(len(namelist)):
        if len(namelist[j]) >= (i+1):
            for k in range(len(namelist[j])-i):
                substring = ""
                for l in range(i+1):
                    substring = substring + namelist[j][k+l]
                if substring not in comb:
                    comb.append(substring)
                    comb2.append(1)
                else:
                    comb2[comb.index(substring)] = comb2[comb.index(substring)] + 1
    comblist.append(comb)
    combfreq.append(comb2)
    combtotal = 0
    for j in range(len(combfreq[i])):
        combtotal = combtotal + combfreq[i][j]
    for j in range(len(combfreq[i])):
        comb3.append(combfreq[i][j] / combtotal)
    combprob.append(comb3)
    print(i)

#for i in range(len(comblist[1])):
#    print(comblist[1][i] + ": " + str(combfreq[1][i]) + " | " + str(combprob[1][i] * 100) + "%")

def generateFirstLetter(namelist, problist):
    return random.choices(namelist, weights=problist, k=1)

def generateLetter(namestart, comblist, combfreq):
    gnextletter = []
    gcombfreq = []
    for h in range(len(namestart)):
        for i in range(len(comblist)):
            for j in range(len(comblist[i])):
                if namestart[-h-1:] in comblist[i][j]:
                    for k in range(len(comblist[i][j])-h):
                        if namestart[-h-1:] == comblist[i][j][k:k+h+1]:
                            if k+h+1 != len(comblist[i][j]):
                                if comblist[i][j][k+h+1] not in gnextletter:
                                    gnextletter.append(comblist[i][j][k+h+1])
                                    gcombfreq.append(pow(averagewordlength,h))
                                else:
                                    gcombfreq[gnextletter.index(comblist[i][j][k+h+1])] = gcombfreq[gnextletter.index(comblist[i][j][k+h+1])] + pow(averagewordlength,h)
    return random.choices(gnextletter, weights=gcombfreq, k=1)[0]            

def generateName(comblist, combfreq):
    name = ";"
    name = name + generateLetter(name, comblist, combfreq)
    while name[-1] != ";":
        name = name + generateLetter(name, comblist, combfreq)
    name = name[1:-1].capitalize()
    
    return name

print("Generating names...")
namelistoutput = []
namelistexisting = []

for i in range(no):
    name = generateName(comblist, combfreq)
    name2 = ";" + name.lower() + ";"
    while (name2 in namelist) or (name in namelistoutput):
        namelistexisting.append(name)
        name = generateName(comblist, combfreq)
        name2 = ";" + name.lower() + ";"        
    namelistoutput.append(name)
    print(str(i+1) + "/" + str(no))

print()
print("Generated original names:")
print(namelistoutput)
print()
print("Generated existing names:")
print(namelistexisting)
