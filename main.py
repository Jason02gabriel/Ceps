from tqdm import tqdm
import time
import requests


#abrir txt
with open('ceps.txt','r') as arquivo:
    ceps = arquivo.read()
    ceps = ceps.split("\n")
#pegar ceps
enderecos_de_entrega = []
for cep in tqdm(ceps):
    link = f'https://cep.awesomeapi.com.br/json/{cep}'
#verificar se a cidade e rio de janeiro
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
#se for rio de janeiro printar cep e bairro
    if cidade == "Rio de Janeiro":
        enderecos_de_entrega.append((cep,bairro))
with open('arq01.txt', 'w') as arquivo:
    for item in enderecos_de_entrega:
        arquivo.write(f'{item}\n')
print('\033[1;32mProcesso finalizado com sucesso!')