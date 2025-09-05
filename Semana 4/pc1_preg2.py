class Nodo:
    def __init__(self,url, pag, hora):
        self.url=url
        self.pag=pag
        self.hora=hora
        self.ant=None
        self.sig=None

class listaDoble:
    def __init__(self):
        self.inicio=None
        self.fin=None

    def agregar(self, url, pag, hora):
        nuevo = Nodo(url, pag, hora)
        if(self.inicio is None):
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.fin.sig = nuevo
            nuevo.ant = self.fin
            self.fin = nuevo

    def mostrar_avanzando(self):
        p=self.inicio
        while p: #Mientra p is not none
            print(p.url, p.pag, p.hora, end=" <==> ")
            p=p.sig
    
    def retroceder(self):
        p=self.fin 
        retro="s"
        while p and retro=="s":
            if p.ant:
                print("\nLa pagina anterior es: ", p.ant.pag)
            else:
                print("\nYa no hay mas paginas...")
            p=p.ant
            retro=input("Desea seguir retrocediendo? [S/N] : ").lower()
    
    def avanzar(self):
        p=self.inicio
        avanza="s"
        while p and avanza=="s":
            if p.sig:
                print("\nLa siguiente pagina es: ", p.sig.pag)
            else:
                print("\nYa no existen mas paginas...")
            p=p.sig
            avanza=input("Desea seguir avanzando? [S/N] : ").lower()

    def buscarU(self,urlB):
        p=self.inicio
        while p:
            if p.url==urlB:
                print("Se encontró el URL buscado: ", p.url)
                break
            else:
                p=p.sig
        return

    def eliminar_por_url(self, urlBuscado):
        p = self.inicio
        while p:
            if p.url == urlBuscado:
                if p.ant:
                    p.ant.sig = p.sig
                else:
                    self.inicio = p.sig
                if p.sig:
                    p.sig.ant = p.ant
                else:
                    self.fin = p.ant
                print("Página eliminada:", p.pag)
                return
            p = p.sig
        print("No se encontró el URL.")

#--------------------------------------

listaD=listaDoble()
#Agregar una nueva pagina al final del historial
def poblar():
        r="s"
        while r=="s":
            url=input("Ingrese su URL: ")
            pag=input("Nombre de la pagina: ")
            hora=input("Hora de ingreso: ")
            listaD.agregar(url,pag,hora)
            r=input("Desea seguir ingresando datos? [S/N] : ").lower()
poblar()
#Retroceder el historial
print("Ingresando a retroceder paginas ")
listaD.retroceder()

#Avanzar el historial
print("Ingresando a avanzar paginas ")
listaD.avanzar()

#Eliminar una pagina por su URL
url_a_eliminar = input("Ingrese el URL de la página que desea eliminar: ")
listaD.eliminar_por_url(url_a_eliminar)


#Buscar una pagina por URL
def buscar():
    print("BUSQUEDA DE PAGINA..")
    datoB=input("Que url desea buscar : ")
    listaD.buscarU(datoB)
buscar()

#Mostrar el historial
print("LISTA COMPLETA...")
listaD.mostrar_avanzando()