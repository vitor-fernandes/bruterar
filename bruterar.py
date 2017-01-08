#!/bin/python
# Coding: -*- UTF-8 -*-

import os, getopt, sys

def banner():
	print("\033[1;31m_____            ___     \033[1;32;40m______           ______	  ")
	print("\033[1;31m|  _ \           | |     \033[1;32;40m|  __ \     /\   |  __ \  ")
	print("\033[1;31m| |_) |_ __ _   _| |_ ___\033[1;32;40m| |__) |   /  \  | |__) | ")
	print("\033[1;31m|  _ <| '__| | | | __/ _ \033[1;32;40m\  _  /   / /\ \ |  _  /  ")
	print("\033[1;31m| |_) | |  | |_| | ||  __\033[1;32;40m/ | \ \  / ____ \| | \ \  ")
	print("\033[1;31m|____/|_|   \__,_|\__\___\033[1;32;40m|_|  \_\/_/    \_\_|  \_\ \033[0;37;40m")


def help():
	print("\nBem vindo ao BruteRar Versão 1.0 !!!")
	print("Script Brute Force para arquivos .rar")
	print("Desenvolvido por: Vitor Fernandes\n")
	print("Opções:")
	print("	-h para visualizar essa mensagem")
	print("	-f [arquivo.rar] para especificar o arquivo compactado")
	print("	-w [wordlist] para especificar a wordlist")
	print("	-v para visualizar a versão do script")
	print("")
	
def usage():
	print("Exemplo")
	print("	python bruterar.py -f arquivo.rar -w wordlist")

def crack():
	try:
		opts, args = getopt.getopt(sys.argv[1:], '-f:-w:-h:-v')
	except getopt.GetoptError as err:
		print(err) # retorna o erro onde o parametro está incorreto
		sys.exit()
	for  o,a in opts:
		if o in ("-f"): # o parametro passados depois do -f será o arquivo
			file = a # a variavel ira receber o arquivo compactado
		elif o in ("-w"): # o parametro passado depois do -w será a wordlist
			wordlist = open(a, "r") # a variavel ira receber a wordlist passada
			while KeyboardInterrupt:
				print("\n\033[1;33;40mQUEBRANDO O ARQUIVO \033[1;34;40m[%s]\033[0;37;40m\n" %(file))
				for w in wordlist: # vai varrer o arquivo com a wordlist passada pelo usuario
					try:
						crackeado = os.system("unrar x '%s' -inul -or -p%s" %(file, w)) # unrar é o programa para extração, -inul para não mostrar mensagem, -or para auto renomear, -p para senha(na wordlist)
						if crackeado != 0: # Se o retorno for 2560 ele não conseguiu quebrar com a chave da vez
							print("[+] \033[91mFalha ==> Password: %s \033[0;37;40m" %(w), end='')
						elif crackeado == 0: # Se o retorno for 0, ele quebrou com sucesso
							print("[+] \033[1;32;40mSucesso ==> Password: %s" %(w), end='')
							break
					except:
						print("")
				break
		elif o in ("-h"): # a opção -h, mostra apenas as opções disponíveis
			print("")
		elif o in ("-v"): # -v para versão do script
			print("[*] Versão 1.0\n")
		else:
			sys.exit()
banner()
help()
usage()
crack()