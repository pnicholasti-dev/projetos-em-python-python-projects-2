# projetos-em-python-python-projects-2
Vários projetos em python / python projects
1 - (PT-BR)O programa solicita números ao usuário e realiza a soma continuamente.
Enquanto a soma for menor que 100, novos valores podem ser inseridos.
Quando o total atingir ou ultrapassar 100, o programa encerra exibindo a soma final.
Conceitos utilizados:
Estrutura de repetição while
Variáveis acumuladoras
Entrada de dados com input
Condições (if)

(EN)The program prompts the user for numbers and continuously performs the sum.
As long as the sum is less than 100, new values ​​can be entered.
When the total reaches or exceeds 100, the program ends, displaying the final sum.
Concepts used:
While loop structure
Accumulator variables
Data input with input
Conditions (if)

2- (PT-BR)Foi desenvolvido um sistema básico de login que solicita usuário e senha.
Enquanto os dados estiverem incorretos, o programa informa erro e pede novamente as informações.
Ao inserir o login e senha corretos, o acesso é liberado e o programa encerrado.
Credenciais utilizadas:
Login: admin
Senha: 1234
Conceitos utilizados:
Estrutura de repetição while
Operadores lógicos
Validação de dados
Condicionais

(EN)A basic login system was developed that requests a username and password.
While the data is incorrect, the program displays an error and requests the information again.
Upon entering the correct login and password, access is granted and the program terminates.
Credentials used:
Login: admin
Password: 1234
Concepts used:
While loop structure
Logical operators
Data validation
Conditional statements

3-(PT-BR)O programa recebe valores de compras de clientes e realiza a soma total das vendas do dia.
O sistema continua funcionando até que o operador digite 0, encerrando o programa e exibindo o valor total arrecadado.
Conceitos utilizados:
Estrutura de repetição while
Variável acumuladora
Entrada de dados com input
Condição de parada

(EN)The program receives purchase values ​​from customers and calculates the total sales for the day.
The system continues to run until the operator enters 0, ending the program and displaying the total amount collected.
Concepts used:
While loop structure
Accumulator variable
Data input with input
Stopping condition

4-(PT-BR)Foi desenvolvido um sistema que registra a quantidade de entregas realizadas em cada viagem.
O usuário informa os valores continuamente e o sistema soma todas as entregas feitas.
O programa encerra quando o valor 0 é digitado, mostrando o total final de entregas.
Conceitos utilizados:
Loop while
Soma acumulativa
Controle de fluxo
Entrada e validação de dados

(EN)A system was developed that records the number of deliveries made on each trip.
The user continuously enters the values, and the system sums all the deliveries made.
The program ends when the value 0 is entered, showing the final total of deliveries.
Concepts used:
While loop
Cumulative sum
Flow control
Data input and validation

5-(PT-BR)Sistema simples de caixa para uma loja contendo três produtos:
Feijão — R$ 8,00
Arroz — R$ 6,50
Farinha — R$ 5,00
O programa permite registrar vendas, calcular automaticamente o total vendido e encerrar somente quando o usuário escolher a opção de saída.
Conceitos utilizados:
while True
Menus interativos
Estruturas condicionais (if, elif)
Acumuladores
Simulação de sistema de vendas

(EN)Simple point-of-sale system for a store containing three products:
Beans — R$ 8.00
Rice — R$ 6.50
Flour — R$ 5.00
The program allows registering sales, automatically calculating the total sold, and closing only when the user chooses the exit option.
Concepts used:
while True
Interactive menus
Conditional structures (if, elif)
Accumulators
Sales system simulation

6- (PT-BR)O programa solicita ao usuário a quantidade de compras realizadas durante o dia e, em seguida, registra o valor de cada compra individualmente.
Ao final, o sistema exibe o valor total faturado formatado em reais.
Conceitos utilizados:
Estrutura de repetição for
Variáveis acumuladoras
Entrada de dados com input
Formatação monetária

(EN)The program asks the user for the number of purchases made during the day and then records the value of each purchase individually.
At the end, the system displays the total amount billed, formatted in reais (Brazilian currency).
Concepts used:
For loop structure
Accumulator variables
Data input with input system
Current formatting

7-(PT-BR)Sistema desenvolvido para registrar lotes de produtos adicionados ao estoque.
O usuário informa quantos lotes chegaram e a quantidade de itens presente em cada lote.
Ao final, o programa mostra o total de itens adicionados ao estoque.
Conceitos utilizados:
Loop for
Soma acumulativa
Controle de estoque simples
Manipulação de variáveis

(EN)System developed to record batches of products added to inventory.
The user enters how many batches have arrived and the quantity of items in each batch.
At the end, the program displays the total number of items added to inventory.
Concepts used:
For loop
Cumulative sum
Simple inventory control
Variable manipulation

8- (PT-BR)O programa registra a quantidade de viagens realizadas por uma empresa de logística e a quantidade de entregas feitas em cada viagem.
Ao final, o sistema exibe:
Total de entregas realizadas
Média de entregas por viagem
Conceitos utilizados:
Estrutura de repetição for
Cálculo de média
Acumuladores
Processamento de dados numéricos

(EN)The program records the number of trips made by a logistics company and the number of deliveries made on each trip.
At the end, the system displays:
Total deliveries made
Average deliveries per trip
Concepts used:
For loop structure
Average calculation
Accumulators
Numerical data processing

Desafio/Challenge
(PT-BR)
Este repositório contém um sistema desenvolvido em Python utilizando menus interativos e estruturas condicionais para simular módulos de uma instituição escolar.

O projeto foi dividido em três áreas principais: cadastro de alunos, cadastro de professores e setor financeiro.

✅ Funcionalidades do sistema
1. Cadastro de alunos

O sistema permite cadastrar alunos informando:

Nome
Duas notas

Após o cadastro, o programa calcula automaticamente a média do aluno e informa sua situação:

Aprovado → média maior que 70
Recuperação → média entre 60 e 70
Reprovado → média menor que 40

Conceitos utilizados:

Entrada de dados
Estruturas condicionais (if, elif, else)
Cálculo de média
Menus interativos
2. Cadastro de professores

Módulo responsável pelo registro de professores e validação da titulação acadêmica.

O sistema:

Lê o nome e a titulação
Verifica permissões de acordo com a formação
Regras implementadas:
Professores com mestrado ou doutorado podem orientar projetos
Professores com graduação podem ministrar apenas aulas básicas
Qualquer outro valor informado é tratado como titulação inválida

Conceitos utilizados:

Validação de dados
Condicionais
Manipulação de texto
Estrutura de menus
3. Setor financeiro

Sistema responsável pelo cálculo financeiro de alunos e professores.

Funcionalidades:
Aluno
Exibe mensalidade fixa
Verifica se o pagamento foi realizado em dia
Professor
Calcula valor da hora:
salário ÷ 160 horas
Calcula horas extras com acréscimo de 50%
Exibe o total a receber:
salário + horas extras

Conceitos utilizados:

Operações matemáticas
Cálculo de porcentagem
Estruturas condicionais
Organização modular do sistema

(EN)This repository contains a system developed in Python using interactive menus and conditional structures to simulate modules of a school institution.

The project was divided into three main areas: student registration, teacher registration, and financial sector.

✅ System Functionalities

1. Student Registration

The system allows you to register students by providing:

Name
Two grades

After registration, the program automatically calculates the student's average and informs their status:

Passed → average greater than 70
Recovery → average between 60 and 70
Failed → average less than 40

Concepts used:

Data input
Conditional structures (if, elif, else)
Average calculation
Interactive menus

2. Teacher Registration

Module responsible for registering teachers and validating academic qualifications.

The system:

Reads the name and academic title. Checks permissions according to the educational background.
Implemented rules: Professors with a master's or doctoral degree can supervise projects. Professors with a bachelor's degree can only teach basic classes. Any other value entered is treated as an invalid academic title.

Concepts used:

Data validation. Conditional statements. Text manipulation. Menu structure.

3. Financial Sector

System responsible for calculating the financial costs of students and professors.

Functionalities:
Student: Displays fixed monthly fee. Checks if payment was made on time.
Professor: Calculates hourly rate: (salary ÷ 160 hours). (Calculates overtime with a 50% increase). (Displays the total to be received: salary + overtime).

Concepts used:

Mathematical operations. (Percentage calculation). (Conditional structures). (Modular system organization).
