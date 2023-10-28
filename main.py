import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from github import Github

# Token de acesso pessoal para acessar a API do GitHub
g = Github("SEU_TOKEN_AQUI")

query = "clean architecture"  # Sua consulta de pesquisa
results = g.search_repositories(query)

# Contador de repositórios coletados
repos_collected = 0

# Dataframe para armazenar os resultados
data = {
    "Nome do Repositório": [],
    "Descrição do Repositório": [],
    "URL do Repositório": [],
    "Número de Estrelas": [],
    "Linguagem Principal": [],
    "Data de Criação": [],
    "Última Atualização": [],
    "Número de Forks": [],
    "Número de Issues Abertos": []
}

for repo in results:
    # Define um limite de 1000 repositórios coletados
    if repos_collected >= 1000:
        break  # Sai do loop quando o limite é atingido

    data["Nome do Repositório"].append(repo.full_name)
    data["Descrição do Repositório"].append(repo.description)
    data["URL do Repositório"].append(repo.html_url)
    data["Número de Estrelas"].append(repo.stargazers_count)
    data["Linguagem Principal"].append(repo.language)
    data["Data de Criação"].append(repo.created_at)
    data["Última Atualização"].append(repo.updated_at)
    data["Número de Forks"].append(repo.forks_count)
    data["Número de Issues Abertos"].append(repo.open_issues_count)

    repos_collected += 1

df = pd.DataFrame(data)

# Imprima o dataframe contendo um ranking das linguagens mais utilizadas
ranking_linguagens = df["Linguagem Principal"].value_counts()

# Crie um gráfico de barras com o ranking de linguagens
plt.figure(figsize=(10, 6))
sns.barplot(x=ranking_linguagens.values, y=ranking_linguagens.index)
plt.title("Ranking de Linguagens Mais Utilizadas")
plt.xlabel("Número de Repositórios")

# Exiba o gráfico
plt.show()

# Imprima os resultados
print("Resumo da Pesquisa sobre Clean Architecture:")
print(f"Total de Repositórios Coletados: {repos_collected}")
