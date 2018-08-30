# Django admin
no seu urls.py vc pode reescrever as 3 principais variáveis de nome do django-admin
```python
admin.site.site_header = 'My project'                    # default: "Django Administration"
admin.site.index_title = 'Features area'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"
```
Alterando o padrão de campos ManyToMany no admin do django para ficar igual ao de permissões.
```python
#em admin.py da sua app
class EmployeeAdmin(admin.ModelAdmin):
   filter_horizontal = ('field',)
```
Nas listagens que o django-admin cria, ainda é possível definir um, ou vários filtros a serem usados na listagem. Esse recurso permite a visualização apenas do que interessa na listagem ou um subconjunto de dados mais relevante.
```python
#em admin.py da sua app
class MyModelAdmin(admin.ModelAdmin):
   list_filter = ['field_01', 'field_02']
```
Definindo um campo como apenas leitura
```python
#em admin.py da sua app
class MyModelAdmin(admin.ModelAdmin):
   readonly_fields = (''field’,)
```
Personalizando as colunas que aparecem na listagem do django-admin ('index do model')
```python
#em admin.py da sua app
class MyModelAdmin(admin.ModelAdmin):
   list_display = ('nome', 'email')
```
Configure *search_fields* para habilitar uma caixa de busca na página de listagem do admin. Este deve ser configurado com uma lista de nomes de campos que serão afetados pela busca, sempre que alguém submeter um texto por esta caixa de texto.
```python
#em admin.py da sua app
class MyModelAdmin(admin.ModelAdmin):
   search_fields = ('nome', 'email')
```
Você pode também executar uma pesquisa relacionada a ForeignKey com a lookup API “siga” a notação:
```python
#em admin.py da sua app
class MyModelAdmin(admin.ModelAdmin):
   search_fields = ['foreign_key__related_fieldname']
```