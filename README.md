# Sistema de Controle de Qualidade
### Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

Esse repositório faz parte do trabalho final da disciplina de "Algoritmos e Lógica de Programação" do curso: "Graduação Tecnológica em Inteligência Artificial e Automação Digital" da Faculdade de Tecnologia Rocketseat em parceria com a UniFECAF.

Foi desenvolvido um script em Python com o intuito de resolver a situação de uma empresa que precisa de uma solução digital para auxiliar "no controle de produção e qualidade das peças fabricadas em sua linha de montagem", tornando o processo mais rápido, preciso e menos custoso com a diminuição de falhas causadas pela inspeção manual.


# Funcionamento

A principal função consiste em receber dados de uma peça produzida e verificar automaticamente se ela está aprovada ou reprovada de acordo com critérios de qualidade:

- Peso: entre 95g e 105g
- Cor: azul ou verde
- Comprimento: entre 10cm e 20cm

Peças aprovadas são armazenadas em caixas com limite de até 10 itens, sendo fechadas automaticamente quando ficar cheia e iniciando uma nova caixa.
As peças reprovadas podem ser listadas com seus respectivos motivos de reprova.

Toda peça deve ter um ID único para rastreabilidade adequada.

---

As funções do sistema são acessíveis de forma intuitiva por meio de um menu inicial. E são elas:

1 - Cadastrar nova peça

2 - Listar peças (podendo escolher entre aprovadas, reprovadas ou todas)

3 - Remover peça pelo ID

4 - Listar caixas

5 - Gerar relatório

# Como Executar na Máquina Local

É necessário ter Python 3.x instalado no sistema: [download](https://www.python.org/downloads)

## Passo a passo
1 - Baixar o arquivo `main.py`

2 - Abrir o terminal/prompt de comando

3 - Navegar até a pasta onde está o arquivo. Ex.:
```bash
   cd caminho/para/a/pasta
 ```

4 - Executar o programa:
```bash
   python main.py
 ```

5 - O menu do programa aparecerá, e então basta começar a usar.

---
# Exemplos de entrada e saída

### 01: Cadastro de peça aprovada
```
Escolha uma opção: 1

--- CADASTRAR NOVA PEÇA ---
ID da peça: P001
Peso (g): 100
Cor: azul
Comprimento (cm): 15

✓ Peça APROVADA
```

### 02: Cadastro de peça reprovada
```
Escolha uma opção: 1

--- CADASTRAR NOVA PEÇA ---
ID da peça: P002
Peso (g): 90
Cor: vermelho
Comprimento (cm): 25

✗ Peça REPROVADA
Motivo: Peso fora do padrão. Cor inválida. Comprimento fora do padrão.
```

### 03: Gerar relatório
```
Escolha uma opção: 5

==================================================
RELATÓRIO FINAL DE PRODUÇÃO
==================================================

Total de peças processadas: 15
Peças aprovadas: 12
Peças reprovadas: 3
Caixas utilizadas: 2

--- DETALHES DAS REPROVAÇÕES ---
Peça P002: Peso fora do padrão. Cor inválida. Comprimento fora do padrão.
Peça P008: Cor inválida.
Peça P013: Peso fora do padrão.

--- DETALHES DAS CAIXAS ---
Caixa 1: 10 peças (FECHADA)
Caixa 2: 2 peças (EM PREENCHIMENTO)

==================================================
```
