# Rails

## Convenções

É um framework web que permite um desenvolvimento agil porém ele tem uma forma bem rigida de programar onde o dev precisa seguir suas convenções para extrair o maximo rendimento, ele usa massivamente geradores para tudo que vc precisar e as principais convenções são:

- views que atendem um metodo de um controller devem ficar no caminho

``` bash
app/views/nome_do_controller/nome_do_metodo_do_controller.html.erb
```

- variaveis de instancia - *@var* - criadas no metodo do controller estarão automaticamente disponiveis para serem usadas na views
- metodos ruby escritos no helper application estarão disponiveis em todo o sistema e metodos escritos nos helpers com nome de recurso estarão disponíveis no controler, models e views do recurso especifico
- nos métodos a ultima linha sempre é retornada como se fosse precedida implicitamente por um return, se precisar usar o return no meio de um metodo ele tambem está disponivel

### criar projeto

Para criar um novo projeto em rails existem as seguintes opções:

```bash
rails new app_name # novo projeto com configs default
rails new app_name --database=mysql # pré definindo o db
rails new app_name -api # nova api
rails new app_name -m https://raw.github.com/RailsApps/rails-composer/master/composer.rb # novo projeto com rails composer, uma espécie de wizard que te ajuda a deixar tudo configurado
```

Loga após cria faça ...

``` bash
cd nome_projeto         #entra na pasta
bundle install          #instala as dependencias
```

No arquivo config/database.yml vc deve colocar as configurações de acesso ao seu bd e rodar

``` bash
rails db:create         #cria o banco de dados
```

## Generator

### Scaffold

``` bash
rails generate scaffold User name:string description:text age:integer cpf:integer:uniq username:string{30}:uniq social_class:references birthday:datetime active:boolean
```

Esse comando irá criar model(User), migration(users), tabela no banco(users), fixture, helper, controller, views, assets (js, sass) e tests para todo o CRUD de users e ainda adicionará a rota recurso no começo de seu arquivo de rotas. De acordo com os campos passados sua tabela no banco será criada com as seguintes colunas:

- name (varchar 255)
- description (text)
- age (int)
- cpf (int, unique)
- username (varchar 30)
- social_class_id (integer, not null, que vai guardar o id da relação com social_classes)
- birthday (datetime)
- active (boolean)

#### Outros tipos que podem ser usados no scaffold

- integer
- primary_key
- decimal
- float
- boolean
- binary
- string
- text
- date
- time
- datetime
- timestamp

Caso precise alterar colunas no recurso criado gere um migração com a seguinte estrutura no comando generate.
por exemplo, se voce quiser adicionar a coluna nome a tabela pessoas, e nome é do tipo string, seria assim:

```bash

rails g migration add_nome_to_pessoas nome:string

#o generate migration funciona da seguinte forma: verbo(add/remove/change),nome da coluna, to/from, nome da tabela no plural e depois um espaço e o nome da coluna:tipo da coluna.
```

Caso precise remover um recurso adicionado com scaffold faça

```bash
rails destroy scaffold ModelName
```

## Rotas

O arquivo de rotas fica em *config/routes.rb*, ele aceita os seguintes tipos de rotas

``` ruby
get 'welcome/hello' # verbo 'controller/metodo'
root 'posts#index' # rota default do projeto
resources :posts # rota recurso (laravel like)
```

## Validações

no rails as validações ficam no model, um exemplo de como tornar o campo 'title' obrigatorio é adicionar no model do recurso o seguinte:

``` ruby
validates_presence_of :title #title agora é required nesse recurso
validates_uniqueness_of :titulo # o title deve ser unico na tabela
validates_presence_of :nome, message: 'não pode ser deixado em branco'
validates :email, presence: {message: 'não pode ser deixado em branco'}, length: {minimum: 10, message: 'deve ter pelo menos 10 caracteres'}, uniqueness: {message: 'deve ser único'} # varias validações para um campo
validates_length_of :telefone, maximum: 11, message: 'deve ter até 11 caracteres'
validates_length_of :endereco, in: 10..100, message: 'deve ter entre 10 e 100 caracteres'
validates_numericality_of :idade, message: 'deve ser um número'

validates_length_of :cpf, :is => 11, :allow_blank => true # o numero deve ter exatamente 11 digitos mas é permitido valor em branco
```

Com as validações criadas no model fica disponivel para você o metodo valid? que retorna um boolean informando se o objeto passa em todas as validações ou não

``` ruby
post.valid? # true/false de acordo com o resultado nos testes de validações do model
```

## Seeders

Seeders servem para popular seu banco de dados a fim de ter dados para fazer suas funcionalidades sem precisar inseri-los na mão toda vez que instala uma nova instancia do app, eles ficam em *db/seeds.rb* e usam a seguinte sintaxe:

``` ruby
movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])

Character.create(name: 'Luke', movie: movies.first)

Product.create(name: 'Apple', price: 1)
Product.create(name: 'Orange', price: 1)
Product.create(name: 'Pineapple', price: 2.4)
Product.create(name: 'Marble cake', price: 3)
```

Se a sua intenção for apenas popular o banco com dados fakers para simular o funcionamento do app vc pode fazer algo assim:

``` ruby
# criando 50 posts no banco (aprender gem faker)
50.times do |i|
    Post.create(title: "Titulo de um post #{i}", body: "Corpo de um post #{i}")
end
```

Após configurá-los com seus dados vc pode rodá-los com o comando

``` bash
rails db:seed #popula o banco
```

## Dicas

Você pode ativar um console interativo com seu projeto carregado digitando

``` bash
rails console
```

para resetar um banco de dados *nunca faça isso em produção*

``` bash
rails db:drop db:create db:migrate #joga o bd fora, cria um novo e cria as tabelas
rails db:seed #popula o banco
```

Você pode visualizar no navegador todas as rotas da aplicação em

``` bash
localhost:3000/rails/info/routes
```

## Simbolos

``` ruby
:exemplo
```

À princípio o conceito de Símbolos pode parecer estranho e
confuso pois trata-se de algo específico de Ruby que você não vai
encontrar na maioria das outras linguagens.

Símbolos são textos iniciados com o sinal de dois pontos “:” - Eles estão presentes por todo o framework Rails (como nos exemplos
de relacionamento entre models que fizemos acima em que usamos
os símbolos :eventos e :categoria)

Pense em símbolos como “String levinhas”: Como tudo na linguagem
Ruby é um objeto, todas as vezes que você cria um string um novo
objeto é instanciado na memória. Os símbolos representam nomes
mas não são tão pesadas como strings.
