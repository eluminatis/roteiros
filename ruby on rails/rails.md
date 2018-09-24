# Rails
## Convenções
É um framework web que permite um desenvolvimento muito agil porém ele tem uma forma bem rigida de programar onde o dev precisa seguir suas convenções para extrair o maximo rendimento, ele usa massivamente geradores para tudo que vc precisar e as principais convenções são:
- views que atendem um metodo de um controller devem ficar no caminho

``` bash
app/views/nome_do_controller/nome_do_metodo_do_controller.html.erb
```

- variaveis de instancia - *@var* - criadas no metodo do controller estarão automaticamente disponiveis para serem usadas na views
- metodos ruby escritos no helper application estarão disponiveis em todo o sistema e metodos escritos nos helpers com nome de recurso estarão disponíveis no controler, models e views do recurso especifico

## Generator

### criar projeto

``` bash
rails new nome_projeto  #cria o projeto
cd nome_projeto         #entra na pasta
bundle install          #instala as dependencias
```

No arquivo config/database.yml vc deve colocar as configurações de acesso ao seu bd e rodar

``` bash
rails db:create         #cria o banco de dados
```

### criar um recurso para o projeto

``` bash
rails generate scaffold Post title:string body:text
rails db:migrate
```

Esse comando irá criar model, migration, tabela no banco, fixture, helper, controller, views, assets (js, sass) e tests para todo o CRUD de posts com os campos fornecidos acima e ainda adicionará a rota recurso no começo de seu arquivo de rotas.

Caso precise de um scafold com relações de FK mencione o nome do recurso relacionado no singular

``` bash
rails generate scaffold Comment post:references body:text
rails db:migrate
```

## Rotas

Para definir uma rota simples monte seu nome assim

``` ruby
get 'welcome/hello' # verbo 'controller/metodo'
```

## Validações

no rails as validações ficam no model, um exemplo de como tornar o campo 'title' obrigatorio é adicionar no model do recurso o seguinte:

``` ruby
validates_presence_of :title #title agora é required nesse recurso
```

## Dicas
Você pode ativar um cosole interativo com seu projeto carregado digitando

``` bash
rails console
```

para resetar um banco de dados *nunca faça isso em produção*

``` bash
rails db:drop db:create db:migrate db:seed #joga o bd fora, cria um novo, cria as tabelas e as popula
```

Você pode visualizar no navegador todas as rotas da aplicação em

``` bash
localhost:3000/rails/info/routes
```