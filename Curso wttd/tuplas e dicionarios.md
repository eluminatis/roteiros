# Tuplas 

tuplas são sequencias imutaveis, significa que toda operação feita com elas vai retornar um novo objeto

# Dicionarios

dicionarios são hashmaps mutaveis que armazenam chaves e seus valores

para criar um dicionario vc pode

```python
dic = {'nome':'peter', 'sobre':'passos'}

ou

dic = dict( (('nome', 'peterson'),('sobrenome', 'passos)) ) #passando uma tupla de tuplas com 2 itens cada para o construtor dict

ou 

dic = dict(nome='peterson', sobrenome='passos') #passando uma lista de parametros nomeados
```
eles não tem ordem por ser hashmaps, vc pega os indices pelas suas chaves
para verificar se uma chave esta em um dicionario use o operador 'in'
ex.:

```python
if 'b' in alfa:
	# o dic alfa contem b
else:
	# o dic alfa não contem b

if 'b' in dic.values():
	# o dic contem b em seus valores
else:
	# o dic não contem b em seus valores
```

para não retornar erro ao acessar uma chave use o metodo get

```python
dic.get('chave', valor_padrao) # se não achar a chave retorna o segundo parametro e se ele não for passado retorna None
```

para adicionar um novo par de chave:valor a um dicionario use a seguinte sintaxe

```python
dic[nova_chave] = 'novo_valor'

ou

dic.update(nova_chave='novo_valor')
```

para deletar um par use

```python
del dic['chave'] #simplesmente deleta o par chave:valor

ou

c = dic.pop['chave'] #extrai o par do dicionario e o retorna
```

