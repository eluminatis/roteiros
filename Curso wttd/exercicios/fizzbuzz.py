"""

Jogo FizzBuzz

Quando o número for multiplo de 3, fala fizz;
Quando o número for multiplo de 5, fala buzz;
Quando o número for multiplo de 3 e 5, fala fizzbuzz;
Para os demais diga o próprio número;

"""


def robot(pos):
    if pos % 3 == 0 and pos % 5 == 0:
        return 'fizzbuzz'
    elif pos % 3 == 0:
        return 'fizz'
    elif pos % 5 == 0:
        return 'buzz'
    else:
        return str(pos)


if __name__ == "__main__":
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'