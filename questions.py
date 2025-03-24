import random
import os
# Preguntas para el juego
questions = [
"¿Que funcion se usa para obtener la longitud de una cadena en Python?",
"¿Cual de las siguientes opciones es un numero entero en Python?",
"¿Como se solicita entrada del usuario en Python?",
"¿Cual de las siguientes expresiones es un comentario valido en Python?",
"¿Cual es el operador de comparacion para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Indice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#Puntaje del jugador
score = 0

#Se seleccionan tres preguntas al azar
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario debera contestar las tres preguntas seleccionadas
# Se muestra la pregunta y las respuestas posibles

for question, answers, correct_answers_index in questions_to_ask:
    print(question)
    print(*[f"{i + 1}. {answer}" for i, answer in enumerate(answers)], sep="\n")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")

        # Se verifica si el valor ingresado es valido
        if not user_answer.isdigit():
            print("Respuesta no válida. Ingrese un número entre 1 y 4")
            sys.exit(1)

        # Se convierte a entero después de la verificación para comprobar el rango
        user_answer = int(user_answer) - 1

        # Se verifica si el valor ingresado está dentro del rango de respuestas posibles
        if user_answer >= len(answers):
            print("Respuesta no válida. Ingrese un número entre 1 y 4")
            sys.exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == correct_answers_index:
            print("¡Correcto!")
            score += 1
            break
        else:
            print("Incorrecto. Intente de nuevo")
            score -= 0.5
    else:
    # Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es: ", answers[correct_answers_index])

# Se imprime un blanco al final de la pregunta
print()

#Se imprime el puntaje final 
print(f"Tu puntaje final es: {score}")
