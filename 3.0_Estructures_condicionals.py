#0. 
n = 8
if n > 10:
    print('major que 10')
elif n < 10:
    print('menor que 10')
else:
    print('igual que 10')

#1.
n=10
print(10<n)

#2.El codi de sota donarà error. Per avaluar una condició (igual o no) s’ha de fer ús de l’operador ==
#if n = 10

#3. En aquest cas, estem comprovant si el nom de la posició 1 de la llista noms és‘Laura’.
# En cas afirmatiu,s’ha d’imprimir ‘nomcorrecte’ i, en cas contrari, s’ha d’imprimir ‘nomincorrecte’.
noms = ['Ernest', 'Laura', 'Miquel', 'Maria']
if noms[1]=='Laura':
    print('nom correcte')
else:print('nom incorrecte')

# 4.En aquest cas, com si existeix la primera posició en la llista “noms” donarà el resultat de “Ernest està present en noms”
noms = ['Ernest', 'Laura', 'Miquel', 'Maria']

if noms[1] in noms:
    print(noms[1],'està present en noms')
else:
    print(noms[1],'noestàpresentennoms')

#5. Aquí estem avaluant si n és més gran o igual que 10, o bé si n és més petit o igual que 5. En el cas que cap de les dues condicions es compleixi, s’imprimirà ‘major que 5 i menor que 10
if n >= 10:
    print('major o igual que 10')
elif n<=5:
    print('menor o igual que 5')
else:
    print('majorque5imenor que 10')
    
# 6. El que estem fent aquí és, primer, introduir per teclat un nou nom i un número
# Després,  el  número introduït  el  posem  com  a  condició  i,  segons  si  aquest  número  és  menor  o igual que 20, s’afegirà a la llista el nou nom o, en el cas contrari, s’eliminarà el de l’última posició
nom_nou = input()
n=int(input())

noms=['Ernest','Laura','Miquel','Maria']

if n <= 20:
    noms.append(nom_nou)
else:
    noms.pop()

print(noms)

#7. Aquí estem avaluant dos valors de dues claus diferents del diccionari. 
# En el cas que la ciutat sigui Barcelona, s’afegirà una nova clau-valor (‘barri’: ‘Eixample’). 
# A més, també s’avalua sil’edat és menor que 30 i, en el cas que sigui així, el diccionari tindrà una altra parella clau-valor(‘categoria’:‘Jove’).

dades = {'nom': 'Miquel', 'ciutat': 'Barcelona', 'edat': 28}

if dades['ciutat']=='Barcelona':
    dades['barri']='Eixample'

if dades['edat'] < 30:
    dades['categoria']='Jove'

print(dades)

