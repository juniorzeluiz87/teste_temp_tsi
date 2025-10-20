import ollama

# Texto simples
texto = "Python é uma ferramenta inteligente."

# Gerar embeddings com o modelo llama3.2:1b
response = ollama.embeddings(model='llama3.2:1b', prompt=texto)

# Extrair vetor
vetor = response['embedding']

# Exibir resumo
print("Tamanho do vetor:", len(vetor))
print("Primeiros 10 valores:", vetor[:10])