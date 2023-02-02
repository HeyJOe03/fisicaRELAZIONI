import numpy as np
from typing import Final as const

raggio_sferetta: const = 0.005 / 2
massa_5sferette_5mm: const = 0.0025494 #kg
massa_sferetta_5mm: const = massa_5sferette_5mm / 5
volume_sferetta_5mm: const = (4.0/3)*np.pi*np.power(raggio_sferetta,3) # 
densita_sferetta: const = round(massa_sferetta_5mm / volume_sferetta_5mm,0)

densita_glicerina: const = 1249 #kg/m3
temperatura: const = 24.5 # °C

v_limite_misurata = 0.1/2.985 # spazio/tempo misurato in misure ed errori

viscosita = 2 * 9.81 * (raggio_sferetta**2) * (densita_sferetta - densita_glicerina) / (9 * v_limite_misurata)

print(f"viscosità misurata: {viscosita}")
aspettazione = np.exp(-2.18-0.099*temperatura)

print(f"viscosità aspettata: {aspettazione}")


# 1.256