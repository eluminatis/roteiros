# Autenticação basica para rotas de API no laravel

No arquivo de rotas proteja a rota desejada com o middleware auth.basic

```php
Route::resource('vehicles', 'VehicleController')->middleware('auth.basic')
```

Para ter acesso a essa rota vc deve mandar um header na requisição chamado Authorization e seu conteudo devera ser a string 'Basic' + espaço + um base64 do 'user@email.com:userPassword' do usuario

### Exemplo:

Dado um usuario com email `admin@admin.com` e senha `password`

- concatenamos `email` + `:` + `senha` resultando na string `admin@admin.com:password`

- convertemos essa string para base64 resultando em `YWRtaW5AYWRtaW4uY29tOnBhc3N3b3Jk`

e Enviamos o seguinte header na request protegida por autenticação

```
Authorization  :  Basic YWRtaW5AYWRtaW4uY29tOnBhc3N3b3Jk
```
