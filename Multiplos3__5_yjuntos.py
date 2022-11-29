# /*
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

def main():
   for i in range(1,100):
       divi3 = i % 3 == 0
       divi5 = i % 5 == 0

       if divi3 and divi5:
           print("fizzbuzz")
       elif divi3:
           print("fizz")
       elif divi5:
           print("buzz")
       else:
           print(i)


if __name__ == "__main__":
    main()
