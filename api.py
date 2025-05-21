import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)  # Corregido el cálculo

# Calcular la distancia cubierta por una ruta
def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta)-1):
        ciudad1, ciudad2 = ruta[i], ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # Completar el ciclo
    return total

def simulated_annealing(ruta, coord):
    T = 20
    T_MIN = 0.1
    V_enfriamiento = 100

    while T > T_MIN:
        dist_actual = evalua_ruta(ruta, coord)
        for _ in range(V_enfriamiento):
            # Intercambio de dos ciudades aleatoriamente
            i, j = random.sample(range(len(ruta)), 2)
            ruta_tmp = ruta[:]
            ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
            dist_tmp = evalua_ruta(ruta_tmp, coord)

            delta = dist_actual - dist_tmp
            if dist_tmp < dist_actual or random.random() < math.exp(delta/T):
                ruta = ruta_tmp[:]
                dist_actual = dist_tmp

        T *= 0.95  # Enfriamiento exponencial
    
    return ruta

if __name__ == "__main__" :
    coord = {
        'Jiloyork' :(19.916012, -99.580580),
        'Toluca':(19.289165, -99.655697),
        'Atlacomulco':(19.799520, -99.873844),
        'Guadalajara':(20.677754472859146, -103.34625354877137),
        'Monterrey':(25.69161110159454, -100.321838480256),
        'QuintanaRoo':(21.163111924844458, -86.80231502121464),
        'Michohacan':(19.701400113725654, -101.20829680213464),
        'Aguascalientes':(21.87641043660486, -102.26438663286967),
        'CDMX':(19.432713075976878, -99.13318344772986),
        'QRO':(20.59719437542255, -100.38667040246602)
    }

    # Crear una ruta inicial aleatoria
    ruta = list(coord.keys())
    random.shuffle(ruta)

    ruta_optima = simulated_annealing(ruta, coord)
    print(ruta_optima)
    print("Distancia Total:", evalua_ruta(ruta_optima, coord))
