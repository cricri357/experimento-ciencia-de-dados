# Experimento de Comparação entre Sistemas Operacionais

Experimento desenvolvido para comparar o desempenho de **Windows e Linux** em operações de memória, utilizando medições de tempo.

## Objetivo

Executar as mesmas operações nos dois sistemas operacionais e comparar o tempo necessário para:

* Alocação de memória
* Escrita
* Leitura
* Liberação de memória

São utilizados blocos de **100 MB a 1000 MB**, em intervalos de 100 MB, com **100 repetições para cada tamanho**.

## Funcionamento

Para cada teste, o programa:

1. Aloca um bloco de memória.
2. Mede o tempo da alocação.
3. Escreve dados no bloco e mede o tempo.
4. Lê os dados e mede o tempo.
5. Libera a memória e mede o tempo.
6. Registra os resultados no CSV somente após a conclusão das operações.

As medições são realizadas utilizando `time.perf_counter_ns()` e convertidas para milissegundos.

## Código-fonte

O sistema operacional é definido pela variável:

```python
SISTEMA = "Windows"
```

ou:

```python
SISTEMA = "Linux"
```

O programa gera automaticamente um arquivo correspondente:

```text
resultados_windows.csv
resultados_linux.csv
```

O CSV possui o seguinte cabeçalho:

```text
bloco_MB,teste,alloc_ms,write_ms,read_ms,free_ms
```

## Execução

Execute o mesmo código em cada sistema operacional, alterando apenas a variável `SISTEMA`.

```bash
python experimento.py
```

Os arquivos CSV gerados são posteriormente utilizados para a análise estatística e comparação entre os sistemas.
