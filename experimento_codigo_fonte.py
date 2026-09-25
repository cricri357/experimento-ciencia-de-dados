import time
import csv

# valores entre 100 e 1000 saltos de 100
TAMANHOS_MB = range(100, 1001, 100)
REPETICOES = 100

SISTEMA = "sistema"

ARQUIVO_SAIDA = f"resultados/resultados_{SISTEMA}.csv"

with open(ARQUIVO_SAIDA, "w", newline="", encoding="utf-8") as arquivo:

    escritor = csv.writer(arquivo)

    # cabeçalho
    escritor.writerow([
        "bloco_MB",
        "teste",
        "alloc_ms",
        "write_ms",
        "read_ms",
        "free_ms"
    ])

    for mb in TAMANHOS_MB:

        bloco_bytes = mb * 1024 * 1024

        for teste in range(1, REPETICOES + 1):

            # alocação
            inicio = time.perf_counter_ns()

            bloco = bytearray(bloco_bytes)

            fim = time.perf_counter_ns()

            alloc_ms = (fim - inicio) / 1_000_000

            # escrita
            padrao = b"\xAA" * bloco_bytes

            inicio = time.perf_counter_ns()

            bloco[:] = padrao

            fim = time.perf_counter_ns()

            write_ms = (fim - inicio) / 1_000_000

            # leitura
            inicio = time.perf_counter_ns()

            soma = sum(bloco)

            fim = time.perf_counter_ns()

            read_ms = (fim - inicio) / 1_000_000

            # liberação
            inicio = time.perf_counter_ns()

            bloco.clear()
            del bloco

            fim = time.perf_counter_ns()

            free_ms = (fim - inicio) / 1_000_000

            # registro
            # bloco_MB,teste,alloc_ms,write_ms,read_ms,free_ms
            print(
                f"bloco_MB:{mb}",
                f"teste:{teste}", 
                f"alloc_ms:{alloc_ms:.6f}", 
                f"write_ms:{write_ms:.6f}", 
                f"read_ms:{read_ms:.6f}", 
                f"free_ms:{free_ms:.6f}")

            escritor.writerow([
                mb,
                teste,
                f"{alloc_ms:.6f}",
                f"{write_ms:.6f}",
                f"{read_ms:.6f}",
                f"{free_ms:.6f}"
            ])

print("Fim")