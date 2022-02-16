user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done: \n')

# Creamos la variable que almacena el texto
user_input = ''
# Creamos la lista que almacena cada uno de los textos que el usuario ingresa
inputs = []

# Ciclo while
while user_input.lower() != 'done':
    # Verificamos si hay un valor en user_input
    if user_input:
        # Almacenamos ese valor en la lista
        inputs.append(user_input)
    # Capturamos un nuevo valor
    user_input = input('Enter a new value, or done when done: \n')

print(inputs)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

# De la biblioteca time, importamos (traemos) la clase sleep

from time import sleep

# Creamos una lista de 5 números llamada countdown
countdown = [4, 3, 2, 1, 0]

# Para cada número en countdown
for number in countdown:
    #Muestra el número
    print(number)

    # Espera (1segundo)
    sleep(1)

# Muestra el mensaje Blast off
print("Blast off!! 🚀")