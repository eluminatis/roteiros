# Otimização de consultas django

para pré carregar os objetos relacionados ('one_to_one') de um objeto 'pai' use a seguinte sintaxe


    pessoa = Pessoa.objects.select_related('cpf').get(id=1)

e ja teremos o objeto cpf que carrega a fk daquela pessoa acessivel em pessoa.cpf

para relação one_to_many utilize 

    pessoa = Pessoa.objects.prefetch_related('carros').get(id=1)

e ja teremos todos os carros da pessoa acessivel no iteravel pessoa.carros
