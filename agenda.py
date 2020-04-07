from prettytable import PrettyTable
import requests
import json

from banco_dados import salva_contato, busca_contatos, busca_por_nome, busca_por_email, deleta_contato

from contato import Contato

contatos = []

def novo_contato():
	nome = input("Digite um nome para o contato: ")
	email = input("Digite um email para o contato: ")
	telefone = input("Digite um telefone para o contato (xx xxxx-xxxx): ")
	
	contato = busca_contato_email(email)
	
	if contato:
		print("O email {} já está cadastrado.".format(email))
		return

	salva_contato(Contato(nome, email, telefone))

	lista_contatos()		
		
def lista_contatos():
	table = PrettyTable(["Nome", "Email", "Telefone"])

	for contato in busca_contatos():
		table.add_row([contato.nome, contato.email, contato.telefone])

	print(table)
	
def busca_contato_nome(nome):
	table = PrettyTable(["Nome", "Email", "Telefone"])
	
	for contato in busca_por_nome(nome):
		table.add_row([contato.nome, contato.email, contato.telefone])
		
	print(table)
	
	
def busca_contato_email(email):
	resultado = busca_por_email(email)
	
	if not resultado:
		return
	
	return resultado
	
	
def altera_contato(email):
	contato = busca_contato_email(email)
	
	if not contato:
		print("Não existe o contato com o email: {}".format(email))
		return
		
	nome = input("Digite um nome para o contato: ")
	telefone = input("Digite um telefone para o contato (xx xxxxx-xxxx): ")
	
	contato.nome = nome
	contato.telefone = telefone
	
	lista_contatos()
	
def exclui_contato(email):

	contato = busca_contato_email(email)
	
	if not contato:
		print("Não existe um contato com o email: {}".format(email))
		return
		
	deleta_contato(contato)
	
	lista_contatos()
	
	
def carrega_contatos():
	response = requests.get("https://randomuser.me/api")
	
	if response.status_code != 200:
		print("Erro ao consumir o serviço de contatos.")
		return
		
	resultado = response.json()
	
	contato = Contato(nome="{} {}".format(resultado['results'][0]['name']['first'], resultado['results'][0]['name']['last']),
	email=resultado['results'][0]['email'],
	telefone=resultado['results'][0]['phone'])
	
	salva_contato(contato)
	
	lista_contatos()
		