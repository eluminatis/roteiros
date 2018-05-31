# Laravel Queues

Nesse tutorial usaremos apenas o modo database

## Conceito

- Criamos as tabelas que abrigarão as filas
- Criamos varias filas de acordo com nossa necessidade para classificar os tipos de jobs que vamos enfileirar
- Criamos os jobs que receberão nossas variaveis pelo construct e jogarão em atributos protected para poder usar no processamento
- Uma vez criado um job e preparado para receber as variaveis pelo construtor e passar para seus proprios atributos 'protected', criamos nossa logica de processamento dentro do metodo handle() usando os atributos protected criados no construtor para popular as variaveis da logica
- Nos controllers instanciamos o job passando o que precisamos  de variaveis para seu construtor ('as variaveis devem ser passadas no método dispatch para cair no construtor do job') e damos um dispatch para mandar o job pra fila
- Instanciamos um laravel-worker que vai tomar conta dessa fila e processar cada job que cair nela, apagando os concluidos e mandando para a tabela failed_jobs aqueles que não puderam ser feitos por algum motivo


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
//fila default
'database' => [             //nome da conexão
    'driver' => 'database', //driver
    'table' => 'jobs',      //tabela ('mantenha o padrao jobs')
    'queue' => 'default',   //nome da fila
    'retry_after' => 90,    //tempo para tentar refazer um job falhado
],
//nossa fila personalizada emails
'database' => [             //nome da conexão
    'driver' => 'database', //driver
    'table' => 'jobs',      //tabela ('mantenha o padrao jobs')
    'queue' => 'emails',   //nome da fila
    'retry_after' => 90,    //tempo para tentar refazer um job falhado
],
```

### Criamos os jobs que receberão nossas variaveis pelo construct e jogarão em atributos protected para poder usar no processamento

#### para esse exemplo vamos fazer uma fila de emails que recebe duas variaveis: o remetente e o laravel_mailable ja instanciado e preenchido 

- Crie a fila

```php
php artisan make:job EmailQueue
```

- A classe job ficará +- assim

```php
<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Support\Facades\Mail;// <<< use no Mail
use Illuminate\Queue\SerializesModels;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;

class EmailQueue implements ShouldQueue
{
    use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

    //attrs que recebem os dados que vem pelo construct
    protected $destinatario;
    protected $mailable; 
    
    /**
     * Create a new job instance.
     *
     * @return void
     */
    public function __construct($destinatario, $mailable)
    {
        //passando vars recebidas no construct para attrs do job
        $this->destinatario = $destinatario;
        $this->mailable = $mailable;
    }

    /**
     * Execute the job.
     *
     * @return void
     */
    public function handle()
    {
        //aqui fica a logica do job
        Mail::to($this->destinatario)->send($this->mailable);
    }
}

```

## No controller instanciamos o job e damos um dispatch para mandar ele pra fila

### Instanciamos o job passando o que precisamos  de variaveis para seu metodo dispatch() que jogara as vars passadas no construct do job

```php
$data['token'] = '123'; //dados para criar o mailable
$mailable = new App\Mail\EmailConfirmation($data); //criando mailable
$destinatario = 'peterson.jfp@gmail.com'; //destinatario do mailable
App\Jobs\EmailQueue::dispatch($destinatario, $mailable);
                //->delay(now()->addSeconds(30)) add um delay para execução apos cair na fila
                //->onQueue('olar') escolhe a fila p colocar o job, se nenhuma for escolhida caira na fila default
```

## Instanciamos um laravel-worker para tomar conta da fila

### O worker processa cada job que cair na fila, apagando os concluidos e mandando para a tabela failed_jobs aqueles que não puderam ser feitos por algum motivo


```php
php artisan queue:work
```