## Campos disponiveis para models no django

```python
from django.db import models

#tupla de tuplas que serão usadas como opções de um select
BEBIDAS = (('cafe',u'Café expresso'), ('mate',u'Chá mate'), ('chocolate',u'Chocolate quente'))

# perceba que campos de textos não obrigatórios devem ser 'blank=True' pq o valor minimo que o 
# django trabalho para um campo texto é um texto em branco, o 'null=True' deve ser usado em todos 
# os outros tipos de campo não obrigatorios exceto em campos texto que deve obrigatoriamente ser
# blank

class Pessoa(Models.model):
    # campo de texto com max 191 caracteres, pode ser um teto em branco e unique com mensagens de erro personalizadas para cada tipo de validação que pode dar errada
    name = models.CharField(
        'Nome', 
        max_length=191, 
        blank=True,
        unique=True,
        error_messages={
            'unique': _("A user with that username already exists."),
            'null': _('Não pode ser nulo!')
        },
    )

    # campo inteiro, se n for passado assume o valor padrao de 0
    bank_balance = models.IntegerField('Saldo na conta', default=0)
    
    # campo inteiro que não aceita numeros negativos
    qt_friends = models.PositiveIntegerField('Quantidade de amigos', default=0)
    
    # decimal de 8 casas sendo 2 apos a virgula ('ideal para valores monetarios')
    value_in_the_pocket = models.DecimalField('Valor no bolso', max_digits=8, decimal_places=2)
    
    # campo date
    birth_date = models.DateField('Data de nascimento')
    
    # campo datetime
    first_kiss = DateTimeField('Data e hora do primeiro beijo')
    
    # campo time
    when_wake_up = TimeField('Horário em que acorda')
    
    # campo texto com validação 'é um slug'
    slug = models.slugField('Slug', help_text='Texto de ajuda do campo. Usado em formulário gerados pelo Django. Útil para exibir exemplo de preenchimento')
    
    # campo texto longo permite texto em branco
    description = models.TextField('Descrição', blank=True)
    
    # fk apontando para um objeto cpf com relação 1 x 1 e clausula de ser deletado em cascata
    credit_card = models.OneToOneField(CreditCard, on_delete=models.CASCADE)
    
    # fk para varios objetos Livro com tabela pivot
    livros = models.ManyToManyField(Livro)
    
    # campo texto que é apresentado como um select apresentando as opções definidas na constante que é passada como parametro
    favorite_drink = models.CharField('Bebida Favorita', max_length=16, choices=BEBIDAS)
    
    # campo texto com validação para email not null
    email = EmailField('Email', null=False)
    
    # campo texto com validação para url
    site = URLField('Endereço na web')
    
    # campo texto apresentado como um input file que armazenara o caminho no banco e o arquivo no sistema de arquivos
    curriculum = FileField('Currículo em PDF')
    
    # campo texto apresentado como um input file que armazenara o caminho no banco e o arquivo no sistema de arquivos, com validação para o arquivo ser tipo imagem
    photo = ImageField('Foto do perfil')

    #######################################################################################################
    # O Django trata uploads salvando o arquivo no sistema de arquivos e o caminho do arquivo no banco de #
    # dados, para isso vc deve setar em seu settings do projeto a pasta onde ele salvara os arquivos      #
    # Colocar no settings:  MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')                                #
    #######################################################################################################
    
    # campo file que armazenara o arquivo em uploads/files/
    curriculum = models.FileField('Currículo em PDF', upload_to='files', null=True, blank=True)
    # campo file com validação para imagens que armazenara o arquivo em uploads/files/images/
    photo = models.ImageField('Foto do perfil', upload_to='images', null=True, blank=True)
    # auto_now_add=True significa que sera preenchido com o datetima atual quando o objeto for criado
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    # auto_now=True significa que sera preenchido com o datetima atual sempre que o objeto for salvo
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    # A 'class Meta' serve para definir metadados da classe
    class Meta:
        # como a classe sera ordenada na exibição em lista
        ordering = ('name', 'birth_date', 'qt_friends')
        
        # label do model
        verbose_name = 'Serumaninho'
        
        # label do model no plural
        verbose_name_plural = 'Pessoinhas'
        
        # Estabelece o campo DateTime a ser usado como critério para o método de consulta latest.
        get_latest_by = self.first_kiss
        
        # Define que este é um modelo abstrato (abstract model), que não será persistido em uma tabela mas será usado para definir um esquema reutilizável por herança.
        abstract = False
        
        # Define o nome da tabela que corresponde ao modelo. Quando esta opção não é usada o nome da tabela é aplicao_modelo (ex.: catalogo_livro é o modelo Livro da aplicação catalogo.
        db_table = 'nem rela aqui, so com banco legado'
```
