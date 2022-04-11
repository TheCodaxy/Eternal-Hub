#<---------------------------->
import colorama
import base64
import json
import hashlib
import requests
from turtle import clear
from time import sleep
#<---------------------------->

#<---------------------------->
Preto = "\033[1;30m"
Vermelho = "\033[1;31m"
Verde = "\033[1;32m"
Amarelo = "\033[1;33m"
Azul = "\033[1;34m"
Magenta = "\033[1;35m"
Ciano = "\033[1;36m"
Cinza_claro = "\033[1;37m"
Cinza_escuro = "\033[1;90m"
Vermelho_claro = "\033[1;91m"
Verde_claro  = "\033[1;92m"
Amarelo_claro = "\033[1;93m"
Azul_claro = "\033[1;94m"
Magenta_claro = "\033[1;95m"
Ciano_claro = "\033[1;96m"
Branco = "\033[1;97m"
Negrito = "\033[;1m"
Inverte = "\033[;7m"
Reset = "\033[0;0m"
#<---------------------------->

#<---------------------------->
print(Azul_claro + '''
 .\\            //.
. \ \          / /.
.\  ,\     /` /,.-
 -.   \  /'/ /  .
 ` -   `-'  \  -
   '.       /.\`       ETERNAL - HUB
      -    .-
      :`//.'
      .`.'
      .'           

''')

print(Azul_claro + '''╭──── CONSULTAS''', 
Branco + '''\n├ 1 » Consultar ip
├ 2 » Consultar cnpj
├ 3 » Consultar cep
╰ 4 » Consultar ddd
''')

print(Azul_claro + '''╭──── CRIPTOGRAFIAS''', 
Branco + '''\n├ 5 » Criptografar base64
├ 6 » Descriptografar base64
╰ 7 » Criptografar md5
''')

print(Azul_claro + '''╭──── OUTRAS FUNÇÕES''', 
Branco + '''\n├ 8 » Sobre o hub
╰ 9 » Sair do hub
''')

hint = int(input(Amarelo_claro + '''
╭ Qual função deseja utilizar?
│ 
╰► '''))
#<---------------------------->

#<---------------------------->
if hint == 1:
     ip = input(Branco + '''
╭ Insira o ip:
│ 
╰► ''')
     r = requests.get('http://ip-api.com/json/{}' .format(ip))
     data = r.json()
     print(Vermelho_claro , data)
     print(Reset + '')

if hint == 2:
     cnpj = input(Branco + '''
╭ Insira o cnpj:
│ 
╰► ''')
     r = requests.get('https://api-publica.speedio.com.br/buscarcnpj?cnpj={}' .format(cnpj))
     data = r.json()
     print(Vermelho_claro , data)
     print(Reset + '')

if hint == 3:
     cep = input(Branco + '''
╭ Insira o cep:
│ 
╰► ''')
     r = requests.get('https://viacep.com.br/ws/{}/json' .format(cep))
     data = r.json()
     print(Vermelho_claro , data)
     print(Reset + '')

if hint == 4:
     ddd = input(Branco + '''
╭ Insira o ddd:
│ 
╰► ''')
     r = requests.get('https://brasilapi.com.br/api/ddd/v1/{}' .format(ddd))
     data = r.json()
     print(Vermelho_claro , data)
     print(Reset + '')

if hint == 5:
     texto = input(Branco + '''
╭ Insira o texto:
│ 
╰► ''')
     message_bytes = texto.encode('ascii')
     base64_bytes = base64.b64encode(message_bytes)
     base64_message = base64_bytes.decode('ascii')
     print(Vermelho_claro , base64_message)
     print(Reset + '')

if hint == 6:
     texto = input(Branco + '''
╭ Insira o base64:
│ 
╰► ''')
     print(Reset + '')
     base64_bytes = texto.encode('ascii')
     message_bytes = base64.b64decode(base64_bytes)
     message = message_bytes.decode('ascii')
     print(Vermelho_claro , message)
     print(Reset + '')

if hint == 7:
     texto = input(Branco + '''
╭ Insira o base64:
│ 
╰► ''').encode()
     hash = hashlib.md5(texto)
     print(Vermelho_claro , hash.hexdigest())
     print(Reset + '')

if hint == 8:
     print(Azul_claro + '''
 .\\            //.
. \ \          / /.
.\  ,\     /` /,.-
 -.   \  /'/ /  .
 ` -   `-'  \  -
   '.       /.\`       ETERNAL - HUB
      -    .-
      :`//.'
      .`.'
      .'           

''')
     print(Azul_claro + '''╭──── INFORMAÇÕES''', 
Branco + '''\n├ Versão » 1.0
├ Dev » Codaxy
├ Helper » Zim 
╰ Linguagem » Python
''')
     print(Branco + 'λ ► https://github.com/TheCodaxy')
     print(Branco + 'λ ► https://github.com/zim0024')
     print(Reset + '')

if hint == 9:
     clear()
     print(Reset + '')
     quit()
#<---------------------------->
