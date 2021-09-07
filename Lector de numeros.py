class Convertir_y_Leer_numero():
    def __init__(self, input_numero):
        self.numero = str(input_numero)
    def Convertir(self):
        self.lista = []                                 #lista donde se va a guardar el numero
        if (len(self.numero)) < 11:                     #Verifica si el numero es menor que 1000000000
            for i in range(10):                         
                try:                                    
                    self.lista.append(self.numero[i])   #Agrega a la lista los valores del numero    
                except:                                 
                    self.lista.insert(0,"-")            #Completa el resto de digitos con guiones al inicio de la lista
    def Leer(self):
        leer_resultado=[]                               #Crea una lista en la que se va a guardar el resultado
        resultado = ""
        for i in range(10):
            try:
                valor_actual = self.lista[i]           #Lee un numero a la vez del numero introducido
                valor_siguiente = self.lista[i+1]      #Variable auxiliar que contiene el numero siguiente
            except:
                pass
            #Numeros escritos
            valores_uno=["","cien","doscientos","trescientos","cuatrocientos","quinientos","seiscientos","setecientos","ochocientos","novecientos"]
            valores_dos=["","diez","veinte","treinta","cuarenta","cincuenta","sesenta","setenta","ochenta","noventa"]
            valores_tres=["","y uno","y dos","y tres","y cuatro","y cinco","y seis","y siete","y ocho","y nueve"]
            valores_last=["","uno","dos","tres","cuatro","cinco","seis","siete","ocho","nueve"]
            valores_11_15=["once","doce", "trece", "catorce", "quice"]
            valores_extra=["millones","mil"]
            try:
                if i == 0:                                                          #Valor maximo posible para el programa
                    if int(valor_actual) == 1:
                        leer_resultado.append("Mil millones")
                if i == 1:                                                          #Numero mas alto de millones
                    leer_resultado.append(valores_uno[int(valor_actual)])
                if i == 2:                                                          #Segundo y tercer numero de los millones
                    verificar_11_15 = str(valor_actual) + str(valor_siguiente)      #Verifica si el valor esta entre 11 y 15, ya que se escriben diferente
                    if int(verificar_11_15) > 10 and int(verificar_11_15) <=15:
                        valor = int(verificar_11_15[1])-1
                        leer_resultado.append(valores_11_15[int(valor)])
                        leer_resultado.append(valores_extra[0]) 
                    elif int(verificar_11_15) > 15 or int(verificar_11_15) <=10:
                        leer_resultado.append(valores_dos[int(valor_actual)])
                        leer_resultado.append(valores_tres[int(valor_siguiente)])
                        leer_resultado.append(valores_extra[0])                         #Agrega la palabra millones, despues de leerlos
                if i == 4:                                                          #Numero mas alto de miles
                    leer_resultado.append(valores_uno[int(valor_actual) ])
                if i == 5:                                                          #Segundo y tercer numero de miles
                    verificar_11_15 = str(valor_actual) + str(valor_siguiente)
                    if int(verificar_11_15) > 10 and int(verificar_11_15) <=15:
                        valor = int(verificar_11_15[1])-1
                        leer_resultado.append(valores_11_15[int(valor)])
                        leer_resultado.append(valores_extra[1])    
                    elif int(verificar_11_15) > 15 or int(verificar_11_15) <=10:
                        leer_resultado.append(valores_dos[int(valor_actual)])
                        leer_resultado.append(valores_tres[int(valor_siguiente)])
                        leer_resultado.append(valores_extra[1])                         #Agrega la palabra mil, despues de leerlos
                if i == 7:
                    leer_resultado.append(valores_uno[int(valor_actual)])
                if i == 8:
                    verificar_11_15 = str(valor_actual) + str(valor_siguiente)
                    if int(verificar_11_15) > 10 and int(verificar_11_15) <=15:
                        valor = int(verificar_11_15[1])-1
                        leer_resultado.append(valores_11_15[valor])
                    elif int(verificar_11_15) > 15 or int(verificar_11_15) <=10:
                        leer_resultado.append(valores_dos[int(valor_actual)])
                if i == 9 and (len(leer_resultado)) == 0:
                    leer_resultado.append(valores_last[int(valor_actual)])
                elif i == 9:
                    leer_resultado.append(valores_tres[int(valor_actual)])
            except:
                pass
        for i in range(len(leer_resultado)):
            actual = str(leer_resultado[i])
            resultado += actual
            resultado += " "
        print(resultado)
numero = input("Ingrese un numero entre 0 y 1.000.000.000: ")
try:
    numero = numero.replace(".","")   #En caso de tener . en la entrada los elimina, dejando el numero limpio
except:
    pass    
x = Convertir_y_Leer_numero(numero)
x.Convertir()
x.Leer()