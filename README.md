# GIF em Tempo Real

## Introdução:

O projeto baseia-se na criação de um gif em tempo real, o qual rotaciona a tela da câmera com o centro no meio da imagem e possui funcionalidades para outros efeitos, como: Alterar velocidade, Expansão e Contração.

## Implementação:

1. Certifique-se de ter o python instalado em seu computador;<br>
2. Clone esse repositório para algum lugar de sua máquina;<br>
3. Instale as bibliotecas necessárias contidas no arquivo "requirements.txt", através do comando:
```
 pip install -r requirements.txt
```

## Organização:

O código do Gif do projeto foi desenvolvido por completo no arquivo "demo.py", além da criação de um arquivo "requirements.txt" para instalação de bibliotecas. Além dos comentários iniciais, para a melhor organização, a cada processo foi adicionado um comentário de explicação.

## Funções e Equações:

### Criar Índices:

1. Cria uma lista de tuplas contendo todas as combinações cartesianas de elementos entre os intervalos especificados para i e j;

4. Extrai os valores i de cada tupla na lista L e os converte em um array NumPy idx_i;

5. Similar ao passo anterior, extrai os valores j de cada tupla na lista L e os converte em um array NumPy idx_j;

6. Empilha verticalmente (vertical stack) os arrays idx_i e idx_j para criar uma matriz bidimensional idx, onde a primeira linha contém todos os valores de i e a segunda linha contém todos os valores de j;

7. Retorna a matriz idx, que contém todos os índices cartesianos no intervalo especificado.

### Inicialização:
1. Tamanho da tela definido em 640x480;
2. $\theta$ inicializado em 0;
3. Velocidade de aumento começando em 0.05;
4. Matriz D identidade inicializada.

### Matrizes:
1. Matriz D:
Matriz identidade, que é alterada ao clicar "e" ou "c" para expansão e contração, respectivamente;

2. Matriz T:
Definição da Matriz de Translação, dado o tamanho da tela;

3. Matriz A:
Matriz de Rotação que começa com o $\theta$ = 0 e aumenta através da variável "vel" a cada clique na tecla "v". Representada na fórmula abaixo:
$$
A = 
\begin{bmatrix}
    \cos(\theta) & -\sin(\theta) & 0 \\
    \sin(\theta) & \cos(\theta) & 0 \\
    0 & 0 & 1
\end{bmatrix}
$$

4. Matriz B:
Matriz B definida para cálculo da tela, realizada através da multiplicação das matrizes T, D, A e inversa da T. A multiplicação de T e inversa de T é realizada, pois para rotacionar ao redor de um ponto arbitrário é preciso deslocar esse ponto para a origem (ou seja, realizar uma translação), realizar a rotação e, por último, desfazer a translação. Já a matriz D é multiplicada para a implementação da expansão e contração da imagem.

### Filtro, Clip e Artefatos:

Filtro aplicado para que a imagem fique no tamanho da tela, não acessando pixels inexistentes, independete do lado, em conjunto de método "clip" para recorte ideal. Além da remoção de possíveis artefatos para clareza da imagem.

## Arquivo Demo e Insruções:

1. Rode o arquivo "demo.py";<br>
2. A câmera de seu computador abrirá com a tela "girando";<br>
3. Aperte "c" para contrair a imagem;<br>
4. Aperte "e" para expandir a imagem (apenas se a imagem estiver contraída);<br>
5. Aperte "v" para aumentar a velocidade de rotação da imagem;<br>
6. Aperte "q" para sair.

## Referências:

1. Código desenvolvido com o auxílio do "Notebook" realizado pelo professor Marcio Fernando Stabile Junior.

## Equipe:
Projeto desenvolvido por Gustavo Colombi Ribolla e Rafaela Afférri de Oliveira.