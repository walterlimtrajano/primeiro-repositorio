# -*- coding: utf-8 -*-
"""Alunomedia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bDIkcgFfFaKqT25X4qfH2bza3eOCQonn
"""

aluno = input('digite o nome do aluno: ')
n1 = int(input('digite a primeira nota'))
n2 = int(input('digite a segunda nota'))
n3 = int(input('digite a terceira nota'))
media = (n1+n2+n3)/3
if media >= 7:
    situacao = 'aprovado'
elif media >= 4:
    situacao = 'em recuperação'
else:
    situacao = 'reprovado'
print(f'o aluno {aluno} está em situação {situacao} com média {media}')