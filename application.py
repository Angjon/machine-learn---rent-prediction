from flask import Flask, request
import joblib
from datetime import datetime
import sqlite3

# Instantiate the app
Aplicativo = Flask(__name__)

# Load model
modelo = joblib.load('Modelo_Floresta_Aleatorio_v100.pkl')


## Function to receive API
@Aplicativo.route('/API_preditivo/<area>;<rooms>;<bathroom>;<parking_spaces>;<floor>;<animal>;<furniture>;<hoa>;<property_tax>', methods = ['GET'])
def funcao_01(area,rooms,bathroom,parking_spaces,floor,animal,furniture,hoa,property_tax):
    
    data_inicio = datetime.now()

    lista = [ 
        float(area),float(rooms),float(bathroom),float(parking_spaces),float(floor),
        float(animal),float(furniture),float(hoa),float(property_tax)
    ]
    
    try:
        previsao = modelo.predict([lista])

        # Insert prediction value
        lista.append( str(previsao) )

        # string transformation
        Input = ''
        for Valor in lista:
            Input = Input + ';' + str(Valor)

        # end process
        data_fim = datetime.now()
        processamento = data_fim - data_inicio

        ## create conection to data base
        conexao_banco = sqlite3.connect('Banco_dados_API.db')
        cursor = conexao_banco.cursor()

        ## query
        query_inserir = f'''
        INSERT INTO Log_API ( Inputs, Inicio, Fim, Processamento )
        VALUES ('{ Input}', '{data_inicio}', '{data_fim}', '{processamento}')
    '''
        ## execute query    
        cursor.execute(query_inserir)
        conexao_banco.commit()

        #close conection
        cursor.close()

        return {'Valor aluguel': str(previsao)}

    except:
        return{'Aviso':'Deu algum erro!'}


if __name__ == '__main__':
    Aplicativo.run(debug=True)

