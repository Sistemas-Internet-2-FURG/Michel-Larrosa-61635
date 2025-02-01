
> DOCUMENTAÇÃO CONSTRUÍDA DO SWAGGER

### Instalação pelo Docker (RECOMENDADO)
`sudo apt install docker.io`

### Execute o Swagger UI: (Swagger Editor não necessário para leitura)
- Instale:
```shell
sudo docker pull swaggerapi/swagger-ui
```
- Se já estiver instalado, só precisa executar(usei porta 8086 para exclusividade):
```shell
sudo docker run -p 8086:8080 swaggerapi/swagger-ui
```
- Acesse no navegador: http://localhost:8086


> **Nota:** Swagger UI não aceita arquivos carregados (file:///), só aceita arquivos servidos (http://)

**Use um servidor local simples como PHP ou Python**
- Na pasta .../API/

```shell
php -S localhost:8010
```
```bash
python3 -m http.server 8010
```
**Insira o caminho no Swagger UI:** `localhost:8010/openapi.yaml` ou `localhost:8010/openapi.json`
