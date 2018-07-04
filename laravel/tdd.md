# TDD com Laravel e PHPUnit

Tutorial baseado na série de artigos de Jeff Simons Decena. Link [aqui](https://medium.com/@jsdecena/simple-tdd-in-laravel-with-11-steps-c475f8b1b214).

## Preparando a suíte de testes do Laravel

No diretório raiz do projeto, atualize o arquivo `phpunit.xml` com:

```xml
<env name="DB_CONNECTION" value="sqlite"/>
<env name="DB_DATABASE" value=":memory:"/>
<env name="API_DEBUG" value="false"/>
<ini name="memory_limit" value="512M" />
```

Ficará algo parecido com isso:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<phpunit backupGlobals="false"
         backupStaticAttributes="false"
         bootstrap="vendor/autoload.php"
         colors="true"
         convertErrorsToExceptions="true"
         convertNoticesToExceptions="true"
         convertWarningsToExceptions="true"
         processIsolation="false"
         stopOnFailure="false">
    <testsuites>
        <testsuite name="Feature">
            <directory suffix="Test.php">./tests/Feature</directory>
        </testsuite>

        <testsuite name="Unit">
            <directory suffix="Test.php">./tests/Unit</directory>
        </testsuite>
    </testsuites>
    <filter>
        <whitelist processUncoveredFilesFromWhitelist="true">
            <directory suffix=".php">./app</directory>
        </whitelist>
    </filter>
    <php>
        <env name="APP_ENV" value="testing"/>
        <env name="CACHE_DRIVER" value="array"/>
        <env name="SESSION_DRIVER" value="array"/>
        <env name="QUEUE_DRIVER" value="sync"/>
        <env name="DB_CONNECTION" value="sqlite"/>
        <env name="DB_DATABASE" value=":memory:"/>
        <env name="API_DEBUG" value="false"/>
        <env name="MAIL_DRIVER" value="log"/>
        <ini name="memory_limit" value="512M" />
    </php>
</phpunit>
```

Usando o banco de dados como `:memory` acelera os testes, bem como `sqlite`. Futuramente, com os testes ficando mais complexos, deve-se ajustar o `memory_limit` para um valor maior.

O Debugging também é desabilitado para mostrar apenas os resultados dos testes.

## Tipos de testes

### Testes Unitários (Unit Testing)

Servem para testar suas classes: Models, Repositórios, Funções, etc.

### Testes de Funcionalidade (Feature Testing)

Servem para testar se seu código, por exemplo, acessa os controllers e verica (asserts) se as ações tomadas são as esperadas, ou até mesmo erros. Por exemplo, acessando uma página que precisa de autenticação, se um erro gera uma _Flash Message_ na sessão ou até mesmo se um redirecionamento ocorre de forma correta.
