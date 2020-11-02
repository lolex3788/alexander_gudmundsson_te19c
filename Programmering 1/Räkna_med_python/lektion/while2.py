# Mjölkuppgift - while

# 1L mjölk 1 500 000 bakterier i rumstemp.

# Bakterier ökar med 50%/timme i rumstemp.

# Mjölk surnar när vi har mer än 10 000 000 st.

# Hur många timmar tar det tills mjölken surnar?

import matplotlib.pyplot as plt
import numpy as np

bakterier = 1.5*10**6
sur = 1e7
faktor = 1.5
timmar = 0

y_bakterier = [bakterier] #lista som ska hålla bakteriernas förändring.

while bakterier < sur:
    bakterier = faktor*bakterier
    timmar += 1
    y_bakterier.append(bakterier) # lägger till bakterier till våran lista

x_timmar = np.arange(timmar + 1)

print(x_timmar)

print(f"Det tar {timmar}h i rumstemperatur för att mjölken ska surna.")
print(f"x = {x_timmar}")
print(f"y = {y_bakterier}")

plt.plot(x_timmar, y_bakterier)
plt.xlabel("Timmarc(h")
plt.ylabel("Antal bakterier")
plt.title("Bakterietillväxt i mjölk i rumstemperatur")
plt.show()



