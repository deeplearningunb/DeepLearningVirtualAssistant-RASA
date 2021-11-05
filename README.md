# Deep Learning Virtual Assistent 🤖

## Fale com o bot sobre bots;
ChatBot em desenvolvimento 🚧

## Projeto

Projeto idealizado na disciplina de Tópicos Especiais de Engenharia de Software na UnB.
<br>É um projeto que consiste na criação de um chatbot utilizando a framework RASA que visa auxiliar no aprendizado/ensino de Deep Learning bem como suas subareas.

## Problemática

Conteúdo novo e extenso com referências não muito fáceis de encontrar e geralmente encontrados apenas em inglês

## Proposta de Solução

O projeto DLVA(Deep Learning Virtual Assistant) visa criar um chatbot capaz de auxiliar o professor e os alunos da disciplina, por meio de respostas em português as dúvidas mais frequentes, disponibilizar informações sobre o plano de ensino e notas da disciplina.

### Objetivos:

- Trazer definições dos conteúdos (com links) 

- Dizer as datas de entregas dos trabalhos 

- Mandar links dos slides das aulas 

### Vantagens:

-  Respostas imediatas 

- Informações atualizadas 

- Respostas homologadas pelo professor 

## Arquitetura da Rede Neural

<br>O modelo de solução utilizado neste  projeto conta com o framework RASA que utiliza a arquitetura chamada Transformer Neural NetWork. Dentro dos principais arquivos de configuração do Rasa, encontra-se o TEDPolicy e  DietClassifier que são essenciais para a configuração da inteligência do bot e assim gerar um modelo treinado com capacidade de responder o usuário. Para realizar o treinamento e fazer a configuração, utiliza-se no TEDPolicy 3 camadas de transformers, uma camada de normalização e outra de sigmoíde. Para o DietClassifier 2 camadas de transformers, uma camada de normalização e outra sigmoíde. 

### 💻 Tecnologias usadas:
IDE: Visual Studio Code.
<br>Linguagem de programação: Python.
<br>Bibliotecas: Pandas, Keras, TensorFlow e Jupyter.
<br>Frameworks: RASA
<br>Plataforma: Anaconda

### 👦👦👦 Membros :
| Nome | Matrícula |
|:------------ |---|
| Gabriel Ferreira da Silva | 20/0018060 |
| Mateus de Siqueira Silva | 20/0024787 |
| Pedro Vitor Augusto de Jesus | 20/0073249 |

## 💻 Como executar

### 1. Clone o repositório na sua máquina:
```git clone https://github.com/deeplearningunb/``` 
### 2. Instale o Anaconda:

https://www.anaconda.com/products/individual
#### 2.1 Instale o Anaconda-Navigator (Opcional) 

https://anaconda.org/anaconda/anaconda-navigator
### 3. Crie um ambiente conda:

```conda create -n smartbot-demo python=3.8```

### 4. Ative o ambiente conda:

```source activate smartbot-demo```

### 5. Instale o RASA no ambiente:

```conda install rasa```

### 6. Para rodar o projeto no terminal rode na pasta raiz:

```rasa shell```
## RoadMap: 

<img alt="" title="" src="https://github.com/deeplearningunb/SmartBot-RASA/blob/main/img/smartbot_2021-10-30_02.16am.png">
