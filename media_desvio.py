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
        "bloco_MB",
        "operacao",
        "media_linux",
        "media_windows",
        "desvio_linux",
        "desvio_windows"
        ])

    # csv do linux
    for mb in TAMANHOS_MB: # percorre os blocos de memória

        for operacao in OPERACOES: # percorre cada tipo de operação

            media_l = LINUX.loc[LINUX["bloco_MB"] == mb, operacao].mean()
            media_w = WINDOWS.loc[WINDOWS["bloco_MB"] == mb, operacao].mean()
            desvio_l = LINUX.loc[LINUX["bloco_MB"] == mb, operacao].std()
            desvio_w = WINDOWS.loc[WINDOWS["bloco_MB"] == mb, operacao].std()

            print(
                f"bloco_MB:{mb}",
                f"operacao:{operacao}", 
                f"media_linux:{media_l:.6f}", 
                f"media_windows:{media_w:.6f}", 
                f"desvio_linux:{desvio_l:.6f}", 
                f"desvio_windows:{desvio_w:.6f}")

            escritor.writerow([
                mb,
                operacao,
                f"{media_l:.6f}",
                f"{media_l:.6f}",
                f"{desvio_l:.6f}",
                f"{desvio_w:.6f}"
            ])

    