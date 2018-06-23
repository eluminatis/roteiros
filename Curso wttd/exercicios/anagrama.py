"""
Mais formalmente, dado um número {\displaystyle n=n_{0}} n=n_{0}, Define uma seqüência {\displaystyle n_{1}} n_{1}, {\displaystyle n_{2}} n_{2}, ... onde {\displaystyle n_{i+1}} n_{{i+1}} é a soma dos quadrados dos dígitos {\displaystyle n_{i}} n_{i}. Então {\displaystyle n} n é feliz se e somente se existe i tal modo que {\displaystyle n_{i}=1} n_{i}=1.[2]

Exemplos
7 é um número feliz:[3]

72 = 49
42 + 92 = 97
92 + 72 = 130
12 + 32 + 02 = 10
12 + 02 = 1.
Se n não é feliz, a soma dos quadrados nunca dará 1, serão gerados infinitos termos.

4, 16, 37, 58, 89, 145, 42, 20, 4, ...
Os números felizes entre 1 e 500 são:

1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139, 167, 176, 188, 190, 192, 193, 203, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490 e 496.
"""


def happy(num):
    pass


if __name__ == "__main__":
    assert happy(1) == True
    assert happy(7) == True
    assert happy(10) == True
    assert happy(13) == True
    assert happy(230) == True

    assert happy(4) == False
    assert happy(16) == False
    assert happy(25) == False
    assert happy(117) == False
    assert happy(232) == False
    