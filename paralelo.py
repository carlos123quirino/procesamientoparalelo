import math, sys, md5, time
import pp

def md5test (hash, start, end):
    "" "Calcula md5 de los enteros entre 'start' y 'end' y lo compara con 'hash'" ""
    para x en xrange (inicio, fin):
        if md5.new (str (x)). hexdigest () == hash:
            return x

print "" "Uso: python reverse_md5.py [ncpus]
    [ncpus] - el número de trabajadores que se ejecutarán en paralelo,
    si se omite, se establecerá en el número de procesadores en el sistema
"" "

ppservers = ()
#ppservers = (" 10.0 .0.1 ",)

if len (sys.argv)> 1 :
    ncpus = int (sys.argv [ 1 ])
    # Crea jobserver con ncpus trabajadores
job_server = pp.Server (ncpus, ppservers = ppservers)
else :
    # Crea jobserver con número de trabajadores detectado automáticamente
job_server = pp.Server (ppservers = ppservers)

imprimir "Empezando pp con" , job_server.get_ncpus (), "trabajadores"

# Calcula el hash md5 a partir del número dado
hash = md5.new ( "1829182" ) .hexdigest ()
print "hash =" , hash
# Ahora intentaremos encontrar el número con este valor hash

start_time = time.time ()
start = 1
fin = 2000000
partes = 128

pasos = (fin - inicio) / partes 1
trabajos = []

para el índice en xrange (partes):
    starti = start + index * step
    endi = min (start + (index + 1) * paso, fin)
   
para el trabajo en trabajos:
    resultado = trabajo ()
    si resultado:
        interrupción

# Imprimir los resultados
si resultado:
    imprimir " Invertir md5 para ", hash, "is" , result
else :
    print "md5 inverso para" , hash, "no se ha encontrado"

print "Tiempo transcurrido:" , time.time () - start_time, "s"
job_server.print_stats ()