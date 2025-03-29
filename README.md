# Itaú Unibanco - Desafio de Programação

## Descrição

Este repositório contém a implementação de uma **API REST** que simula o processamento de transações financeiras, em conformidade com as especificações do **Desafio de Programação do Itaú Unibanco**. A proposta inicial era para ser implementada utilizando **Java**, mas eu refiz o desafio utilizando **Python** e o framework **Flask**.

A API é capaz de:

1. **Receber Transações**:
   - Endpoint `POST /transacao` para registrar transações financeiras com valores e datas válidas.
   
2. **Limpar Transações**:
   - Endpoint `DELETE /transacao` para apagar todas as transações armazenadas em memória.
   
3. **Calcular Estatísticas**:
   - Endpoint `GET /estatistica` para retornar estatísticas sobre transações ocorridas nos últimos 60 segundos, incluindo:
     - Contagem (`count`)
     - Soma (`sum`)
     - Média (`avg`)
     - Mínimo (`min`)
     - Máximo (`max`)

## Requisitos Técnicos

- **Sem uso de banco de dados**: Todos os dados são armazenados em memória.
- **Formato de entrada e saída**: A API recebe e responde com dados em formato **JSON**.
- **Restrição de tempo**: A transação deve ser registrada com uma data que não seja no futuro e com valores não negativos.

## Funcionalidades

1. **Receber Transações (POST /transacao)**:
   - Recebe dados no formato JSON:
     ```json
     {
       "valor": 123.45,
       "dataHora": "2020-08-07T12:34:56.789-03:00"
     }
     ```
   - Valida que a transação possui valor não negativo e que ocorreu no passado.
   - Respostas possíveis:
     - `201 Created` (transação validada e registrada)
     - `422 Unprocessable Entity` (erro de validação)
     - `400 Bad Request` (erro no formato do JSON)

2. **Limpar Transações (DELETE /transacao)**:
   - Limpa todas as transações armazenadas.
   - Resposta:
     - `200 OK` (sucesso)

3. **Calcular Estatísticas (GET /estatistica)**:
   - Retorna as estatísticas das transações realizadas nos últimos 60 segundos:
     ```json
     {
       "count": 10,
       "sum": 1234.56,
       "avg": 123.456,
       "min": 12.34,
       "max": 123.56
     }
     ```
   - Resposta:
     - `200 OK` com os valores de **count**, **sum**, **avg**, **min** e **max**.

## Tecnologias Utilizadas

- **Flask** para criação da API
- **NumPy** para cálculo das estatísticas (Soma, Média, Mínimo e Máximo)
- **datetime** para manipulação e validação de datas e horários


A proposta original do desafio foi feita utilizando Java e Spring Boot. Para entender melhor a implementação proposta, veja o vídeo aqui: https://www.youtube.com/watch?v=uke3i4uOejs&feature=youtu.be
