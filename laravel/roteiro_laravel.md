# Roteiro Laravel

### Configurações Iniciais

**Criando um projeto:**

Vá com o terminal ate a pasta htdocs

    cd /opt/lampp/htdocs

Digite o comando:

    composer create-project --prefer-dist laravel/laravel nome_projeto

Feito isso, o composer vai baixar o laravel, criar a pasta `nome_projeto` e instalá-lo dentro dele

Você deve dar permissao de escrita para a pasta `storage` que é onde o fw guarda os logs e arquivos. 

Se for trabalhar com uploads crie uma pasta `uploads` dentro de `public`

Verifique qual é o usuário que seu webserver utiliza. No Ubuntu, o usuário do apache é o `www-data`

    # Muda o grupo da pasta para o do apache
    sudo chown -R seu_usuario:www-data public/uploads
    sudo chown -R seu_usuario:www-data storage

    # Aplica as permissões corretas
    sudo chmod -R 774 storage
    sudo chmod -R 774 public/uploads

No netbeans, crie um novo projeto com codigo fonte existente e aponte para a pasta do seu projeto

Crie o banco para seu projeto com a seguinte collation: 

`utf8mb4_unicode_ci` padrão do laravel

Abra o projeto na pasta raiz e abra o arquivo `.env`. Caso não exista, renomeie o `.env.example` para `.env` e insira os seguintes dados:

    APP_URL = url base de seu projeto
    APP_NAME = nome do seu projeto

Inserir também dados de acesso ao database

Altere o timezone default para o BR em: 
    
    config/app.php 
    
    'timezone' => 'America/Sao_Paulo',

### Ajustes finos

Em:

    app/Providers/AppServiceProvider.php@boot

addicionar no método:

    Schema::defaultStringLength(191)

No `namespace`:

    use Illuminate\Support\Facades\Schema; 

Isso evita conflitos de tamanho de string no Banco de Dados MySQL e MariaDB

### Configurando tradução / linguagem / locale

    cd resources/lang/

Clone um projeto de traduçao open do git

    git clone https://github.com/enniosousa/laravel-5.5-pt-BR-localization.git ./pt-br

Para que a tradução entre no seu controle de versão principal faça:
    
    # Remove o repositório do vendor anterior
    rm -r pt-br/.git/


Agora só configurar no `config/app.php`

    'locale' => 'pt-br',

### Adicionando barra de debbug ao projeto (app_debug === true)

    composer require barryvdh/laravel-debugbar

### Inserindo Helper próprio

coloque seu helper dentro da pasta App/MyHelper.php

add ao composer

```javascript
"autoload": {
    "classmap": [
        "database/seeds",
        "database/factories"
    ],
    "psr-4": {
        "App\\": "app/"
    },
    "files": [
        "app/MyHelper.php" //Seu arquivo aqui
    ]
},
```

### Removendo arquivos desnecessários ao controle de versão

Adicione ao .gitignore da pasta raiz as seguintes linhas

```bash
/nbproject //se estiver usando netbeans
/storage/*
```

### Convenções de nomenclatura

Quando você vai criar um `model`, coloque o nome no singular com a primeira letra maiúscula. Ele irá alterar essa string para gerar `controler` e `migration` compatíveis com a nomenclatura padrão

Links de ações colocados em botos nas tabelas de crud devem seguir a seguinte formação

    tabela/{{id_item}}/editar

## Banco de dados

### Criando os dados da aplicação (Migrations)

Nesse ponto você precisa já ter definido todas as tabelas e relações requeridas para sua aplicação. De preferência utilizar algum gerador de MER (Modelo Entidade Relacionamento)

Para cada tabela  necessária a seu app, digite no terminal já dentro da pasta de seu app 

    php artisan make:model –all Models\\NOME
    
onde `NOME` é o nome no singular e com a primeira letra maiuscula de sua classe.

Feito isso, o `artisan` ira criar a `model`, o `controller` e a `migration`, tudo com as convenções de nomenclatura do fw e nas suas respectivas pastas e também registrar os autoloads necessarios.

Abra a migration criada e preencha as colunas necessárias à sua tabela

Rode `php artisan migrate` que serão criadas todas as tabelas das quais você criou as `migrations`

**Estudar melhor os conceitos de migrations**

**Vale lembrar**

Não mexer no `id`.
Por padrão o laravel salva o horario de criação e uúltima edição de cada tupla do banco, 
se quiser manter esse comportamento não delete `timestamps` da migration e caso não precise
retire o `timestamps` e adiciona na model a variavel protected $timestamps = false;

### Principais tipos de dados para colunas na migration:

```php
$table->string('name', 100); // VARCHAR 2° param tamanho opcional
$table->text('description'); // TEXT
$table->longText('description'); // LONGTEXT
$table->integer('votes'); // INT
$table->tinyInteger('votes'); // TINYINT
$table->bigInteger('votes'); // BIGINT
$table->float('amount', 8, 2) // FLOAT 8,2
$table->dateTime('created_at'); // DATETIME
```

**Principais modificadores de colunas:**

```php
$table->integer('votes')->charset('utf8'); // charset da coluna
$table->integer('votes')->collation('utf8_unicode_ci'); //collation da coluna
$table->integer('votes')->comment('my comment'); // comentário da coluna
$table->integer('votes')->nullable(); // aceitar null
$table->string('email')->unique(); //não aceita dois registros com o mesmo valor nessa coluna
```

### Add chave estrangeira

```php
$table->integer('user_id')->unsigned();
$table->foreign('user_id')->references('id')->on('users');
```

a tabela `user` já deve estar criada e a coluna que a referencia também, após isso você pode criar a relação.

adicionar `->ondelete(‘cascade’)` à `fk` para que se um pai for deletado, deletar tambem os filhos, não deixando assim registros orfãos no sistema.

Tabelas pivo devem ser feitas com as models na ordem alfabética `model1_model2`

Caso tenha feito um `php artisan make:model` com nome errado, delete os arquivos e após isso rode um 

    composer dump-autoload

## Integrando o adminLTE

Após ter feito todos os passos anteriores vamos integrar o `adminLTE` ao laravel. Instalar o pacote com o `composer`

    composer require jeroennoten/laravel-adminlte

Adicione o serviço a `config/app.php`

    JeroenNoten\LaravelAdminLte\ServiceProvider::class

Publique os assets públicos

    php artisan vendor:publish --provider="JeroenNoten\LaravelAdminLte\ServiceProvider" --tag=assets

Crie a integração

    php artisan make:adminlte

Publique o arquivo de configurações

    php artisan vendor:publish --provider="JeroenNoten\LaravelAdminLte\ServiceProvider" --tag=config

Rode as migrations para criar as tabelas necessárias ao sistema de autenticação

    php artisan migrate

As configurações de menus e defaults você faz em `config/adminlte`.

Pronto, já está integrado e com sistema de autenticação funcionando. Veja a documentação no repositório

https://github.com/jeroennoten/Laravel-AdminLTE

## Mensagens flash:

São mensagens que ficam na sessão apenas pela próxima requisição, ideal para mensagens de aviso/sucesso ao usuario.

Crie a view `messages/msgs.blade.php` com o seguinte conteudo:

```html
@if ($errors->any())
    <div class="alert alert-danger">
        <ul>
            @foreach ($errors->all() as $error)
            <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif
@if(Session::has('flash_msg'))
    <div class="alert alert-primary text-center">
        <p class="text-bold">{{Session::get('flash_msg')}}</p>
    </div>
@endif
@if(Session::has('flash_msg_primary'))
    <div class="alert alert-primary text-center">
        <p class="text-bold">{{Session::get('flash_msg_primary')}}</p>
    </div>
@endif
@if(Session::has('flash_msg_success'))
    <div class="alert alert-success text-center">
        <p class="text-bold">{{Session::get('flash_msg_success')}}</p>
    </div>
@endif
@if(Session::has('flash_msg_info'))
    <div class="alert alert-info text-center">
        <p class="text-bold">{{Session::get('flash_msg_info')}}</p>
    </div>
@endif
@if(Session::has('flash_msg_warning'))
    <div class="alert alert-warning text-center">
        <p class="text-bold">{{Session::get('flash_msg_warning')}}</p>
    </div>
@endif
@if(Session::has('flash_msg_danger'))
    <div class="alert alert-danger text-center">
        <p class="text-bold">{{Session::get('flash_msg_danger')}}</p>
    </div>
@endif
@if(Session::has('flash_msg_alert'))
    <script>
        alert('{{Session::get("flash_msg_alert")}}');
    </script>
@endif
```

**Criada a view e usada como include nos forms e telas que vc precisa exibir a mensagem basta defini-la antes do redirect com:**

```php
\Session::flash('flash_msg', 'Ação realizada com sucesso.');
\Session::flash('flash_msg_primary', 'Ação realizada com sucesso.');
\Session::flash('flash_msg_success', 'Ação realizada com sucesso.');
\Session::flash('flash_msg_info', 'Ação realizada com sucesso.');
\Session::flash('flash_msg_warning', 'Ação realizada com sucesso.');
\Session::flash('flash_msg_danger', 'Ação realizada com sucesso.');
\Session::flash('flash_msg_alert', 'Ação realizada com sucesso.');
```

**Laravel BD Transaction**

No laravel você pode colocar uma sequencia de transações com o banco dentro de uma especie de `try/catch` onde se todas tiverem sucesso serão todas gravadas e se acontecer algum erro no meio do caminho todas as transações do bloco serão desfeitas.

**Exemplo de uso:**

```php
use DB;
DB::beginTransaction();                 //abre o bloco de transaction
    $insercao_1 = create(‘ble ble’);    //transação 1
    $insercao_2 = create(‘bla bla’);    //transação 2
if($insercao_1 && $insercao_2){         //verifica se tudo correu bem
    DB::commit();                       //salva tudo no banco
}else{
    DB::rollback();                     //caso deu algum erro da rollback em todas as transações feitas dentro do bloco
}
```

## Eloquent

Quando você cria um model através do `artisan` ele já vem associado à tabela criada pelo seu migration e vários metodos usaveis do ORM eloquent.

Para exemplificar usaremos um registro `user` com:

- name
- telefone
- status

Seguindo as convenções de nomenclatura do laravel o model sera User e a tabela users.

Entre os principais métodos estão:

**Criando um usuario:**

```php
$user = new User();
$user->name = ‘Peter’;
$user->telefone = ‘992192851’;
$user->status =1;
$user->save();
$id = $user->id;                //voce pode recuperar o id imediatamente após salvar o objeto no banco se precisar
```

**Resgatando um registro:**

```php
$user = User::find($id);                    //retorna o registro em forma de objeto se existir ou null
$user = User::findOrFail($id)               // retorna o registro em forma de objeto ou da erro se ele não existir
$users = User::find([1, 2, 3]);             // retorna um array de objetos (Collection) usuários dos ids passados
$users = User::all();                       // retorna um array de objetos com todos os registros do banco
$users = User::where(‘name’, ‘Peterson’)    // retorna um array de objetos 
            ->orderBy(‘name’, ‘desc’)       // onde name = peterson order by 
            ->take(10)                      // name desc limit 0,10
            ->get();
$user = User::where(‘status’, 1)->first();  //retorna o primeiro status 1 da tabela ou null
$user = User::where(‘status’, ‘>’, 0)->firstOrFail(); //retorna o primeiro status maior que zero da tabela ou um erro
$usersActives = User::where(‘status’, 1)->count();  //int com o número de status =1 da tabela
```

**Alterando um registro**

```php
$user = User::find($id);
$user->name = ‘novo nome’;
$user->save();
```

**Apagando o registro `id=1` do banco**

```php
$user = User::find(1);
$user->delete();
```

ou

```php
User::destroy(1);
User::destroy([1,2,3]); //vc pode deletar vários se precisar
```

**Sobre SoftDeletes**

`SoftDelete` é um conceito muito interessante que você tem que estudar para implementar no projeto. Trata-se de uma lixeira para onde vão os registros e excluidos e que podem ser listados, recuperados ou excluídos definitivamente depois.

## Fluxo de programação

Diferente de outros frameworks, o laravel não define rotas automaticamente para cada controller. 

Se a rota não existir vai dar erro, logo você precisar registrar todas as rotas de seu app.

Principais tipos de rotas:

```php
# Chamando uma view
Route::get('/', function () {
    return view('welcome');
});

# Chamando view passando variaveis a ela
Route::get('/', function () {
    $dados = array(
      'titulo' => 'Peterson'
    );
    return view('welcome', $dados);
});

# Chamando um metodo de um controller
Route::get('/home', 'HomeController@index');
```

## Acrescentando helpers personalizados

Há duas maneiras de adicionar seus próprios helpers a aplicação,

A primeira é jogar suas functions helpers no arquivo: 

`vendor\laravel\framework\src\Illuminate\Foundation\helpers.php`

A segunda é criando dentro de `app/helpers/seu_helper.php`, adiciona-lo ao `composer.json` e dar um `composer dump` no terminal

Exemplo de como add ao `composer.json`:

```json
    "psr-4": {
        "App\\": "app/"
    },
    "files": [
        "app/Helpers/MyHelper.php"
    ]
```

## Logs

```php

use Illuminate\Support\Facades\Log; //registre o uso do log no seu controller

# use um dos niveis de log definidos na rfc5424 e registre sua mensagem, 
# os logs ficam em storage/logs
    Log::emergency($message);
    Log::alert($message);
    Log::critical($message);
    Log::error($message);
    Log::warning($message);
    Log::notice($message);
    Log::info($message);
    Log::debug($message);
```

## Requisições

- todo o formulario deve conter a linha `{{ csrf_field() }}`
- a rota que recebe o formulario deve especificar se é uma requisição POST ou GET ou qualquer outra personalizada
- no controller a requisição vem na forma de um objeto `$request` do laravel e para receber os dados você usa assim:

```php
nome = $request->nome #sendo nome = name do input que você tá recebendo
```

- no formulario de edição você deve especificar o `id` do item editado na url para o routes saber que se trata de uma variavel e passar para o controller ex.:

```php

<form method="post" action="{{ url('noticia/'.$news->id.'/editar') }}">

Route::post('/noticia/{news}/editar', 'newsController@edit');

public function update(Request $request, News $news)
{

    $news->title = $request->title;
    $news->text = $request->text;
    $news->save();

    return redirect(route('listar_noticias'));
}
```

No formulario de edição os `values` dos inputs devem ser preenchidos assim value="{{ $news->title }}"

## Validando requisições

a forma mais simples de fazer isso é validando no controllers antes de salvar os dados vindos da request. 

Exemplo:

```php
$request->validate([
    'title' => 'required|unique:posts|max:255',
    'text' => 'required|min:6',
]);
```

dentro do array validate você passa como primeiro parametro o name do campo que esta chegando pela request e no segundo parametro as regras de validação.

Se passar na validação, o método vai prosseguir normalmente, se não passar irá retornar para o form onde você deve colocar o seguinte metodo antes da abertura do form para exibir os erros:

```php
@if ($errors->any())
    <div class="alert alert-danger">
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif
```

## Principais regras de validação

Regra | Efeito
--- | ---
accepted  | somente checkbox marcado
alpha  | somente caracteres alphabetics
alpha_num  | somente alfanumericos
confirmed | deve bater com outro campo de nome igual mais sufixo _confirmation ex.: pass = pass_confirmation
e-mail  | deve ser um e-mail valido
image  | deve ser uma imagem jpeg, png, bmp, gif ou svg
integer  | deve ser um inteiro
max:999  | numero maximo de caracteres
min:9 | numero minimo de caracteres
nullable | pode ser nulo input type text
numeric | somente numeros
required | obrigatorio
string | somente texto
unique:tabela | deve ser unico na tabela com a coluna do mesmo name

## Traduzindo nomes de campos nas mensagens de erro

Vá ate o final do arquivo `resources/lang/pt-BR/validation.php` e edite o seguinte array:

```php
'attributes' => [
    'name_do_input'    => 'Nome conforme você quer que apareça na mensagem',
    'name_do_input'    => 'Nome conforme você quer que apareça na mensagem',
],
```

## Sistema de autenticação nativo

Se você for inserir um usuário por outro método, você deve passar a senha dele pela funcao `bcrypt(‘123’)` para que depois o metodo autenticador reconheça essa senha

## Sistema de niveis de acesso nativo

Existem dois métodos de se fazer isso:

1) As regras (Gates) que servem para visualização de itens ou acesso a area restritas daquele nivel entre outras coisa

2) As politicas onde você define regras para cada model especifico.

```php
Gate::define('habilidade_requerida', function ($user, $post) {
    return 'uma logica que retorne true ou false para a permissao';
});
```

Nesse exemplo estou validando um `post` passado como parametro. O `user` **não** precisa ser passado pois o Gate já pega o objeto user logado.

No controller verifique assim:

```php
if (Gate::denies('habilidade_requerida', $post)) {
    // se entrou aqui é porque o usuario não pode executar essa ação então mande um erro.
}
```

Não esqueça de dar um `use Gate` no controller.

## Upload de arquivos

Existem varias formas mas a que eu achei mais facil é a seguinte:

- dentro da pasta `public`, crie uma pasta `images` e ponha a `sua_imagem.jpeg` lá
- dentro de sua pasta public crie uma pasta uploads e de permissões para ela
- no arquivo config/filesystem.php configura o root do disco local na linha 48 para public_path()
- no formulario não esquece o enctype e o input tipe file
- no controler você recebe conforme o exemplo abaixo onde usei o nome image para o input

```php
if ($request->hasFile('image') && $request->file('image')->isValid()) {
     $nome_da_imagem_salva = $request->image->store('uploads');
}
```

Na view para exibir a imagem você usa o source assim:

    {{ asset($nome_da_imagem_salva) }}

Na hora de excluir a imagem do banco, exclua o arquivo da seguinte forma:

```php
if (!empty($post->image) && file_exists(public_path($post->image))) {
    unlink(public_path($post->image));
}
```

## Front-end

Atalhos úteis do Blade Template:

```php
{{ url(‘/seu link’) }} = url base
{{ asset('css/app.css') }} = url base da pasta public
{{ config('app.name', 'Laravel') }} = pega o nome da aplicação do .env ou coloca o segundo parametro se a opção não estiver definida
{{ Auth::user()->name }} = exibir dados do usuario logado
{{ route('name_da_rota') }} = você pode definir um ->name(‘nome’) para suas rotas e chamar os links delas no front dessa forma simplificada 
{{ csrf_field() }} = campo de segurança obrigatorio em todos os formularios do app
```

### Exibir itens somente para quem esta logado

@guest
    ‘convidado’
@else
    ‘usuario logado’
@endguest = if que faz ações diferentes se o usuario for ou não convidado

@auth
    ‘logado’
@else
    ‘nao logado’
@endauth = if que faz ações diferentes se o usuario estiver ou não logado

## Exibir itens somente para quem tem permissao de ver aquele item

```php
@can(‘nivel de acesso exigido’, alguma variavel que você precise passar para verificação)
    ‘pode visualizar pois tem o nivel necessario de acesso’
@else 
    ‘opcional para aparecer caso o conteudo tenha sido bloqueado por falta de acesso’
@endcan

value="{{ old('email') }}" = preenche o campo com o valor submisso anteriormente caso de algum erro

```

## Usando layouts do blade

Você cria um layout mestre com cabeçalho e rodapé no meio dele você utiliza a tag `@yield('content')` por exemplo.

Quando você for colocar algo dentro daquele espaço você faz assim:

```php
# Exemplo de um arquivo que extende um layout master

# Vai buscar a view dentro de /resources/views/layouts e extende a view 'app.blade.php'
@extends('layouts.app')
@section('content')
// Seu HTML vai aqui
@endsection
```

você estendeu o layout padrao e definiu aquele bloco de codigo `//Seu HTML vai aqui`  como aquela section dele

## Projeto no mundo real

- crie um novo site no painel da hostinger
- acesse ele por ssh e com o composer crie uma nova aplicação laravel
- crie outra pasta na raiz chamada repo.git pára abrigar seu repositorio
- dentro dessa pasta crie um repositório git do tipo **bare** com: `git init –-bare`
- puxe o projeto da pasta da aplicação para esta do repo
- crie o hook post receive
- puxe a aplicaçao para sua maquina local via git clone
- configure o git remoto para o repo.git do servidor
- as vezes vem com permissoes eradas, puxe a pasta para a pasta home, rode `sudo chown -R seu_user:seu_user`
- jogue ela devolta para o htdocs
- codifique mt e a cada commit você da um push para o repositorio remoto que você configurou
- quando você cria algo no artisan em localhost, ao subir deve executar um composer dump-autoload para as novas classes serem reconhecidas
