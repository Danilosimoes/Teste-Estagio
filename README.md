### Teste Estagiário - REST API

O teste pode ser realizado na linguagem de programação de sua preferência.

### O script deve consumir uma API REST do IBGE e com sua resposta realizar uma conversão para um arquivo CSV com a quantidade de estados por região. 

**Endpoint:** https://servicodados.ibge.gov.br/api/v1/localidades/estados/

**Exemplo de retorno da API**

```JSON
[
    {
        "id": 1,
        "sigla": "RO",
        "nome": "Rondônia",
        "regiao": {
            "id": 1,
            "sigla": "N",
            "nome": "Norte"
        }
    }
]
```

#### **Exemplo do arquivo CSV**

| Regiao   | Qtd. Estados |
| :------- | ------------ |
| Norte    | 1            |
| Sul      | 2            |
| Nordeste | 3            |

#### **Requisitos**

- [ ] O arquivo CSV deve ser criado com o separador Pipe (**|**).
- [ ] A quantidade de estados deve ser um número inteiro.

Fique a vontade para clonar este repositório.

**Entrega**

- Crie um repositório para o desenvolvimento do teste.
- Crie um diretório **csv** para armazenar o csv gerado.
-  Envie o link do seu repositório para o e-mail: ***cintia.andrade@edi-labs.com***.
