def gera_registro(qtd):
    for url in ['http://localhost:8idx8idx/pessoas/'+str(qtd)]:
        try:
            etapa = None
            response = requests.get(url)
            data = json.loads(response.text)
    
            for idx in range(qtd):
    
                sexo = data['pessoas'][idx]['sexo']
                mae = data['pessoas'][idx]['mae']
                senha = data['pessoas'][idx]['senha']
                sangue = data['pessoas'][idx]['sangue']
                emprego = data['pessoas'][idx]['emprego']
                nascimento = data['pessoas'][idx]['nascimento']
                nome = data['pessoas'][idx]['nome']
                peso = data['pessoas'][idx]['peso']
                telefone = data['pessoas'][idx]['telefone']
                email = data['pessoas'][idx]['email']
                altura = data['pessoas'][idx]['altura']
                cvv = data['pessoas'][idx]['cartao de credito']['cvv']
                validade = data['pessoas'][idx]['cartao de credito']['validade']
                numero = data['pessoas'][idx]['cartao de credito']['numero']
                rg = data['pessoas'][idx]['documentos']['rg']
                cpf = data['pessoas'][idx]['documentos']['cpf']
                cidade = data['pessoas'][idx]['endereco']['cidade']
                uf = data['pessoas'][idx]['endereco']['uf']
                logradouro = data['pessoas'][idx]['endereco']['logradouro']
                cep = data['pessoas'][idx]['endereco']['cep']
        
                connection = connecta_orcl('APP_1','APP_1','192.168.71.186','1521','pdb_app_1')
                etapa = '0'
                cursor = connection.cursor()
                cursor.execute("ALTER SESSION SET NLS_DATE_FORMAT = 'DD/MM/RRRR'")
    
                etapa = '1'
                cursor = connection.cursor()
                cursor.execute("INSERT INTO TB_CADASTRO_PESSOA(USUARIO_ID, SEXO, MAE, SENHA, SANGUE, EMPREGO, NASCIMENTO, NOME, PESO, TELEFONE, EMAIL, ALTURA) VALUES(SEQ_TRANSACTION.NEXTVAL, :1, :2 , :3, :4, :5, :6, :7, :8, :9, :1idx, :11)",(sexo, mae, senha, sangue, emprego, nascimento, nome, peso, telefone, email, altura))
                
    
                etapa = '2'
                cursor = connection.cursor()
                cursor.execute("INSERT INTO TB_CARTAO_CREDITO(USUARIO_ID, CVV, VALIDADE, NUMERO) VALUES(SEQ_TRANSACTION.CURRVAL,:1, :2 , :3)",(cvv, validade,numero))
                
    
                etapa = '3'
                cursor = connection.cursor()
                cursor.execute("INSERT INTO TB_DOCUMENTO(USUARIO_ID, RG, CPF) VALUES(SEQ_TRANSACTION.CURRVAL,:1, :2)",(rg,cpf))
            
    
                etapa = '4'
                cursor = connection.cursor()
                cursor.execute("INSERT INTO TB_ENDERECO(USUARIO_ID, CIDADE, UF, LOGRADOURO, CEP) VALUES(SEQ_TRANSACTION.CURRVAL, :1, :2, :3, :4)",(cidade, uf, logradouro, cep))
                connection.commit()
    
            
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
        
        except Exception as err:
            print(f'Other error occurred: {err}')  
            print(etapa)
        
        else:
            print('Success!')





kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic sql-insert 



kafka-console-producer.bat --broker-list localhost:9092 --topic sql-insert 


kafka-console-consumer.bat --bootstrap-server localhost:2181 --topic sql-insert



Producer : bin ./kafka-console-producer.sh --broker-list host1:9092,host2:9092 --topic "topic_name"

Consumer: bin  ./kafka-console-consumer.sh --bootstrap-server :9092 --topic "topic_name" --from-beginning; 


















kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test


kafka-topics.bat --list --bootstrap-server localhost:9092


kafka-console-producer.bat --broker-list localhost:9092 --topic test


kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning