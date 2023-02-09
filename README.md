# TING 💻🔬
> Trybe is Not Google

Consiste em uma aplicação que simula um algoritmo de indexação de documentos similar ao do Google, capaz de identificar ocorrências presentes em arquivos TXT.

* Solucionado com a utilizando da linguagem Python

<br />

<details>
  <summary><strong>Descrição das soluções criadas:</strong></summary><br />

| Função/Classe | Descrição | Localização |
|---|---|---|
| `Queue` | Classe criada para armazenamento de arquivos por filas | `ting_file_management/queue.py` |
| `txt_importer` | Função capaz de ler os arquivos TXT e retorna em formato de array`/`lista` | `ting_file_management/file_management.py` |
| `process` | Função para importar informações do arquivo TXT e adicionar na instância da Classe Queue informada | `ting_file_management/file_process.py` |
| `remove` | Função para remover o primeiro arquivo presente na instância informada | `ting_file_management/file_process.py` |
| `file_metadata` | Função para encontrar um dado presente na instância atráves do index informado | `ting_file_management/file_process.py` |
| `exists_word` | Função para verificar existência de uma palavra em todos os arquivos processados, retornando um relatório simplificado | `ting_word_searches/word_search.py` |
| `search_by_word` | Função para verificar existência de uma palavra em todos os arquivos processados, retornando um relatório completo | `ting_word_searches/word_search.py` |

<br />
</details>

<details>
  <summary><strong>Descrição do teste criado:</strong></summary><br />
 
| Teste | Descrição | Localização |
|---|---|---|
| `test_basic_priority_queueing` | Criação dos testes para função de priorização das informações em relação ao número de linhas | `tests/priority_queue/test_priority_queue.py` |


<br />
</details>

### Estrutura do Projeto

```
.
├──statics
│   ├──🔸arquivo_teste.csv
│   ├──🔸arquivo_teste.txt
│   ├──🔸nome_pedro.txt
│   ├──🔸novo_paradigma_globalizado-min.txt
│   └──🔸novo_paradigma_globalizado.txt
├──tests
│   ├──priority_queue
│   │   ├──🔹test_priority_queue.py
│   │   └──🔸__init__.py
│   └──🔸__init__.py
├──ting_file_management
│   ├──🔸__init__.py
│   ├──🔸abstract_queue.py
│   ├──🔹file_management.py
│   ├──🔹file_process.py
│   ├──🔸priority_queue.py
│   └──🔹queue.py
├──ting_word_searches
│   ├──🔸__init__.py
│   └──🔹word_search.py
├──🔸dev-requirements.txt
├──🔹main.py
├──🔸pyproject.toml
├──🔸README.md
├──🔸requirements.txt
├──🔸setup.cfg
└──🔸setup.py

Legenda:
🔸 Arquivos desenvolvidos pela Trybe (não foram alterados).
🔹 Arquivos desenvolvidos por mim.

```



### Instruções

- Realize o clone do projeto e utilize os comandos a seguir:

```
Para instalar as dependências e iniciar as aplicações:
<-- na raiz do projeto -->
python3 -m venv .venv // para criar o ambiente virtual
source .venv/bin/activate // para ativar o ambiente virtual
python3 -m pip install -r dev-requirements.txt // instalação das dependências


Para rodar os testes:
<-- na raiz do projeto -->
python3 -m pytest
```


### Execução da Aplicação
> No arquivo `main.py` contém os exemplos para execução da aplicação descritos abaixo:
> comando: python3 -m main

<br />
1. Criei uma instância da Classe Queue e adicione informações presentes nos arquivos TXT presentes no diretório `statics`:

```
queue = Queue()
process('statics/arquivo_teste.txt', queue)
process('statics/nome_pedro.txt', queue)

print('--> Primeiro Elemento da Fila:', queue.search(0))
print('--> Segundo Elemento da Fila:', queue.search(1))

<br />
2. Outra forma de localizar as informações presentes mediante ao `index` é atráves da função `file_metadata`:

```
file_metadata(queue, 0)  # Retorna o Primeiro Elemento
file_metadata(queue, 1)  # Retorna o Segundo Elemento
file_metadata(queue, 99)  # Retorna "Posição inválida"

<br />
3. Podemos criar relatório de buscas de palavras presentes na instância atráves das funções `exists_word` e `search_by_word`:

`print(exists_word('adoção', queue))`

```
Retorno:
[
  {
    'palavra': 'adoção',
    'arquivo': 'statics/arquivo_teste.txt,
    'ocorrencias': [
        {'linha': 2},
     ],
  },
]
```

`print(search_by_word('adoção', queue))`

```
Retorno:
[
  {
    'palavra': 'adoção',
    'arquivo': 'statics/arquivo_teste.txt,
    'ocorrencias': [
        {
          'linha': 2,
          'conteudo': 'é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga'
        },
     ],
  },
]
```

<br />
4. Para remover as informações presentes na instância criada, podemos utilizar a função criada `remove`:

```
remove(queue)  # Arquivo statics/arquivo_teste.txt removido com sucesso
    remove(queue)  # Arquivo statics/nome_pedro.txt removido com sucesso
    file_metadata(queue, 0)  # Retorna "Posição inválida"



