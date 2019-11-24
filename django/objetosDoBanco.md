Como trabalhar com objetos vindos do banco de dados em django

```python
#criando um objetona memoria
q = Question(question_text="What's new?", pub_date=timezone.now())
# salvando no banco
>>> q.save()
# agora ele ja tem um ID.
>>> q.id
1
# acessando os valores de seus campos
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)
# Mudando o valor de um campo e depois salvando-o
>>> q.question_text = "What's up?"
>>> q.save()
# objects.all() retorna todos os objetos do banco daquele model
>>> qs = Question.objects.all()
# contando os objetos
>>> qs.count()
# retorna todos os objetos do banco daquele model em ordem pelo campo passado
>>> qs = Question.objects.order_by('headline')
# retorna todos os objetos do banco daquele model em ordem descendente pelo campo passado
>>> qs = Question.objects.order_by('headline').desc()
# retorna todos os objetos do banco daquele model em ordem ascendente pelo campo passado
>>> qs = Question.objects.order_by('headline').asc()
# pegando por chave primaria ('id')
>>> q = Question.objects.get(pk=1)

###############################################################################
#                                  Lookups                                    #
###############################################################################
# são sufixos que começam com __ e que representam filtros para serem usados  #
# na query                                                                    #
###############################################################################

# pegando por id passando um array, retorna um queryset
>>> q = Question.objects.filter(id__in=[1, 3, 4])
# filtrando por campos
>>> q = Question.objects.filter(question_text="What's up?")
# filtrando por campos mas ignorando caixa alta/caixa baixa
>>> q = Question.objects.get(name__iexact="what's up?")
# filtrando por campos que contem aquele conteudo
>>> q = Question.objects.get(name__contains='up')
# filtrando por campos que contem aquele conteudo mas ignorando caixa alta/caixa baixa
>>> q = Question.objects.get(name__icontains='uP')
# inicia com
>>> q = Question.objects.filter(question_text__startswith='What')
# inicia com, mas ignorando caixa alta/caixa baixa
>>> q = Question.objects.filter(question_text__istartswith='What')
# termina com
>>> q = Question.objects.filter(question_text__endswith='up')
# termina com, mas ignorando caixa alta/caixa baixa
>>> q = Question.objects.filter(question_text__iendswith='UP')
# datetime pertence ao ano de 2018
>>> q = Question.objects.get(pub_date__year=2018)
# datetime tem mes de 12
>>> q = Question.objects.get(pub_date__month=12)
# datetime tem dia de 21
>>> q = Question.objects.get(pub_date__day=21)
# datetime tem dia da semana como segunda-feira
# ('1 == domingo' '2 == segunda' ... '7 == sabado')
>>> q = Question.objects.get(pub_date__week_day=2)
# datetime tem data == Null
>>> q = Question.objects.get(pub_date__isnull=True)
# datetime tem data != Null
>>> q = Question.objects.get(pub_date__isnull=False)
# datetime com ano maior ou igual a 2015
>>> q = Question.objects.get(pub_date__year__gte=2015)
# exclui pub com data maior a hoje ('__gt == grand than')
>>> q = Question.objects.exclude(pub_date__gt=datetime.date.today())
# filtra os com data menor a hoje ('__lt == less than')
>>> q = Question.objects.filter(pub_date__lt=datetime.date.today())
# exclui pub com data maior ou igual a hoje ('__gte == grand than equal')
>>> q = Question.objects.exclude(pub_date__gte=datetime.date.today())
# filtra os com data menor ou igual a hoje ('__lte == less than equal')
>>> q = Question.objects.filter(pub_date__lte=datetime.date.today())
# pega as questions filtrando por um name no Blog que é um attr relacionado ('fk')
# basta usar o nome do model relacionado todo em caixa baixa
>>> q = Question.objects.filter(blog__name='Beatles Blog')
# Este exemplo retorna todos os objetos Blog``os quais tem pelo menos uma ``Entry a qual o headline contém 'Lennon':
>>> b = Blog.objects.filter(entry__headline__contains='Lennon')

# LIMIT
# pega 5 objetos ('indices negativos não sao suportados')
>>> q = Question.objects.all()[:5]
# pega do 5° ao 10° objeto ('indices negativos não sao suportados')
>>> q = Question.objects.all()[5:10]
# pega do 5° ao 10° objeto ('indices negativos não sao suportados')
>>> q = Question.objects.all()[5:10]
# range de datas ('BETWEEN')
import datetime
start_date = datetime.date(2005, 1, 1)
end_date = datetime.date(2005, 3, 31)
>>> q = Question.objects.filter(pub_date__range=(start_date, end_date))

```
