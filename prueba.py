def parar():
    input("Presione <ENTER> para continuar")

def capturar():
    
    try:
        t = float(input("Por favor digite la temperatura: "))
        return t
    except Exception as ex:
        print(f"Error: {ex}")
        return 0

def celsius_fahrenheit(c):
     # F = (C * 9/5) + 32
     return (c * 9/5) + 32

def celsius_kelvin(c):
     # K = C + 273.15
     return c + 273.15

def kelvin_fahrenheit(k):
     # F = (K - 273.15) * 9/5 + 32
     return (k - 273.15) * 9/5 + 32

def kelvin_celsius(k):
     # C = K - 273.15
     return k - 273.15

def fahrenheit_kelvin(f):
     # K = (F - 32) * 5/9 + 273.15
     return (f - 32) * 5/9 + 273.15

def fahrenheit_celsius(f):
     # C = (F - 32) * 5/9
     return (f - 32) * 5/9

def main():
    try:
        continuar = True
        t = 0
        while continuar:
            print("\n--- MENÚ DE CONVERSIÓN ---")
            print("1--> Capturar Temperatura")
            print("2--> Celsius a Fahrenheit")
            print("3--> Celsius a Kelvin")
            print("4--> Kelvin a Fahrenheit")
            print("5--> Kelvin a Celsius")
            print("6--> Fahrenheit a Kelvin")
            print("7--> Fahrenheit a Celsius")
            print("0--> Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                t = capturar()
            elif opcion == '2':
                print(f"{t}°C equivale a {celsius_fahrenheit(t)} °F")
                parar()
            elif opcion == '3':
                print(f"{t}°C equivale a {celsius_kelvin(t)} K")
                parar()
            elif opcion == '4':
                print(f"{t} K equivale a {kelvin_fahrenheit(t)} °F")
                parar()
            elif opcion == '5':
                print(f"{t} K equivale a {kelvin_celsius(t)} °C")
                parar()
            elif opcion == '6':
                print(f"{t}°F equivale a {fahrenheit_kelvin(t)} K")
                parar()
            elif opcion == '7':
                print(f"{t}°F equivale a {fahrenheit_celsius(t)} °C")
                parar()
            elif opcion == '0':
                print("Bye")
                continuar = False
            else:
                print("Seleccione una opción válida")
                
    except Exception as ex:
        print(f"Ocurrió un error: {ex}")

if __name__ == "__main__":
    main()