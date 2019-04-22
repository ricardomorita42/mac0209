import math
import matplotlib.pyplot as plt

def nexty(yt, vt, deltat):
    return yt+vt*deltat

def nextv(vt, g, deltat):
    return vt-g*deltat

f=open("dados/resultados/proc_sensor1.csv", "r")

time = []
ares=[]

for line in f.readlines()[1:]:
    aux = line.split(",")
    aux[3] = aux[3].split("\n")[0]
    time.append(float(aux[0]))
    aresatual = math.sqrt(float(aux[1])**2+float(aux[2])**2+float(aux[3])**2)
    ares.append(aresatual)

plt.plot(time,ares)
plt.show()

v0 = 0
y0 = 0
deltat = 1
g = 10
tfinal = 30

proxy = nexty(y0,v0,deltat)
proxv = nextv(v0,g,deltat)

for i in range(int(tfinal/deltat)):
    proxy = nexty(proxy,proxv,deltat)
    proxv = nextv(proxv,g,deltat)
