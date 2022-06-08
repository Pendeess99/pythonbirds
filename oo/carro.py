"""
VOCê DEVE CRIAR UMA CLASSE CARRO QUE VAI POSSUIR
DOIS ATRIBUTOS COMPOSTOS PÓR OUTRAS DUAS CLASSES:

1) MOTOR
2) DIREÇÃO

O MOTOR TERÁ A RESPONSABILIDADE DE CONTROLAR A VELODICADE.
ELE OFERECE OS SEGUINTES ATRIBUTOS:
1) ATRIBUTO DE DADO VELOCIDADE
2) MÉTODO ACELERAR QUE DEVERÁ ICREMENTAR A VELOCIDADE DE UMA UNIDADE
3) MÉTODO FREAR QUE DEVERÁ DECREMENTAR A VELOCIDADE DE UMA UNIDADE

A DIREÇÃO TERÁ A RESPONSABILIDADE DE CONTROLAR A DIREÇÃO. ELA OFERECE
OS SEGUINTES ATRIBUTOS:
1) VALOR DE DIREÇÃO COM VALORES POSSIVEIS: NORTE, SUL, LESTE, OESTE.
2) METODO GIRAR A DIREITA
3) METODO GIRAR A ESQUERDA

  N
O   L
  S
  EXEMPLO:
  # testando motor
  >>> motor = Motor()
  >>> motor.velocidade
  0
  >>> motor.acelerar()
  >>> motor.velocidade
  1
  >>> motor.acelerar()
  >>> motor.velocidade
  2
  >>> motor.acelerar()
  >>> motor.velocidade
  3
  >>> motor.frear()
  >>> motor.velocidade
  1
  >>> motor.frear()
  >>> motor.velocidade
  0
  >>> # testando direção
  >>> direcao = Direcao()
  >>> direcao.valor
  'Norte'
  >>>direcao.girar_a_direita()
  >>>direcao.valor
  'Leste'
  >>>direcao.girar_a_direita()
  >>>direcao.valor
  'Sul'
  >>>direcao.girar_a_direita()
  >>>direcao.valor
  'Oeste'
  >>>direcao.girar_a_direita()
  >>>direcao.valor
  'Norte'
  >>>direcao.girar_a_esquerda()
  >>>direcao.valor
  'Oeste'
  >>>direcao.girar_a_esquerda()
  >>>direcao.valor
  'Sul'
  >>>direcao.girar_a_esquerda()
  >>>direcao.valor
  'Leste'
  >>>direcao.girar_a_esquerda()
  >>>direcao.valor
  'Norte'
  >>> carro = Carro(direcao, motor)
  >>> carro.calcular_velocidade
  0
  >>> carro.acelerar()
  >>> carro.calcular_velocidade
  1
  >>> carro.acelerar()
  >>> carro.calcular_velocidade
  2
  >>> carro.frear()
  >>> carro.calcular_velocidade
  0
  >>> carro.calcular_direcao()
  >>> 'Norte'
  >>> carro.girar_a_direita()
  >>> carro.calcular_direcao()
  >>>> 'Leste'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  >>>> 'Norte'
  >>> carro.girar_a_esquerda()
  >>> carro.calcular_direcao()
  >>>> 'Oeste'






"""