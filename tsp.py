import math
import random

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def evalua_ruta(ruta, coord):
    total = sum(distancia(coord[ruta[i]], coord[ruta[i+1]]) for i in range(len(ruta)-1))
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # Completar el ciclo
    return total

def simulated_annealing(ruta, coord, T, T_MIN, V_enfriamiento):
    while T > T_MIN:
        dist_actual = evalua_ruta(ruta, coord)
        for _ in range(V_enfriamiento):
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

CITIES = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346253),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163111, -86.802315),
    'Michoacán': (19.701400, -101.208296),
    'Aguascalientes': (21.876410, -102.264386),
    'CDMX': (19.432713, -99.133183),
    'Querétaro': (20.597194, -100.386670)
}
