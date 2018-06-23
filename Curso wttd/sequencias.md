# sequencias

```python
nome = 'henrique'
```

strings no python alem de objetos tb sao sequencias então vc pode tratar ela com funções feitas para sequencias

```python
nome[0]
>>> 'h'
nome[1]
>>> 'e'
nome[7] ou nome[len(nome)-1] ou nome[-1] 
>>> 'e'		#retorna o ultimo elemento

for indice, char in enumerate('peterson'): #enumerate faz com que cada iteração recebe uma tupla com o item e seu n° de indice
    print('letra %s: %s' % (indice, char))

>>> letra 0: p
>>> letra 1: e
>>> letra 2: t
>>> letra 3: e
>>> letra 4: r
>>> letra 5: s
>>> letra 6: o
>>> letra 7: n

```

## slice

```python
nome[0:4] 
>>> 'henr'		#retorna uma fatia da string do 1° ao 4° elemento (perceba que passamos um range de 5(0 a 4) e ele retornou ate antes do 4)

nome[1:-1]
>>> 'enriqu'		#o slice é um intervalo fechado no começo e aberto no final, ele vai ate a posição que vc pediu mas excluindo ela

nome[1:]
>>> 'enrique'		#vc passou final aberto ele vai ate receber um aviso que n tem mais nada p iterar

nome[:4]
>>> 'henr'		#omitindo o 1° parametro o python entende que é desde o começo

nome[:]
>>> 'henrique'		#omitindo o primeiro e o segundo parametros o python entende ('do começo ao fim')

nome[1:7:2]
>>> 'erq'		#o 3° parametro do slice é o step('um pulo de casas')

nome[::2]
>>> 'hniu'		#pegue do começo ao fim pulando de dois em dois

nome[::-1]
>>> 'euqirneh'		#pegue do começo ao fim do fim para o começo
```