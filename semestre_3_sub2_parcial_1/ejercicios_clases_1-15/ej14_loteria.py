import random

elementos = [1,2,3,4,5,6,7,8,9,10,"A","B","C","D","E"]
sorteo = random.sample(elementos, 4)
print(f"Los números/letras ganadores son: {sorteo}")
