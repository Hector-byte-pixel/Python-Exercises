"""
### Contar el número de duplicados

Escribe una función que devuelva la cantidad de caracteres 
alfabéticos y dígitos numéricos distintos, sin distinguir 
entre mayúsculas y minúsculas, que aparecen más de una vez en 
la cadena de entrada. Se puede asumir que la cadena de entrada 
contiene únicamente letras, tanto mayúsculas como minúsculas, y 
dígitos numéricos.

### Ejemplos

"abcde" -> 0 `# ningún carácter se repite más de una vez`
"aabbcde" -> 2 `# 'a' y 'b'`
"aabBcde" -> 2 `# 'a' aparece dos veces y 'b' dos veces (`b`y`B`)`
"indivisibility" -> 1 `# 'i' aparece seis veces`
"Indivisibilities" -> 2 `# 'i' aparece siete veces y 's' aparece dos veces`
"aA11" -> 2 `# 'a' y '1'`
"ABBA" -> 2 `# 'A' y 'B' aparecen dos veces cada uno`
"""

from collections import Counter

def duplicate_count(text):
    return sum([1 for i in Counter(text.lower()).values() if i > 1])

print(duplicate_count("aabb"))