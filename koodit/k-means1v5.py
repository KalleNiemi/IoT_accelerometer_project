import numpy as np
import matplotlib.pyplot as plt

#Ladataan data, ja muodostetaan 2d array

log = np.loadtxt(fname="putty.log")
sensorValues = np.genfromtxt('groupid77data.csv', delimiter=',',usecols=(6,7,8))
#numberOfRows = int(log.size / 3) #näin monta sensori arvoa suoraan intiksi
id = np.genfromtxt('groupid77data.csv', delimiter=',',usecols=(10))
numberOfRows = int(sensorValues.size/3)
safetyStop =0
safetyReset =0
safetyStopper = 2

# print("id77Data: ")
# print(sensorValues)
#print(id77numrow)

#sensorValues= np.reshape(log, (numberOfRows,3)) #muutetaan data 2d arrayksi



# print(sensorValues)

'''
# sensorValues = np.zeros((40,3)) #luodaan taulukko

# x=0;
# y=0;
# c=0;
# for y in range(40):
    
#     for x in range(3):         #pistetään rivi kerrallaan
#         sensorValues[y,x]=log[c]
#         c=c+1
'''

#Sensoriarvojen akselit erillisiin muuttujiin

x = sensorValues[np.arange(numberOfRows), 0]
y = sensorValues[np.arange(numberOfRows), 1]
z = sensorValues[np.arange(numberOfRows), 2]
# print(x) #testataan että ottaahan se varmasti nyt sarakkeen arvot peräkkäin tänne



#Random keskipisteet 4kpl

#centerPoints = np.zeros((4,3))
maxVal = np.amax(sensorValues)
minVal = np.amin(sensorValues)
centerPoints = np.random.randint(maxVal, size=(6,3))
print("Random keskipisteet")
print(centerPoints)

#tulostetaan kuva testidatasta
sV3D = plt.figure().add_subplot(projection='3d')
plt.scatter(x,y,z)
plt.show()

#Init datastructures
totalKierrokset = 100
centerPointCumulativeSum = np.zeros((6,3))  #Tähän summataan aina voittavalle keskipisteelle yhden datapisteen x,y,z komponentit
counts = np.zeros((1,6))        #tänne kasvatetaan aina voittavan keskipisteen datapisteiden lukumäärää yhdellä jokaisen voiton jälkeen
distances = np.zeros((1,6))     #tähän talletetaan laskennan edetessä yksittäisen x,y,z pisteen etäisyys kaikkiin keskipisteet datarakenteessa oleviin 4 keskipisteeseen ja nuo 4 etäisyysarvoa talletetaan tähän muuttujaan
idPointcounter = np.zeros((6,6))   #tähän tallennetaan id hitit per random keskipiste rivit = random keskipiste, sarakkeet on ID
idPoints = np.zeros((1,6))

#Algoritmin toteutus vaiheittan jatkuu...




#print(test1[1])

# def randomScatter():
    # y=1
    # x=0
    # while distance3D(centerPoints[x,:],centerPoints[y,:]) <=10:
        # 
        # 
# 
        # if distance3D(centerPoints[x,:],centerPoints[y,:]) <= 10:


#3D etäisyysfunktio
dif=np.zeros((1,3))

def distance3D(point1, point2):
    for x in range(3):
        dif[0,x]=point2[x]-point1[x]
    pointSum=np.power(dif[0,0],2)+np.power(dif[0,1],2)+np.power(dif[0,2],2)
    P = np.sqrt(pointSum)
    return(P)
'''
#testataan yllä oleva funktio

#test1 = np.array([240,1,240])
#test2 = np.array([240,101,240])
# distanceTest =distance3D(test1,test2)
# print(distanceTest)
'''

print("LOOPIT ALKAA TÄSTÄ:")
print("-------------------")

for kierrokset in range(totalKierrokset):
    #alustetaan
    idPointcounter = np.zeros((6,6))   #tähän tallennetaan id hitit per random keskipiste
    idPoints = np.zeros((1,6))
    centerPointCumulativeSum = np.zeros((6,3))
    counts = np.zeros((1,6))
    distances = np.zeros((1,6))
    previousRound = centerPoints.copy()     #kopsataan keskipisteet myöhempää vertailua varten

    for x in range (numberOfRows):      #kierretään kaikki senosoriarvot
        for y in range(6):
            distances[0,y]=distance3D(sensorValues[x],centerPoints[y])

        min = np.argmin(distances)      #tämä on lyhimmän etäisyyden indeksi positio

        counts[0,min]=counts[0,min]+1   #tässä lisätään counts muuttujaan lyhimmän etäisyyden indeksi positioon +1, uuden keskipisteen laskemista
        centerPointCumulativeSum[min]=centerPointCumulativeSum[min]+sensorValues[x] #tässä on uuden keskipisteen laskemisen toinen vaihe

        #Tässä nyt kerätään tietoa mikä käsiteltävän sensoridatan ID on
        idc=int(id[x])-1
        idPointcounter[min,idc]=counts[0,min]

    #Tämä looppi joko generoi tai laskee uusia keskipisteitä

    for x in range(6):
        if counts[0,x] == 0:#toimii, uudet random pisteet jos saatiin 0 voittoa
            centerPoints[x,:]=np.random.randint(maxVal,size=(1,3)) 
        else: #täällä nyt lasketaan uudet keskipisteet
            centerPoints[x,:]=centerPointCumulativeSum[x,:]/counts[0,x]
        

    print("uudet pisteet")
    print(centerPoints)
    print("Pisteet per keskipiste: ",counts," kierroksella",kierrokset+1)
    print("------------------")
    print(previousRound)
    
    #Safetystopper
    if np.array_equal(previousRound, centerPoints) == False:
        safetyStop = 0
    if np.array_equal(previousRound, centerPoints) == True:
        safetyStop=safetyStop+1
        if safetyStop >> 0:
            safetyReset = safetyReset +1
        if safetyStop == safetyStopper:
            print("Keskipisteet löydetty jo kierroksella ",kierrokset+1-safetyStopper,", lopetetaan rullaaminen.")
            break
    print("safetystop: ",safetyStop)


print("Looppi räpellys tarvottu läpi!")

print("Confusion matrix:")
print("ID: 1    2    3    4    5    6")
print(idPointcounter)

print(" Keskipisteet | ID")
#tämä nyt poimii minkä ID datan omaavia pisteitä on menny mihinkin keskipisteeseen
for x in range(6):
    idPoints[0,x] = int(np.argmax(idPointcounter[x,:])+1)
    print(centerPoints[x],"|",int(idPoints[0,x]))

print("Kierron pysäytin nollattu ",safetyReset-safetyStopper," kertaa.")

#kirjoitetaan header file
cP = np.reshape(centerPoints, (1,18))        
np.savetxt("centerpoints.h", cP, fmt='%i', header="int cP[] = {",delimiter=",", footer="};",comments="")

