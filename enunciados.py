"""Enunciados da Equipe 14 adaptados para leitura no terminal."""

MINAS = """Questão 01.3 — Volume a extrair de cada mina

Uma obra precisa de 4.800 m³ de areia, 5.800 m³ de cascalho fino e
5.700 m³ de cascalho grosso. A composição de cada mina é:

          Areia   Cascalho fino   Cascalho grosso
Mina 1     55%         30%              15%
Mina 2     25%         45%              30%
Mina 3     25%         20%              55%

a) Escreva o sistema linear que representa a demanda de materiais.
b) Desenvolva um programa que resolva sistemas semelhantes por um método direto.
c) Determine quantos metros cúbicos devem ser extraídos de cada mina."""

CIRCUITO = """Questão 02.3 — Correntes nas cinco malhas

Considere o circuito da questão 02.3. As incógnitas I1 a I5 representam
as correntes de malha, em ampères.

a) Aplique a lei das tensões de Kirchhoff para montar o sistema linear.
   Em texto, as equações correspondentes à figura são:

     9,5 I1 − 2,5 I2 − 2 I4             =  12
    −2,5 I1 + 11 I2 − 3,5 I3 − 5 I5    = −16
    −3,5 I2 + 15,5 I3 − 4 I5            =  14
      −2 I1 + 7 I4 − 3 I5                =  10
      −5 I2 − 4 I3 − 3 I4 + 12 I5       = −30

b) Desenvolva um programa que resolva esse sistema e outros semelhantes
   pelo método de Gauss-Seidel.
c) Determine as cinco correntes. Use bᵢ/aᵢᵢ como aproximação inicial
   em cada linha e precisão de 0,0001."""

RESISTOR = """Questão 03.2 — Queda de tensão em um resistor

Em um ensaio de laboratório, foram medidas as quedas de tensão V para
diferentes correntes i em um resistor:

i (A)    0,25    0,75    1,25    1,50    2,00
V (V)   −0,45   −0,60    0,70    1,88    6,00

Estime a queda de tensão para i = 1,15 A pelas formas de Lagrange e
Newton, usando polinômios de graus 2, 3 e 4. Escolha os pontos mais
próximos de 1,15 A, distribuídos em torno desse valor sempre que possível."""

RIO = """Questão 04.2 — Área da superfície do rio

A partir de uma linha reta de referência, foram medidas as distâncias
até as margens M1 e M2 nas posições x. Todas as medidas estão em metros.

x             0      10      20      30      40
M1(x)      50,8    86,2   136,0    72,8    51,0
M2(x)     113,6   144,5   185,0   171,2    95,3

Determine a área aproximada da superfície do rio no intervalo [0, 40]
pelas regras do trapézio repetida e de Simpson 1/3 repetida."""
