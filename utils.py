from pathlib import Path
CUR_DIR = Path(__file__).parent

def extract_route(route):
    return route.split()[1][1:] if len(route.split()) > 1 else ""

def read_file(path):
    try:
        file = open(path, 'rb')
        content = file.read()
        file.close()
        return content
    except:
        return None
    
import json
def load_data(JsonFile):
    try:
        path = CUR_DIR / "data"
        file = open(f"data\{JsonFile}" , 'r')
        data = json.load(file)
        file.close()
        return data
    except:
        return None

def update_data(JsonFile, data):
    try:
        path = CUR_DIR / "data"

        file = open(path / JsonFile, 'r')
        old_data = json.load(file)
        file.close()

        file = open(path / JsonFile, 'w')
        old_data.append({"titulo": f"{data[0]}","detalhes": f"{data[1]}"},)
        json.dump(old_data, file)
        file.close()

        return True
    except:
        print("Erro encontrado no update_data")
        return False


def load_template(Template):
    try:
        path = CUR_DIR / "templates"
        print(path)
        file = open(f"templates\{Template}", 'r',encoding="utf-8")
        data = file.read()
        file.close()
        return data
    except:
        print("Erro encontrado no load_template")
        return None
    
def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
         return (f"HTTP/1.1 {code} {reason}\n\n{body}").encode()
    return (f"HTTP/1.1 {code} {reason}\n{headers}\n\n{body}").encode()
    