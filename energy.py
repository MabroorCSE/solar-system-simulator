#Runs the simulation headless and graphs total energy over time

import matplotlib.pyplot as plt

from bodies import create_bodies
from physics import apply_gravity
from constants import SUN_MASS, G, epsilon, SUBSTEPS

STEPS = 20000

def kinetic_energy(Bodies):
    total_kinetic_energy = 0
    for i in range(len(Bodies)):
        total_kinetic_energy += 0.5 * Bodies[i].mass * Bodies[i].velocity.dot(Bodies[i].velocity)
    return total_kinetic_energy


def potential_energy(Bodies):
    total_potential_energy = 0

    for i in range(len(Bodies)):
        for j in range(i + 1, len(Bodies)):
            displacement = Bodies[j].position - Bodies[i].position
            dist_squared = displacement.dot(displacement)
            total_potential_energy += -G * Bodies[i].mass * Bodies[j].mass / (dist_squared + epsilon**2)**0.5


    return total_potential_energy

Bodies = create_bodies(SUN_MASS)

kinetic, potential, total = [], [], []
for step in range(STEPS):
    ke = kinetic_energy(Bodies)
    pe = potential_energy(Bodies)
    kinetic.append(ke)
    potential.append(pe)
    total.append(ke + pe)
    for _ in range(SUBSTEPS):
        apply_gravity(Bodies, 1 / SUBSTEPS)

E0 = total[0]
drift = [100 * (E - E0) / abs(E0) for E in total]
print(f"Initial energy: {E0:.2f}")
print(f"Max drift: {max(drift, key=abs):+.4f}%   Final drift: {drift[-1]:+.4f}%")

#Plot: components on top, relative drift of total below
plt.rcParams.update({"font.size": 10, "axes.edgecolor": "#c3c2b7",
                     "axes.labelcolor": "#52514e", "xtick.color": "#52514e",
                     "ytick.color": "#52514e"})
fig, (top, bottom) = plt.subplots(2, 1, figsize=(10, 7), sharex=True,
                                  facecolor="#fcfcfb", height_ratios=[3, 2])

for ax in (top, bottom):
    ax.set_facecolor("#fcfcfb")
    ax.grid(color="#e8e7e2", linewidth=0.8)
    ax.spines[["top", "right"]].set_visible(False)

top.plot(kinetic, color="#2a78d6", linewidth=1.5, label="Kinetic")
top.plot(potential, color="#eb6834", linewidth=1.5, label="Potential")
top.plot(total, color="#1baf7a", linewidth=2, label="Total")
top.axhline(0, color="#a5a49d", linewidth=0.8)
top.set_ylabel("Energy (sim units)")
top.set_title("Energy over time", loc="left", color="#0b0b0b", fontsize=13)
top.legend(frameon=False, loc="upper right", labelcolor="#0b0b0b")

bottom.plot(drift, color="#1baf7a", linewidth=1.5)
bottom.axhline(0, color="#a5a49d", linewidth=0.8)
bottom.set_ylabel("Total energy drift (%)")
bottom.set_xlabel("Step")

fig.tight_layout()
fig.savefig("energy.png", dpi=150)
print("Saved energy.png")
