
# Django-Mongodb-Docker project

Este é um simples projeto demonstrando com utilizar Docker, Django e Mongodb para
a criação de uma aplicação simples que recebe sugestões de usuários.

A aplicação pode ser instanciada utilizando (testado com a versão
1.20.0, Linux):

```
docker-compose up
```
Caso sua versão do docker compose seja mais antiga, é ncessário especificar que os Dockerfiles sejam construídos:
```
docker-compose up --build
```

Os seguintes containers compõe a aplicação:
* 3 containers Mongodb(`mongo1`, `mongo2`, `mongo3`). Devido ao descontínuo do campo
`deploy` no `docker-compose`, três instâncias separadas são utilizadas para
prover alta-disponibilidade através de um ReplicaSet.
* Um container utilizando a imagem MongoDB para a inicialização do ReplicaSet (`replSetInitiate`), contendo um pequeno _script_ para passar a configuração para o banco.
O comando é executado no container `mongo1`, porém poderia ser executado em qualquer
um dos 3 container de mongo.
* Containers para provisionamento do `zabbix`. Estes são:
  * `zabbix-server`: backend do Zabbix.
  * `zabbix-web-nginx-pgsql`: Frontend de configuração para o Zabbix, que reponde na porta `http://localhost:8081`. O usuário e senha padrão foram mantidos, por simplicidade. :)
  * `postgres-server` : banco onde as configurações do zabbix são armazenadas. Um volume é mantido em `./zbx_env/var/lib/postgresql/data` para que as configurações permaneçam persistentes. O volume contido no arquivo comprimido já possui configurações de monitoramento e descoverta automática de hosts.
  * `zabbix-agent`: Agente responsável por fazer as checagens.
* O Container da aplicação Django(`app`). A aplicação escuta em `http://localhost:8000/sugestions`. A aplicação apresenta um formulário simples Que pega nome, usuário e Sugestão do usuário e as salva no MongoDB. Os _hosts_ do banco de dados podem ser setados através da variável de ambiente `DB_HOSTS`, assim como a porta pode ser atribuída com `DB_PORT`.

Alguns detalhes sobre a configuração utilizada:
* Os MongoDBs não podem ser acessados fora da rede do `docker-compose` (`app-network`), já que estão configurados na porta padrão e há botnets que atacam-os.
* As configurações do banco do Zabbix são salvas on arquivo `.env_db_pgsql`, para evitar repetições.
* As 3 intancias do MongoDB e a Aplicação são verificadas de minuto em minuto.
* A precedência do deploy é a seguinte:
  - `mongo1`, `mongo2`, `mongo3`, `postgres-server`, sem precedência entre eles.
  - `replSetInitiate`, para garantir que o `replSet` esteja funcional
  - `app`
  - `zabbix-server`
  - `zabbix-agent`
  - `zabbix-web-nginx-pgsql`

E está é a configuração da aplicação.
