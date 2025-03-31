class Edad:
    def __init__(self, edades):
        self.edades = edades
    
    def calcular_media(self):
        return sum(self.edades) / len(self.edades)
    
    def mostrar_media(self):
        return f"La media de las edades es: {self.calcular_media():.2f}"

def main():
    edades = []
    
    while True:
        try:
            edad = int(input("Ingrese una edad (0 para terminar) => "))
            if edad == 0:
                break
            edades.append(edad)
        except ValueError:
            print("Error: Debe ingresar un número válido")
    if(not edades):
        print("No se ingresaron edades")
        return
    edad_obj = Edad(edades)
    print(edad_obj.mostrar_media())
    
if __name__ == "__main__":
    main()

