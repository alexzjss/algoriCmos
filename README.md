# algoriCmos

Gerador de exercícios aleatórios, em português, para estudo de Programação em C, análise de algoritmos e estruturas de dados.

## Como executar

É necessário Python 3.10 ou superior. Não há dependências externas.

```bash
python main.py
python main.py --topic arrays
python main.py --topic ponteiros --difficulty intermediario
python main.py --count 5
python main.py --theory ponteiros
```

Para ver os nomes e aliases aceitos:

```bash
python main.py --list-topics
```

São aceitos nomes em português e inglês quando disponíveis, como `arrays`/`vetores`, `functions`/`funcoes`, `pointers`/`ponteiros`, `struct`/`structs`, `linked-list`/`lista-ligada`, `sorting`/`ordenacao`, `search`/`busca` e `switch-case`/`suitcase`.

## Tópicos cobertos

- Funções, argumentos, passagem por valor e por endereço
- Variáveis, escopo e comandos básicos de C
- Arrays, ponteiros, structs e alocação dinâmica
- Lista ligada
- Algoritmos e problemas de ordenação; algoritmos de busca
- `switch-case`, justificativas de complexidade e pegadinhas em C