# Fake Data Generator Project

This project is a simple fake data generator using the Faker library to create realistic simulated information.

---

## Electronics Store Data Generator

### Description

The `geradorfake.py` script generates a JSON file containing **6000 fictitious sales records** for a store named **"Loja de Eletrônicos XYZ"**.

Each record includes:

* Store name
* Address
* Neighborhood
* City
* Product sold
* Sale value
* Unique ID

---

## Gym Data Generator

### Description

The `geradorfake.py` script can also generate a JSON file containing **6000 fictitious records** for a gym named **"Superação Fitness"**.

Each record includes:

* Gym name
* Address
* Neighborhood
* City
* Unique ID

---

## Requirements

* Python **3.6 or higher**
* **Faker** library

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DMaia-afk/Gerador_dados.git
cd Gerador_dados
```

Install dependencies:

```bash
pip install faker
```

---

## Usage

Run the Python script:

```bash
python geradorfake.py
```

### Output

* **Electronics store:** generates `dados_vendas_6000_registros.json`
* **Gym:** generates `dados_academia_6000_registros.json`

---

## Data Structure

| Key          | Store (Sales)                                     | Gym (General)           |
| ------------ | ------------------------------------------------- | ----------------------- |
| name/store   | "Loja de Eletrônicos XYZ"                         | "Superação Fitness"     |
| address      | Fictitious address                                | Fictitious address      |
| neighborhood | Fictitious neighborhood                           | Fictitious neighborhood |
| city         | Fictitious city                                   | Fictitious city         |
| product      | Smartphone, Notebook, Tablet, Smart TV, Headphone | N/A                     |
| value        | Number between 100 and 5000                       | N/A                     |
| record_id    | 1 to 6000                                         | 1 to 6000               |

---

## Example Output (JSON)

```json
[
  {
    "name": "Superação Fitness",
    "address": "Rua das Flores, 123",
    "neighborhood": "Centro",
    "city": "São Paulo",
    "record_id": 1
  }
]
```

---

## Customization

You may modify the script to change:

* Number of records: change `NUM_REGISTROS`
* Store/gym name: change `NOME_LOJA` / `NOME_ACADEMIA`
* Product list: change `ITENS_VENDAS`
* Value range: change `fake.random_int(min=100, max=5000)`
* Seed: change `Faker.seed(42)`
* Locale: change `fake = Faker('pt_BR')`

---

## License

Open-source project. Feel free to use and modify as needed.

---

## Author

**DMaia-afk**
