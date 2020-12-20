
f = open('ERR486827_1.fastq')

contenido = f.read()
lineas = contenido.splitlines()

i = 0
archivo = ""
while i + 1 < len(lineas):
    archivo += lineas[i].replace('@', '>') + "\n"
    archivo += lineas[i+1] + "\n"
    i = i + 4

f = open('ERR486827_1.fasta', 'w')
f.write(archivo)
f.close()

secuencias = archivo.split('>')
print("Cantidad de secuencias: ", len(secuencias) - 1)

i = 1
N = 0
total = 0

while i < len(lineas):
    N = N + 1
    total = total + len(lineas[i])
    i = i + 4

print("Promedio de longitud de secuencias: ", total/N)
