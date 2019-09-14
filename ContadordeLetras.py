# -*- coding:utf-8 -*-

lista = ['a','b','c','d','e','f','g']
texto = 'Esta é a minha mensagem para voces irmaos do metal'

for x in lista:
	cont = texto.count(x)
	print('[*] Letra {}:{}'.format(x,str(cont)))
size = len(texto)
print('[{}] caracteres na mensagem'.format(str(size)))
