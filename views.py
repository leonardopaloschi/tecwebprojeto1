from utils import load_data, load_template, update_data, build_response
from database import Database, Note
from urllib.parse import unquote_plus
db = Database('banco')
def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            chave, valor = chave_valor.split('=')
            params[unquote_plus(chave)] = unquote_plus(valor)
        titulo = params.get('titulo',"" )
        detalhes = params.get('detalhes',"")
        db.add(Note(title=titulo, content=detalhes))
        return build_response(code=303, reason='See Other', headers='Location: /') 
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id=dados.id)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    return build_response(body=load_template('index.html').format(notes=notes))
        
def delete(id):
    db.delete(id)
    return build_response(code=303, reason='See Other', headers='Location: /') 

def edit(request):
    request = request.replace('\r', '')  # Remove caracteres indesejados
    partes = request.split('\n\n')
    corpo = partes[1]
    print("SEPARADORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
    print(corpo)
    print(request)
    note_id = corpo.split('=')[1]
    note = db.get(note_id)
    return build_response(body=load_template('edit.html').format(id=note.id, title=note.title, details=note.content))
            
def update(request):
    request = request.replace('\r', '')  # Remove caracteres indesejados
    partes = request.split('\n\n')
    corpo = partes[1]
    note_id, title, details = corpo.split('&')
    note_id = note_id.split('=')[1]
    title = unquote_plus(title.split('=')[1])
    content = unquote_plus(details.split('=')[1])
    db.update(int(note_id), title, content)
    return build_response(code=303, reason='See Other', headers='Location: /')
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
   
