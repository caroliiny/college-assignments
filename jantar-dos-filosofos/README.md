# 🧠 Jantar das Cientistas da Computação

Este projeto é uma adaptação gráfica do clássico problema do **Jantar dos Filósofos**, utilizando **Python**, **Tkinter** e **Pillow**, com um toque especial: cientistas da computação representadas por fotos (no projeto original havia fotos reais das cientistas, porém para respeitar sua privacidade resolvi deixar fotos padrão).

## 🎯 Objetivo

Simular a concorrência entre threads representando cientistas da computação que alternam entre pensar e comer, compartilhando recursos limitados (garfos) com um controle de concorrência para evitar deadlock.

## 📸 Interface

A interface gráfica apresenta:
- Imagens das cinco cientistas.
- Seus estados em tempo real:
  - **"Só sei que nada sei"** (pensando) – azul
  - **"MDS FOME"** (com fome) – vermelho
  - **"Esperando a vez"** – amarelo
  - **"Comendo"** – verde claro

## 🛠️ Tecnologias

- Python 3
- Tkinter (interface gráfica)
- Threading (concorrência)
- Pillow (para manipulação de imagens)

## 📁 Estrutura de Arquivos

