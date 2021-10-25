# Respostas

## ANN

    Definição
    ----------
       ANN significa artificial neural network, traduzido para português como rede neural artificial.
        A rede neural artificial é uma rede artificial que utiliza uma série de neurônios para aprender, sendo este um sistema de hardware e/ou software padronizado após a operação de neurônios no cérebro humano.

    Arquitetura
    -----------
        Uma rede ANN contém um grande número de neurônios artificiais (por isso que é chamada de rede neural artificial), organizadas em uma série de camadas, onde cada camada é composta por uma série de neurônios. 

    Ativadores
    ----------
        A função de ativação, em geral, é o conjunto de funções de transferência usadas para obter a saída desejada dela. Existem vários sabores da função de ativação, mas principalmente conjuntos lineares ou não lineares de funções. Algumas das funções de ativação mais utilizadas são as funções de ativação binária, sigmoidal (linear) e sigmoidal hiperbólica tan (não linear). 

    Camadas
    -------
        3 camadas moldam a rede neural artificial, sendo a primeira camada de entrada, a segunda camada oculta e a terceira camada de saída.
            As camadas de entrada contêm esses neurônios artificiais (denominados como unidades) que devem receber entrada do mundo exterior. É aí que o aprendizado real na rede acontece, ou o reconhecimento acontece, então ele irá processar.

            As camadas ocultas são mencionadas ocultas entre as camadas de entrada e as camadas de saída. O único trabalho de uma camada oculta é transformar a entrada em algo significativo que a camada / unidade de saída possa usar de alguma forma.
            A maioria das redes neurais artificiais estão todas interconectadas, o que significa que cada uma das camadas ocultas é conectada individualmente aos neurônios em sua camada de entrada e também em sua camada de saída, não deixando nada pairando no ar. Isso possibilita um processo de aprendizado completo e também o aprendizado ocorre ao máximo quando os pesos dentro da rede neural artificial são atualizados após cada iteração. 

            
            As camadas de saída contêm unidades que respondem às informações que são alimentadas no sistema e também se ela aprendeu alguma tarefa ou não.

    Fonte: https://mindmajix.com/artificial-neural-network-and-how-it-works

## CNN

    Definição

    CNN significa Convolutional Neural Network, traduzido para português como rede neural convolucional.
    Uma Rede Neural Convolucional (ConvNet / Convolutional Neural Network / CNN) é um algoritmo de Aprendizado Profundo que pode captar uma imagem de entrada, atribuir importância (pesos e vieses que podem ser aprendidos) a vários aspectos / objetos da imagem e ser capaz de diferenciar um do outro. O pré-processamento exigido em uma ConvNet é muito menor em comparação com outros algoritmos de classificação. Enquanto nos métodos primitivos os filtros são feitos à mão, com treinamento suficiente, as ConvNets têm a capacidade de aprender esses filtros / características.

    Arquitetura

        A arquitetura de uma ConvNet é análoga àquela do padrão de conectividade de neurônios no cérebro humano e foi inspirada na organização do Visual Cortex. Os neurônios individuais respondem a estímulos apenas em uma região restrita do campo visual conhecida como Campo Receptivo. Uma coleção desses campos se sobrepõe para cobrir toda a área visual. Os neurônios são conectados entre si para formar uma rede.
        As Redes Neurais Convolucionais são compostas por quatro camadas primárias: CONV, POOL, RELU e FC. Pegando essas camadas e empilhando-as em um determinado padrão rende uma arquitetura CNN.

    Ativadores

        Em um CNN, aplicamos uma função de ativação não linear, como ReLU, ELU ou qualquer uma das outras variantes Leaky ReLU. Normalmente denotamos camadas de ativação como RELU em diagramas de rede, uma vez que as ativações de ReLU são mais comumente usadas, também podemos simplesmente declarar ACT - em ambos os casos, estamos deixando claro que uma função de ativação está sendo aplicada dentro da arquitetura de rede.

    Camadas

        A camada CONV é o bloco de construção central de uma Rede Neural Convolucional. Os parâmetros de camada CONV consistem em um conjunto de filtros k aprendendo (ou seja, "kernels"), onde cada filtro tem uma largura e uma altura, e são quase sempre quadrados. Estes filtros são pequenos (em termos de suas dimensões espaciais), mas se estendem por toda a profundidade do volume.

        Depois de cada camada CONV em uma CNN, aplicamos uma função de ativação não linear, as camadas de ativação não são tecnicamente "camadas" (devido ao fato de que nenhum parâmetro/pesos são aprendidos dentro de uma camada de ativação) e às vezes são omitidos dos diagramas de arquitetura de rede, pois se presume que uma ativação segue imediatamente uma convolução

        Existem dois métodos para reduzir o tamanho de um volume de entrada — camadas CONV com um passo > 1 e camadas POOL. É comum inserir camadas POOL entre camadas CONV consecutivas em uma arquitetura CNN:
        INSUMO => CONV => RELU =pool de > => CONV => RELU =pool de > => FC
        A função principal da camada POOL é reduzir progressivamente o tamanho espacial (isto é, largura e altura) do volume de entrada. Isso nos permite reduzir a quantidade de parâmetros e computação na rede - o pooling também nos ajuda a controlar o overfitting.
        As camadas POOL operam em cada uma das fatias de profundidade de uma entrada, independentemente, usando a função máxima ou média. O pool máximo é normalmente feito no meio da arquitetura CNN para reduzir o tamanho espacial, enquanto o pooling médio é normalmente usado como a camada final da rede (por exemplo, GoogLeNet, SqueezeNet, ResNet), onde desejamos evitar o uso de camadas FC inteiramente. O tipo mais comum de camada POOL é o pool máximo, embora essa tendência esteja mudando com a introdução de micro-arquiteturas mais exóticas. 

        Os neurônios nas camadas FC estão totalmente conectados a todas as ativações na camada anterior, como é o padrão para redes neurais feedforward. As camadas FC são sempre colocadas no final da rede (ou seja, não aplicamos uma camada CONV, depois uma camada FC, seguida por outra camada CONV).É comum usar uma ou duas camadas FC antes de aplicar o classificador softmax

    fontes:
    https://www.tensorflow.org/tutorials/images/cnn
    https://www.inf.ufpr.br/todt/IAaplicada/CNN_Presentation.pdf
    https://www.deeplearningbook.com.br/introducao-as-redes-neurais-convolucionais/
    https://www.youtube.com/watch?v=zAfBy74c2AI
    https://www.pyimagesearch.com/2021/05/14/convolutional-neural-networks-cnns-and-layer-types/

## RNN

    Definição

        RNN significa recurrent neural network, trauduzido para português como rede neural recorrente.
        Uma Rede Neural Recorrente (RNN) é um algoritmo de Aprendizado Profundo que pode captar uma sequência de dados e ser capaz de aprender a reconhecer essa sequência.
        As conexões entre os nós formam um grafo direcionado ao longo de uma sequência temporal. Isso permite que ele exiba um comportamento dinâmico temporal. Derivado de redes neurais feedforward, os RNNs podem usar seu estado interno (memória) para processar sequências de entradas de comprimento variável.

    Arquitetura

        Considerando uma rede Neural feed-forward simples com uma camada oculta. Se {X} _ {t} for a entrada e {Y} _ {t} for a saída na etapa de tempo t, tudo o que precisamos fazer é criar um feedback conexão da camada oculta a ela mesma para acessar informações na etapa t-1. O ciclo de feedback implica que há um atraso de uma unidade de tempo. Portanto, uma das unidades de entrada em {h} _ {t} é {h} _ {t-1} , por sua vez a camada oculta recebe ambos {X } _ {t} e seu próprio último valor. Portanto, em poucas palavras, esse ciclo de feedback permite que as informações sejam passadas de uma etapa da rede para a próxima e, portanto, atua como memória na rede.

    Ativadores

        A função de ativação pode ser qualquer uma das não linearidades ocultas habituais que geralmente é sigmoid, tanh ou ReLu. É um hiper parâmetro como outros tipos de redes neurais.

    Camadas

        Geralmente existem 3 tipos de camadas RNN disponíveis, você pode encontrá-las na biblioteca tensorflow, sendo elas: Basic RNN Block, LSTM e GRU.

    Exemplos:
        https://youtu.be/LY7x2Ihqjmc

    Uso:
        https://github.com/deeplearningunb/building-rnn

    font :
    https://towardsmachinelearning.org/recurrent-neural-network-architecture-explained-in-detail/
    https://docs.google.com/presentation/d/1MU-IQB6nxd6fPt9-1hJaByOzTAxSSXT4Gb17JxBz72o/edit#slide=id.g5a466f77f0_0_58
    https://pianalytix.com/recurrent-neural-network-rnn/

## SAE

    Definição

        SAE significa "Sequential Autoencoder", ou seja, uma rede autoencoder sequencial.
        A rede autoencoder sequencial é uma rede neural que aprende a reconhecer uma sequência de dados, usando um processo de treinamento de recursos de aprendizagem não supervisionados por cada camada, o que resulta em uma precisão de previsão consideravelmente melhorada do modelo de calibração.

    Arquitetura

        A rede SAE é um modelo não supervisionado, ou seja, não tem um conjunto de dados de treinamento, sendo esta construída como uma camada oculta, que é a camada intermediária entre a entrada e a saída.

    fonte:
    https://www.sciencedirect.com/science/article/abs/pii/S135044952030668X#:~:text=The%20stacked%20auto-encoder%20%28SAE%29%20deep%20neural%20network%20is,considerably%20improved%20prediction%20accuracy%20of%20the%20calibration%20model%2C%2C.

## SOM

    Definição

        SOM signfica Self Organizing Map, traduzindo para português temos Mapa Auto Organizável, esta é uma rede neural que aprende a reconhecer um mapa de dados, usando um processo de treinamento de recursos de aprendizagem não supervisionados por cada camada, o que resulta em uma precisão de previsão consideravelmente melhorada do modelo de calibração.

    Arquitetura

        O SOM um contém duas camadas: uma camada de entrada e uma camada de saída (mapa de feições). O SOM inicia o mapeamento de recursos inicializando um vetor de peso. Pesos em SOM têm uma conotação completamente diferente do que em ANN. Na modelagem de uma rede neural: a função de ativação é aplicada à combinação linear dos pesos e valores de entrada para produzir saída para cada um dos neurônios na arquitetura. Por outro lado, o SOM não aplica a função de ativação e emprega pesos como as características do neurônio na arquitetura. Os pesos geralmente são gerados aleatoriamente. A motivação de usar o vetor de peso como características do neurônio é empurrar cada uma das linhas (observações) dos dados fornecidos para um espaço imaginário onde cada uma das linhas atua como um ponto. 

    Ativadores

        A rede SOM não possui ativadores e a função de ativação é aplicada ao vetor de pesos.

    Camadas
    
        O SOM possui apenas uma camada de entrada e uma camada de saída.

    fontes:
    www.academia.edu/4029195/SOM_ARTIFICIAL_NEURAL_NETWORK
