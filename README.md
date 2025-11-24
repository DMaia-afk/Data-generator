# Gerador de Dados Falsos para Academia

Este projeto é um gerador simples de dados falsos para uma academia de ginástica, utilizando a biblioteca Faker para criar informações simuladas realistas.

## Descrição

O script `geradorfake.py` gera um arquivo JSON contendo 6000 registros de dados fictícios para uma academia chamada "Superação Fitness". Cada registro inclui informações como nome da academia, endereço, bairro, cidade e um ID único.

## Requisitos

- Python 3.6 ou superior
- Biblioteca Faker

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/DMaia-afk/Gerador_dados.git
   cd Gerador_dados
   ```

2. Instale as dependências:
   ```
   pip install faker
   ```

## Uso

Execute o script Python:
```
python geradorfake.py
```

Isso irá gerar um arquivo chamado `dados_academia_6000_registros.json` no diretório atual, contendo os dados simulados.

## Estrutura dos Dados

Cada registro no JSON é um objeto com as seguintes chaves:
- `nome`: Nome da academia (fixo como "Superação Fitness")
- `endereco`: Endereço fictício
- `bairro`: Bairro fictício
- `cidade`: Cidade fictícia
- `id_registro`: ID único do registro (de 1 a 6000)

## Exemplo de Saída

```json
[
  {
    "nome": "Superação Fitness",
    "endereco": "Rua das Flores, 123",
    "bairro": "Centro",
    "cidade": "São Paulo",
    "id_registro": 1
  },
  ...
]
```

## Personalização

Você pode modificar o script para alterar:
- O número de registros: mude a variável `NUM_REGISTROS`
- O nome da academia: mude `NOME_ACADEMIA`
- A semente para reprodutibilidade: mude `Faker.seed(42)`
- O locale: mude `fake = Faker('pt_BR')` para outro locale suportado pelo Faker

## Licença

Este projeto é de código aberto. Sinta-se à vontade para usar e modificar conforme necessário.

## Autor

DMaia-afk
