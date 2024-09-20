from flask import Flask,render_template,request
from models.anime import SamuraiWarriors,Shurato,Yuyuhakusho,Cdz
import requests
import json

app = Flask(__name__)

@app.route('/Samurai-Warriors/<int:id>')
def index(id):
    try:
        id
        api="https://anime-62323-default-rtdb.firebaseio.com/"
        dados = requests.get(f'{api}/Samurai-Warriors/-NTZkntxY5L53IxTyn65/{id}.json')
        res=dados.json()
        nome = res['nome']
        anime = res['anime']
        print(dados)
        print(dados.json())
        if id > 38:
            raise Exception('Não existe epísodio')
    except:
        return 'Episodio não existe'
    return render_template('index.html',res=res,id=id,anime=anime,nome=nome)
@app.route('/Samurai-Warriors/buscar', methods=['GET','POST'])
def buscar():
    try:
        api = SamuraiWarriors(request.form['id'],['nome'],['anime'])
        res = json.loads(requests.get(f'https://anime-62323-default-rtdb.firebaseio.com/Samurai-Warriors/-NTZkntxY5L53IxTyn65/{api.id}.json').text)
        id=res['id']
        nome=res['nome']
        anime=res['anime']
        api.id=id
        api.nome=nome
        api.anime=anime
    except Exception as ex:
        print(ex)
        return 'Episodio não existe'
    return render_template('index.html',
                           id=api.id,
                           nome=api.nome,
                           anime=api.anime
                           )
@app.route('/Shurato/<int:id>')
def shurato(id):
    try:
        id
        api="https://anime-62323-default-rtdb.firebaseio.com/"
        dados = requests.get(f'{api}/Shurato/-NTfDXKejGqQ-6CJYw3r/{id}.json')
        res=dados.json()
        nome = res['nome']
        url = res['url']
        print(dados)
        print(dados.json())
        if id > 37:
            raise Exception('Não existe epísodio')
    except:
        return 'Episodio não existe'
    return render_template('shurato.html',res=res,id=id,url=url,nome=nome)
@app.route('/Shurato/buscar', methods=['GET','POST'])
def reishura():
    try:
        api = Shurato(request.form['id'],['url'])
        res = json.loads(requests.get(f'https://anime-62323-default-rtdb.firebaseio.com/Shurato/-NTfDXKejGqQ-6CJYw3r/{api.id}.json').text)
        id=res['id']
        url=res['url']
        api.id=id
        api.url=url
    except Exception as ex:
        print(ex)
        return 'Episodio não existe'
    return render_template('shurato.html',
                           id=api.id,
                           url=api.url
                           )

@app.route('/Yuyuhakusho/<int:id>')
def yuyuhakusho(id):
    try:
        id
        api="https://anime-62323-default-rtdb.firebaseio.com/"
        dados = requests.get(f'{api}/Yu-yu-hakusho/-NVb2WbapX2AAkedGDgI/{id}.json')
        res=dados.json()
        url = res['url']
        print(dados)
        print(dados.json())
        if id > 111:
            raise Exception('Não existe epísodio')
    except:
        return 'Episodio não existe'
    return render_template('yuyuhakusho.html',res=res,id=id,url=url)

@app.route('/Yuyuhakusho/buscar', methods=['GET','POST'])
def yusuki():
    try:
        api = Yuyuhakusho(request.form['id'],['url'])
        res = json.loads(requests.get(f'https://anime-62323-default-rtdb.firebaseio.com/Yu-yu-hakusho/-NVb2WbapX2AAkedGDgI/{api.id}.json').text)
        id=res['id']
        url=res['url']
        api.id=id
        api.url=url
    except Exception as ex:
        print(ex)
        return 'Episodio não existe'
    return render_template('yuyuhakusho.html',
                           id=api.id,
                           url=api.url
                           )

@app.route('/Cdz/<int:id>')
def cdz(id):
    try:
        id
        api=requests.get(f'https://anime-62323-default-rtdb.firebaseio.com/Cdz/Episodio/{id}.json')
        res=api.json()
        url=res['url']
        if id > 145:
            raise Exception('Não existe episodio')
    except Exception as ex:
        print(ex)
        return 'Episodio não existe'
    return render_template('cdz.html',
                           id=id,
                           res=res,
                           url=url)
@app.route('/Cdz/buscar', methods=["GET","POST"])
def ocdz():
    try:
        api = Cdz(request.form['id'],['nome'],['url'])
        dados = json.loads(requests.get(f'https://anime-62323-default-rtdb.firebaseio.com/Cdz/Episodio/{api.id}.json').text)
        id=dados['id']
        url=dados['url']
        api.id=id
        api.url=url
    except Exception as ex:
        print(ex)
        return 'Episodio não existe.'
    return render_template('cdz.html',
                           id=api.id,
                           url=api.url)

app.run(host='0.0.0.0', port=81)