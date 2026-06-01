# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> Flappy PUC

## 2. Integrantes do grupo

Liste os integrantes do grupo.

- Nome 1: Gabriel Sousa Aguiar
- Nome 2: Nelson Buralli Dabes
- Nome 3: Rafael Mota Azevedo
- Nome 4: Yudy Samuel Ramos

## 3. Tipo de jogo

Indique o tipo de jogo que será desenvolvido.

Exemplos:

- jogo de desviar de obstáculos;
- jogo de coleta de itens;
- labirinto simples;
- jogo de perguntas e respostas;
- jogo de memória;
- Pong;
- Snake;
- Breakout;
- nave desviando de meteoros;
- corrida simples com obstáculos;
- jogo de clique rápido;
- jogo de sobrevivência simples.

Tipo escolhido pelo grupo:

> Jogo de desviar de obstáculos.

## 4. Descrição geral do jogo

Explique, em poucas linhas, como o jogo funcionará.

Procure responder:

- O que aparece na tela?
- O que o jogador controla?
- O que o jogador precisa fazer?
- Quais desafios aparecem durante a partida?

Descrição:

> O jogo será inspirado no Flappy Bird. O jogador controlará um pássaro que deverá atravessar espaços entre canos sem colidir com eles. Os canos aparecerão continuamente e o objetivo será sobreviver pelo maior tempo possível enquanto acumula pontos.

## 5. Objetivo do jogador

Explique qual é o objetivo principal do jogador.

Exemplos:

- coletar o maior número possível de itens;
- sobreviver pelo maior tempo possível;
- chegar até o final do labirinto;
- acertar alvos;
- responder perguntas corretamente;
- evitar obstáculos;
- quebrar todos os blocos.

Objetivo:

> Passar pelo maior número possível de obstáculos sem colidir, obtendo a maior pontuação possível.

## 6. Regras principais

Liste as principais regras do jogo.

Exemplo:

- O jogador começa com 3 vidas.
- Cada moeda coletada vale 10 pontos.
- Cada colisão com obstáculo remove 1 vida.
- A partida termina quando as vidas chegam a zero.
- O jogador vence se alcançar 100 pontos.

Regras do grupo:

- Regra 1: O pássaro cai devido à gravidade.
- Regra 2: O jogador pode fazer o pássaro subir pressionando a barra de espaço.
- Regra 3: Os canos se movimentam da direita para a esquerda.
- Regra 4: Cada obstáculo ultrapassado gera um ponto.
- Regra 5: Ao colidir com um cano ou sair da área de jogo, a partida termina.

## 7. Condição de vitória

Explique como o jogador vence ou conclui o jogo.

Exemplos:

- atingir determinada pontuação;
- chegar ao final da fase;
- sobreviver até o tempo acabar;
- responder uma quantidade mínima de perguntas;
- quebrar todos os blocos.

Condição de vitória:

> O objetivo é alcançar a maior pontuação possível. O jogador pode considerar uma vitória ao superar o recorde anterior.

## 8. Condição de derrota ou encerramento

Explique como o jogador perde ou quando a partida termina.

Exemplos:

- perder todas as vidas;
- acabar o tempo;
- colidir com determinado obstáculo;
- errar muitas perguntas;
- deixar a bola cair, no caso de Breakout ou Pong.

Condição de derrota ou encerramento:

> A partida termina quando o pássaro colide com um cano, com o chão ou com o limite superior da tela.

## 9. Elementos previstos no jogo

Descreva os principais elementos que farão parte do jogo.

## Jogador ou elemento principal

Exemplo:

> Um personagem controlado pelas setas do teclado.

Descrição:

> Um pássaro controlado pelo jogador.

## Obstáculos, inimigos ou desafios

Exemplo:

> Obstáculos aparecem em posições aleatórias e devem ser evitados.

Descrição:

> Canos posicionados com aberturas aleatórias para o jogador atravessar.

## Itens, alvos ou objetos de interação

Exemplo:

> Moedas aparecem na tela e aumentam a pontuação quando coletadas.

Descrição:

> Os próprios espaços entre os canos funcionam como desafios a serem superados.

## Pontuação, vidas, tempo ou progresso

Exemplo:

> O jogador começa com 3 vidas e ganha 10 pontos por item coletado.

Descrição:

> O jogador acumula pontos ao passar pelos obstáculos. O jogo também armazenará o recorde.

## 10. Controles previstos

Informe os comandos que serão utilizados pelo jogador.

Exemplo:

- Seta para cima: mover para cima
- Seta para baixo: mover para baixo
- Seta para esquerda: mover para esquerda
- Seta para direita: mover para direita
- Espaço: realizar ação
- ESC: sair do jogo

Controles do grupo:

- Tecla/comando: Espaço - fazer o pássaro subir.
- Tecla/comando: R - reiniciar a partida.
- Tecla/comando: ESC - encerrar o jogo.

## 11. Organização inicial do código

Explique como o grupo pretende organizar o código.

Exemplo:

- `main.py`: inicia o jogo;
- `src/jogo.py`: contém o loop principal;
- `src/config.py`: guarda configurações como tamanho da tela e cores;
- `src/funcoes.py`: contém funções auxiliares;
- `src/dados.py`: contém funções de leitura e escrita de arquivos.

Organização planejada:

> main.py: inicia o jogo.
> src/jogo.py: loop principal.
> src/passaro.py: movimentação do pássaro.
> src/canos.py: geração e movimentação dos obstáculos.
> src/placar.py: sistema de pontuação e recorde.
> src/dados.py: leitura e gravação do recorde.


## 12. Recursos externos previstos

Informe se o grupo pretende utilizar imagens, sons, fontes, tutoriais ou códigos externos.

Exemplo:

- imagens obtidas de banco gratuito;
- sons gratuitos;
- tutorial usado apenas como referência;
- fonte personalizada.

Recursos previstos:

> Talvez tutoriais, mas apenas como referência para aprendizado do Pygame.

## 13. Principais dificuldades esperadas

Liste as dificuldades que o grupo acredita que poderá enfrentar.

Exemplos:

- movimentação do jogador;
- colisão entre objetos;
- controle de tempo;
- criação do ranking;
- organização do código;
- uso do GitHub;
- testes;
- exibição de textos na tela.

Dificuldades previstas:

- Dificuldade 1: Implementação da colisão entre pássaro e canos.
- Dificuldade 2: Organização do código em módulos.
- Dificuldade 3: Utilização correta do GitHub em grupo.
- Dificuldade 4: Efetuação do recorde ser gravado ao final de cada nova tentativa.

## 14. Escopo mínimo para a entrega final

Descreva qual será a versão mínima aceitável do jogo.

Esta seção é importante para evitar que o grupo escolha uma ideia grande demais.

Exemplo:

> A versão mínima do jogo terá um personagem controlado pelo teclado, obstáculos aparecendo na tela, sistema de vidas, sistema de pontuação e tela de fim de jogo.

Escopo mínimo:

> A versão mínima do jogo terá um pássaro controlável, obstáculos em movimento, sistema de pontuação, condição de derrota e tela de fim de jogo.

## 15. Possíveis melhorias, caso haja tempo

Liste funcionalidades extras que o grupo poderá implementar se conseguir concluir o escopo mínimo.

Exemplos:

- tela inicial;
- sons;
- fases;
- aumento de dificuldade;
- ranking;
- animações;
- novos tipos de obstáculos;
- diferentes personagens;
- menu de pausa.

Melhorias possíveis:

- Melhoria 1: Sistema de ranking.
- Melhoria 2: Aumento progressivo da dificuldade.