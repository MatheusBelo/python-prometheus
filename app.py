from prometheus_client import Counter, start_http_server, Gauge, Summary, Histogram
import time
import http.server
import threading


#servidor http

#criando uma classe manipuladora:

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    pass

#iniciação do servidor:


def start_server():
    port = 9000
    httpd = http.server.HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
    print(f"servindo na porta: {port}")
    httpd.serve_forever()


#inicia o servidor em uma tread separada
    
server_thread = threading.Thread(target=start_server)
server_thread.start()

#métricas

#não funciona com o uso da condição 'with', como abaixo:
# with threading.Thread(target=start_server, daemon=True) as server_thread:
#     server_thread.start()

#módulo para o prometheus usar:

REQUESTS_TOTAL = Counter('http_requests_toal', ' Número total de requisições http')

for _ in range(100):
    REQUESTS_TOTAL.inc()
    time.sleep(0.1)

start_http_server(9000)

#gerenciador de pacotes python no linux é chamado de : pipx

#necessário instalar esse pacote do prometheus no linux:
#sudo apt install --reinstall --install-recommends python3-prometheus-client
