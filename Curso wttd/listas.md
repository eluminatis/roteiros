# listas
listas são sequencias mutaveis, ou seja, posso fazer operações que alteram o estado interno dela poe exemplo:

```python
l= ['A','B','C']

l.append('D')
>>> l = ['A', 'B', 'C', 'D']	#append adiciona um item no final da lista
l.sort(reverse=True)
>>> l = ['D', 'C', 'B', 'A']	#sort ordena a lista e o parametro reverse=True inverte a ordem da lista
l.sort()
>>> l = ['A', 'B', 'C', 'D']	#sort sozinho coloca tudo em ordem
```
## ordenação personalizada

### o metodo sorted pode receber no segundo parametro 'key' uma função lambda que mostra como calcular/encontrar o indice para ordenação

#### Para esse exeplo vamos receber uma lista de tuplas e ordenala pelo ultimo item de cada tupla

ex.:

passamos
```python
tuples = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
```
e precisamos que apos ordenado fique assim
```python
tuples = [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
```

a função fica assim:

```python
return sorted(tuples, key=lambda t:t[-1])
```
a função anonima passada em key diz que para cada item da lista pegue seu ultimo elemento

observe que como lista é um objeto mutavel, os metodos mudam seu estado interno e retornam None
listas podem guardar qualquer tipo de objeto e inclusive outras listas
listas no python são muito leves e extremamante perfomaticas, vc pode usar a vontade
