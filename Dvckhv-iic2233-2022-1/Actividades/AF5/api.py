import json
from parametros import GITHUB_BASE_URL, GITHUB_REPO_NAME, GITHUB_REPO_OWNER
from parametros import GITHUB_USERNAME
from parametros import POKEMON_BASE_URL, POKEMON_NUMERO
import requests


def get_pokemon():
        url=POKEMON_BASE_URL.format(f"/pokemon/{POKEMON_NUMERO}/")
        request=requests.get(url)
        data_pokemon=request.json()
        datos_solicitados=[data_pokemon["name"],data_pokemon["weight"],data_pokemon["height"]]
        lista_tipos=[slot["type"]["name"] for slot in data_pokemon["types"]]
        datos_solicitados.append(lista_tipos)
        return (request.status_code,datos_solicitados)



def post_issue(token, pokemon):
        url=GITHUB_BASE_URL.format(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues")
        
        data=json.dumps({"title":GITHUB_USERNAME,"body":str(pokemon)})
        request=requests.post(url=url,headers={"accept":"application/vnd.github.v3+json","authorization":f"token {token}"},data=data)

        return (request.status_code),request.json()["number"]


def put_lock_issue(token, numero_issue):
        url=GITHUB_BASE_URL.format(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues/{numero_issue}/lock")
        data=json.dumps({"lock_reason":"resolved"})
        request=requests.put(url=url,headers={"accept":"application/vnd.github.v3+json","authorization":f"token {token}"},data=data)
        return request.status_code
def delete_lock_issue(token, numero_issue):
        url=GITHUB_BASE_URL.format(f"{GITHUB_REPO_OWNER}/{GITHUB_REPO_NAME}/issues/{numero_issue}/lock")
        request=requests.delete(url=url,headers={"accept":"application/vnd.github.v3+json","authorization":f"token {token}"})
        return (request.status_code)

