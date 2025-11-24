import json
from faker import Faker

NUM_REGISTROS = 6000
NOME_ACADEMIA = "Superação Fitness"

Faker.seed(42)
fake = Faker('pt_BR')

def gerar_dados_academia(registro_id):
    """Retorna um Dicionário que será salvo no JSON."""
    return {
        "nome": NOME_ACADEMIA, 
        "endereco": fake.street_address(),
        "bairro": fake.bairro(),
        "cidade": fake.city(),
        "id_registro": registro_id 
    }

# Geração da lista de Dicionários (formato JSON)
dados_simulados_json = []
for i in range(NUM_REGISTROS):
    dados_simulados_json.append(gerar_dados_academia(i + 1)) 

# Salvar a lista no arquivo JSON
nome_arquivo = "dados_academia_6000_registros.json"
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        # json.dump é a função que escreve o objeto Python como JSON no arquivo.
        json.dump(dados_simulados_json, f, ensure_ascii=False, indent=2)
    print(f"✅ Arquivo JSON gerado com sucesso: '{nome_arquivo}'!")
except IOError as e:
    print(f"❌ Erro ao escrever o arquivo JSON: {e}")