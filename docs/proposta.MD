# Flappy Python

## Integrantes

* Gabriel Sousa Aguiar
* Nelson Buralli Dabes
* Rafael Mota Azevedo
* Yudy Samuel Ramos

---

## Descrição do Projeto

Flappy Python é um jogo desenvolvido em Python utilizando a biblioteca Pygame, inspirado no clássico Flappy Bird.

O jogador controla um pássaro e deve atravessar obstáculos sem colidir com eles. Durante a partida, o jogador acumula pontos e avança por diferentes cenários, representando cidades distintas. O jogo também conta com sistema de recorde, efeitos sonoros, músicas e tela de vitória.

---

## Objetivo do Jogo

O objetivo é controlar o pássaro, atravessar os obstáculos e alcançar a maior pontuação possível.

O jogador vence ao atingir 50 pontos e completar todas as fases do jogo.

---

## Controles

| Tecla  | Função                            |
| ------ | --------------------------------- |
| Espaço | Iniciar partida                   |
| Espaço | Fazer o pássaro subir             |
| Espaço | Reiniciar após derrota ou vitória |
| ESC    | Fechar o jogo                     |

---

## Mecânicas Implementadas

* Movimentação do pássaro com gravidade;
* Sistema de obstáculos (canos);
* Sistema de pontuação;
* Sistema de recorde salvo em arquivo;
* Colisão com obstáculos;
* Tela inicial;
* Tela de Game Over;
* Tela de vitória;
* Sistema de fases;
* Mudança de cenários;
* Música de menu;
* Música durante a partida;
* Efeitos sonoros.

---

## Fases

O jogo possui cinco cenários diferentes:

1. Campo
2. Cidade Dourada
3. Horizonte Noturno
4. Distrito Industrial
5. Neo Sunset

As fases são alteradas conforme a pontuação do jogador.

---

## Tecnologias Utilizadas

* Python 3
* Pygame
* Git
* GitHub

---

## Estrutura do Projeto

```text
Projeto-Jogo-GNRY/
│
├── assets/
│   ├── imagens/
│   ├── sons/
│   └── fontes/
│
├── docs/
│   └── proposta.md
│
├── src/
│   ├── config.py
│   ├── funcoes.py
│   ├── jogo.py
│   └── sprites.py
│
├── main.py
└── README.md
```

---

## Como Executar

1. Instale o Python 3.
2. Instale a biblioteca Pygame:

```bash
pip install pygame
```

3. Execute o arquivo principal:

```bash
python main.py
```

---

## Conceitos da Disciplina Utilizados

* Variáveis
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Modularização
* Listas
* Dicionários
* Manipulação de arquivos
* Organização de código
* Testes de funções

---

## Desafios Encontrados

* Implementação da colisão entre pássaro e obstáculos;
* Sistema de troca de fases;
* Integração de sons e músicas;
* Persistência do recorde em arquivo;
* Organização do projeto em módulos.

---

## Referências e Recursos Utilizados

### Imagens

* Itch.io

### Sons e músicas

* Pixabay Music
* Freesound

### Fonte

* FS Pixel Sans

### Biblioteca

* Pygame

Os recursos utilizados foram adaptados para fins acadêmicos e educacionais.


