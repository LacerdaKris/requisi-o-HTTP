#importa biblioteca p/ requisições
import requests

#definição da url com parâmetros alterados
url = "https://cosmic-backbone-386318.rj.r.appspot.com/hashCodeServer?nome=KelenCristineLacerda&email=cristinelacerda@protonmail.com&cpf=025.623.210-57"

#passando ambos numa requisição post
resposta = requests.post(url)

#verifica status da resposta se foi executada corretamente
if resposta.status_code == 200:
  print(resposta.text)