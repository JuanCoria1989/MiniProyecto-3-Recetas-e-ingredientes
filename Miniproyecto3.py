#Mini Proyecto 3 Juan Coria
#-------------- Inicio creando txt y sacando información transformandola en lista de ingredientes-----------------------
ingredientestxt= open('ingredientes.txt','w', encoding="UTF-8") #Creando el archivo en modo w
ingredientestxt.write("Tomate 5\nLechuga 2\nHamburguesa 10\nCarne 1\nEspárragos 8\nPan 10\nPapa 5\nCebolla 12")
ingredientestxt= open('ingredientes.txt','r', encoding="UTF-8") #Leyendo el archivo y asignandolo a una lista


filaIngredientes=ingredientestxt.readlines()
listadeingredientes=[]
for filatexto in filaIngredientes:
    fila= filatexto.split()
    listadeingredientes.append(fila)

ingredientestxt.close()

#-------------- Fin creando txt y sacando información transformandola en lista de ingredientes-----------------------

#-------------- Inicio Creando CSV y sacando información transformandola en lista de recetas-----------------------
recetacsv= open('recetas.csv','w', encoding="UTF-8") #Creando el archivo en modo w
recetacsv.write("HamburguesaCasera,Hamburguesa,Tomate,Pan\nPastelDeCarne,Carne,Papa,Cebolla\nEnsaladaEspecial,Lechuga,Espárragos,Tomate")
recetacsv= open('recetas.csv','r', encoding="UTF-8") #Leyendo el archivo y asignandolo a una lista

filaRecetas=recetacsv.readlines()
filaRecetasIngrediente=recetacsv.readlines()
listaRecetaIngredientes=[]


for filatextoreceta in filaRecetas:
    filareceta= filatextoreceta.split(",")
    listaRecetaIngredientes.append(filareceta)
    

#---Inicio sacando los saltos de linea-----
for saltodelinea in listaRecetaIngredientes:
    saltodelinea[3]=saltodelinea[3].strip()
#---Fin sacando los saltos de linea-----
    
    
recetacsv.close()
#-------------- Fin Creando CSV y sacando información transformandola en lista de recetas-----------------------

#---Inicio Transformando el segundo valor de las listas en int-----

#print(listadeingredientes[0][1]) el primero tiene que iterar

for i in range(len(listadeingredientes)): #8
    listadeingredientes[i][1] = int(listadeingredientes [i][1])
    #for j in range(len(listadeingredientes[i])):

diccionarioIngredientes=dict(listadeingredientes)
#print(diccionarioIngredientes)
#print(listadeingredientes)

#---Fin Transformando el segundo valor de las listas en int-----

#---Inicio, creando una lista de listas en la lista recetas con su diccionario-----

listaderecetas=[]
for i in range(len(listaRecetaIngredientes)): #3

    listaderecetas.append(listaRecetaIngredientes[i][0])
    del listaRecetaIngredientes[i][0]
    #del listaderecetas [i][1:4]

#del listaderecetas[0][0]
#del listaderecetas[1][0]
#del listaderecetas[2][0]

"""listaRecetaIngredientes.insert(0,listaderecetas[0])
listaRecetaIngredientes.insert(2,listaderecetas[1])
listaRecetaIngredientes.insert(4,listaderecetas[2])"""

diccionarioRecetas= dict(zip(listaderecetas,listaRecetaIngredientes))

#print(listaRecetaIngredientes)
#print(listaderecetas)

#print(diccionarioIngredientes)
#print(diccionarioRecetas['HamburguesaCasera'])

#print(listaderecetas[0][1:4])
#del listaderecetas[]
#---Fin, creando una lista de listas en la lista recetas con su diccionario-----



print("Ingresa la receta que quieres o REPONER :")
#print("PREPARAR")
#print("REPONER")
#print("STOP")
#global entrada
entrada= input().upper()



def stockActual():

    print("Stock actual de los ingredientes disponibles")
    for i,k in diccionarioIngredientes.items():   #range(len(diccionarioIngredientes))
        print(i,k)



while entrada!="STOP":
    
    if entrada[:8]=="PREPARAR":

        entrada= entrada[9:]
        if entrada=="ENSALADAESPECIAL":

            #print(diccionarioRecetas.get("EnsaladaEspecial"))
            print(listaRecetaIngredientes[2])
            #entrada=="EnsaladaEspecial"
            listaInputRecetas= entrada.split()  
            listaInputRecetas[0]="EnsaladaEspecial"
            cadena = " ".join(listaInputRecetas)
            print(cadena)
            print(diccionarioIngredientes)

            if cadena in listaderecetas: #Verifico si la receta ingresada se encuentra en la lista

                
                for i in range(3):
                    print(listaRecetaIngredientes[2][i])
                    variable2=listaRecetaIngredientes[2][i]
                    if diccionarioIngredientes[variable2]==0:
                        print("*** No se puede hacer ", cadena," porque falta :",variable2," ***")
                    else:
                        diccionarioIngredientes[variable2]=diccionarioIngredientes[variable2]-1
 
                print(diccionarioIngredientes)
                stockActual()

                #falta validar cuando no hay stock de un producto
            else: 
                print("no se encuentra")

        elif entrada=="PASTELDECARNE":

            #print(diccionarioRecetas.get("EnsaladaEspecial"))
            print(listaRecetaIngredientes[2])
            #entrada=="EnsaladaEspecial"
            listaInputRecetas= entrada.split()  
            listaInputRecetas[0]="PastelDeCarne"
            cadena = " ".join(listaInputRecetas)
            print(cadena)
            print(diccionarioIngredientes)

            if cadena in listaderecetas: #Verifico si la receta ingresada se encuentra en la lista

                
                for i in range(3):
                    print(listaRecetaIngredientes[1][i])
                    variable2=listaRecetaIngredientes[1][i]
                    if diccionarioIngredientes[variable2]==0:
                        print("*** No se puede hacer ", cadena," porque falta :",variable2," ***")
                    else:
                        diccionarioIngredientes[variable2]=diccionarioIngredientes[variable2]-1
 
                print(diccionarioIngredientes)
                stockActual()

                #falta validar cuando no hay stock de un producto
            else: 
                print("no se encuentra")

        elif entrada=="HAMBURGUESACASERA":

            #print(diccionarioRecetas.get("EnsaladaEspecial"))
            print(listaRecetaIngredientes[2])
            #entrada=="EnsaladaEspecial"
            listaInputRecetas= entrada.split()  
            listaInputRecetas[0]="PastelDeCarne"
            cadena = " ".join(listaInputRecetas)
            print(cadena)
            print(diccionarioIngredientes)

            if cadena in listaderecetas: #Verifico si la receta ingresada se encuentra en la lista

                
                for i in range(3):
                    print(listaRecetaIngredientes[1][i])
                    variable2=listaRecetaIngredientes[1][i]
                    if diccionarioIngredientes[variable2]==0:
                        print("*** No se puede hacer ", cadena," porque falta :",variable2," ***")
                    else:
                        diccionarioIngredientes[variable2]=diccionarioIngredientes[variable2]-1
 
                print(diccionarioIngredientes)
                stockActual()

                #falta validar cuando no hay stock de un producto
            else: 
                print("no se encuentra")




        else:
                print("*** Lo sentimos pero no preparamos ", entrada," ***")
        
        
        
    elif entrada[:7]=="REPONER":

        entrada= entrada[8:]
        #print(entrada)
        listaInputIngredientes= entrada.title().split() 

        #print(listaInputIngredientes)
        try:
            for i in range(len(listaInputIngredientes)):
                variable=listaInputIngredientes[i]

                diccionarioIngredientes[variable]=diccionarioIngredientes[variable]+1

            stockActual()
        except:
            print("Ingresaste un o más ingrediente que no existen o no están dentro del diccionario \nSolo agregaremos si es que hay alguno correcto")
            print("Ingresa la receta que quieres o REPONER :")
            entrada= input().upper()
            print(entrada)
            
    
        

    else:
        #print("Ingrese un comando correcto --Solo los comandos correctos se agregaron--")
        print("Ingresa la receta que quieres o REPONER :")
        entrada= input().upper()
        print(entrada)


    


print("El programa a terminado")