# Algoritms - Python

Este repositório contém desafios de programação em Python que visam testar suas habilidades em algoritmos e estruturas de dados. Cada desafio aborda um problema específico e você deve implementar uma solução funcional de acordo com as instruções fornecidas.

## Como Funciona

- Dentro do diretório ```challenges``` contém todas as funções.
- Dentro de cada diretório, você encontrará um arquivo README.md com uma descrição detalhada do problema.
- Você deve criar sua solução no arquivo indicado (geralmente com a extensão .py).
- Além disso, em alguns desafios, você também encontrará um arquivo de teste correspondente para verificar a corretude da sua solução.
- Leia atentamente o enunciado de cada desafio e siga as instruções para implementar a solução adequada.

### Lista de Desafios

* ```challenge_study_schedule.py```  Encontre o horário mais movimentado em uma plataforma de educação com base nos registros de entrada e saída dos estudantes. (Algoritmo de Busca)
* ````challenge_encrypt_message.py```` Criptografia de Inversões (Testes):
* ````challenge_palindromes_recursive.py```` Palíndromos (Recursividade):
- ````challenge_anagrams.py```` Desenvolva uma função para comparar duas strings e identificar se são anagramas, sendo case insensitive.
- ````challenge_find_the_duplicate.py```` Descubra um número duplicado em um array de inteiros.
- ````challenge_palindromes_iterative```` Palíndromos (Iteratividade):

## Baixar e executar

Para baixar e executar o projeto, siga estas etapas:

Clone o repositório: Abra o terminal (linha de comando) e navegue até o diretório onde você deseja clonar o repositório. Em seguida, execute o seguinte comando para clonar o repositório:

````
git clone https://github.com/seu-usuario/nome-do-repositorio.git
````
Substitua seu-usuario e nome-do-repositorio pelo seu nome de usuário GitHub e pelo nome do repositório, respectivamente.

Acesse o diretório do projeto: Use o comando cd para entrar no diretório do projeto:

````
cd nome-do-repositorio
````

Crie um ambiente virtual (opcional, mas recomendado): É uma boa prática criar um ambiente virtual para isolar as dependências do projeto. Use o seguinte comando para criar um ambiente virtual (você deve ter o Python instalado em seu sistema):

````
python -m venv venv
````

Isso criará um ambiente virtual chamado venv.

Ative o ambiente virtual (opcional): Dependendo do seu sistema operacional, o comando para ativar o ambiente virtual pode variar:

No Windows (PowerShell):

````
.\venv\Scripts\Activate
````

No macOS e Linux:

````
source venv/bin/activate
````

Instale as dependências: Use o pip para instalar as dependências do projeto listadas no arquivo requirements.txt:

````
pip install -r requirements.txt
````

Execute o projeto: Para executar o projeto, siga as instruções específicas fornecidas no README.md do projeto ou no enunciado dos desafios. Geralmente, você pode executar um script Python específico ou um arquivo de teste.

Por exemplo, para executar um arquivo Python chamado meu_programa.py, use:

````
python meu_programa.py
````

Desative o ambiente virtual (opcional): Quando você terminar de trabalhar no projeto, pode desativar o ambiente virtual com o seguinte comando:

````
deactivate
````

Isso deve permitir que você baixe, configure e execute o projeto em seu ambiente de desenvolvimento local. Certifique-se de ler o README.md do projeto específico para obter instruções adicionais ou informações específicas sobre como executar e testar o projeto.

### Dependências

````
-r requirements.txt

wheel==0.38.4
pytest==7.1.2
pytest-json==0.4.0
flake8==5.0.4
black==22.6.0
pytest-cov==3.0.0
big-O==0.10.2
matplotlib==3.6.3
````