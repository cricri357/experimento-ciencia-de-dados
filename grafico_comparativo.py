import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("resultados/media_desvio.csv")

OPERACOES = ["alloc_ms", "write_ms", "read_ms", "free_ms"]

for operacao in OPERACOES:

    dados_operacao = dados[dados["operacao"] == operacao]
    bloco = dados_operacao["bloco_MB"]

    media_linux = dados_operacao["media_LINUX"]
    desvio_linux = dados_operacao["desvio_LINUX"]
    media_windows = dados_operacao["media_WINDOWS"]
    desvio_windows = dados_operacao["desvio_WINDOWS"]

    plt.figure(figsize=(10, 6))

    plt.plot(
        bloco,
        media_linux,
        marker="o",
        label="Linux"
    )

    plt.plot(
        bloco,
        media_windows,
        marker="o",
        label="Windows"
    )

    plt.fill_between(
        bloco,
        media_linux - desvio_linux,
        media_linux + desvio_linux,
        alpha=0.2
    )

    plt.fill_between(
        bloco,
        media_windows - desvio_windows,
        media_windows + desvio_windows,
        alpha=0.2
    )

    plt.title(f"Tempo da operação {operacao}")
    plt.xlabel("Tamanho do bloco (MB)")
    plt.ylabel("Tempo (ms)")

    plt.xticks(bloco)

    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(f"resultados/grafico_{operacao}.png")
    print(f"Salvo: {operacao}")

