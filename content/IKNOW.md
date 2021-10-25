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

    ### Definição

    > SAD

    ### Arquitetura

    > png

    ### Ativadores

    > att

    ### Camadas

    5

## SAE

    ### Definição

    > SAD

    ### Arquitetura

    > png

    ### Ativadores

    > att

    ### Camadas

    5

## SOM

    ### Definição

    > SAD

    ### Arquitetura

    > png

    ### Ativadores

    > att

    ### Camadas

    5
