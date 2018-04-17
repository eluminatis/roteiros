# Trabalhando com composer

## Criando um Pacote

Inicialmente você precisa de uma conta no Packagist e o composer instalado na sua máquina.

Feito isso rode o comando:

```
composer init
```

Siga as instruções na tela descritas abaixo

### Passo 1 - Package name

Ele deve respeitar o nome de usuário do GitHub/repositório do GitHub

```
eluminatis/meu_projeto
```

### Passo 2 - Descrição

Essa descrição ficará disponível no site do Packagist

### Passo 3 - Autor

O autor deve seguir exatamente a máscara abaixo:

```
Chuck Norris <chuck_norris@roundhousekick.com>
```

### Passo 4 - Estabilidade

Aqui eu coloquei `dev`. Necessário checar a documentação para mais detalhes

### Passo 5 - Tipo de pacote

Escolher um dos disponíveis que o Composer sugere. Os nomes são autoexplicativos

### Passo 6 - Licença (Obrigatório para subir pro Packagist)

Para escolher um tipo de licença existe um site interessante [aqui](http://choosealicense.com/)

- Apache-2.0
- BSD-2-Clause
- BSD-3-Clause
- BSD-4-Clause
- GPL-2.0-only / GPL-2.0-or-later
- GPL-3.0-only / GPL-3.0-or-later
- LGPL-2.1-only / LGPL-2.1-or-later
- LGPL-3.0-only / LGPL-3.0-or-later
- MIT

Mais detalhes na [documentacao do composer](https://getcomposer.org/doc/04-schema.md#license)

Depois o composer perguntará sobre dependências do seu projeto. Você pode definí-las aqui se necessário.

A saída deve ser algo assim:

```json
{
    "name": "eluminatis/meu_projeto",
    "description": "Projeto de teste do Composer",
    "type": "library",
    "license": "GPL-3.0-or-later",
    "authors": [
        {
            "name": "Chuck Norris",
            "email": "chuck_norris@roundhousekick.com"
        }
    ],
    "minimum-stability": "dev",
    "require": {}
}
```

## Preparando os diretórios para o seu pacote

Uma boa prática é incluir os fontes em `src`, por convenção da comunidade.

## Namespaces

Para que seu pacote seja alocado corretamente, você precisa dizer onde "mora" seu namespace. Baseando no namespace escolhido, adicione a diretiva abaixo em seu `composer.json`

```json
"autoload": {
    "psr-4" : { 
        "Eluminatis\\MeuOutroNamespace\\" : "src"
    }
}
```

## Publicando no Packagist

Vá na área "Submit" e aponte para o link do seu repositório no GibHub

Ele fará checagens de sintaxe no seu arquivo `composer.json` e corrija os erros que porventura apareçam

## Autoload no Laravel / Gerando pacotes para Laravel

O Laravel permite que você carregue Service Providers automaticamente se você adicionar a diretiva no `composer.json`

Adicione seu pacote seguindo esse padrão:

```json
"extra": {
    "laravel": {
        "providers": [
            "Eluminatis\\MeuOutroNamespace\\EluminatisServiceProvider"
        ]
    }
}
```

Tudo pronto, teste com:

```
composer require eluminatis/meu_projeto dev-master
```

## TODO

Escrever sobre SemVer e tags/releases no github