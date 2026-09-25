import pandas as pd
import csv

TAMANHOS_MB = range(100, 1001, 100)
OPERACOES = ["alloc_ms", "write_ms", "read_ms", "free_ms"]

LINUX = pd.read_csv("resultados/resultados_linux.csv")
# WINDOWS = 

ARQUIVO_SAIDA = f"resultados/media_desvio.csv"

with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as arquivo:

    escritor = csv.writer(arquivo)

    # cabeçalho
    escritor.writerow([
        "bloco_MB",
        "operacao",
        "media"
        ])

    for mb in TAMANHOS_MB: # percorre os blocos de memória

        for operacao in OPERACOES:

            media = LINUX.loc[LINUX["bloco_MB"] == mb, operacao].mean()

            print(media)

            escritor.writerow([
                mb,
                operacao,
                f"{media:.6f}"
            ])

        