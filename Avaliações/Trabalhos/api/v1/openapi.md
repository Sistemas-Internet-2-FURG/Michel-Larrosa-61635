

```yaml

openapi: 3.0.3
info:
  title: API DE TRABALHO PYTHON FLASK
  description: |-

    ---

    TAREFA DE SISTEMAS PARA INTERNET

    _Projeto iniciado no Primeiro semestre de 2024_
    [github](https://github.com/endereçodorepositorio).

    Requisitos `API/Banco de Dados` :
    - requisições CRUD
    - relação de chave estrangeira no DB

    ---

  termsOfService: http://localhost:8080/api/v1/terms
  contact:
    email: michel@localhost
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
  version: 1.0.11

externalDocs:
  description: Documentação da API
  url: http://localhost:8080/api/v1/docs
servers:
  - url: http://localhost:8080/api/v1
tags:
  - name: aluno
    description: Todo sobre Aluno, criação , atualização e exclusão
    externalDocs:
      description: sem documentos exclusivos
      url: https://localhost
  - name: alunos
    description: Acesso ao conteúdo de Alunos, individual ou ~~coletivo~~ coleção
    externalDocs:
      description: sem documentos exclusivos
      url: https://localhost
  - name: turma
    description: Acesso ao gerenciamento Aluno-Turma
    externalDocs:
      description: sem documentos exclusivos
      url: https://localhost
  - name: equipe
    description: Access ao gerenciamento da Equipe
    externalDocs:
      description: sem documentos exclusivos
      url:  https://localhost
paths:
  /aluno:
    post:
      tags:
        - aluno
      summary: Add a new aluno to the turma
      description: Add a new aluno to the turma
      operationId: addAluno
      requestBody:
        description: Create a new aluno in the turma
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Aluno'
          application/xml:
            schema:
              $ref: '#/components/schemas/Aluno'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Aluno'
        required: true
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Aluno'
            application/xml:
              schema:
                $ref: '#/components/schemas/Aluno'
        '400':
          description: Invalid input
        '422':
          description: Validation exception
      security:
        - alunoturma_auth:
            - write:alunos
            - read:alunos
    put:
      tags:
        - aluno
      summary: Update an existing Aluno - Full Update
      description: Update an existing aluno by Id but with all data
      operationId: updateAluno
      requestBody:
        description: Update an existent aluno in the turma
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Aluno'
          application/xml:
            schema:
              $ref: '#/components/schemas/Aluno'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Aluno'
        required: true
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Aluno'
            application/xml:
              schema:
                $ref: '#/components/schemas/Aluno'
        '400':
          description: Invalid ID supplied
        '404':
          description: Aluno not found
        '422':
          description: Validation exception
      security:
        - alunoturma_auth:
            - write:alunos
            - read:alunos
    patch:
      tags:
        - aluno
      summary: Update an existing aluno - Partial Update
      description: Update an existing aluno by Id
      operationId: updateAluno
      requestBody:
        description: Update an existent aluno in the turma
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Aluno'
          application/xml:
            schema:
              $ref: '#/components/schemas/Aluno'
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/Aluno'
        required: true
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Aluno'
            application/xml:
              schema:
                $ref: '#/components/schemas/Aluno'
        '400':
          description: Invalid ID supplied
        '404':
          description: Aluno not found
        '422':
          description: Validation exception
      security:
        - alunoturma_auth:
            - write:alunos
            - read:alunos
    delete:
      tags:
        - aluno
      summary: Deletes a aluno
      description: delete a aluno
      operationId: deleteAluno
      parameters:
        - name: api_key
          in: header
          description: ''
          required: false
          schema:
            type: string
        - name: alunoId
          in: query
          description: Aluno id to delete
          required: true
          schema:
            type: integer
            format: int64
      responses:
        '400':
          description: Invalid aluno value
      security:
        - alunoturma_auth:
            - write:alunos
            - read:alunos



```
