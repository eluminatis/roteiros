# STRINGS

Strings no python são objetos de alto nivel que implementam toda a complexidade do unicode e que devem ser convertidos para unicode para ser transferido para um arquivo ou banco de dados

```python
string.encode()
```
## Métodos

Como string são objetos temos muitos metodos que podem ser usados com ela, lembrando que as strings são imutáveis então você deve pegar o retorno das funções para formar novas strings conforme sua necessidade, nada impede de vc colocar esdda nova string na variavel que vc estava usando

```python	
nome = 'henrique bastos'

nome.capitalize() 	
>>> 'Henrique bastos'	# retorna a string com a primeira letra maiuscula
nome.upper() 		
>>> 'HENRIQUE BASTOS'	# retorna toda a string em letras maiusculas
nome.lower()
>>> 'henrique bastos'	# retorna toda a string em letras minusculas
nome.title()
>>> 'Henrique bastos' 	# retorna a string sendo cada uma de suas palavras com a primeira letra maiuscula 
nome.replace('s','S')
>>> 'Henrique baStoS'	# retorna a string com todas as ocorrrencias do 1° parametro substituidas pelo 2°
nome.split()
>>> ['henrique', 'bastos']	# retorna uma lista de strings formada pela separação da atual nas ocorrencias do caractere passado como parametro que por padrão é o ' '(espaço)
len(nome)		
>>> 15 			# retorna o comprimento da string
nome.strip()
>>> 'henrique bastos'	# retorna a string sem os espaços laterais assim como a trim() do php
```

## Concatenação

```python
nome + ' ' + sobrenome
>>> 'nome sobrenome'	# retorna a concatenação das 2 strings com o espaço no meio
```

Esse processo não é eficiente pois o python trata strings como objetos e concatena uma a uma, para concatenar varias string crie uma string que sera o separador e com ela chame o metodo join() passando a lista das strings que vc quer concatenar

```python
>>> ' '.join(['henrique', 'bastos'])
'henrique bastos'
```

## Impressão formatada
dentro do print() use '%' para demarcar o espaço onde deve ser colocado cada string e apos escreve-la adicione % e uma tupla com as variaveis que vão substituir as demarcações na ordem respectiva

```python
first_name = 'peterson'
last_name = 'passos'
>>> print('%s jorge ferreira dos %s' % (first_name, last_name))
'peterson jorge ferreira dos passos''
```