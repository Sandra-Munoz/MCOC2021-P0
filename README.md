# MCOC2021-P0

# Mi computador principal

* Marca/modelo: MacBook Air 
* Tipo: Notebook
* Año adquisición: 2014
* Procesador:
  * Marca/Modelo: Intel Core i5-4260U
  * Velocidad Base: 1.40 GHz
  * Velocidad Máxima: 1.40 GHz
  * Numero de núcleos: 2 
  * Humero de hilos: 4
  * Arquitectura: x86 Haswell
  * Set de instrucciones: 
* Tamaño de las cachés del procesador
  * L3: 3 MB
* Memoria 
  * Total: 4 GB
  * Tipo memoria: DDR3
  * Velocidad 1600 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica
  * Marca / Modelo: HD Gragics 5000
  * Memoria dedicada: 
  * Resolución: 1366 x 768
* Disco 1: 
  * Marca: Samsung
  * Tipo: SSD
  * Tamaño: 
  * Particiones: 5
  * Sistema de archivos: MS-DOS FAT32
* Disco 2: 
  * Marca: Samsung
  * Tipo: SSD
  * Tamaño: 
  * Particiones: 2
  * Sistema de archivos: MS-DOS FAT32

  
* Dirección MAC de la tarjeta wifi: 64:76:ba:a8:c6:70
* Dirección IP (Interna, del router): 
* Dirección IP (Externa, del ISP): 
* Proveedor internet: Mi Internet 

# Entrega 2

* ¿Cómo difiere del gráfico del profesor/ayudante?
* La diferencia se da en l velocidad, ya que en mi caso, el gráfico, parte en aproximadamente 1s en el Tiempo transcurrido, y el termino en 1 minuto aproximadamente. Esto se da ya que, e procesador de mi comptador tiene una velocidad menor, lo que genera un mayor tiempo en la ejecución del código.

* ¿A qué se pueden deber las diferencias en cada corrida?
* Pueden haber varios factores qeu interfieran en la diferencia entre cada corrida, ya que el computador puede estar trabajando simultaneamente. Por ejemplo el uso del navegador de internet, el mail, etc, en simultaneo mientras se esta ejecutando el codigo. Tambien, se puede deber a que los procesadores entre computadores son distintos, por lo que la capacidad entre un comptador y otro no es la misma.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
* El tiempo en el que se demora cada ciclo va a depender de la cantidad de cosas que esté realizando el computador al momento de ejecutar cada uno. Mientras que, el proceso que realiza al ejecutar el codigo es siempre el mismo, por lo que en cada ciclo llega a donde mismo, por lo que el gasto siempre será el mismo.

*¿Qué versión de python está usando? Python 3.8.8 MSC v.1916 64 (AMD64)

*¿Qué versión de numpy está usando? 1.20.1

*Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 

![Captura de Pantalla 2021-08-06 a la(s) 11 38 57](https://user-images.githubusercontent.com/88350644/128535297-ff707174-9adf-426d-9076-d8d7814179c2.png)

* Gáfico

![Figure 2021-08-06 104301](https://user-images.githubusercontent.com/88350644/128534126-db006774-09c3-4f42-8cc8-0253d5d2f29e.png)



# Entrega 3

Caso 1 - Half: 
![Rendimiento caso 1 half](https://user-images.githubusercontent.com/88350644/129988921-a13cd09e-317b-40ad-93d4-e43e84032ca0.png)


![Rendimiento caso 1 single](https://user-images.githubusercontent.com/88350644/129988943-8652954c-ab8b-4d44-987b-370de3697838.png)


 ![Rendimiento caso 1 double](https://user-images.githubusercontent.com/88350644/129988970-4baea4ac-85e9-4eec-88b9-3a94985f7c15.png)


 ![Rendimiento caso 1 longdouble](https://user-images.githubusercontent.com/88350644/129988994-f7de4c72-8cee-4a5b-a40e-6a2f7ea93660.png)


 ![Rendimiento caso 2 half](https://user-images.githubusercontent.com/88350644/129989010-883a1321-6159-4fcc-81db-fefdd02f9914.png)


 ![Rendimiento caso 2 single](https://user-images.githubusercontent.com/88350644/129989038-1b032c24-377d-4d4f-969c-db5d723d8514.png)


 ![Rendimiento caso 2 double](https://user-images.githubusercontent.com/88350644/129989077-fb5a6cb6-d7e4-48b9-bcc9-66f4908453ee.png)


 ![Rendimiento caso 2 longdouble](https://user-images.githubusercontent.com/88350644/129990022-2272b6aa-d4e0-48c6-a208-ddecd3ff1e13.png)


 ![Rendimiento caso 3 half](https://user-images.githubusercontent.com/88350644/129990047-eddde346-7f9b-4a18-9e84-dc9d4a4c56a2.png)


 ![Rendimiento caso 3 single](https://user-images.githubusercontent.com/88350644/129990075-c986556e-f51c-45a4-9669-d7588cb62c9c.png)


 ![Rendimiento caso 3 double](https://user-images.githubusercontent.com/88350644/129990090-bd4f1a76-a22c-4d3d-9343-d17901a5a792.png)


 ![Rendimiento caso 3 longdouble](https://user-images.githubusercontent.com/88350644/129990102-a176803b-d910-4457-bd5e-cb33eaac7087.png)



# Entrega 4

* ¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo? ¿Qué algoritmo gana (en promedio) en cada caso? ¿Depende del tamaño de la matriz? ¿A que se puede deber la superioridad de cada opción? ¿Su computador usa más de un proceso por cada corrida? ¿Que hay del uso de memoria (como crece)? 

* Al comparar el tiempo entre el uso de eigh y solve, eigh toma un tiempo considerable al ejecutar el codigo cuando la matriz es grande, como al utilizar N=10000. Este tiempo es mucho mayor que el que se gasta al utilizar solve.
* En cuanto al algoritmo que gana en promedio, se puede decir que ese es solve, ya que es mucho mas eficiente, debido que, para un N=8000, que fue el maximo valor para realizar la matriz, el tiempo promedio que tomo el codigo en ejecutar fue de aproximadamente 20 a 30 segundos, a diferencia de eigh que uso un teimpo promedio de aproximandamente 2,5 minutos para el mismo N.
* El tiempo de ejecución sí depende del tamaño de la matriz, ya que mientas más grande sea esta, mayor será el tiempo que tarde el codigo en finalizar.

# Entrega 5 

* Código matriz laplaciana.


def matriz_laplaciana(N,t=double):
     e=eye(N)-eye(N,N,1)
     return t(e+e.T)

for i in range(10):
    
    for N in Ns:
       
        t1=perf_counter()
        A=matriz_laplaciana(N)
        b=matriz_laplaciana(N)
        Acsr1=sparse.csr_matrix(A)
        Acsr2=sparse.csr_matrix(b)
        t2=perf_counter()
        x=Acsr1@Acsr2
        t3=perf_counter()
        
        dt=t2-t1 #tiempo ensamblado
        dt2=t3-t2 #tiempo de solución
        Dts.append(dt)
        Dts2.append(dt2)
        

* Matriz llena:

 ![plot matriz llena](https://user-images.githubusercontent.com/88350644/131199295-cff9cbcd-bdc1-4b5f-b057-5359f8e82c55.png)

* Matriz dispersa:

![plot matriz dispersa](https://user-images.githubusercontent.com/88350644/131199469-c2d03510-ec8b-42a6-b3a6-4e384740b060.png)

* En relación a los resultados obtenidos, se puede ver que el tiempo que demora la multiplicación es bstante menor en la matriz dispersa, lo que se debe principalemente a que en esta, no se consideran los ceros como es en la matriz llena, lo que hace que el teimpo se reduzca considerablemente. 


# Entrega 6

* Código matriz laplaciana para inversa de matriz llena

def matriz_laplaciana(N,t=double):
     e=eye(N)-eye(N,N,1)
     return t(e+e.T)

for i in range(10):
    
    for N in Ns:
       
        t1=perf_counter()
        A=matriz_laplaciana(N)
        b=matriz_laplaciana(N)
        Acsr1=sparse.csr_matrix(A)
        Acsr2=sparse.csr_matrix(b)
        t2=perf_counter()
        x=inv(A)
        t3=perf_counter()
        
        dt=t2-t1 #tiempo ensamblado
        dt2=t3-t2 #tiempo de solución
        Dts.append(dt)
        Dts2.append(dt2)

* Para el caso de solve, la matriz dispersa fue la que más se demoró en completar los diez ciclo, en aproximadamente 4350 segundos, mientras que la matriz llena en completar los diez ciclos ocupo un tiempo de 2300 segundos aproximadamente.
* En cuanto al caso Inv, el tiempo que demoró la matriz dispersa fue de aproximadament 4500 segundos y la matriz llena 7500 segundos aproximadamente.
* Esto indica que el mejor método es utilizando solve, ya que el tiempo que domoraron en completarse los 10 ciclos en la matriz dispersa y llena son menores que usando Inv
* Para Inv en la matriz llena cada uno de los ciclos tienen tiempos casi iguales, lo que hace que se bastante estable. Para la matriz dispersa en promedio, entre un ciclo y otro hubo una variacion de 0,4 segundos en cada uno de los N de la matriz, lo cual, aun que sea una diferencia minima, si es considerable em el tiempo final una vez terminados los 10 ciclos 
* Para solve, la matriz llena, tiene diferencias de menos de 0,1 segundos por cada N en los 10 ciclos, lo cual no genera mayores aumentos en el tiempo final una vez terminados los 10 ciclos, a diferencia de la amtriz dispersa que hay un tiempo aproximado de 0,5 segundos de diferencia entre cada N de cada ciclo.

* Matriz llena Solve:

![Plot matriz llena solve](https://user-images.githubusercontent.com/88350644/132080687-bfe64233-13ef-4617-8ac3-bf257f4808ca.png)

* Matriz llena Inv:

![Plot Matriz llena inv](https://user-images.githubusercontent.com/88350644/132080706-12de89c3-b424-45b2-90e6-1762f6a9ee3f.png)

* Matriz dispersa Solve:

![Plot Matriz dispersa solve](https://user-images.githubusercontent.com/88350644/132080729-4bcfdf37-8bed-4152-95b6-357deb202ee5.png)

* Matriz dispersa Inv:

![Plot Matriz dispersa Inv](https://user-images.githubusercontent.com/88350644/132080734-5c2f4911-5194-402d-aabb-2674e56a35bc.png)


