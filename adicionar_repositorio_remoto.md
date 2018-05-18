# Adicionar repositorio remoto no git 

## Adicionando o host abra o arquivo /etc/host

    sudo nano /etc/hosts
    adicione o ip do servidor junto com o nome que vc quiser dar a conexão
    31.170.161.43   exemplo_homologa
  
## Adicionando o ssh Editar o arquivo (se não existir crie)

    sudo nano ~/.ssh/config
  
adicione aqui o host que vc criou com user e port

    Host exemplo_homologa
      User meu_user
      Port 1234
    
## Adicionando ao git Agora que vc add o host e os dados de ssh vc pode adicionar o remote ao git

    git remote add homologa exemplo_homologa:repo.git
 
Pronto, agora vc ja pode dar push para homologa que o git so vai pedir a senha de ssh
