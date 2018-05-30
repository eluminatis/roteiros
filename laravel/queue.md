# Laravel Queues

Nesse tutorial usaremos apenas o modo database

## Conceito

- Criamos as tabelas que abrigarão as filas
- Criamos varias filas de acordo com nossa necessidade para classificar os tipos de jobs que vamos enfileirar
- Criamos os jobs que receberão nossas variaveis pelo construct e jogarão em atributos protected para poder usar no processamento
- Uma vez criado um job e preparado para receber as variaveis pelo construtor e passar para seus proprios atributos 'protected', criamos nossa logica de processamento dentro do metodo handle() usando os atributos protected criados no construtor para popular as variaveis da logica
- Nos controllers instanciamos o job passando o que precisamos  de variaveis para seu construtor e damos um dispatch para mandar o job pra fila
- Instanciamos um laravel-worker que vai tomar conta dessa fila e processar cada job que cair nela


## Instruções

### Criamos as tabelas que abrigarão as filas

Primeiramente você deve gerar a tabela e rodar a migration para que os jobs possam ser enfileirados nessa tabela e os falhados enfileirados na tabela failedjobs para tratamento posterior

```php
php artisan queue:table
php artisan queue:failed-table

php artisan migrate
```

### Criamos varias filas de acordo com nossa necessidade para classificar os tipos de jobs que vamos enfileirar

arquivo config/queue.php

```php
'database' => [             //nome da conexão
    'driver' => 'database', //driver
    'table' => 'jobs',      //tabela ('mantenha o padrao jobs')
    'queue' => 'default',   //nome da fila
    'retry_after' => 90,    //tempo para tentar refazer um job falhado
],
```

### Criamos os jobs que receberão nossas variaveis pelo construct e jogarão em atributos protected para poder usar no processamento

#### para esse exemplo vamos fazer uma fila de emails

- crie a fila

```php
php artisan make:job EmailQueue
```

