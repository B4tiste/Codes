import matplotlib.pyplot as plt

# Débit
x1 = [
    0.0025,
    0.0021,
    0.0018,
    0.0015,
    0.0013,
    0.001,
    0.0007,
]

# Renolds
x2 = [
    74721,
    62267,
    53965,
    45663,
    37360,
    29058,
    20756,
]

# Pression
y1 = [
    1677.51,
    1167.39,
    961.38,
    706.32,
    451.26,
    304.11,
    176.58,
]

# plot
axe_1 = plt.gca()
axe_2 = axe_1.twiny()

axe_1.plot(x1, y1, "bo", label="Perte de charge = f(Débit)")
axe_1.set_xlabel("Débit (m3/s)")
axe_1.set_ylabel("Perte de charge (Pa)")
axe_1.set_xlim(0, max(x1))
axe_1.set_ylim(0, max(y1))
axe_1.legend(loc="lower right")

axe_2.plot(x2, y1, "ro", label="Perte de charge = f(Reynolds)")
axe_2.set_xlabel("Reynolds")
axe_2.set_xlim(0, max(x2))
axe_2.set_ylim(0, max(y1))
axe_2.legend(loc="upper left")

# plot
plt.show()
