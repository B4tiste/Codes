# -*- coding: utf-8 -*-

"""

Created on Mon May 27 16:23:01 2019



@author: Josh

"""

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.image as mpimg

from matplotlib.animation import FuncAnimation

import matplotlib.animation as animation

import time as t

#iterations = int(input("Entrez le nombre d'itérations souchaitées (jupiter : periode de révolution de 4380 jours)\n"))
iterations = 200

j = 0


def convertingOrbitalElements(a, e, i, Omega, omega, M, E):
    X = a*(np.cos(E) - e)
    Y = a * np.sqrt(1 - e**2) * np.sin(E)

    Vector = np.array([[X],
                       [Y],
                       [0]])

    pos = R3(-Omega)@R1(-i)@R3(-omega) @ Vector

    position = []

    for i in range(pos.shape[0]):
        position.append(pos[i, 0])

    return position


def convertingOrbitalElementsSpeed(a, e, i, Omega, omega, M, E):
    n = k/np.sqrt(a**3)
    r = a*(1 - e*np.cos(E))
    Xdot = - (n*a**2)/r * np.sin(E)
    Ydot = (n*a**2)/r * np.sqrt(1 - e**2) * np.cos(E)

    Vector = np.array([[Xdot],
                       [Ydot],
                       [0]])

    vit = R3(-Omega)@R1(-i)@R3(-omega) @ Vector

    vitesse = []

    for i in range(vit.shape[0]):
        vitesse.append(vit[i, 0])

    return vitesse


def R1(theta):
    M = np.array([[1, 0, 0],
                  [0, np.cos(theta), np.sin(theta)],
                  [0, -np.sin(theta), np.cos(theta)]])

    return M


def R3(theta):
    M = np.array([[np.cos(theta), np.sin(theta), 0],
                  [-np.sin(theta), np.cos(theta), 0],
                  [0, 0, 1]])

    return M


def calculateE(E, e, M):  # faire converger E à chaque fois en partant de M (askip 6 iterations suffisent)
    #M = M0 + n(t - t0)
    E = M
    for i in range(6):
        E = E - (E - e*np.sin(E) - M)/(1 - e*np.cos(E))
    return E


def calculateM(t):
    n = k/np.sqrt(aJ**3)
    M = M_0_J + n*(t)
    return M


def JupiterPos(t):
    T = 2*np.pi * np.sqrt((aJupiter**3)/(G))
    theta = (2*np.pi * t)/T

    return [aJupiter*np.cos(theta), aJupiter * np.sin(theta), 0]


aTerre = 3.27


G = (4 * (np.pi)**2) / (365.25636567**2)
k = np.sqrt(G)


masseSolaire = 1.9884e30

masseSoleil = 1

masseTerre = 3.0024e-6

masseJupiter = 1/1047.3486


# data for the asteroid :

aP = 5.454
eP = 0.3896
iP = 108.358 * np.pi/180
omegaP = 226.107 * np.pi/180
OmegaP = 276.509 * np.pi/180
M_0_P = 146.88 * np.pi/180
E_P = calculateE(M_0_P, eP, M_0_P)


XTerre = aTerre

YTerre = 0

ZTerre = 0


#positionTerre = [XTerre, YTerre, ZTerre]
positionTerre = convertingOrbitalElements(
    aP, eP, iP, OmegaP, omegaP, M_0_P, E_P)
vitesseTerre = convertingOrbitalElementsSpeed(
    aP, eP, iP, OmegaP, omegaP, M_0_P, E_P)


#VXTerre = 0
#
#VYTerre = np.sqrt(G)/np.sqrt(aTerre)
#
#VZTerre = 0
#
#vitesseTerre = [VXTerre, VYTerre, VZTerre]


positionSoleil = [0, 0, 0]


xJupiter = 5.2

yJupiter = 0

zJupiter = 0


Jupiter = [xJupiter, yJupiter, zJupiter, 0, 0, 0]

aJupiter = 5.2  # en UA


Xs = 0

Ys = 0

Zs = 0


h = 1


# conditions initiales Jupiter :

aJ = 5.202575  # AU
eJ = 0.048908  # e
iJ = 1.3038 * np.pi/180  # deg
OmegaJ = 100.5145 * np.pi/180  # deg
omegaJ = 273.8752 * np.pi/180  # deg
M_0_J = 80.0392 * np.pi/180  # deg
E_j = calculateE(M_0_J, eJ, M_0_J)

print(E_j)

Xgraph = []

Ygraph = []

Zgraph = []


def grav(posI, posJ, posJ2, mJ, mJ2, t):  # somme des forces

    xi = posI[0]

    yi = posI[1]

    zi = posI[2]

    xs = posJ[0]

    ys = posJ[1]

    zs = posJ[2]

#    xj = posJ2[0]
#
#    yj = posJ2[1]
#
#    zj = posJ2[2]

    MJ = calculateM(t)

    E_J = calculateE(E_j, eJ, MJ)

#    posJupiter = JupiterPos(t)
    posJupiter = convertingOrbitalElements(aJ, eJ, iJ, OmegaJ, omegaJ, MJ, E_J)

    Xgraph.append(posJupiter[0])

    Ygraph.append(posJupiter[1])

    Zgraph.append(posJupiter[2])

    xj = posJupiter[0]

    yj = posJupiter[1]

    zj = posJupiter[2]

    x = xi - xs

    y = yi - ys

    z = zi - zs

    aX = (-G * x * 1/(np.sqrt(x**2 + y**2 + z**2))**3)

    aY = (-G * y * 1/(np.sqrt(x**2 + y**2 + z**2))**3)

    aZ = (-G * z * 1/(np.sqrt(x**2 + y**2 + z**2))**3)

    x = xi - xj

    y = yi - yj

    z = zi - zj

    aX += (-G * masseJupiter) * (x/((np.sqrt(x**2 + y**2 + z**2))**3) + xj /
                                 ((np.sqrt(xj**2 + yj**2 + zj**2)**3)))  # 2eme element : on rend le ref galileen

    aY += (-G*masseJupiter) * (y/((np.sqrt(x**2 + y**2 + z**2))**3) +
                               yj/((np.sqrt(xj**2 + yj**2 + zj**2)**3)))

    aZ += (-G*masseJupiter) * (z/(np.sqrt(x**2 + y**2 + z**2))
                               ** 3 + zj/((np.sqrt(xj**2 + yj**2 + zj**2)**3)))

    acceleration = [aX, aY, aZ]

    #print("acceleration = ",acceleration)

    return acceleration


Terre = [positionTerre[0], positionTerre[1], positionTerre[2],
         vitesseTerre[0], vitesseTerre[1], vitesseTerre[2]]

Soleil = [0, 0, 0, 0, 0, 0]

JupiterPosition = convertingOrbitalElements(
    aJ, eJ, iJ, OmegaJ, omegaJ, M_0_J, E_j)
Jupiter = [JupiterPosition[0], JupiterPosition[1], JupiterPosition[2], 0, 0, 0]

print(Jupiter)


def fonction(donnees, posJ, posJ2, mJ, mJ2, t):  # la fonction f de runge-kutta

    resultat = []

    pos = []

    # print(donnees)

    pos.append(donnees[0])

    pos.append(donnees[1])

    pos.append(donnees[2])

    resultat.extend((donnees[3], donnees[4], donnees[5]))

    resultat.extend(grav(pos, posJ, posJ2, mJ, mJ2, t))

    return resultat


#print(fonction(Jupiter, positionEurope, positionSoleil, masseEurope, masseSoleil))


def calcul(donnees, posJ, posJ2, mJ, mJ2, t):  # Runge-Kutta

    k1p = []

    k2p = []

    k3p = []

    k2 = []

    k3 = []

    k4 = []

    Yn = donnees

    k1 = fonction(donnees, posJ, posJ2, mJ, mJ2, t)

    #print("vrai k1 = ", k1)

    for i in range(len(k1)):

        k1p.append(Yn[i] + k1[i] * (h/2))

    k2 = fonction(k1p, posJ, posJ2, mJ, mJ2, t+h/2)

    for i in range(len(k2)):

        k2p.append(Yn[i]+k2[i]*(h/2))

    k3 = fonction(k2p, posJ, posJ2, mJ, mJ2, t+h/2)

    for i in range(len(k2)):

        k3p.append(Yn[i]+k3[i]*h)

    k4 = fonction(k3p, posJ, posJ2, mJ, mJ2, t)

    for i in range(len(k1)):

        k1[i] *= h/6

    for i in range(len(k2)):

        k2[i] *= h/3

    for i in range(len(k3)):

        k3[i] *= h/3

    for i in range(len(k1)):

        k4[i] *= h/6

    #print("new K1 = ", k1)

    #Ynplus1 = Yn + k1 + k2 + k3 + k4

    Ynplus1 = []

    for i in range(len(Yn)):

        a = Yn[i] + k1[i] + k2[i] + k3[i] + k4[i]

        Ynplus1.append(a)

    return Ynplus1


Xgraph = []

Ygraph = []

Xtgraph = []

Ytgraph = []

Xsgraph = []

Ysgraph = []


eParticle = []
aParticle = []


Tj = 4380
pasTemps = iterations
t = 0

while j < iterations:

    if j % 1000 == 0:
        print("Avancement : " + str(j/iterations * 100))

    t += h
    #Jupiter = [5.2*np.cos((2*np.pi * t)/Tj), 5.2*np.sin((2*np.pi * t)/Tj), 0, 0, 0, 0]


#    Xgraph.append(Jupiter[0]) graph is done is "calcul" for now
#
#    Ygraph.append(Jupiter[1])

    Xtgraph.append(Terre[0])

    # on récupère les données pour tracer les trajectoires
    Ytgraph.append(Terre[1])

    Xsgraph.append(Soleil[0])

    Ysgraph.append(Soleil[1])

    positionJupiter = Jupiter[0:3]

    Terre = calcul(Terre, positionSoleil, positionJupiter,
                   masseSoleil, masseJupiter, t)

    positionTerre = Terre[0:3]

    positionSoleil = Soleil[0:3]

    mu = G*masseSoleil

    vTerre = Terre[3:6]
    pTerre = Terre[0:3]

    E = np.linalg.norm((np.cross(vTerre, np.cross(
        pTerre, vTerre)) / mu) - pTerre/np.linalg.norm(pTerre))
    eParticle.append(E)

    A = 1/(2/np.linalg.norm(pTerre) - (np.linalg.norm(vTerre)**2)/mu)
    aParticle.append(A)

    j += 1


temp = [Xtgraph[0], Ytgraph[0]]
# propagate forward and backward
# to prove stability :)

#h *= -1
#
#Xtgraph2 = []
#Ytgraph2 = []
#
#j = 0
# while j <= iterations:
#
#    Xgraph.append(Jupiter[0])
#
#    Ygraph.append(Jupiter[1])
#
#    Xtgraph2.append(Terre[0])
#
#    Ytgraph2.append(Terre[1]) #on récupère les données pour tracer les trajectoires
#
#    Xsgraph.append(Soleil[0])
#
#    Ysgraph.append(Soleil[1])
#
#    #print("Jupiter = ", Jupiter)
#
#    #print("Terre = ", Terre)
#
#    #Jupiter = calcul(Jupiter, positionSoleil, positionTerre, masseSoleil, masseTerre)
#
#    Terre = calcul(Terre, positionSoleil, positionJupiter, masseSoleil, masseJupiter)
#
#    Soleil = calcul(Soleil, positionJupiter, positionTerre, masseJupiter, masseTerre)
#
#    positionTerre = Terre[0:3]
#
#    #positionJupiter = Jupiter[0:3]
#
#    positionSoleil = Soleil[0:3]
#
#
#    j += 1
#
#print(np.linalg.norm(np.array(temp) - np.array([Xtgraph2[-1], Ytgraph2[-1]])))
#
# print(temp)
#print([Xtgraph2[-1], Ytgraph2[-1]])


# %% PLOTTING TIME
# plt.plot(Xgraph,Ygraph, 'b-') #tracer la trajectoire de Jupiter (en bleu)
#
# plt.plot(Xtgraph,Ytgraph, 'r-') #tracer la trajectoire de la Terre (en rouge)
#
# plt.plot(0,0,'yo')


# img = plt.imread("background animation 2.jpg") #pour ajouter des images de fond mais c est trop lent


#fig = plt.figure(figsize=(8,8), dpi=1920/16, frameon = "false")
#
#ax = plt.subplot(111)
##ax2 = plt.subplot(122)
#
#
#ln1, = plt.plot([], [], 'r--')
#ln2, = plt.plot([], [], 'b--')
#pl1, = plt.plot([], [], 'ro')
#pl2, = plt.plot([], [], 'bo')
#sl, = plt.plot([], [], 'yo')
#slLines = plt.plot([], [], 'y--')
#
# ax.set(facecolor = "black") #fond noir, pas mal du tout
#
#ax.plot(Xtgraph, Ytgraph, 'b')
#
# plt.xlim([-9,9])
# plt.ylim([-9,9])
#
#
#
#ax.plot(Xgraph, Ygraph, 'r')
#
#
#
# plt.show()

# pour plot instantannément


T = np.linspace(0, iterations, iterations)

f2 = plt.figure(2)
plt.subplot(121)
plt.plot(T, eParticle)
plt.ylim([0.3, 0.45])
plt.title("eccentricity")
# plt.show()

plt.subplot(122)
plt.plot(T, aParticle)
#plt.ylim([3.2, 3.3])
plt.title("semi major axis")
# plt.show()


Delai1 = 36500
Delai2 = 36500

fig = plt.figure(figsize=(8, 8), dpi=1920/16, frameon="false")

ax = plt.subplot(111)


ln1, = plt.plot([], [], 'r--')
ln2, = plt.plot([], [], 'b--')
pl1, = plt.plot([], [], 'ro', label="Jupiter", ms=7)
pl2, = plt.plot([], [], 'bo', label="Asteroid", ms=7)
sl, = plt.plot([], [], 'yo')
slLines = plt.plot([], [], 'y--')

ax.set(facecolor="black")  # fond noir, pas mal du tout


def init():
    plt.xlim([-9, 9])
    plt.ylim([-9, 9])

    return ln1,


def update(j):
    i = int(j)*150

    if i == 0:
        tracesX1.clear()
        tracesY1.clear()

        tracesXt1.clear()
        tracesYt1.clear()


#    if i % 10 == 0:
#        print("progrès : jour ",i)

    if len(tracesXt1) < Delai2:
        tracesXt1.append(Xtgraph[i])
        tracesYt1.append(Ytgraph[i])

    if len(tracesXt1) < Delai1:
        tracesX1.append(Xgraph[i])
        tracesY1.append(Ygraph[i])

    ln1.set_data(tracesX1, tracesY1)
    ln2.set_data(tracesXt1, tracesYt1)
    pl1.set_data(Xgraph[i+1], Ygraph[i+1])
    pl2.set_data(Xtgraph[i+1], Ytgraph[i+1])
    sl.set_data(Xsgraph[i+1], Ysgraph[i+1])

    return ln1, pl1, ln2, pl2, sl


tracesX1 = []
tracesY1 = []

tracesXt1 = []
tracesYt1 = []

plt.legend(loc="lower left", facecolor="black", labelcolor="white")

myAnimation = animation.FuncAnimation(fig, update,
                                      interval=10, frames=iterations - 1,
                                      init_func=init, blit=True, repeat=False)



plt.show()


#myAnimation.save('perturbatedAsteroid.mp4', writer = "ffmpeg", fps = 60, dpi = 1920/16)
