# Flappy Python

Flappy Pithon

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

## Integrantes do grupo

* Gabriel Sousa Aguiar
* Nelson Buralli Dabes
* Rafael Mota Azevedo
* Yudy Samuell Ramos

## Estrutura do projeto

* `main.py`: ponto de entrada da aplicação.
* `src/`: código-fonte principal do jogo (loop, regras, lógica e dados).
* `assets/`: imagens, fontes e sons.
* `data/`: arquivos persistentes (recorde e ranking).
* `tests/`: testes unitários com `pytest`.
* `docs/`: documentação do projeto.

## Descrição do jogo

O Flappy Python é um jogo em que o jogador controla um pássaro que deve atravessar espaços entre canos sem colidir com eles. A cada obstáculo ultrapassado, a pontuação aumenta. O objetivo é alcançar a maior pontuação possível e superar o recorde armazenado pelo jogo.

## Objetivo do jogador

Controlar o pássaro utilizando a tecla Espaço para evitar colisões com os canos, o teto e o chão, acumulando a maior quantidade de pontos possível.

## Regras do jogo

* O pássaro é afetado pela gravidade e cai constantemente.
* Ao pressionar a tecla Espaço, o pássaro sobe.
* Canos são gerados periodicamente e se movem da direita para a esquerda.
* O jogador ganha pontos ao ultrapassar um cano.
* O jogo termina quando ocorre colisão com um cano, com o teto ou com o chão.
* O recorde é salvo em arquivo para ser utilizado nas próximas partidas.

## Controles

* Espaço: faz o pássaro subir.
* Fechar a janela: encerra o jogo.
* Espaço após Game Over: reinicia a partida.

## Estruturas de Dados Utilizadas

O projeto utiliza:

* Listas para armazenar os canos ativos na tela.
* Dicionários para armazenar os dados do pássaro e dos obstáculos.
* Arquivos para salvar e carregar o recorde do jogador.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Funcionalidades Implementadas

* Sistema de pontuação.
* Sistema de recorde persistente.
* Geração automática de obstáculos.
* Detecção de colisão.
* Tela de Game Over.
* Reinício da partida.
* Testes básicos de lógica.

## Checklist mínimo para entrega

* Jogo executável.
* README atualizado.
* Testes implementados.
* Utilização de listas e dicionários.
* Leitura e escrita de arquivos.
* Estrutura modularizada em múltiplos arquivos.

