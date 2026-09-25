import pandas as pd
import csv

TAMANHOS_MB = range(100, 1001, 100)
OPERACOES = ["alloc_ms", "write_ms", "read_ms", "free_ms"]

LINUX = pd.read_csv("resultados/resultados_linux.csv")
WINDOWS = pd.read_csv("resultados/resultados_windows.csv")

ARQUIVO_SAIDA = f"resultados/media_desvio.csv"

with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as arquivo:

    escritor = csv.writer(arquivo)

    # cabeçalho
    escritor.writerow([
        "sistema",
        "bloco_MB",
        "operacao",
        "media",
        "desvio_padrao"
        ])

    # csv do linux
    for mb in TAMANHOS_MB: # percorre os blocos de memória

        for operacao in OPERACOES: # percorre cada tipo de operação

            media = LINUX.loc[LINUX["bloco_MB"] == mb, operacao].mean()
            desvio = LINUX.loc[LINUX["bloco_MB"] == mb, operacao].std()

            print(
                "linux",
                f"bloco_MB:{mb}",
                f"operacao:{operacao}", 
                f"media:{media:.6f}", 
                f"desvio:{desvio:.6f}")

            escritor.writerow([
                "linux",
                mb,
                operacao,
                f"{media:.6f}",
                f"{desvio:.6f}"
            ])

    # csv do windows
    for mb in TAMANHOS_MB: # percorre os blocos de memória

        for operacao in OPERACOES: # percorre cada tipo de operação

            media = WINDOWS.loc[WINDOWS["bloco_MB"] == mb, operacao].mean()
            desvio = WINDOWS.loc[WINDOWS["bloco_MB"] == mb, operacao].std()

            print(
                "windows",
                f"bloco_MB:{mb}",
                f"operacao:{operacao}", 
                f"media:{media:.6f}", 
                f"desvio:{desvio:.6f}")

            escritor.writerow([
                "windows",
                mb,
                operacao,
                f"{media:.6f}",
                f"{desvio:.6f}"
            ])
        