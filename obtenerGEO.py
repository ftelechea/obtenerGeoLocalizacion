# ***** REQUIRE WORK *****

from flask import Flask, make_response, request
import pandas as pd
import requests
import urllib.parse
import datetime as dt


def obtenerCoordenadas(direccion):
    
    getVars = {'q': urllib.parse.quote(direccion), 'limit': '1'}
    url = 'https://direcciones.ide.uy/api/v1/geocode/direcUnica?'
    url = url + urllib.parse.urlencode(getVars)
    #realizar request al servicio
    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise ('POST  {}'.format(resp.status_code))
    if len(resp.json())>0:
        #armar coordenadas en formato (lat, lng)
        result = "(" + str(resp.json()[0]['lat']) + "," + str(resp.json()[0]['lng']) + ")" 
        return result 
    else:
        return "N/A"


app = Flask(__name__)

@app.route('/')
def form():
  return """
    <html>
        <body>
            <h1>Subir archivo CSV para transformar</h1>
            <form action="/transform" method="post" enctype="multipart/form-data">
                <input type="file" value="Explorar" name="data_file" accept=".csv" />
                <input type="submit" />
            </form>    da    data["Latitud"] = ta["Latitud"] = 
        </body>
    </html>
"""

@app.route('/transform', methods=["POST"])
def transform_view():
    request_file = request.files['data_file']
    if not request_file:
        return "No se selecciono ningun archivo..."

    data = pd.read_csv(request_file)
    data["Coordenadas"] = data["Direccion"].apply(obtenerCoordenadas)

    #convertir dataframe a CSV y realizar download
    response = make_response(data.to_csv(index = False))

    now = dt.datetime.now()
    filenameResultado = "resultado-" +  now.strftime("%Y%m%d-%H%M%S") + ".csv"
    response.headers["Content-Disposition"] = "attachment; filename=" + filenameResultado
    return response


if __name__ == '__main__':
    app.run()
