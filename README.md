# Fake Data Generator Project

Este projeto é um gerador simples de dados falsos utilizando a biblioteca **Faker** para criar informações simuladas realistas.

---

## 🛍️ Electronics Store Data Generator

### Descrição

O script `geradorfake.py` gera um arquivo JSON contendo **6000 registros fictícios de vendas** para uma loja chamada **"Loja de Eletrônicos XYZ"**.

Cada registro inclui:

* Nome da loja
* Endereço
* Bairro
* Cidade
* Produto vendido
* Valor da venda
* ID único

---

## 💪 Gym Data Generator

### Descrição

O script `geradorfake.py` também pode gerar um arquivo JSON contendo **6000 registros fictícios** para uma academia chamada **"Superação Fitness"**.

Cada registro inclui:

* Nome da academia
* Endereço
* Bairro
* Cidade
* ID único

---

## 🛠️ Requisitos Comuns

* Python **3.6 ou superior**
* Biblioteca **Faker**

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/DMaia-afk/Gerador_dados.git
cd Gerador_dados
```

Instale as dependências:

```bash
pip install faker
```

---

## ▶️ Uso

Execute o script Python:

```bash
python geradorfake.py
```

### Saída

* **Loja de Eletrônicos:** gera `dados_vendas_6000_registros.json`
* **Academia:** gera `dados_academia_6000_registros.json`

---

## 📊 Estrutura dos Dados

| Chave       | Loja (Vendas)                                     | Academia (Geral)    |
| ----------- | ------------------------------------------------- | ------------------- |
| nome/loja   | "Loja de Eletrônicos XYZ"                         | "Superação Fitness" |
| endereco    | Endereço fictício                                 | Endereço fictício   |
| bairro      | Bairro fictício                                   | Bairro fictício     |
| cidade      | Cidade fictícia                                   | Cidade fictícia     |
| produto     | Smartphone, Notebook, Tablet, Smart TV, Headphone | N/A                 |
| valor       | Número entre 100 e 5000                           | N/A                 |
| id_registro | 1 a 6000                                          | 1 a 6000            |

---

## 📁 Exemplo de Saída JSON

```json
[
  {
    "nome": "Superação Fitness",
    "endereco": "Rua das Flores, 123",
    "bairro": "Centro",
    "cidade": "São Paulo",
    "id_registro": 1
  }
]
```

---

## 🔧 Personalização

Você pode modificar o script para alterar:

* **Quantidade de registros**: altere `NUM_REGISTROS`
* **Nome da loja/academia**: altere `NOME_LOJA` / `NOME_ACADEMIA`
* **Lista de produtos**: altere `ITENS_VENDAS`
* **Faixa de valores**: altere `fake.random_int(min=100, max=5000)`
* **Seed**: altere `Faker.seed(42)`
* **Idioma**: altere `fake = Faker('pt_BR')`

---

## 📄 Licença

Projeto open-source. Use e modifique como desejar.

---

## ✍️ Autor

**DMaia-afk**
