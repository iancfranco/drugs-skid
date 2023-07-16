import time
import os
import math
import random
var_controle = False
tutorial = False
mod_dificuldade_int = 1
mod_dificuldade_dec = 1

# Altere apenas as categorias indicadas com [ Alterável ] ao lado direito.

# Config Basica
if var_controle == False:
    os.system('cls')
    print("----------------------------------------")
    print("              Drug's Skid               ")
    print("----------------------------------------")
    while True:
        resposta = input("Deseja ver o tutorial - recomendado para iniciantes - [S/N]? ")
        if resposta == "S" or resposta == "s":
            print("Iniciando o tutorial.")
            time.sleep(3)
            tutorial = True
            os.system('cls')
            break
        elif resposta == "N" or resposta == "n":
            print("Nenhuma dica será mostrada.")
            time.sleep(2)
            tutorial = False
            os.system('cls')
            break
        else:
            print("Por favor insira um valor válido (S ou N).")
            time.sleep(2)
            print("\033[F" + " " * 100)
    while True:
        print("----------------------------------------")
        print("              Drug's Skid               ")
        print("----------------------------------------")
        if tutorial == True:
            print("Seja bem vindo ao Drug's Skid!")
            time.sleep(0.5)
            print("Drug's Skid é um jogo de negócios e estratégia baseado em dias/turnos.")
            time.sleep(0.5)
            print("No jogo você se torna um traficante de drogas para pagar suas dívidas com um agiota.")
            time.sleep(0.5)
            print("O objetivo do jogo é pagar suas dívidas e ganhar o máximo de dinheiro em um certo tempo(dias) definido por você.")
            time.sleep(0.5)
            print("É importante que você se atente a sua dívida com o agiota, já que a cada dia ela aumenta e caso você não pague dentro do prazo, você será cobrado.")
            time.sleep(0.5)
            print("O jogador começa com $2000, 30kg disponíveis e três dias para pagar uma dívida de $2500. ")
            time.sleep(0.5)
            print("Toda vez que o usuário utiliza a interação de passar para o próximo dia, o valor das drogas é atualizado, a dívida com o agiota aumenta, seu dinheiro no banco rende, as fábricas produzem, entre várias outras coisas.")
            time.sleep(0.5)
            print("O jogador pode utilizar as lojas para comprar armas para se proteger ou realizar assaltos, coletes para aumentar sua vida, mochilas para aumentar a capacidade/peso, medicamentos para recuperar sua vida, entre outros.")
            time.sleep(0.5)
            print("Diversas outras interações como trabalhar no banco, hospital ou agiota, comprar negócios, fábricas, e muito mais estão disponíveis, deixamos para que você descubra.")
            time.sleep(5)
            resposta = input("Pressione enter para continuar.")
            time.sleep(0.5)
            os.system('cls')
        if tutorial == True:
            print("Tutorial: Quantidade máxima de dias/rodadas que você vai jogar:")
        max_dias = input("Deseja jogar por quantos dias? ")
        if max_dias.isnumeric() == False:
            print("Por favor, insira um número de dias válido (número inteiro).")
            time.sleep(2)
            os.system('cls')
        elif max_dias < 1:
            print("Por favor, insira um número de dias maior ou igual a 1.")
            time.sleep(2)
            os.system('cls')
        else:
            max_dias = int(max_dias)
            print("----------------------------------------")
            print("[1] - Muito fácil")
            print("[2] - Fácil")
            print("[3] - Normal")
            print("[4] - Difícil")
            print("[5] - Impossível")
            if tutorial == True:
                print("Tutorial: Dificuldade de jogo, cada uma tem um multiplicador diferente que altera valores no jogo como preços, quantidades, chances, etc.")
            pergunta_dificuldade = input("Deseja jogar em qual dificuldade? ")
            if pergunta_dificuldade.isnumeric() == False:
                print("Por favor, insira um valor válido (número inteiro).")
                time.sleep(2)
                os.system('cls')
            elif pergunta_dificuldade < 1 and pergunta_dificuldade > 5:
                print("Por favor, insira um valor entre 1 e 5.")
                time.sleep(2)
                os.system('cls')
            else:
                pergunta_dificuldade = int(pergunta_dificuldade)
                break
    max_dias += 1
    time.sleep(2)
    os.system('cls')

#Dificuldades [ Alterável ]
if pergunta_dificuldade == 1:
    mod_dif_preco_droga_max = 3
    mod_dif_preco_droga_min = 0.25
    mod_dif_qty_droga_max = 3
    mod_dif_qty_droga_min = 0.5
    mod_dif_peso_ini = 3
    mod_dif_saldo_ini = 3
    mod_dif_debito_ini = 0.5
    mod_dif_aumento_deb = 0.5
    mod_dif_salario = 3
    mod_dif_bonus = 3
    mod_dif_peso_itens = 0.5
    mod_dif_peso_mochila = 3
    mod_dif_rendimento = 3
    mod_dif_preco_arma = 0.5
    mod_dif_preco_mochila = 0.5
    mod_dif_preco_colete = 0.5
    mod_dif_dano_agiota = 0.25
    mod_dif_hp_colete = 3
    mod_dif_dia_pgto_agiota = 2
    mod_dif_preco_medicamento = 0.5
    mod_dif_hp_medicamento = 3
    mod_dif_chances = 3
    mod_dif_vida = 3
    mod_dif_boost = 3

if pergunta_dificuldade == 2:
    mod_dif_preco_droga_max = 1.5
    mod_dif_preco_droga_min = 0.5
    mod_dif_qty_droga_max = 3
    mod_dif_qty_droga_min = 0.5
    mod_dif_peso_ini = 2
    mod_dif_saldo_ini = 1.5
    mod_dif_debito_ini = 1
    mod_dif_aumento_deb = 0.75
    mod_dif_salario = 1.5
    mod_dif_bonus = 1.5
    mod_dif_peso_itens = 0.75
    mod_dif_peso_mochila = 1.5
    mod_dif_rendimento = 1.5
    mod_dif_preco_arma = 0.75
    mod_dif_preco_mochila = 0.75
    mod_dif_preco_colete = 0.75
    mod_dif_dano_agiota = 0.75
    mod_dif_hp_colete = 1.5
    mod_dif_dia_pgto_agiota = 1.5
    mod_dif_preco_medicamento = 0.75
    mod_dif_hp_medicamento = 1.5
    mod_dif_chances = 1.5
    mod_dif_vida = 2
    mod_dif_boost = 1.5

if pergunta_dificuldade == 3:
    mod_dif_preco_droga_max = 1
    mod_dif_preco_droga_min = 1
    mod_dif_qty_droga_max = 1
    mod_dif_qty_droga_min = 1
    mod_dif_peso_ini = 1
    mod_dif_saldo_ini = 1
    mod_dif_debito_ini = 1
    mod_dif_aumento_deb = 1
    mod_dif_salario = 1
    mod_dif_bonus = 1
    mod_dif_peso_itens = 1
    mod_dif_peso_mochila = 1
    mod_dif_rendimento = 1
    mod_dif_preco_arma = 1
    mod_dif_preco_mochila = 1
    mod_dif_preco_colete = 1
    mod_dif_dano_agiota = 1
    mod_dif_hp_colete = 1
    mod_dif_dia_pgto_agiota = 1
    mod_dif_preco_medicamento = 1
    mod_dif_hp_medicamento = 1
    mod_dif_chances = 1
    mod_dif_vida = 1
    mod_dif_boost = 1

if pergunta_dificuldade == 4:
    mod_dif_preco_droga_max = 0.75
    mod_dif_preco_droga_min = 0.75
    mod_dif_qty_droga_max = 0.75
    mod_dif_qty_droga_min = 0.75
    mod_dif_peso_ini = 0.75
    mod_dif_saldo_ini = 0.75
    mod_dif_debito_ini = 1.25
    mod_dif_aumento_deb = 1.25
    mod_dif_salario = 0.75
    mod_dif_bonus = 0.75
    mod_dif_peso_itens = 1.5
    mod_dif_peso_mochila = 0.75
    mod_dif_rendimento = 0.75
    mod_dif_preco_arma = 1.5
    mod_dif_preco_mochila = 1.5
    mod_dif_preco_colete = 1.5
    mod_dif_dano_agiota = 1.25
    mod_dif_hp_colete = 0.75
    mod_dif_dia_pgto_agiota = 0.75
    mod_dif_preco_medicamento = 1.5
    mod_dif_hp_medicamento = 0.75
    mod_dif_chances = 0.65
    mod_dif_vida = 0.75
    mod_dif_boost = 0.75

if pergunta_dificuldade == 5:
    mod_dif_preco_droga_max = 0.5
    mod_dif_preco_droga_min = 0.5
    mod_dif_qty_droga_max = 0.5
    mod_dif_qty_droga_min = 0.5
    mod_dif_peso_ini = 0.5
    mod_dif_saldo_ini = 0.5
    mod_dif_debito_ini = 1.5
    mod_dif_aumento_deb = 1.5
    mod_dif_salario = 0.5
    mod_dif_bonus = 0.5
    mod_dif_peso_itens = 1.25
    mod_dif_peso_mochila = 0.5
    mod_dif_rendimento = 0.5
    mod_dif_preco_arma = 2
    mod_dif_preco_mochila = 2
    mod_dif_preco_colete = 2
    mod_dif_dano_agiota = 1.5
    mod_dif_hp_colete = 0.5
    mod_dif_dia_pgto_agiota = 0.5
    mod_dif_preco_medicamento = 2
    mod_dif_hp_medicamento = 0.5
    mod_dif_chances = 0.35
    mod_dif_vida = 0.5
    mod_dif_boost = 0.5

#Modificadores [ Não Alterável ]
if var_controle == False:
    modificador_qty_mercado = 1
    modificador_peso = 1
    modificador_peso_mochila = 0
    modificador_rendimento = 1

#Atributos [ Alterável ]
if var_controle == False:
    total_dinheiro_inv = 0 # Não alterar
    saldo_banco = 0 # Saldo no banco inicial
    peso_inv = 0 # Não alterar
    peso_alterar = round(30*mod_dif_peso_ini) # Peso inicial do jogador
    saldo = round(2000*mod_dif_saldo_ini) # Saldo na carteira inicial
    vida = round(100*mod_dif_vida) # Vida inicial
    vida_max = round(100*mod_dif_vida) # Alterar para o mesmo valor da vida
    conta_banco = False # False- Não começa com uma conta no banco | True- Começa com uma conta no banco

#Empregos [ Alterável ]
if var_controle == False:
    dias_estudante = 0 # Dias como estudante de medicina
    estudante_hospital = False # False- Não começa como estudante de medicina | True- Começa como estudante de medicina
    empregado_hospital = False # False- Não começa como empregado do hospital | True- Começa como empregado do hospital
    empregado_agiota = False # False- Não começa como empregado do agiota | True- Começa como empregado do agiota
    empregado_banco = False # False- Não começa como empregado do banco | True- Começa como empregado do banco
    estagiario_banco = False # False- Não começa como estagiário do banco | True- Começa como estagiário do banco
    gerente_banco = False # False- Não começa como gerente do banco | True- Começa como gerente do banco
    dias_estagio = 0 # Contagem de dias para passar de estagiário para empregado do banco (0-3)
    cooldown_trabalho = 0 # Definido por cálculos internos, se quiser ficar sem cooldown, coloque -99

#Armas [ Alterável ]
if var_controle == False:
    #Armas

    has_t1 = False # Dá ao jogador a arma tier 1
    hasb_t1 = 0 # Alterar para 1 se alterar o de cima para True
    has_t2 = False # Dá ao jogador a arma tier 2
    hasb_t2 = 0 # Alterar para 1 se alterar o de cima para True
    has_t3 = False # Dá ao jogador a arma tier 3
    hasb_t3 = 0 # Alterar para 1 se alterar o de cima para True
    has_t4 = False # Dá ao jogador a arma tier 4
    hasb_t4 = 0 # Alterar para 1 se alterar o de cima para True
    has_t5 = False # Dá ao jogador a arma tier 5
    hasb_t5 = 0 # Alterar para 1 se alterar o de cima para True

    preco_t1 = round(7000*mod_dif_preco_arma) # Preço da arma tier 1
    preco_t2 = round(18000*mod_dif_preco_arma) # Preço da arma tier 2
    preco_t3 = round(29000*mod_dif_preco_arma) # Preço da arma tier 3
    preco_t4 = round(40000*mod_dif_preco_arma) # Preço da arma tier 4
    preco_t5 = round(51000*mod_dif_preco_arma) # Preço da arma tier 5

    peso_t1 = round(30*modificador_peso*mod_dif_peso_itens) # Peso da arma tier 1
    peso_t2 = round(70*modificador_peso*mod_dif_peso_itens) # Peso da arma tier 2
    peso_t3 = round(140*modificador_peso*mod_dif_peso_itens) # Peso da arma tier 3
    peso_t4 = round(240*modificador_peso*mod_dif_peso_itens) # Peso da arma tier 4
    peso_t5 = round(400*modificador_peso*mod_dif_peso_itens) # Peso da arma tier 5

    #Coletes

    has_ct1 = False # Dá ao jogador o colete tier 1
    hasb_ct1 = 0 # Alterar para 1 se alterar o de cima para True
    has_ct2 = False # Dá ao jogador o colete tier 2
    hasb_ct2 = 0 # Alterar para 1 se alterar o de cima para True
    has_ct3 = False # Dá ao jogador o colete tier 3
    hasb_ct3 = 0 # Alterar para 1 se alterar o de cima para True
    has_ct4 = False # Dá ao jogador o colete tier 4
    hasb_ct4 = 0 # Alterar para 1 se alterar o de cima para True
    has_ct5 = False # Dá ao jogador o colete tier 5
    hasb_ct5 = 0 # Alterar para 1 se alterar o de cima para True

    preco_ct1 = round(6000*mod_dif_preco_colete) # Peso do colete tier 1
    preco_ct2 = round(18000*mod_dif_preco_colete) # Peso do colete tier 1
    preco_ct3 = round(35000*mod_dif_preco_colete) # Peso do colete tier 1
    preco_ct4 = round(60000*mod_dif_preco_colete) # Peso do colete tier 1
    preco_ct5 = round(90000*mod_dif_preco_colete) # Peso do colete tier 1

    peso_ct1 = round((15*modificador_peso)*mod_dif_peso_itens) #Obs: não tirar o /2, altere apenas o primeiro valor. 
    peso_ct2 = round((40*modificador_peso)*mod_dif_peso_itens) #Obs: não tirar o /2, altere apenas o primeiro valor.
    peso_ct3 = round((85*modificador_peso)*mod_dif_peso_itens) #Obs: não tirar o /2, altere apenas o primeiro valor.
    peso_ct4 = round((115*modificador_peso)*mod_dif_peso_itens) #Obs: não tirar o /2, altere apenas o primeiro valor.
    peso_ct5 = round((160*modificador_peso)*mod_dif_peso_itens) #Obs: não tirar o /2, altere apenas o primeiro valor.

    hp_ct1 = round(15*mod_dif_hp_colete)
    hp_ct2 = round(25*mod_dif_hp_colete)
    hp_ct3 = round(40*mod_dif_hp_colete)
    hp_ct4 = round(50*mod_dif_hp_colete)
    hp_ct5 = round(75*mod_dif_hp_colete)

    #Mochilas

    has_mt1 = False # Dá ao jogador a arma tier 1
    hasb_mt1 = 0 # Alterar para 1 se alterar o de cima para True
    has_mt2 = False # Dá ao jogador a arma tier 2
    hasb_mt2 = 0 # Alterar para 1 se alterar o de cima para True
    has_mt3 = False # Dá ao jogador a arma tier 3
    hasb_mt3 = 0 # Alterar para 1 se alterar o de cima para True
    has_mt4 = False # Dá ao jogador a arma tier 4
    hasb_mt4 = 0 # Alterar para 1 se alterar o de cima para True
    has_mt5 = False # Dá ao jogador a arma tier 5
    hasb_mt5 = 0 # Alterar para 1 se alterar o de cima para True

    preco_mt1 = round(6500*mod_dif_preco_mochila)
    preco_mt2 = round(18000*mod_dif_preco_mochila)
    preco_mt3 = round(35000*mod_dif_preco_mochila)
    preco_mt4 = round(60000*mod_dif_preco_mochila)
    preco_mt5 = round(85000*mod_dif_preco_mochila)

    peso_mt1 = round(15*mod_dif_peso_mochila) # Alterar apenas esse valor = Alterar capacidade da mochila tier 1
    peso_mt1 += (modificador_peso_mochila * peso_mt1)
    peso_mt2 = round(45*mod_dif_peso_mochila) # Alterar apenas esse valor = Alterar capacidade da mochila tier 2
    peso_mt2 += (modificador_peso_mochila * peso_mt2)
    peso_mt3 = round(90*mod_dif_peso_mochila) # Alterar apenas esse valor = Alterar capacidade da mochila tier 3
    peso_mt3 += (modificador_peso_mochila * peso_mt3)
    peso_mt4 = round(155*mod_dif_peso_mochila) # Alterar apenas esse valor = Alterar capacidade da mochila tier 4
    peso_mt4 += (modificador_peso_mochila * peso_mt4)
    peso_mt5 = round(220*mod_dif_peso_mochila) # Alterar apenas esse valor = Alterar capacidade da mochila tier 5
    peso_mt5 += (modificador_peso_mochila * peso_mt5)

#Agiota
if var_controle == False:
    debito_agiota = round(1334*mod_dif_debito_ini) #Débito inicial com o agiota
    dano_agiota = 0 #Não alterar / Gerado com base no cálculo de dívida
    dias_pagar_agiota = round(5*mod_dif_dia_pgto_agiota)+1 # Quantos dias o jogador tem para pagar a dívida com o agiota. Obs: não remova o +1, é apenas para cálculos internos e não interfere no valor final.
    alt_debito_agiota = 0 # Não alterar
    cobranca_agiota = False #Não alterar
    dia_cobranca = 0 #Não alterar
    cobranca_diaria_agiota = False

#Hospital
if var_controle == False:
    #Preços
    preco_analgesico = round(4500*mod_dif_preco_medicamento)
    preco_faixa = round(6850*mod_dif_preco_medicamento)
    preco_atadura = round(10200*mod_dif_preco_medicamento)
    preco_kit_pequeno = round(15500*mod_dif_preco_medicamento)
    preco_kit_grande = round(20000*mod_dif_preco_medicamento)

    #HP Recuperado
    hp_analgesico = round(15*mod_dif_hp_medicamento)
    hp_faixa = round(20*mod_dif_hp_medicamento)
    hp_atadura = round(30*mod_dif_hp_medicamento)
    hp_kit_pequeno = round(40*mod_dif_hp_medicamento)
    hp_kit_grande = round(50*mod_dif_hp_medicamento)

    #Inventário
    qty_inv_analgesico = 0
    qty_inv_faixa = 0
    qty_inv_atadura = 0
    qty_inv_kit_pequeno = 0
    qty_inv_kit_grande = 0

    #Cooldown 
    cd_analgesico = False
    cd_faixa = False
    cd_atadura = False
    cd_kit_pequeno = False
    cd_kit_grande = False

    #Peso
    peso_analgesico = round(25*mod_dif_peso_itens)
    peso_faixa = round(35*mod_dif_peso_itens)
    peso_atadura = round(45*mod_dif_peso_itens)
    peso_kit_pequeno = round(60*mod_dif_peso_itens)
    peso_kit_grande = round(75*mod_dif_peso_itens)

#Has Drugs
if var_controle == False:
    # Cada drug é desbloqueada em um ambiente diferente.
    # Para comprar a drug você precisa desbloquear o ambiente e ela.
    # True = Desbloqueado | False = Bloqueado

    #ambientes
    has_fazenda = False
    has_laboratorio = False
    has_farmacia = False

    #fazenda
    has_maconha = True
    has_opium = True
    has_cogumelo = True
    has_skank = True

    #Drugs rua
    has_speed = True
    has_cocaina = False
    has_crack = False
    has_oxi = False
    has_heroina = False

    #Drugs laboratório
    has_cristal = False
    has_lsd = False
    has_ecstasy = False

    #Drugs farmacia
    has_morfina = False
    has_diazepam = False
    has_zolpidem = False
    has_codeina = False
    has_alprazolam = False
    has_zopiclona = False

#Drugs Fazenda (Inicias)
if var_controle == False:
    #Drugs
    
    # Opium
    preco_max_Opium = round(3000*mod_dif_preco_droga_max) #Preço máximo Opium
    preco_min_Opium = round(1500*mod_dif_preco_droga_min) # Preço mínimo Opium
    qty_inv_Opium = 0 #Quantidade inicial de Opium no inventário (influencia no peso)
    peso_Opium = round(15*modificador_peso*mod_dif_peso_itens) #Peso de cada Opium no inventário
    qty_mercado_Opium = 0 #Gerado aleatoriamente
    qty_min_mercado_Opium = round(2*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Opium = round(5*mod_dif_qty_droga_min)*modificador_qty_mercado
    preco_Opium = 0 #Gerado aleatoriamente

    # Maconha
    preco_max_Maconha = round(1200*mod_dif_preco_droga_max) #Preço máximo Maconha
    preco_min_Maconha = round(600*mod_dif_preco_droga_min) # Preço mínimo Maconha
    qty_inv_Maconha = 0 #Quantidade inicial de Maconha no inventário (influencia no peso)
    peso_Maconha = round(7.5*modificador_peso*mod_dif_peso_itens) #Peso de cada Maconha no inventário
    qty_mercado_Maconha = 0 #Gerado aleatoriamente
    qty_min_mercado_Maconha = round(5*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Maconha = round(10*mod_dif_qty_droga_max)*modificador_qty_mercado
    preco_Maconha = 0 #Gerado aleatoriamente

    # Speed
    preco_max_Speed = round(500*mod_dif_preco_droga_max) #Preço máximo Speed
    preco_min_Speed = round(250*mod_dif_preco_droga_min) # Preço mínimo Speed
    qty_inv_Speed = 0 #Quantidade inicial de Speed no inventário (influencia no peso)
    peso_Speed = round(4.5*modificador_peso*mod_dif_peso_itens) #Peso de cada Speed no inventário
    qty_mercado_Speed = 0 #Gerado aleatoriamente
    qty_min_mercado_Speed = round(10*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Speed = round(20*mod_dif_qty_droga_max)*modificador_qty_mercado
    preco_Speed = 0 #Gerado aleatoriamente

    # Skank
    preco_max_Skank = round(200*mod_dif_preco_droga_max) #Preço máximo Opium
    preco_min_Skank = round(100*mod_dif_preco_droga_min) # Preço mínimo Opium
    qty_inv_Skank = 0 #Quantidade inicial de Opium no inventário (influencia no peso)
    peso_Skank = round(3*modificador_peso*mod_dif_peso_itens) #Peso de cada Opium no inventário
    qty_mercado_Skank = 0 #Gerado aleatoriamente
    qty_min_mercado_Skank = round(20*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Skank = round(40*mod_dif_qty_droga_max)*modificador_qty_mercado
    preco_Skank = 0 #Gerado aleatoriamente

    # Cogumelos 
    preco_max_Cogumelos = round(80*mod_dif_preco_droga_max) #Preço máximo cogumelo
    preco_min_Cogumelos = round(40*mod_dif_preco_droga_min) # Preço mínimo cogumelo
    qty_inv_Cogumelos = 0 #Quantidade inicial de cogumelo no inventário (influencia no peso)
    peso_Cogumelos = round(1.5*modificador_peso*mod_dif_peso_itens) #Peso de cada cogumelo no inventário
    qty_mercado_Cogumelos = 0 #Gerado aleatoriamente | Não alterar
    qty_min_mercado_Cogumelos = round(40*mod_dif_qty_droga_min)*modificador_qty_mercado #Quantidade mínima de cogumelos no mercado
    qty_max_mercado_Cogumelos = round(80*mod_dif_qty_droga_max)*modificador_qty_mercado #Quantidade máxima de cogumelos no mercado
    preco_Cogumelos = 0 #Gerado aleatoriamente | Não alterar

dia = 0 #Não alterar
resposta = 111101001 # Não alterar

#Buffers / Modificadores
boost_1 = False # True = Desabilita o boost nível 1 | False = Habilida o boost nível 1
saldo_b1 = 150000*mod_dif_boost
boost_2 = False # True = Desabilita o boost nível 2 | False = Habilida o boost nível 2
saldo_b2 = 300000*mod_dif_boost
boost_3 = False # True = Desabilita o boost nível 3 | False = Habilida o boost nível 3
saldo_b3 = 600000*mod_dif_boost
boost_4 = False # True = Desabilita o boost nível 4 | False = Habilida o boost nível 4
saldo_b4 = 1200000*mod_dif_boost
boost_5 = False # True = Desabilita o boost nível 5 | False = Habilida o boost nível 5
saldo_b5 = 2400000*mod_dif_boost
boost_6 = False # True = Desabilita o boost nível 6 | False = Habilida o boost nível 6
saldo_b6 = 4800000*mod_dif_boost
boost_7 = False # True = Desabilita o boost nível 7 | False = Habilida o boost nível 7
saldo_b7 = 9600000*mod_dif_boost
boost_8 = False # True = Desabilita o boost nível 8 | False = Habilida o boost nível 8
saldo_b8 = 15000000*mod_dif_boost
boost_9 = False # True = Desabilita o boost nível 9 | False = Habilida o boost nível 9
saldo_b9 = 25000000*mod_dif_boost
boost_10 = False # True = Desabilita o boost nível 10 | False = Habilida o boost nível 10
saldo_b10 = 40000000*mod_dif_boost

##########################################
### Não altere nada abaixo dessa linha ###
##########################################
dias_tentar_roubar_banco = 0
dias_roubo_banco = 0
vida_dias_var = True

def aumentar_drug_mercado():
    fim_jogo()
    global boost_1, boost_2, boost_3, boost_4, boost_5, boost_6, boost_7, boost_8, boost_9, boost_10
    global vida, vida_max, modificador_qty_mercado, modificador_rendimento, modificador_peso, modificador_peso_mochila
    if saldo >= saldo_b1 and boost_1 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 1!")
        if tutorial == True and dia != 0:
            print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
            print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
            print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
        modificador_qty_mercado = 2
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 1.1
        modificador_peso = 0.9
        modificador_peso_mochila = 0.5
        boost_1 = True
    elif saldo >= saldo_b2 and boost_2 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 2!")
        modificador_qty_mercado = 4
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 1.25
        modificador_peso = 0.85
        modificador_peso_mochila = 1
        boost_2 = True
    elif saldo >= saldo_b3 and boost_3 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 3!")
        modificador_qty_mercado = 8
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 1.45
        modificador_peso = 0.8
        modificador_peso_mochila = 1.5
        boost_3 = True
    elif saldo >= saldo_b4 and boost_4 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 4!")
        modificador_qty_mercado = 16
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 1.75
        modificador_peso = 0.75
        modificador_peso_mochila = 2
        boost_4 = True
    elif saldo >= saldo_b5 and boost_5 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 5!")
        modificador_qty_mercado = 32
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 2
        modificador_peso = 0.7
        modificador_peso_mochila = 2.5
        boost_5 = True
    elif saldo >= saldo_b6 and boost_6 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 6!")
        modificador_qty_mercado = 64
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 2.5
        modificador_peso = 0.65
        modificador_peso_mochila = 3
        boost_6 = True
    elif saldo >= saldo_b7 and boost_7 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 7!")
        modificador_qty_mercado = 128
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 3
        modificador_peso = 0.6
        modificador_peso_mochila = 3.5
        boost_7 = True
    elif saldo >= saldo_b8 and boost_8 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 8!")
        modificador_qty_mercado = 256
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 3.5
        modificador_peso = 0.55
        modificador_peso_mochila = 4
        boost_8 = True
    elif saldo >= saldo_b9 and boost_9 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 9!")
        modificador_qty_mercado = 512
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 4
        modificador_peso = 0.5
        modificador_peso_mochila = 4.5
        boost_9 = True
    elif saldo >= saldo_b10 and boost_10 == False:
        print("----------------------------------------")
        print("Parabéns! Você chegou ao Boost 10!")
        modificador_qty_mercado = 1024
        #vida_max -= (vida_max*(-0.25))
        #vida += vida_max*
        #vida_max += vida_max*
        modificador_rendimento = 5
        modificador_peso = 0.40
        modificador_peso_mochila = 5
        boost_10 = True
    fim_jogo()
        
# Dano Agiota + Cobrança Agiota
def agiota(dano_agiota, cobranca_agiota):
    global resposta
    global debito_agiota
    global dia_cobranca
    global dias_pagar_agiota
    global dia
    fim_jogo()
    if debito_agiota > 0 and dias_pagar_agiota > 0:
        if dia == 0:
            if tutorial == True and dia != 0:
                print("Tutorial: Você está devendo o agiota e deve pagar ele na quantidade de dias dita abaixo.")
                print("Tutorial: Caso você não pague, todo dia terá uma chance dele vir atrás de você baseado no valor de sua dívida, dívida maior, chance maior.")
                print("Tutorial: Cada vez que ele vem te cobrar você perde uma quantidade de vida baseada em: Sua dívida divido 1000.")
                print("Tutorial: Caso o jogo acabe e você continue o devendo, a dívida final será multiplicada por 5 e tirada da sua pontuação.")
            print(f"Você deve pagar o agiota daqui a {dias_pagar_agiota-1} dias.")
        else:
            if tutorial == True and dia != 0:
                print("Tutorial: Você está devendo o agiota e deve pagar ele na quantidade de dias dita abaixo.")
                print("Tutorial: Caso você não pague, todo dia terá uma chance dele vir atrás de você baseado no valor de sua dívida, dívida maior, chance maior.")
                print("Tutorial: Cada vez que ele vem te cobrar você perde uma quantidade de vida baseada em: Sua dívida divido 1000.")
                print("Tutorial: Caso o jogo acabe e você continue o devendo, a dívida final será multiplicada por 5 e tirada da sua pontuação.")
            print(f"Você deve pagar o agiota daqui a {dias_pagar_agiota} dias.")
    if debito_agiota > 0 and dias_pagar_agiota <= 0:
        if tutorial == True and dia != 0:
            print("Tutorial: Essa mensagem significa que você está devendo o agiota e corre o risco dele te cobrar.")
        print("Atenção, você está devendo o agiota!")
        dano_agiota = (debito_agiota/1000)*0.5
        cobrar_agiota = random.randint(1,100)
        if debito_agiota <= 1000:
            if cobrar_agiota <= 10:
                cobranca_agiota = True
        elif debito_agiota <= 2002:
            if cobrar_agiota <= 20:
                cobranca_agiota = True
        elif debito_agiota <= 3000:
            if cobrar_agiota <= 30:
                cobranca_agiota = True
        elif debito_agiota <= 4000:
            if cobrar_agiota <= 40:
                cobranca_agiota = True
        elif debito_agiota <= 5000:
            if cobrar_agiota <= 50:
                cobranca_agiota = True
        elif debito_agiota <= 7500:
            if cobrar_agiota <= 60:
                cobranca_agiota = True
        elif debito_agiota <= 12500:
            if cobrar_agiota <= 70:
                cobranca_agiota = True
        elif debito_agiota <= 15000:
            if cobrar_agiota <= 80:
                cobranca_agiota = True
        elif debito_agiota <= 17500:
            if cobrar_agiota <= 90:
                cobranca_agiota = True
        elif debito_agiota > 20000:
            if cobrar_agiota <= 100:
                cobranca_agiota = True
        elif debito_agiota > 50000:
            if cobrar_agiota <= 100:
                dano_agiota = dano_agiota * (0.25*((dias_pagar_agiota*-1)/2))
                cobranca_agiota = True
        elif debito_agiota > 100000:
            if cobrar_agiota <= 100:
                dano_agiota = dano_agiota * (0.5*((dias_pagar_agiota*-1)/2))
                cobranca_agiota = True
        elif debito_agiota > 200000:
            if cobrar_agiota <= 100:
                dano_agiota = dano_agiota * (0.75*((dias_pagar_agiota*-1)/2))
                cobranca_agiota = True
        elif debito_agiota > 200000:
            if cobrar_agiota <= 100:
                dano_agiota = dano_agiota * (1*((dias_pagar_agiota*-1)/2))
                cobranca_agiota = True
    fim_jogo()
    return dano_agiota, cobranca_agiota

def alterar_valores():
    global qty_min_mercado_Opium, qty_max_mercado_Opium, qty_min_mercado_Maconha, qty_max_mercado_Maconha, qty_min_mercado_Speed, qty_max_mercado_Speed, qty_min_mercado_Skank, qty_max_mercado_Skank, qty_min_mercado_Cogumelos, qty_max_mercado_Cogumelos, peso_t1, peso_t2, peso_t3, peso_t4, peso_t5, peso_ct1, peso_ct2, peso_ct3, peso_ct4, peso_ct5, peso_Opium, peso_Maconha, peso_Speed, peso_Skank, peso_Cogumelos, peso_mt1, peso_mt2, peso_mt3, peso_mt4, peso_mt5
    global mod_dif_preco_droga_max, mod_dif_preco_droga_min, mod_dif_qty_droga_max, mod_dif_qty_droga_min, mod_dif_peso_ini, mod_dif_saldo_ini, mod_dif_debito_ini, mod_dif_aumento_deb, mod_dif_salario, mod_dif_bonus, mod_dif_peso_itens, mod_dif_peso_mochila, mod_dif_rendimento, mod_dif_preco_arma, mod_dif_preco_mochila, mod_dif_preco_colete, mod_dif_dano_agiota, mod_dif_hp_colete, mod_dif_dia_pgto_agiota, mod_dif_preco_medicamento, mod_dif_hp_medicamento, mod_dif_chances, mod_dif_vida, mod_dif_boost
    fim_jogo()
    qty_min_mercado_Opium = round(2*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Opium = round(5*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_min_mercado_Maconha = round(5*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Maconha = round(10*mod_dif_qty_droga_max)*modificador_qty_mercado
    qty_min_mercado_Speed = round(10*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Speed = round(20*mod_dif_qty_droga_max)*modificador_qty_mercado
    qty_min_mercado_Skank = round(20*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Skank = round(40*mod_dif_qty_droga_max)*modificador_qty_mercado
    qty_min_mercado_Cogumelos = round(40*mod_dif_qty_droga_min)*modificador_qty_mercado
    qty_max_mercado_Cogumelos = round(80*mod_dif_qty_droga_max)*modificador_qty_mercado
    peso_t1 = round(30*modificador_peso*mod_dif_peso_itens)
    peso_t2 = round(70*modificador_peso*mod_dif_peso_itens)
    peso_t3 = round(140*modificador_peso*mod_dif_peso_itens)
    peso_t4 = round(240*modificador_peso*mod_dif_peso_itens)
    peso_t5 = round(400*modificador_peso*mod_dif_peso_itens)
    peso_ct1 = round((15*modificador_peso)*mod_dif_peso_itens)
    peso_ct2 = round((40*modificador_peso)*mod_dif_peso_itens)
    peso_ct3 = round((85*modificador_peso)*mod_dif_peso_itens)
    peso_ct4 = round((115*modificador_peso)*mod_dif_peso_itens)
    peso_ct5 = round((160*modificador_peso)*mod_dif_peso_itens)
    peso_Opium = round(15*modificador_peso*mod_dif_peso_itens)
    peso_Maconha = round(7.5*modificador_peso*mod_dif_peso_itens)
    peso_Speed = round(4.5*modificador_peso*mod_dif_peso_itens)
    peso_Skank = round(3*modificador_peso*mod_dif_peso_itens)
    peso_Cogumelos = round(1.5*modificador_peso*mod_dif_peso_itens)
    peso_mt1 = round(15*mod_dif_peso_mochila) + (modificador_peso_mochila * peso_mt1 )
    peso_mt2 = round(45*mod_dif_peso_mochila) + (modificador_peso_mochila * peso_mt2)
    peso_mt3 = round(90*mod_dif_peso_mochila) + (modificador_peso_mochila * peso_mt3)
    peso_mt4 = round(155*mod_dif_peso_mochila) + (modificador_peso_mochila * peso_mt4)
    peso_mt5 = round(220*mod_dif_peso_mochila) + (modificador_peso_mochila * peso_mt5)
    fim_jogo()

def interface_usuario():
    fim_jogo()
    alterar_valores()
    global peso_t1, cooldown_trabalho, gerente_banco, dias_estagio, peso, saldo, vida, debito_agiota, qty_inv_Opium, peso_Opium, preco_Opium, peso_inv, qty_mercado_Opium, dia, alt_debito_agiota, cobranca_agiota, dias_pagar_agiota, qty_inv_Maconha, peso_Maconha, preco_Maconha, qty_mercado_Maconha, qty_inv_Speed, peso_Speed, preco_Speed, qty_mercado_Speed, qty_inv_Skank, peso_Skank, preco_Skank, qty_mercado_Skank, qty_inv_Cogumelos, peso_Cogumelos, preco_Cogumelos, qty_mercado_Cogumelos, saldo_banco, vida_max, peso_t2, peso_t3, peso_t4, peso_t5, peso_ct1, peso_ct2, peso_ct3, peso_ct4, peso_ct5, peso_mt1, peso_mt2, peso_mt3, peso_mt4, peso_mt5
    global boost_1, boost_2, boost_3, boost_4, boost_5, boost_6, boost_7, boost_8, boost_9, boost_10
    global vida, vida_max, modificador_qty_mercado, modificador_rendimento, modificador_peso, modificador_peso_mochila
    global estudante_hospital, dias_estudante, empregado_hospital, cobranca_diaria_agiota, dias_tentar_roubar_banco, dias_roubo_banco
    while dia < max_dias and vida > 0.000000001:
        fim_jogo()
        alterar_valores()
        peso_inv = peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) # (peso_mt1 * hasb_mt1) - (peso_mt2 * hasb_mt2) - (peso_mt3 * hasb_mt3) - (peso_mt4 * hasb_mt4) - (peso_mt5 * hasb_mt5))
        peso_inv += ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))
        resposta = 0
        while resposta != 9 and dia < max_dias and vida > 0.00000:
            fim_jogo()
            print("----------------------------------------")
            print("              Drug's Skid               ")
            print("----------------------------------------")
            if tutorial == True and dia != 0:
                print("Tutorial: Dia atual.")
            print("Dia", dia)
            if dia == 0:
                if tutorial == True and dia == 0:
                    print("Tutorial: Sempre que você iniciar o jogo, estará no dia 0.")
                    print("Tutorial: O dia 0 é um dia para representar o começo do jogo, portanto não é possível fazer nada nele.")
                    print("Tutorial: O jogo irá negar qualquer ação que você tente fazer no dia 0. Para iniciar seu jogo você deve inserir 9 e ir para o dia 1.")
                print("################################################################")
                print("Atenção! Você está no dia 0, passe para o 1 para iniciar o jogo.")
                print("################################################################")
            if tutorial == True and dia != 0:
                print("Tutorial: Espaço total é a contagem do espaço inicial + espaço disponibilizado pelas mochilas.")
                print("Tutorial: Espaço disponível é o espaço total menos o espaço gasto com os itens, ou seja, o que você pode gastar.")
            print(f"Espaço total: {(peso_alterar + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))):.2f}kg")
            print(f"Espaço disponível: {peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5)):.2f}kg")
            print("----------------------------------------")
            fim_jogo()
            dano_agiota = 0
            dano_agiota, cobranca_agiota = agiota(dano_agiota, cobranca_agiota)
            if cobranca_agiota == True and cobranca_diaria_agiota == False:
                if tutorial == True and dia != 0 and cobranca_diaria_agiota == False:
                    print("Tutorial: O agiota veio te cobrar por causa de sua dívida e você perdeu pontos de vida. Atente-se!")
                print(f"Você perdeu {dano_agiota:.2f} pontos de vida por estar devendo o agiota.")
                vida -= dano_agiota
                cobranca_agiota = False
                cobranca_diaria_agiota = True
            if tutorial == True and dia != 0:
                print("Tutorial: Sua vida deve sempre ser maior que zero, caso contrário, o jogo acaba. Cuidado, existem diversas formas de perder vida.")
                print("Tutorial: Seu saldo atual é seu dinheiro na carteira, utilizado para realizar compras.")
            print("Vida: ", vida)
            print("Saldo atual: $", saldo)
            if dia == 0: 
                if tutorial == True and dia != 0:
                    print("Tutorial: Seu débito atual é o quanto você deve ao agiota.")
                print(f"Débito atual: ${debito_agiota} + ${alt_debito_agiota} = ${alt_debito_agiota+debito_agiota}")
            else:
                if tutorial == True and dia != 0:
                    print("Tutorial: Seu débito atual é o quanto você deve ao agiota.")
                print(f"Débito atual: ${debito_agiota} + ${alt_debito_agiota} = ${alt_debito_agiota+debito_agiota}")
            print("[1] - Compra")
            print("[2] - Venda")
            print("[3] - Agiota")
            print("[4] - Banco")
            print("[5] - Hospital")
            print("[6] - Loja de Armas")
            print("[7] - Inventário")
            print("[9] - Próximo dia")
            fim_jogo()
            if tutorial == True and dia != 0:
                    print("Tutorial: Nesse menu estão todas as opções do menu principal.")
                    print("Tutorial: Para interagir com o menu, basta olhar para onde deseja ir e escrever abaixo seu respectivo número mostrado a esquerda.")
            resposta = input("Para onde deseja ir? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                resposta = int(resposta)
            if dia == 0 and resposta!= 9 and type(resposta) == int:
                print("Você está no dia 0 e não pode fazer isso!")
                print("Para jogar você precisa iniciar o primeiro dia.")
                print("Insira 9 para ir para o próximo dia e começar o jogo.")
                time.sleep(3)
                os.system('cls')
            elif resposta < 1 or resposta > 9:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
            elif resposta == 1:
                fim_jogo()
                resposta = 0
                qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos = compra_Opium(qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos)  # Atualiza o saldo e a quantidade disponível no mercado
            elif resposta == 2:
                fim_jogo()
                resposta = 0
                venda_Opium()
            elif resposta == 3:
                fim_jogo()
                resposta = 0
                ir_agiota()
            elif resposta == 4:
                fim_jogo()
                resposta = 0
                ir_banco()
            elif resposta == 5:
                fim_jogo()
                ir_hospital()
            elif resposta == 6:
                fim_jogo()
                saldo = loja_armas(saldo)
            elif resposta == 7:
                fim_jogo()
                inventario()
            elif resposta == 9:
                fim_jogo()
                resposta = 0
                time.sleep(2)
                os.system('cls')
                if conta_banco == True:
                    saldo -= 1200
                if estagiario_banco == True:
                    dias_estagio += 1
                    if dias_estagio == 4:
                        if tutorial == True and dia != 0:
                            print("Tutorial: Você concluiu seu periodo como estagiário e agora pode utilizar a função trabalhar no banco.")
                            print("Tutorial: Quando você finaliza o estágio, existe uma chance de 1% de você se tornar gerente do banco e ganhar três vezes mais, além de outros benefícios.")
                        print("Parabéns! Você concluiu seus quatro dias como estagiário e agora trabalha como funcionário do banco.")
                        time.sleep(2)
                        estagiario_banco == False
                        empregado_banco == True
                        if random.randint(1,100) < 1:
                            if tutorial == True and dia != 0:
                                print("Tutorial: Parabéns! Existe uma chance de 1% de você se tornar gerente do banco ao terminar seu estágio.")
                            print("O dono do banco achou que seu desempenho como estagiário foi incrível e por isso você entrará como gerente.")
                            time.sleep(1)
                            print("Agora como gerente você recebe:")
                            time.sleep(1)
                            print("Um bônus inicial de $5000.")
                            time.sleep(0.5)
                            saldo += 5000
                            print("Um salário de $7500 ~ $12500.")
                            time.sleep(0.5)
                            print("Chance de 50% de trabalhar duas vezes no dia.")
                            time.sleep(3)
                            gerente_banco = True
                fim_jogo()
                resposta = 0
                if gerente_banco == True:
                    if random.randint(1,2) == 1:
                        if cooldown_trabalho == 1 and cooldown_trabalho > -2:
                            cooldown_trabalho -= 2
                    else:
                        if cooldown_trabalho == 1 and cooldown_trabalho > -2:
                            cooldown_trabalho -= 1
                if empregado_agiota == True and cooldown_trabalho >= 1:
                    cooldown_trabalho -= 1
                if empregado_banco == True and cooldown_trabalho >= 1:
                    cooldown_trabalho -= 1
                if vida <= 0:
                    break
                qty_mercado_Opium = random.randint(qty_min_mercado_Opium, qty_max_mercado_Opium)
                qty_mercado_Maconha = random.randint(qty_min_mercado_Maconha, qty_max_mercado_Maconha)
                qty_mercado_Speed = random.randint(qty_min_mercado_Speed, qty_max_mercado_Speed)
                qty_mercado_Skank = random.randint(qty_min_mercado_Skank, qty_max_mercado_Skank)
                qty_mercado_Cogumelos = random.randint(qty_min_mercado_Cogumelos, qty_max_mercado_Cogumelos)
                preco_Opium = random.randint(preco_min_Opium, preco_max_Opium)
                preco_Maconha = random.randint(preco_min_Maconha, preco_max_Maconha)
                preco_Speed = random.randint(preco_min_Speed, preco_max_Speed)
                preco_Skank = random.randint(preco_min_Skank, preco_max_Skank)
                preco_Cogumelos = random.randint(preco_min_Cogumelos, preco_max_Cogumelos)
                peso_inv = peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) # (peso_mt1 * hasb_mt1) - (peso_mt2 * hasb_mt2) - (peso_mt3 * hasb_mt3) - (peso_mt4 * hasb_mt4) - (peso_mt5 * hasb_mt5))
                peso_inv += ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))
                fim_jogo()
                if peso_inv < 0:
                    peso_inv *= -1
                dia += 1
                if dia == 1:
                    debito_agiota += debito_agiota*0.5
                else: 
                    debito_agiota += debito_agiota*0.35
                if vida > vida_max:
                    vida_max = vida
                dias_pagar_agiota -= 1
                fim_jogo()
                if saldo >= 150000 and boost_1 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 1!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 2
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 1.1
                    modificador_peso = 0.9
                    modificador_peso_mochila = 0.5
                    boost_1 = True
                elif saldo >= 300000 and boost_2 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 2!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 4
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 1.25
                    modificador_peso = 0.85
                    modificador_peso_mochila = 1
                    boost_2 = True
                elif saldo >= 600000 and boost_3 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 3!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 8
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 1.45
                    modificador_peso = 0.8
                    modificador_peso_mochila = 1.5
                    boost_3 = True
                elif saldo >= 1200000 and boost_4 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 4!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 16
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 1.75
                    modificador_peso = 0.75
                    modificador_peso_mochila = 2
                    boost_4 = True
                elif saldo >= 240000 and boost_5 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 5!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 32
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 2
                    modificador_peso = 0.7
                    modificador_peso_mochila = 2.5
                    boost_5 = True
                elif saldo >= 4800000 and boost_6 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 6!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 64
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 2.5
                    modificador_peso = 0.65
                    modificador_peso_mochila = 3
                    boost_6 = True
                elif saldo >= 9600000 and boost_7 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 7!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 128
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 3
                    modificador_peso = 0.6
                    modificador_peso_mochila = 3.5
                    boost_7 = True
                elif saldo >= 15000000 and boost_8 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 8!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 256
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 3.5
                    modificador_peso = 0.55
                    modificador_peso_mochila = 4
                    boost_8 = True
                elif saldo >= 25000000 and boost_9 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 9!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 512
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 4
                    modificador_peso = 0.5
                    modificador_peso_mochila = 4.5
                    boost_9 = True
                elif saldo >= 40000000 and boost_10 == False:
                    print("----------------------------------------")
                    print("Parabéns! Você chegou ao Boost 10!")
                    if tutorial == True and dia != 0:
                        print("Tutorial: Os boosts são bônus e modificadores que o jogador ganha ao longo do jogo ao ultrapassar uma certa quantidade de saldo na carteira.")
                        print("Tutorial: Boosts te garantem vários benefícios como maior rendimento no banco, aumento dos pesos das mochilas, diminuição do peso dos itens(drogas,armas,coletes,etc), aumento da quantidade de drogas disponíveis no mercado, entre outros.")
                        print("Tutorial: O primeiro nível dos boosts é alcançado ao atingir $150.000. Existem no total dez níveis, cada um aumenta mais os benefícios.")
                    modificador_qty_mercado = 1024
                    #vida_max -= (vida_max*(-0.25))
                    #vida += vida_max*
                    #vida_max += vida_max*
                    modificador_rendimento = 5
                    modificador_peso = 0.40
                    modificador_peso_mochila = 5
                    boost_10 = True
                if conta_banco == True:
                    saldo_banco += ((saldo_banco/100)*5)*modificador_rendimento
                if estudante_hospital == True:
                    dias_estudante += 1
                    saldo -= 1000
                if dias_estudante == 8 and estudante_hospital == True:
                    print("Parabéns! Você se formou na faculdade e agora  pode trabalhar como médico.")
                    estudante_hospital = False
                    empregado_hospital = True
                    dias_estudante = 0
                if saldo < 0 and estudante_hospital == True:
                    print("Você se endividou muito e não possui mais dinheiro na conta para pagar sua faculdade.")
                    print("Sua matrícula foi cancelada.")
                    estudante_hospital = False
                    dias_estudante = 0
                    time.sleep(5)
                if saldo < 0 and conta_banco == True:
                    print("Você se endividou muito e não possui mais dinheiro na carteira para manter sua conta no banco.")
                    print("Sua conta no banco foi bloqueada.")
                    conta_banco == False
                    if estagiario_banco == True or empregado_banco == True:
                        print("Você foi mandado embora do banco já que você não possui mais uma conta.")
                        estagiario_banco == False
                        empregado_banco == False
                        dias_estagio = 0
                    print("Para desbloquear o saldo em sua conta do banco você deve abri-la novamente.")
                    time.sleep(5)
                cobranca_diaria_agiota = False
                if dias_tentar_roubar_banco > 0:
                    dias_tentar_roubar_banco -= 1
                if dias_roubo_banco > 0:
                    dias_roubo_banco -= 1
                alterar_valores()
                fim_jogo()

def interface_usuario2():
    fim_jogo()
    global dia
    global max_dias
    global vida
    global saldo
    global debito_agiota
    global peso_inv
    global peso_Opium
    global peso_Maconha
    global qty_inv_Opium
    global qty_inv_Maconha
    global preco_Opium
    global preco_Maconha
    global qty_mercado_Opium
    global qty_mercado_Maconha
    global resposta
    global peso_Speed
    global qty_inv_Speed
    global preco_Speed
    global qty_mercado_Speed
    global peso_Skank
    global qty_inv_Skank
    global preco_Skank
    global qty_mercado_Skank
    global peso_Cogumelos
    global qty_inv_Cogumelos
    global preco_Cogumelos
    global qty_mercado_Cogumelos
    os.system('cls')
    print("----------------------------------------")
    print("              Drug's Skid               ")
    print("----------------------------------------")
    if tutorial == True and dia != 0:
        print("Tutorial: Dia atual.")
        print("Tutorial: Sua vida deve sempre ser maior que zero, caso contrário, o jogo acaba. Cuidado, existem diversas formas de perder vida.")
        print("Tutorial: Seu saldo atual é seu dinheiro na carteira, utilizado para realizar compras.")
    print("Dia", dia)
    print(f"Vida: {vida}")
    print(f"Saldo atual: ${saldo}")
    if dia == 0: 
        if tutorial == True and dia != 0:
            print("Tutorial: Seu débito atual é o quanto você deve ao agiota.")
        print(f"Débito atual: ${debito_agiota} + ${alt_debito_agiota} = ${alt_debito_agiota+debito_agiota}")
    else:
        if tutorial == True and dia != 0:
            print("Tutorial: Seu débito atual é o quanto você deve ao agiota.")
        print(f"Débito atual: ${debito_agiota} + ${alt_debito_agiota} = ${alt_debito_agiota+debito_agiota}")
    resposta = 0
    fim_jogo()

def compra_Opium(qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos):
    fim_jogo()
    global resposta
    global peso_inv
    resposta = 0
    while resposta != 9:
        global qty_inv_Opium
        global qty_inv_Maconha
        global qty_inv_Speed
        global qty_inv_Skank
        global qty_inv_Cogumelos
        interface_usuario2()
        print("--------------------------------")
        if tutorial == True and dia != 0:
            print("Tutorial: Essa é a loja de drogas, aqui você pode comprar e acompanhar os preços das drogas.")
            print("Tutorial: Diariamente os preços variam, é uma jogada inteligente utilizar a variação a seu favor.")
            print("Tutorial: Para realizar uma compra é fácil, basta digitar o número do que deseja de acordo com o menu abaixo (igual ao menu principal) e em seguida a quantidade.")
            print("Tutorial: Um ponto importante é a quantidade disponível de cada droga. Todos os dias são disponibilizadas drogas em uma certa quantidade, que aumenta conforme você avança nos boosts (vantagens ao atingir certa quantidade monetária).")
            print("Tutorial: Na maioria dos menu utilizados no jogo, o valor 9 é utilizado para voltar ao menu anterior.")
            print("--------------------------------")
        print(f"[1] - Opium = ${preco_Opium}")
        print(f"Disponível: {qty_mercado_Opium}")
        print(f"[2] - Maconha = ${preco_Maconha}")
        print(f"Disponível: {qty_mercado_Maconha}")
        print(f"[3] - Speed = ${preco_Speed}")
        print(f"Disponível: {qty_mercado_Speed}")
        print(f"[4] - Skank = ${preco_Skank}")
        print(f"Disponível: {qty_mercado_Skank}")
        print(f"[5] - Cogumelos = ${preco_Cogumelos}")
        print(f"Disponível: {qty_mercado_Cogumelos}")
        print(f"[9] - Voltar")
        print("--------------------------------")
        fim_jogo()
        resposta = input("O que deseja comprar? ")
        if resposta.isnumeric() == False:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        else:
            resposta = int(resposta)
        if resposta < 1 or resposta > 9:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        elif dia == 0:
            print("Você não pode fazer isso no dia 0.")
        elif resposta == 1:
            fim_jogo()
            qty_compra = input("Quantidade a comprar: ")
            if qty_compra.isnumeric() == False:
                print('Por favor insira um valor numérico.')
                time.sleep(1)
            else:
                qty_compra = int(qty_compra)
                print(f"Preço total da compra: {qty_compra * preco_Opium}")
                resposta = input("Tem certeza que deseja continuar? [S/N] ")
                if resposta.isalpha() == False:
                    print("Por favor responda com S ou N.")
                    time.sleep(1)
                else:
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_Opium > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra <= 0:
                                print("Valor menor ou igual a zero.")
                                time.sleep(1)
                            else:
                                if qty_compra > qty_mercado_Opium:
                                    print("Quantidade a comprar maior que a disponível.")
                                    time.sleep(1)
                                else:
                                    if qty_compra * peso_Opium > peso_inv:
                                        print("Peso insuficiente.")
                                        time.sleep(2)
                                    else:
                                        saldo -= qty_compra * preco_Opium
                                        qty_mercado_Opium -= qty_compra
                                        qty_inv_Opium += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_Opium} = {qty_compra * preco_Opium}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        peso_inv -= peso_Opium * qty_compra
                                        return qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos  # Retorna o saldo atualizado e a quantidade disponível
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')
        elif resposta == 2:
            fim_jogo()
            qty_compra = input("Quantidade a comprar: ")
            if qty_compra.isnumeric() == False:
                print('Por favor insira um valor numérico.')
                time.sleep(1)
            else:
                qty_compra = int(qty_compra)
                print(f"Preço total da compra: {qty_compra * preco_Maconha}")
                resposta = input("Tem certeza que deseja continuar? [S/N] ")
                if resposta.isalpha() == False:
                    print("Por favor responda com S ou N.")
                    time.sleep(1)
                else:
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_Maconha > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra <= 0:
                                print("Valor menor ou igual a zero.")
                                time.sleep(1)
                            else:
                                if qty_compra > qty_mercado_Maconha:
                                    print("Quantidade a comprar maior que a disponível.")
                                    time.sleep(1)
                                else:
                                    if qty_compra * peso_Maconha > peso_inv:
                                        print("Peso insuficiente.")
                                        time.sleep(2)
                                    else:
                                        saldo -= qty_compra * preco_Maconha
                                        qty_mercado_Maconha -= qty_compra
                                        qty_inv_Maconha += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_Maconha} = {qty_compra * preco_Maconha}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        peso_inv -= peso_Maconha * qty_compra
                                        return qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos  # Retorna o saldo atualizado e a quantidade disponível
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')
        elif resposta == 3:
            qty_compra = input("Quantidade a comprar: ")
            if qty_compra.isnumeric() == False:
                print('Por favor insira um valor numérico.')
                time.sleep(1)
            else:
                qty_compra = int(qty_compra)
                print(f"Preço total da compra: {qty_compra * preco_Speed}")
                resposta = input("Tem certeza que deseja continuar? [S/N] ")
                if resposta.isalpha() == False:
                    print("Por favor responda com S ou N.")
                    time.sleep(1)
                else:
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_Speed > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra <= 0:
                                print("Valor menor ou igual a zero.")
                                time.sleep(1)
                            else:
                                if qty_compra > qty_mercado_Speed:
                                    print("Quantidade a comprar maior que a disponível.")
                                    time.sleep(1)
                                else:
                                    if qty_compra * peso_Speed > peso_inv:
                                        print("Peso insuficiente.")
                                        time.sleep(2)
                                    else:
                                        saldo -= qty_compra * preco_Speed
                                        qty_mercado_Speed -= qty_compra
                                        qty_inv_Speed += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_Speed} = {qty_compra * preco_Speed}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        peso_inv -= peso_Speed * qty_compra
                                        return qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos  # Retorna o saldo atualizado e a quantidade disponível
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')
        elif resposta == 4:
            qty_compra = input("Quantidade a comprar: ")
            if qty_compra.isnumeric() == False:
                print('Por favor insira um valor numérico.')
                time.sleep(1)
            else:
                qty_compra = int(qty_compra)
                print(f"Preço total da compra: {qty_compra * preco_Skank}")
                resposta = input("Tem certeza que deseja continuar? [S/N] ")
                if resposta.isalpha() == False:
                    print("Por favor responda com S ou N.")
                    time.sleep(1)
                else:
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_Skank > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra <= 0:
                                print("Valor menor ou igual a zero.")
                                time.sleep(1)
                            else:
                                if qty_compra > qty_mercado_Skank:
                                    print("Quantidade a comprar maior que a disponível.")
                                    time.sleep(1)
                                else:
                                    if qty_compra * peso_Skank > peso_inv:
                                        print("Peso insuficiente.")
                                        time.sleep(2)
                                    else:
                                        saldo -= qty_compra * preco_Skank
                                        qty_mercado_Skank -= qty_compra
                                        qty_inv_Skank += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_Skank} = {qty_compra * preco_Skank}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        peso_inv -= peso_Skank * qty_compra
                                        return qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos # Retorna o saldo atualizado e a quantidade disponível
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')
        elif resposta == 5:
            qty_compra = input("Quantidade a comprar: ")
            if qty_compra.isnumeric() == False:
                print('Por favor insira um valor numérico.')
                time.sleep(1)
            else:
                qty_compra = int(qty_compra)
                print(f"Preço total da compra: {qty_compra * preco_Cogumelos}")
                resposta = input("Tem certeza que deseja continuar? [S/N] ")
                if resposta.isalpha() == False:
                    print("Por favor responda com S ou N.")
                    time.sleep(1)
                else:
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_Cogumelos > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra <= 0:
                                print("Valor menor ou igual a zero.")
                                time.sleep(1)
                            else:
                                if qty_compra > qty_mercado_Cogumelos:
                                    print("Quantidade a comprar maior que a disponível.")
                                    time.sleep(1)
                                else:
                                    if qty_compra * peso_Cogumelos > peso_inv:
                                        print("Peso insuficiente.")
                                        time.sleep(2)
                                    else:
                                        saldo -= qty_compra * preco_Cogumelos
                                        qty_mercado_Cogumelos -= qty_compra
                                        qty_inv_Cogumelos += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_Cogumelos} = {qty_compra * preco_Cogumelos}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        peso_inv -= peso_Cogumelos * qty_compra
                                        return qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos # Retorna o saldo atualizado e a quantidade disponível
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')
        elif resposta == 9:
            print("Voltando...")
            time.sleep(2)
            os.system('cls')
            interface_usuario()
            break

def venda_Opium():
    fim_jogo()
    global resposta
    resposta = 0
    while resposta != 3:
        global qty_inv_Maconha, qty_mercado_Maconha, qty_inv_Opium, qty_mercado_Opium, qty_inv_Speed, qty_mercado_Speed, qty_inv_Skank, qty_mercado_Skank, qty_inv_Cogumelos, qty_mercado_Cogumelos
        global saldo, peso_inv  # Declarando as variáveis como globais
        interface_usuario2()
        if tutorial == True and dia != 0:
            print("--------------------------------")
            print("Tutorial: Aqui você vende suas drogas.")
            print("Tutorial: Para realizar uma venda é fácil, basta digitar o número do que deseja de acordo com o menu abaixo (igual ao menu principal) e em seguida a quantidade a vender.")
            print("Tutorial: Na maioria dos menu utilizados no jogo, o valor 9 é utilizado para voltar ao menu anterior.")
        print("--------------------------------")
        print(f"[1] - Opium = ${preco_Opium}")
        print(f"[2] - Maconha = ${preco_Maconha}")
        print(f"[3] - Speed = ${preco_Speed}")
        print(f"[4] - Skank = ${preco_Skank}")
        print(f"[5] - Cogumelos = ${preco_Cogumelos}")
        print(f"[9] - Voltar")
        print("--------------------------------")
        resposta = input("O que deseja vender? ")
        if resposta.isnumeric() == False:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        else:
            resposta = int(resposta)
        if resposta < 1 or resposta > 9:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        elif dia == 0:
            print("Você não pode fazer isso no dia 0.")
            time.sleep(1)
        elif resposta == 1:
            resposta = input("Quanto deseja vender? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_venda = int(resposta)
                resposta = int(resposta)
            if dia == 0 and resposta!= 9 and type(resposta) == int:
                print("Você está no dia 0 e não pode fazer isso!")
                print("Para jogar você precisa iniciar o primeiro dia.")
                print("Insira 9 para ir para o próximo dia e começar o jogo.")
                time.sleep(3)
                os.system('cls')
            if qty_venda <= 0:
                print("Valor menor ou igual a zero.")
                time.sleep(1)
            else:
                if qty_venda > qty_inv_Opium:
                    print("Quantidade a vender maior que a disponível.")
                    print(f"Inventário: {qty_inv_Opium}")
                    time.sleep(2)
                else:
                    saldo += qty_venda * preco_Opium
                    qty_inv_Opium -= qty_venda
                    qty_mercado_Opium += qty_venda
                    peso_inv += qty_venda * peso_Opium  # Atualizando o peso do inventário
                    print(f"Você vendeu com sucesso {qty_venda} Opium, e agora está com {qty_inv_Opium} no inventário.")
                    print(f"Valor da venda: {qty_venda * preco_Opium}")
                    print(f"Saldo atual: {saldo}")
                    time.sleep(2)
        if resposta == 2:
            resposta = input("Quanto deseja vender? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_venda = int(resposta)
                resposta = int(resposta)
            if dia == 0 and resposta!= 9 and type(resposta) == int:
                print("Você está no dia 0 e não pode fazer isso!")
                print("Para jogar você precisa iniciar o primeiro dia.")
                print("Insira 9 para ir para o próximo dia e começar o jogo.")
                time.sleep(3)
                os.system('cls')
            if qty_venda <= 0:
                print("Valor menor ou igual a zero.")
                time.sleep(2)
            else:
                if qty_venda > qty_inv_Maconha:
                    print("Quantidade a vender maior que a disponível.")
                    print(f"Inventário: {qty_inv_Maconha}")
                    time.sleep(2)
                else:
                    saldo += qty_venda * preco_Maconha
                    qty_inv_Maconha -= qty_venda
                    qty_mercado_Maconha += qty_venda
                    peso_inv += qty_venda * peso_Maconha  # Atualizando o peso do inventário
                    print(f"Você vendeu com sucesso {qty_venda} maconha, e agora está com {qty_inv_Maconha} no inventário.")
                    print(f"Valor da venda: {qty_venda * preco_Maconha}")
                    print(f"Saldo atual: {saldo}")
                    time.sleep(2)
        if resposta == 3:
            resposta = input("Quanto deseja vender? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_venda = int(resposta)
                resposta = int(resposta)
            if dia == 0 and resposta!= 9 and type(resposta) == int:
                print("Você está no dia 0 e não pode fazer isso!")
                print("Para jogar você precisa iniciar o primeiro dia.")
                print("Insira 9 para ir para o próximo dia e começar o jogo.")
                time.sleep(3)
                os.system('cls')
            if qty_venda <= 0:
                print("Valor menor ou igual a zero.")
                time.sleep(2)
            else:
                if qty_venda > qty_inv_Speed:
                    print("Quantidade a vender maior que a disponível.")
                    print(f"Inventário: {qty_inv_Speed}")
                    time.sleep(2)
                else:
                    saldo += qty_venda * preco_Speed
                    qty_inv_Speed -= qty_venda
                    qty_mercado_Speed += qty_venda
                    peso_inv += qty_venda * peso_Speed  # Atualizando o peso do inventário
                    print(f"Você vendeu com sucesso {qty_venda} speed, e agora está com {qty_inv_Speed} no inventário.")
                    print(f"Valor da venda: {qty_venda * preco_Speed}")
                    print(f"Saldo atual: {saldo}")
                    time.sleep(2)
        if resposta == 4:
            resposta = input("Quanto deseja vender? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_venda = int(resposta)
                resposta = int(resposta)
            if dia == 0 and resposta!= 9 and type(resposta) == int:
                print("Você está no dia 0 e não pode fazer isso!")
                print("Para jogar você precisa iniciar o primeiro dia.")
                print("Insira 9 para ir para o próximo dia e começar o jogo.")
                time.sleep(3)
                os.system('cls')
            if qty_venda <= 0:
                print("Valor menor ou igual a zero.")
                time.sleep(2)
            else:
                if qty_venda > qty_inv_Skank:
                    print("Quantidade a vender maior que a disponível.")
                    print(f"Inventário: {qty_inv_Skank}")
                    time.sleep(2)
                else:
                    saldo += qty_venda * preco_Skank
                    qty_inv_Skank -= qty_venda
                    qty_mercado_Skank += qty_venda
                    peso_inv += qty_venda * peso_Skank  # Atualizando o peso do inventário
                    print(f"Você vendeu com sucesso {qty_venda} skank, e agora está com {qty_inv_Skank} no inventário.")
                    print(f"Valor da venda: {qty_venda * preco_Skank}")
                    print(f"Saldo atual: {saldo}")
                    time.sleep(2)
        if resposta == 5:
            resposta = input("Quanto deseja vender? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_venda = int(resposta)
                resposta = int(resposta)
            if dia == 0 and resposta!= 9 and type(resposta) == int:
                print("Você está no dia 0 e não pode fazer isso!")
                print("Para jogar você precisa iniciar o primeiro dia.")
                print("Insira 9 para ir para o próximo dia e começar o jogo.")
                time.sleep(3)
                os.system('cls')
            if qty_venda <= 0:
                print("Valor menor ou igual a zero.")
                time.sleep(2)
            else:
                if qty_venda > qty_inv_Cogumelos:
                    print("Quantidade a vender maior que a disponível.")
                    print(f"Inventário: {qty_inv_Cogumelos}")
                    time.sleep(2)
                else:
                    saldo += qty_venda * preco_Cogumelos
                    qty_inv_Cogumelos -= qty_venda
                    qty_mercado_Cogumelos += qty_venda
                    peso_inv += qty_venda * peso_Cogumelos  # Atualizando o peso do inventário
                    print(f"Você vendeu com sucesso {qty_venda} cogumelo, e agora está com {qty_inv_Cogumelos} no inventário.")
                    print(f"Valor da venda: {qty_venda * preco_Cogumelos}")
                    print(f"Saldo atual: {saldo}")
                    time.sleep(2)
        elif resposta == 9:
            print("Voltando...")
            time.sleep(1)
            os.system('cls')
            interface_usuario()
            break
    return saldo

def ir_agiota():
    fim_jogo()
    global debito_agiota
    global resposta
    global saldo
    global empregado_agiota
    global qty_inv_Opium
    global cooldown_trabalho
    global dias_pagar_agiota
    resposta = 0
    while resposta != 9:
        time.sleep(2)
        os.system('cls')
        interface_usuario2()
        if tutorial == True and dia != 0:
            print("--------------------------------")
            print("Tutorial: Aqui você pode interagir com o agiota.")
            print("Tutorial: Você pode pagar suas dívidas, pegar empréstimos e trabalhar para ele.")
            print("Tutorial: Para empréstimos, você pode pegar no máximo 150% do seu saldo atual.")
            print("Tutorial: Assim como cada trabalho tem seus requisitos, o agiota também exige um requisito inicial para trabalhar para ele.")
        print("--------------------------------")
        print("Seja bem vindo ao agiota.")
        print("[1] - Pagar agiota.")
        print("[2] - Pegar empréstimo.")
        print("[3] - Trabalhar.")
        print("[4] - Tornar-se empregado.")
        print("[9] - Sair")
        print("--------------------------------")
        resposta = input("O que deseja fazer? ")
        if resposta.isnumeric() == False:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        else:
            resposta = int(resposta)
        if resposta < 1 or resposta > 9:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        elif dia == 0:
            print("Você não pode fazer isso no dia 0.")
        elif resposta == 1:
            if debito_agiota == 0:
                print("Você não está devendo nada ao agiota.")
                time.sleep(2)
            else:
                print(f"Você está devendo {debito_agiota} ao agiota.")
                valor_pagar_agiota = input("Quanto quer pagar ao agiota? ")
                try:
                    valor_pagar_agiota = float(valor_pagar_agiota)
                except ValueError:
                    print("Por favor insira um valor válido.")
                    time.sleep(2)
                    break
                resposta = input("Tem certeza? [S/N] ")
                if resposta == "s" or resposta == "S":
                    if saldo >= valor_pagar_agiota and valor_pagar_agiota <= debito_agiota:
                        debito_agiota -= valor_pagar_agiota
                        saldo -= valor_pagar_agiota
                        print(f"Você pagou ao agiota {valor_pagar_agiota} e agora está devendo {debito_agiota}.")
                        time.sleep(2)
                        if debito_agiota == 0:
                            dias_pagar_agiota = 0
                    else:
                        print("Você não possui dinheiro o suficiente ou o valor excede a dívida.")
                        time.sleep(2)
                else:
                    print("Operação cancelada.")
        elif resposta == 2:
            if debito_agiota == 0:
                valor_emprestimo_agiota = input("Quanto quer pegar de empréstimo? ")
                try:
                    valor_pagar_agiota = float(valor_pagar_agiota)
                except ValueError:
                    print("Por favor insira um valor válido.")
                    time.sleep(2)
                    break
                if valor_emprestimo_agiota <= 0:
                    print("Não é possível pegar esse valor, já que é menor ou igual a zero.")
                    time.sleep(2)
                else:
                    if valor_emprestimo_agiota > saldo * 2:
                        print("Não é possível pegar esse valor, já que é muito acima do seu saldo atual.")
                        time.sleep(2)
                    else:
                        debito_agiota = valor_emprestimo_agiota
                        saldo += valor_emprestimo_agiota
                        print("Você pegou o empréstimo com sucesso.")
                        dias_pagar_agiota = 0 
                        dias_pagar_agiota = 3
                        print(f"O agiota irá te cobrar o valor daqui a {dias_pagar_agiota} dias, esteja com o dinheiro em mãos.")
                        time.sleep(2)
            else:
                print("Você já tem um débito com o agiota. Pague-o primeiro!")
                time.sleep(2)
        elif resposta == 3:
            if empregado_agiota == False:
                print("Você não é empregado do agiota e não pode fazer isso!")
                time.sleep(2)
            elif cooldown_trabalho == 0:
                opium_empregado_agiota = random.randint(1,3)
                salario_empregado_agiota = opium_empregado_agiota * preco_Opium
                saldo += salario_empregado_agiota
                cooldown_trabalho += 1
                print(f"Você trabalhou para o agiota e ganhou {opium_empregado_agiota} opium, que foram vendidos por ${salario_empregado_agiota}.")
                time.sleep(2)
                if random.randint(1,100) > 50:
                    vida_perdida_emprego = random.randint(15,40)
                    print(f"Enquanto trabalhava para o agiota, você perdeu {vida_perdida_emprego} de vida!")
                    time.sleep(2)
                if random.randint(1,100) <= 20:
                    bonus_emprego = random.randint(2500, 6000)
                    print(f"Você fez um ótimo trabalho hoje e recebeu um bônus do agiota no valor de ${bonus_emprego}, parabéns!")
                    time.sleep(2)
                    saldo += bonus_emprego
            else:
                print("O agiota ainda não tem nenhum trabalho para você. Volte mais tarde.")
                time.sleep(2)
        elif resposta == 4:
            if empregado_agiota == False:
                if empregado_banco == True or empregado_hospital == True or estagiario_banco == True or estudante_hospital == True or gerente_banco == True:
                    print("Você não pode se tornar empregado do agiota se estiver na faculdade, fazendo estágio ou em outro trabalho.")
                else:
                    if tutorial == True and dia != 0:
                        print("--------------------------------")
                        print("Tutorial: Aqui você pode ser contratado pelo agiota.")
                        print("Tutorial: Para entrar basta cumprir os requisitos, porém atente-se, esse trabalho pode ser perigoso.")
                        print("Tutorial: Você pode trabalhar apenas uma vez no dia e não é possível sair do trabalho, então tenha certeza do que está fazendo.")
                        print("--------------------------------")
                    print("O agiota está contratando novos funcionários e quer saber se você é capacitado.")
                    if debito_agiota != 0:
                        print("Você não pode estar devendo o agiota se quiser trabalhar para ele!") 
                        time.sleep(2)
                    else:
                        print("O agiota cobra uma taxa de 15 Opium para quem quer se candidatar.")
                        resposta = input("Deseja de candidatar? [S/N]")
                        if resposta == "s" or resposta == "S":
                            if qty_inv_Opium < 15:
                                print("Você não possui 15 Opium.")
                                time.sleep(2)
                            else:
                                qty_inv_Opium -= 15
                                resposta = input("Você está disposto a dar sua vida pelo agiota? [S/N] ")
                                if resposta == "s" or resposta == "S":
                                    print("Você foi contratado pelo agiota.")
                                    empregado_agiota = True
                                    time.sleep(2)
                                else:
                                    print("Você não está pronto para essa função.")
                                    time.sleep(2)
                        else:
                            print("Operação cancelada.")
                            time.sleep(2)
                            os.system('cls')
                            break
            else:
                print("Você já é empregado do agiota.")
                time.sleep(2)
        elif resposta == 9:
            print("Voltando...")
            time.sleep(1)
            os.system('cls')
            break

def ir_banco():
    fim_jogo()
    global resposta
    global saldo
    global empregado_agiota
    global estagiario_banco
    global dias_estagio
    global conta_banco
    global saldo_banco
    global cooldown_trabalho
    global vida
    global dias_tentar_roubar_banco, dias_roubo_banco
    rendeu_guardas = False
    rendeu_guardas2 = False
    resposta = 0
    while resposta != 6:
        os.system("cls")
        interface_usuario2()
        if empregado_agiota == True:
            print("Você não pode usar o banco sendo empregado do agiota!")
            time.sleep(2)
        elif dias_roubo_banco == 0 and dias_tentar_roubar_banco == 0:
            if conta_banco == False:
                if tutorial == True and dia != 0:
                    print("Tutorial: Para abrir uma conta no banco você precisa ter mais de $6200 de saldo, pagar uma taxa de $5000 e uma taxa diária de $1200.")
                print("Você não possui uma conta no banco.")
                resposta = input("Deseja abrir? [Abrir[S] / Sair[N] ")
                if dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == "s" or resposta == "S":
                    print("Você precisa pagar uma taxa de 5000 reais para abrir a conta e uma taxa de manutenção diária de 1200 reais.")
                    print("Para garantirmos a estabilidade financeira dos clientes, abrimos contas apenas para quem possui mais de 6200 na conta.")
                    resposta = input("Deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if saldo >= 6200:
                            print("Você abriu com sucesso uma conta no banco, meus parabéns!")
                            saldo -= 5000
                            conta_banco = True
                            time.sleep(1)
                            os.system('cls')
                        else:
                            print("Você não possui 6200 ou mais.")
                            time.sleep(1)
                            os.system('cls')
                            break
                    else:
                        print("Operação cancelada, nenhum valor foi debitado.")
                        time.sleep(1)
                        os.system('cls')
                        break
                else:
                    print("Operação cancelada, nenhum valor foi debitado.")
                    time.sleep(1)
                    os.system('cls')
                    break
            if conta_banco == True:
                time.sleep(1)
                resposta = 0
                if tutorial == True and dia != 0:
                    print("--------------------------------")
                    print("Tutorial: O banco é onde você pode deixar seu dinheiro rendendo, trabalhar, ou roubar.")
                    print("Tutorial: Seu dinheiro depositado renderá uma taxa diária, mas não poderá ser gasto enquanto estiver no banco.")
                    print("Tutorial: No roubo ao banco, você precisa possuir uma arma, quanto mais cara, maior sua chance de sucesso.")
                print("--------------------------------")
                print("Saldo: ", saldo)
                print("Saldo no banco: ", saldo_banco)
                print("--------------------------------")
                print("Seja bem vindo ao banco.")
                print("[1] - Depositar.")
                print("[2] - Sacar")
                print("[3] - Trabalhar.")
                print("[4] - Tornar-se empregado.")
                print("[5] - Roubar banco.")
                print("[9] - Sair")
                resposta = input("O que deseja fazer? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 9:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    resposta = input("Qual valor deseja depositar? ")
                    try:
                        resposta = float(resposta)
                    except ValueError:
                        print("Por favor insira um valor válido.")
                        time.sleep(2)
                        break
                    if resposta > saldo:
                        print("Valor acima do saldo disponível.")
                        time.sleep(2)
                    else:
                        saldo_banco += resposta
                        saldo -= resposta
                        print("Você depositou o valor com sucesso!")
                        print(f"Saldo no banco: {saldo_banco}")
                        print(f"Saldo: {saldo}")
                        print("--------------------------------")
                        time.sleep(2)
                elif resposta == 2:
                    resposta = input("Qual valor deseja sacar? ")
                    try:
                        valor_pagar_agiota = float(valor_pagar_agiota)
                    except ValueError:
                        print("Por favor insira um valor válido.")
                        time.sleep(2)
                        break
                    if resposta > saldo_banco:
                        print("Valor acima do saldo disponível no banco.")
                        time.sleep(2)
                    else:
                        saldo += resposta
                        saldo_banco -= resposta
                        print("Você sacou o valor com sucesso!")
                        print(f"Saldo no banco: {saldo_banco}")
                        print(f"Saldo: {saldo}")
                        print("--------------------------------")
                        time.sleep(2)
                elif resposta == 3:
                    if empregado_banco == False and gerente_banco == False:
                        print("Você não é empregado do banco e não pode fazer isso!")
                        time.sleep(1)
                        os.system('cls')
                    elif cooldown_trabalho == 0 and empregado_banco == True:
                        salario_empregado_banco = random.randint(1000, 2500)
                        saldo += salario_empregado_banco
                        cooldown_trabalho += 1
                        print(f"Você trabalhou para o banco e ganhou ${salario_empregado_banco}.")
                        time.sleep(2)
                        if random.randint(1,100) < 10:
                            bonus_emprego = random.randint(2500,5000)
                            print(f"Você fez um ótimo trabalho hoje e recebeu um bônus do banco no valor de ${bonus_emprego}, parabéns!")
                            time.sleep(3)
                            saldo += bonus_emprego
                    elif cooldown_trabalho <= 0 and gerente_banco == True:
                        salario_gerente_banco = random.randint(7500, 12500)
                        saldo += salario_gerente_banco
                        cooldown_trabalho += 1
                        print(f"Você trabalhou para o banco e ganhou ${salario_gerente_banco}.")
                        time.sleep(2)
                        if random.randint(1,100) < 10:
                            bonus_emprego = random.randint(10000,15000)
                            print(f"Você fez um ótimo trabalho hoje e recebeu um bônus do banco no valor de ${bonus_emprego}, parabéns!")
                            time.sleep(3)
                            saldo += bonus_emprego
                elif resposta == 4:
                    print("Estão abertas as vagas para se tornar funcionário do banco.")
                    print("Para isso, você deve trabalhar por 4 dias como estagiário do banco, sem receber nada, para desenvolver suas habilidades.")
                    resposta = input("Aceita trabalhar no banco? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        print("Parabéns, você foi contratado e agora trabalha como estagiário no banco.")
                        estagiario_banco = True
                        dias_estagio = 0
                        time.sleep(1)
                        os.system('cls')
                    else: 
                        print("Operação cancelada!")
                        time.sleep(2)
                        os.system('cls')
                elif resposta == 5:
                    resposta = 0
                    while resposta != 4:
                        valor_banco = random.randint(40000, 100000)
                        print("Valor total acumulado no banco: ", valor_banco)
                        max_morte = valor_banco/10000
                        if dias_roubo_banco <= 0 and dias_tentar_roubar_banco <= 0:
                            if valor_banco >= 70000:
                                print("Atenção, este roubo possui chance de morte!")
                            resposta = input("Você tem certeza que deseja roubar o banco?")
                            if resposta == "S" or resposta == "s":
                                if has_t3 == True or has_t4 == True or has_t5 == True:
                                    print("[1] - Arma T3")
                                    print("[2] - Arma T4")
                                    print("[3] - Arma T5")
                                    print("[4] - Voltar")
                                    resposta = input("Para onde deseja ir? ")
                                    fim_jogo()
                                    if resposta.isnumeric() == False:
                                        print("Por favor insira um valor numérico dentro dos limites.")
                                        time.sleep(2)
                                        os.system('cls')
                                        break
                                    else:
                                        resposta = int(resposta)
                                    if dia == 0 and resposta!= 9 and type(resposta) == int:
                                        print("Você está no dia 0 e não pode fazer isso!")
                                        print("Para jogar você precisa iniciar o primeiro dia.")
                                        print("Insira 9 para ir para o próximo dia e começar o jogo.")
                                        time.sleep(3)
                                        os.system('cls')
                                    elif resposta < 1 or resposta > 4:
                                        print("Por favor insira um valor numérico dentro dos limites.")
                                        time.sleep(1)
                                        os.system('cls')
                                        time.sleep(2)
                                    if resposta == 1:
                                        if has_t3 == True:
                                            chance_roubo = 15
                                            time.sleep(1)
                                            print("Você equipou a arma T3.")
                                            arma_equip = 3
                                        else:
                                            print("Você não possui essa arma.")
                                            time.sleep(2)
                                    elif resposta == 2:
                                        if has_t4 == True:
                                            chance_roubo = 11
                                            time.sleep(1)
                                            print("Você equipou a arma T4.")
                                            arma_equip = 4
                                        else:
                                            print("Você não possui essa arma.")
                                            time.sleep(2)
                                    elif resposta == 3:
                                        if has_t5 == True:
                                            chance_roubo = 7
                                            time.sleep(1)
                                            print("Você equipou a arma T5.")
                                            arma_equip = 5
                                        else:
                                            print("Você não possui essa arma.")
                                            time.sleep(2)
                                    elif resposta == 4:
                                        print("Voltando...")
                                        time.sleep(1)
                                        break
                                    if has_t3 == True or has_t4 == True or has_t5 == True:
                                        print("Entrando no banco...")
                                        time.sleep(2)
                                        var_roubo1 = random.randint(1, 2)
                                        var_roubo2 = random.randint(1, 2)
                                        if var_roubo1 == var_roubo2:
                                            print("Você conseguiu entrar no banco!")
                                            time.sleep(2)
                                            print("Rendendo atendentes...")
                                            time.sleep(2)
                                            var_roubo1 = random.randint(1, ((chance_roubo+1)/2))
                                            var_roubo2 = random.randint(1, ((chance_roubo+1)/2))
                                            if var_roubo1 == var_roubo2:
                                                print("Você conseguiu render os atendentes!")
                                                time.sleep(2)
                                                if var_roubo1 % 2 == 0:
                                                    print("Um guarda que estava escondido te surpreendeu.")
                                                    time.sleep(2)
                                                    print("Troca de tiro...")
                                                    time.sleep(2)
                                                    var_roubo3 = random.randint(1,2)
                                                    var_roubo4 = random.randint(1,2)
                                                    if var_roubo3 == var_roubo4:
                                                        print("O guarda te acertou um tiro!")
                                                        resposta = input("Você deseja usar medicamentos [S/N]? ")
                                                        if resposta == "S" or resposta == "s":
                                                            usar_medicamentos()
                                                        time.sleep(2)
                                                        perda_vida_roubo_banco = random.randint(10,round(4*max_morte))
                                                        print(f"Você perdeu {perda_vida_roubo_banco} de vida!")
                                                        vida -= perda_vida_roubo_banco
                                                        print("Vida: ", vida)
                                                        time.sleep(2)
                                                        var_roubo3 = random.randint(1,2)
                                                        var_roubo4 = random.randint(1,2)
                                                        if var_roubo3 == var_roubo4:
                                                            print("O guarda te acertou mais um tiro!")
                                                            resposta = input("Você deseja usar medicamentos [S/N]? ")
                                                            if resposta == "S" or resposta == "s":
                                                                usar_medicamentos()
                                                            time.sleep(2)
                                                            perda_vida_roubo_banco = random.randint(10,round(4*max_morte))
                                                            print(f"Você perdeu mais {perda_vida_roubo_banco} de vida!")
                                                            vida -= perda_vida_roubo_banco
                                                            print("Vida: ", vida)
                                                            time.sleep(2)
                                                        print("Você conseguiu render o guarda.")
                                                        time.sleep(2)
                                                        rendeu_guardas = True
                                                    else:
                                                        print("O guarda não te acertou nenhum tiro e você conseguiu rende-lo.")
                                                        time.sleep(2)
                                                        rendeu_guardas = True
                                                else:
                                                    rendeu_guardas = True
                                                if var_roubo2 % 2 == 0:
                                                    print("Um guarda que estava escondido te surpreendeu.")
                                                    time.sleep(2)
                                                    print("Troca de tiro...")
                                                    time.sleep(2)
                                                    var_roubo3 = random.randint(1,2)
                                                    var_roubo4 = random.randint(1,2)
                                                    if var_roubo3 == var_roubo4:
                                                        print("O guarda te acertou um tiro!")
                                                        resposta = input("Você deseja usar medicamentos [S/N]? ")
                                                        if resposta == "S" or resposta == "s":
                                                            usar_medicamentos()
                                                        time.sleep(2)
                                                        perda_vida_roubo_banco = random.randint(10,round(4*max_morte))
                                                        print(f"Você perdeu {perda_vida_roubo_banco} de vida!")
                                                        vida -= perda_vida_roubo_banco
                                                        print("Vida: ", vida)
                                                        time.sleep(2)
                                                        var_roubo3 = random.randint(1,2)
                                                        var_roubo4 = random.randint(1,2)
                                                        if var_roubo3 == var_roubo4:
                                                            print("O guarda te acertou mais um tiro!")
                                                            resposta = input("Você deseja usar medicamentos [S/N]? ")
                                                            if resposta == "S" or resposta == "s":
                                                                usar_medicamentos()
                                                            time.sleep(2)
                                                            perda_vida_roubo_banco = random.randint(10,round(4*max_morte))
                                                            print(f"Você perdeu mais {perda_vida_roubo_banco} de vida!")
                                                            vida -= perda_vida_roubo_banco
                                                            print("Vida: ", vida)
                                                            time.sleep(2)
                                                        print("Você conseguiu render o guarda.")
                                                        time.sleep(2)
                                                        rendeu_guardas2 = True
                                                    else:
                                                        print("O guarda não te acertou nenhum tiro e você conseguiu rende-lo.")
                                                        time.sleep(2)
                                                        rendeu_guardas2 = True
                                                else:
                                                    rendeu_guardas2 = True
                                                print("Você rendeu os guardas.")
                                                rendeu_guardas = True
                                                if rendeu_guardas == True and rendeu_guardas2 == True and vida > 0.0000000000001:
                                                    print("Você rendeu todos os guardas no local.")
                                                    time.sleep(2)
                                                    print("Entrando no cofre...")
                                                    time.sleep(2)
                                                    var_roubo2 = random.randint(1,(chance_roubo+1)/2)
                                                    var_roubo1 = random.randint(1,(chance_roubo+1)/2)
                                                    if var_roubo1 == var_roubo2:
                                                        print("Você conseguiu entrar no cofre!")
                                                        time.sleep(2)
                                                        var_roubo4 = random.randint(1,10)
                                                        if var_roubo4 > 5:
                                                            roubado = valor_banco
                                                            print(f"Você roubou os ${valor_banco} reais do banco.")
                                                            time.sleep(2)
                                                        else:
                                                            if arma_equip == 5:
                                                                roubado = random.randint(40000, valor_banco)
                                                                roubado = roubado * 1
                                                            elif arma_equip == 4:
                                                                roubado = random.randint(40000, valor_banco)
                                                                roubado = roubado * 0.8
                                                            elif arma_equip == 3:
                                                                roubado = random.randint(40000, valor_banco)
                                                                roubado = roubado * 0.6
                                                            print(f"Você só conseguiu roubar ${roubado}")
                                                            time.sleep(2)
                                                        print("Fugindo do local...")
                                                        time.sleep(4)
                                                        var_roubo1 = random.randint(1,((chance_roubo+3)/2+1)/2)
                                                        var_roubo2 = random.randint(1,((chance_roubo+3)/2+1)/2)
                                                        if var_roubo1 == var_roubo2:
                                                            print(f"Você conseguiu fugir do banco com ${roubado}")
                                                            saldo += roubado
                                                            time.sleep(2)
                                                            dias_roubo_banco = 3
                                                        else:
                                                            var_roubo1 = random.randint(1,3)
                                                            var_roubo2 = random.randint(1,3)
                                                            if var_roubo1 != var_roubo2:
                                                                print("Você não conseguiu fugir com o dinheiro, mas conseguiu sair do local.")
                                                                time.sleep(1)
                                                                os.system('cls')
                                                                dias_tentar_roubar_banco = 2
                                                            else:
                                                                print("Você não conseguiu fugir do local.")
                                                                time.sleep(1)
                                                                os.system('cls')
                                                                dias_tentar_roubar_banco = 2

                                                    else:
                                                        print("Você não conseguiu entrar no cofre!")
                                                        time.sleep(1)
                                                        os.system('cls')
                                                        dias_tentar_roubar_banco = 2
                                            else:
                                                print("Você não conseguiu render os clientes!")
                                                time.sleep(1)
                                                os.system('cls')
                                                dias_tentar_roubar_banco = 2
                                        else:
                                            print("Você não conseguiu entrar no banco.")
                                            time.sleep(1)
                                            os.system('cls')
                                            dias_tentar_roubar_banco = 2
                                else:
                                    print("Você não possui uma arma para roubar o banco (T3,T4 ou T5).")
                                    time.sleep(1)
                                    os.system('cls')
                            else: 
                                print("Todas as operações foram canceladas e você não roubou o banco.")
                                time.sleep(1)
                                os.system('cls')
                                break
                            time.sleep(2)
                        else:
                            if dias_tentar_roubar_banco > 0:
                                print("Você tentou roubar o banco recentemente.")
                                print("Tente novamente mais tarde.")
                                time.sleep(2)
                                os.system('cls')
                                break
                            else:
                                print("Você precisa esperar um tempo para roubar o banco novamente ou será pego.")
                                print("Volte mais tarde.")
                                time.sleep(2)
                                os.system('cls')
                                break

                elif resposta == 9:
                    print("Voltando...")
                    time.sleep(1)
                    os.system('cls')
                    interface_usuario()
                    break
        else:
            print("Você não pode acessar o banco já que roubou ou tentou rouba-lo recentemente.")
            time.sleep(2)
            os.system('cls')
            break

def usar_medicamentos():
    while resposta != 2:
        resposta = 0
        while resposta != 9:
            print("--------------------------------")
            print("[1] - Analgésicos")
            print("[2] - Faixa")
            print("[3] - Atadura")
            print("[4] - Kit Pequeno")
            print("[5] - Kit Grande")
            print("[9] - Voltar")
            print("--------------------------------")
            resposta = input("O que deseja usar? ")
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
            else:
                resposta = int(resposta)
            if resposta < 1 or resposta > 9:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
            elif vida == vida_max:
                print("Sua vida já está no máximo, você não usou nada.")
                time.sleep(2)
            else:
                if resposta == 1:
                    if qty_inv_analgesico > 0 and cd_analgesico == False:
                        qty_inv_analgesico -= 1
                        if vida + hp_analgesico > vida_max:
                            vida = vida_max
                        else:
                            vida += hp_analgesico
                        print("Você utilizou com sucesso 1 analgésico.")
                        time.sleep(1)
                        cd_analgesico = True
                    else:
                        print("Você não possui analgésicos para utilizar ou está em tempo de recarga.")
                        time.sleep(2)
                elif resposta == 2:
                    if qty_inv_faixa > 0 and cd_faixa == False:
                        qty_inv_faixa -= 1
                        if vida + hp_faixa > vida_max:
                            vida = vida_max
                        else:
                            vida += hp_faixa
                        print("Você utilizou com sucesso 1 faixa.")
                        time.sleep(1)
                        cd_faixa = True
                    else:
                        print("Você não possui faixa para utilizar ou está em tempo de recarga.")
                        time.sleep(2)
                elif resposta == 3:
                    if qty_inv_atadura > 0 and cd_atadura == False:
                        qty_inv_atadura -= 1
                        if vida + hp_atadura > vida_max:
                            vida = vida_max
                        else:
                            vida += hp_atadura
                        print("Você utilizou com sucesso 1 atadura.")
                        time.sleep(1)
                        cd_atadura = True
                    else:
                        print("Você não possui atadura para utilizar ou está em tempo de recarga.")
                        time.sleep(2)
                elif resposta == 4:
                    if qty_inv_kit_pequeno > 0 and cd_kit_pequeno == False:
                        qty_inv_kit_pequeno -= 1
                        if vida + hp_kit_pequeno > vida_max:
                            vida = vida_max
                        else:
                            vida += hp_kit_pequeno
                        print("Você utilizou com sucesso 1 kit pequeno.")
                        time.sleep(1)
                        cd_kit_pequeno = True
                    else:
                        print("Você não possui kit pequeno para utilizar ou está em tempo de recarga.")
                        time.sleep(2)
                elif resposta == 5:
                    if qty_inv_kit_grande > 0 and cd_kit_grande == False:
                        qty_inv_kit_grande -= 1
                        if vida + hp_kit_grande > vida_max:
                            vida = vida_max
                        else:
                            vida += hp_kit_grande
                        print("Você utilizou com sucesso 1 kit grande.")
                        cd_kit_grande = True
                        time.sleep(1)
                    else:
                        print("Você não possui kit grande para utilizar ou está em tempo de recarga.")
                        time.sleep(2)
                elif resposta == 9:
                    print("Voltando...")
                    time.sleep(2)
                    os.system('cls')
                    break

def ir_hospital():
    fim_jogo()
    global saldo
    global vida
    global dias_estudante, estudante_hospital, qty_inv_analgesico, qty_inv_faixa, qty_inv_atadura, qty_inv_kit_pequeno, qty_inv_kit_grande, cd_analgesico, cd_faixa, cd_atadura, cd_kit_pequeno, cd_kit_grande, hp_analgesico, hp_faixa, hp_atadura, hp_kit_pequeno, hp_kit_grande
    resposta = 0
    os.system('cls')
    while resposta != 7:
        if tutorial == True and dia != 0:
            print("--------------------------------")
            print("Tutorial: No hospital você pode recuperar sua vida e comprar medicamentos para utilizar depois.")
            print("Tutorial: O sistema de compras é igual ao sistema de compra de drogas, porém com um número limitado de medicamentos de cada tipo.")
            print("Tutorial: Os medicamentos são utilizados para recuperar sua vida, quanto mais caro, mais recupera. Uma consulta ao médico pode ser feita para recuperar completamente sua vida.")
        print("--------------------------------")
        print(f"Dia: {dia}")
        print("--------------------------------")
        print("Vida: ", vida)
        print("Saldo: ", saldo)
        print("--------------------------------")
        print("Seja bem vindo ao hospital.")
        print("[1] - Comprar medicamentos.")
        print("[2] - Consulta médica.")
        print("[3] - Trabalhar.")
        print("[4] - Tornar-se empregado.")
        print("[5] - Roubar medicamentos.")
        print("[6] - Ver meus medicamentos")
        print("[9] - Sair")
        resposta = input("Para onde deseja ir? ")
        fim_jogo()
        if resposta.isnumeric() == False:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
            os.system('cls')
            break
        else:
            resposta = int(resposta)
        if dia == 0 and resposta!= 9 and type(resposta) == int:
            print("Você está no dia 0 e não pode fazer isso!")
            print("Para jogar você precisa iniciar o primeiro dia.")
            print("Insira 9 para ir para o próximo dia e começar o jogo.")
            time.sleep(3)
            os.system('cls')
        elif resposta < 1 or resposta > 9:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(1)
            os.system('cls')
            time.sleep(2)
        if resposta == 1:
            saldo = comprar_medicamentos(saldo)
        elif resposta == 2:
            print("--------------------------------")
            print("Um médico muito experiente veio ao hospital que você frequenta.")
            resposta = input("Deseja realizar uma consulta especial no valor de 85000 e recuperar toda sua vida? [S/N] ")
            print("--------------------------------")
            if resposta == "S" or resposta == "s":
                if saldo >= 85000:
                    resposta = input("Você tem certeza? [S/N] ")
                    if resposta == "S" or resposta == "s":
                        saldo -= 85000
                        vida = vida_max
                        print("Você foi curado completamente.")
                        time.sleep(1)
                    else:
                        print("Cancelando a operação. Nenhum valor foi cobrado.")
                        time.sleep(1)
                else:
                    print("Você não possui saldo o suficiente. Nenhum valor foi cobrado.")
                    time.sleep(1)
            else:
                print("Operação cancelada. Nenhum valor foi cobrado.")
                time.sleep(1)
        elif resposta == 3:
            if empregado_hospital == False:
                        print("Você não é empregado do hospitaç e não pode fazer isso!")
                        time.sleep(2)
            elif cooldown_trabalho == 0 and empregado_hospital == True:
                salario_empregado_hospital = random.randint(6000, 9000)
                saldo += salario_empregado_hospital
                cooldown_trabalho += 1
                print(f"Você trabalhou para o hospital e ganhou ${salario_empregado_hospital}.")
                time.sleep(2)
            if random.randint(1,200) < 3:
                bonus_emprego = random.randint(10000,15000)
                print(f"Você fez um ótimo trabalho hoje e recebeu um bônus do hospital no valor de ${bonus_emprego}, parabéns!")
                time.sleep(2)
                saldo += bonus_emprego
        elif resposta == 4:
            respota = 0
            print("Para se tornar médico você precisa fazer faculdade.")
            time.sleep(2)
            resposta = input("Você deseja entrar na faculdade? [S/N]")
            if respota == "S" or resposta == "s":
                print("Duração: 8 dias")
                print("Matrícula: $2500")
                print("Mensalidade: $1000")
                resposta = input("Deseja realizar a matrícula? [S/N]")
                time.sleep(2)
                if respota == "S" or resposta == "s":
                    if saldo < 6000:
                        print("Verificamos que você possui um saldo abaixo de $6000.")
                        print("Para garantirmos que nossos alunos possuem condição de pagar o curso, aceitamos apenas aqueles com saldo acima de $6000.")
                        time.sleep(1)
                    else:
                        resposta = input("Tem certeza? [S/N]")
                        if respota == "S" or resposta == "s":
                            print("Você se matriculou na faculdade!")
                            saldo -= 2500
                            print("Lembre-se de ter todos os dias $1000 para realizarmos a cobrança ou sua matrícula será cancelada e todo o progresso perdido, sem reembolso.")
                            time.sleep(2)
                            estudante_hospital = True
                            dias_estudante = 8
                        else: 
                            print('Cancelando todas as operações, nenhum valor foi cobrado.')
                            time.sleep(1)
                else:
                    print('Cancelando todas as operações, nenhum valor foi cobrado.')
                    time.sleep(1)        
            else:
                print('Cancelando todas as operações, você não se matriculou.')
                time.sleep(1)
                break      
        elif resposta == 5:
            print("Roubo indisponível.")
            time.sleep(2)

        elif resposta == 6:
            resposta = 0
            while resposta != 2:
                print("--------------------------------")
                print("Analgesicos: ", qty_inv_analgesico)
                print("Faixa: ", qty_inv_faixa)
                print("Atadura: ", qty_inv_atadura)
                print("Kit Pequeno: ", qty_inv_kit_pequeno)
                print("Kit Grande: ", qty_inv_kit_grande)
                print("--------------------------------")
                print("[1] - Usar medicamentos")
                print("[9] - Voltar")
                print("--------------------------------")
                resposta = input("O que deseja fazer? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 9:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    usar_medicamentos()
                elif resposta == 2:
                    print("Voltando...")
                    time.sleep(2)
                    break
        break
                                      
def comprar_medicamentos(saldo):
    fim_jogo()
    resposta = 0
    while resposta != 9:
        global qty_inv_analgesico
        global qty_inv_faixa
        global qty_inv_atadura
        global qty_inv_kit_pequeno
        global qty_inv_kit_grande
        os.system('cls')
        interface_usuario2()
        print("--------------------------------")
        print(f"Analgésicos (10hp) = ${preco_analgesico}")
        print(f"Faixa (15hp) = ${preco_faixa}")
        print(f"Atadura (20hp) = ${preco_atadura}")
        print(f"Kit Pequeno (30hp) = ${preco_kit_pequeno}")
        print(f"Kit Grande (40hp)  = ${preco_kit_grande}")
        print("--------------------------------")
        print("[1] - Analgésicos")
        print("[2] - Faixa")
        print("[3] - Atadura")
        print("[4] - Kit Pequeno")
        print("[5] - Kit Grande")
        print("[9] - Voltar")
        print("--------------------------------")
        resposta = input("O que deseja comprar? ")
        if resposta.isnumeric() == False:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        else:
            resposta = int(resposta)
        if resposta < 1 or resposta > 9:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        elif dia == 0:
            print("Você não pode fazer isso no dia 0.")
        elif resposta == 1:
            resposta = input("Quantos deseja comprar? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_compra = int(resposta)
                resposta = int(resposta)
                if qty_compra+qty_inv_analgesico > 2:
                    print("Você não pode carregar mais que dois analgésicos.")
                    time.sleep(1)
                    break
                else:
                    if peso_inv - peso_analgesico > 0:
                        print(f"Preço total da compra: {qty_compra * preco_analgesico}")
                        resposta = input("Tem certeza que deseja continuar? [S/N] ")
                        if resposta == "s" or resposta == "S":
                            if qty_compra * preco_analgesico > saldo:
                                print("Saldo insuficiente.")
                                time.sleep(1)
                            else:
                                if qty_compra <= 0:
                                    print("Valor menor ou igual a zero.")
                                    time.sleep(1)
                                else:
                                    saldo -= qty_compra * preco_analgesico
                                    qty_inv_analgesico += qty_compra
                                    print(f"Você comprou {qty_compra} x {preco_analgesico} = {qty_compra * preco_analgesico}")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo  # Retorna o saldo atualizado
                        else:
                            print("Operação cancelada.")
                            print("Saldo atual: ", saldo)
                            time.sleep(2)
                            os.system('cls')
                    else:
                        print(f"Você não possui espaço o suficiente no invantário (Analgésico = {peso_analgesico}kg).")
                        time.sleep(2)
                        os.system('cls')
        elif resposta == 2:
            resposta = input("Quantos deseja comprar? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_compra = int(resposta)
                resposta = int(resposta)
                if qty_compra > 2:
                    print("Você não pode comprar mais de duas faixas.")
                    time.sleep(1)
                else:
                    if qty_compra+qty_inv_faixa > 2:
                        print("Você não pode carregar mais que duas faixas.")
                        time.sleep(1)
                    else:
                        if peso_inv - peso_faixa > 0:
                            print(f"Preço total da compra: {qty_compra * preco_faixa}")
                            resposta = input("Tem certeza que deseja continuar? [S/N] ")
                            if resposta == "s" or resposta == "S":
                                if qty_compra * preco_faixa > saldo:
                                    print("Saldo insuficiente.")
                                    time.sleep(1)
                                else:
                                    if qty_compra <= 0:
                                        print("Valor menor ou igual a zero.")
                                        time.sleep(1)
                                    else:
                                        saldo -= qty_compra * preco_faixa
                                        qty_inv_faixa += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_faixa} = {qty_compra * preco_faixa}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        return saldo  # Retorna o saldo atualizado
                            else:
                                print("Operação cancelada.")
                                print("Saldo atual: ", saldo)
                                time.sleep(2)
                                os.system('cls')
                        else:
                            print(f"Você não possui espaço o suficiente no invantário (Analgésico = {peso_faixa}kg).")
                            time.sleep(2)
                            os.system('cls')
        elif resposta == 3:
            resposta = input("Quantos deseja comprar? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_compra = int(resposta)
                resposta = int(resposta)
                if qty_compra > 1:
                    print("Você não pode comprar mais de uma atadura.")
                    time.sleep(1)
                    break
                else:
                    if qty_compra+qty_inv_atadura > 2:
                        print("Você não pode carregar mais que uma atadura.")
                        time.sleep(1)
                        break
                    else:
                        if peso_inv - peso_atadura > 0:
                            print(f"Preço total da compra: {qty_compra * preco_atadura}")
                            resposta = input("Tem certeza que deseja continuar? [S/N] ")
                            if resposta == "s" or resposta == "S":
                                if qty_compra * preco_atadura > saldo:
                                    print("Saldo insuficiente.")
                                    time.sleep(1)
                                    break
                                else:
                                    if qty_compra <= 0:
                                        print("Valor menor ou igual a zero.")
                                        time.sleep(1)
                                        break
                                    else:
                                        saldo -= qty_compra * preco_atadura
                                        qty_inv_atadura += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_atadura} = {qty_compra * preco_atadura}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        return saldo  # Retorna o saldo atualizado
                            else:
                                print("Operação cancelada.")
                                print("Saldo atual: ", saldo)
                                time.sleep(2)
                                os.system('cls')
                                break
                        else:
                            print(f"Você não possui espaço o suficiente no invantário (Analgésico = {peso_atadura}kg).")
                            time.sleep(2)
                            os.system('cls')
                            break
        elif resposta == 4:
            resposta = input("Quantos deseja comprar? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_compra = int(resposta)
                resposta = int(resposta)
                if qty_compra > 1:
                    print("Você não pode comprar mais de um kit pequeno.")
                    time.sleep(1)
                else:
                    if qty_compra+qty_inv_kit_pequeno > 2:
                        print("Você não pode carregar mais que um kit pequeno.")
                        time.sleep(1)
                    else:
                        if peso_inv - peso_kit_pequeno > 0:
                            print(f"Preço total da compra: {qty_compra * preco_kit_pequeno}")
                            resposta = input("Tem certeza que deseja continuar? [S/N] ")
                            if resposta == "s" or resposta == "S":
                                if qty_compra * preco_kit_pequeno > saldo:
                                    print("Saldo insuficiente.")
                                    time.sleep(1)
                                else:
                                    if qty_compra <= 0:
                                        print("Valor menor ou igual a zero.")
                                        time.sleep(1)
                                    else:
                                        saldo -= qty_compra * preco_kit_pequeno
                                        qty_inv_kit_pequeno += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_kit_pequeno} = {qty_compra * preco_kit_pequeno}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        return saldo  # Retorna o saldo atualizado
                            else:
                                print("Operação cancelada.")
                                print("Saldo atual: ", saldo)
                                time.sleep(2)
                                os.system('cls')
                        else:
                            print(f"Você não possui espaço o suficiente no invantário (Analgésico = {peso_kit_pequeno}kg).")
                            time.sleep(2)
                            os.system('cls')
        elif resposta == 5:
            resposta = input("Quantos deseja comprar? ")
            fim_jogo()
            if resposta.isnumeric() == False:
                print("Por favor insira um valor numérico dentro dos limites.")
                time.sleep(2)
                os.system('cls')
                break
            else:
                qty_compra = int(resposta)
                resposta = int(resposta)
                if qty_compra > 1:
                    print("Você não pode comprar mais de um kit grande.")
                    time.sleep(1)
                else:
                    if qty_compra+qty_inv_kit_grande > 2:
                        print("Você não pode carregar mais que um kit grande.")
                        time.sleep(1)
                    else:
                        if peso_inv - peso_kit_grande > 0:
                            print(f"Preço total da compra: {qty_compra * preco_kit_grande}")
                            resposta = input("Tem certeza que deseja continuar? [S/N] ")
                            if resposta == "s" or resposta == "S":
                                if qty_compra * preco_kit_grande > saldo:
                                    print("Saldo insuficiente.")
                                    time.sleep(1)
                                else:
                                    if qty_compra <= 0:
                                        print("Valor menor ou igual a zero.")
                                        time.sleep(1)
                                    else:
                                        saldo -= qty_compra * preco_kit_grande
                                        qty_inv_kit_grande += qty_compra
                                        print(f"Você comprou {qty_compra} x {preco_kit_grande} = {qty_compra * preco_kit_grande}")
                                        print(f"Saldo atual: {saldo}")
                                        time.sleep(2)
                                        os.system('cls')
                                        return saldo  # Retorna o saldo atualizado
                            else:
                                print("Operação cancelada.")
                                print("Saldo atual: ", saldo)
                                time.sleep(2)
                                os.system('cls')
                        else:
                            print(f"Você não possui espaço o suficiente no invantário (Analgésico = {peso_kit_grande}kg).")
                            time.sleep(2)
                            os.system('cls')
        elif resposta == 9:
            print("Voltando...")
            time.sleep(2)
            os.system('cls')
            interface_usuario()
            break

# Comprar armas
def loja_armas(saldo):
    fim_jogo()
    global resposta
    global peso_inv
    resposta = 0
    while resposta != 9:
        if tutorial == True and dia != 0:
            print("--------------------------------")
            print("Tutorial: As armas são utilizadas para proteção ou assaltos.")
            print("Tutorial: Os coletes aumentam sua vida.")
            print("Tutorial: As mochilas são utilizadas para aumentar o peso máximo no inventário.")
        print("--------------------------------")
        print(f"[1] - Comprar armas")
        print(f"[2] - Comprar coletes")
        print(f"[3] - Comprar mochilas")
        print(f"[9] - Voltar")
        resposta = input("O que deseja comprar? ")
        if resposta.isnumeric() == False:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        else:
            resposta = int(resposta)
        if resposta < 1 or resposta > 9:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
        elif dia == 0:
            print("Você não pode fazer isso no dia 0.")
        elif resposta == 1:
            while resposta != 9:
                global has_t1
                global has_t2
                global has_t3
                global has_t4
                global has_t5
                global hasb_t1, hasb_t2, hasb_t3, hasb_t4, hasb_t5
                os.system('cls')
                interface_usuario2()
                print("--------------------------------")
                print(f"[1] - has_t1 - ${preco_t1}")
                print(f"[2] - has_t2 - ${preco_t2}")
                print(f"[3] - has_t3 - ${preco_t3}")
                print(f"[4] - has_t4 - ${preco_t4}")
                print(f"[5] - has_t5 - ${preco_t5}")
                print(f"[9] - Voltar")
                resposta = input("O que deseja comprar? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 9:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_t1}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_t1 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_t1 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_t1 == False:
                                    saldo -= qty_compra * preco_t1
                                    peso_inv -= peso_t1 * qty_compra
                                    has_t1 = True
                                    hasb_t1 = 1
                                    print(f"Você comprou com sucesso uma has_t1 por {preco_t1}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 arma do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 2:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_t2}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_t2 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_t2 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_t2 == False:
                                    saldo -= qty_compra * preco_t2
                                    peso_inv -= peso_t2 * qty_compra
                                    has_t2 = True
                                    hasb_t2 = 1
                                    print(f"Você comprou com sucesso uma has_t2 por {preco_t2}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 arma do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 3:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_t3}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_t3 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_t3 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_t3 == False:
                                    saldo -= qty_compra * preco_t3
                                    peso_inv -= peso_t3 * qty_compra
                                    has_t3 = True
                                    hasb_t3 = 1
                                    print(f"Você comprou com sucesso uma has_t3 por {preco_t3}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 arma do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 4:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_t4}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_t4 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_t4 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_t4 == False:
                                    saldo -= qty_compra * preco_t4
                                    peso_inv -= peso_t4 * qty_compra
                                    has_t4 = True
                                    hasb_t4 = 1
                                    print(f"Você comprou com sucesso uma has_t4 por {preco_t4}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 arma do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 5:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_t5}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_t5 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_t5 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_t5 == False:
                                    saldo -= qty_compra * preco_t5
                                    peso_inv -= peso_t5 * qty_compra
                                    has_t5 = True
                                    hasb_t5 = 1
                                    print(f"Você comprou com sucesso uma has_t5 por {preco_t5}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 arma do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 9:
                    print("Voltando...")
                    time.sleep(2)
                    os.system('cls')
                    interface_usuario()
                    break

                """
                Copy adicionar arma > t222 > change all ocurrences 
                if resposta == 3:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_t222}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_t222 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_t222 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                saldo -= qty_compra * preco_t222
                                peso_inv -= peso_t222 * qty_compra
                                has_t222 = True
                                print(f"Você comprou com sucesso uma has_t222 por {preco_t222}.")
                                print(f"Saldo atual: {saldo}")
                                time.sleep(2)
                                os.system('cls')
                                return saldo # Retorna o saldo atualizado
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls') 
                """
        elif resposta == 2:
            while resposta != 9:
                global has_ct1
                global has_ct2
                global has_ct3
                global has_ct4
                global has_ct5
                global hasb_ct1, hasb_ct2, hasb_ct3, hasb_ct4, hasb_ct5
                global hp_ct1, hp_ct2, hp_ct3, hp_ct4, hp_ct5
                global vida, vida_max
                os.system('cls')
                interface_usuario2()
                print("--------------------------------")
                print(f"[1] - has_ct1 - ${preco_ct1}")
                print(f"[2] - has_ct2 - ${preco_ct2}")
                print(f"[3] - has_ct3 - ${preco_ct3}")
                print(f"[4] - has_ct4 - ${preco_ct4}")
                print(f"[5] - has_ct5 - ${preco_ct5}")
                print(f"[9] - Voltar")
                resposta = input("O que deseja comprar? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 9:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_ct1}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_ct1 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_ct1 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_ct1 == False:
                                    saldo -= qty_compra * preco_ct1
                                    peso_inv -= peso_ct1 * qty_compra
                                    has_ct1 = True
                                    hasb_ct1 = 1
                                    vida_max += hp_ct1
                                    vida += hp_ct1
                                    print(f"Você comprou com sucesso uma has_ct1 por {preco_ct1}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 2:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_ct2}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_ct2 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_ct2 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_ct2 == False:
                                    saldo -= qty_compra * preco_ct2
                                    peso_inv -= peso_ct2 * qty_compra
                                    has_ct2 = True
                                    hasb_ct2 = 1
                                    vida_max += hp_ct2
                                    vida += hp_ct2
                                    print(f"Você comprou com sucesso uma has_ct2 por {preco_ct2}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 3:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_ct3}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_ct3 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_ct3 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_ct3 == False:
                                    saldo -= qty_compra * preco_ct3
                                    peso_inv -= peso_ct3 * qty_compra
                                    has_ct3 = True
                                    hasb_ct3 = 1
                                    vida_max += hp_ct3
                                    vida += hp_ct3
                                    print(f"Você comprou com sucesso uma has_ct3 por {preco_ct3}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 4:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_ct4}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_ct4 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_ct4 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_ct4 == False:
                                    saldo -= qty_compra * preco_ct4
                                    peso_inv -= peso_ct4 * qty_compra
                                    has_ct4 = True
                                    hasb_ct4 = 1
                                    vida_max += hp_ct4
                                    vida += hp_ct4
                                    print(f"Você comprou com sucesso uma has_ct4 por {preco_ct4}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 5:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_ct5}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_ct5 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if qty_compra * peso_ct5 > peso_inv:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if has_t1 == False:
                                    saldo -= qty_compra * preco_ct5
                                    peso_inv -= peso_ct5 * qty_compra
                                    has_ct5 = True
                                    hasb_ct5 = 1
                                    vida_max += hp_ct5
                                    vida += hp_ct5
                                    print(f"Você comprou com sucesso uma has_ct5 por {preco_ct5}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 9:
                    print("Voltando...")
                    time.sleep(2)
                    os.system('cls')
                    interface_usuario()
                    break
        elif resposta == 3:
            while resposta != 9:
                global has_mt1
                global has_mt2
                global has_mt3
                global has_mt4
                global has_mt5
                global hasb_mt1, hasb_mt2, hasb_mt3, hasb_mt4, hasb_mt5
                global peso_mt1, peso_mt2, peso_mt3, peso_mt4, peso_mt5
                os.system('cls')
                interface_usuario2()
                print("--------------------------------")
                print(f"[1] - has_mt1 - ${preco_mt1}")
                print(f"[2] - has_mt2 - ${preco_mt2}")
                print(f"[3] - has_mt3 - ${preco_mt3}")
                print(f"[4] - has_mt4 - ${preco_mt4}")
                print(f"[5] - has_mt5 - ${preco_mt5}")
                print(f"[9] - Voltar")
                resposta = input("O que deseja comprar? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 9:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_mt1}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_mt1 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if var_controle == True:
                                print('oi')
                            else:
                                if var_controle == False:
                                    saldo -= qty_compra * preco_mt1
                                    has_mt1 = True
                                    hasb_mt1 += 1
                                    peso_inv += peso_mt1
                                    print(f"Você comprou com sucesso uma has_mt1 por {preco_mt1}.")
                                    print(f"Saldo atual: {saldo}")
                                    peso_inv = peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) # (peso_mt1 * hasb_mt1) - (peso_mt2 * hasb_mt2) - (peso_mt3 * hasb_mt3) - (peso_mt4 * hasb_mt4) - (peso_mt5 * hasb_mt5))
                                    peso_inv += ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 2:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_mt2}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_mt2 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if var_controle == True:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if var_controle == False:
                                    saldo -= qty_compra * preco_mt2
                                    peso_inv = peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) # (peso_mt1 * hasb_mt1) - (peso_mt2 * hasb_mt2) - (peso_mt3 * hasb_mt3) - (peso_mt4 * hasb_mt4) - (peso_mt5 * hasb_mt5))
                                    peso_inv += ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))
                                    has_mt2 = True
                                    hasb_mt2 += 1
                                    peso_inv += peso_mt2
                                    print(f"Você comprou com sucesso uma has_mt2 por {preco_mt2}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 3:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_mt3}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_mt3 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if var_controle == True:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if var_controle == False:
                                    saldo -= qty_compra * preco_mt3
                                    peso_inv = peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) # (peso_mt1 * hasb_mt1) - (peso_mt2 * hasb_mt2) - (peso_mt3 * hasb_mt3) - (peso_mt4 * hasb_mt4) - (peso_mt5 * hasb_mt5))
                                    peso_inv += ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))
                                    has_mt3 = True
                                    hasb_mt3 += 1
                                    peso_inv += peso_mt3
                                    print(f"Você comprou com sucesso uma has_mt3 por {preco_mt3}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 4:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_mt4}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_mt4 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if var_controle == True:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if var_controle == False:
                                    saldo -= qty_compra * preco_mt4
                                    peso_inv = peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) # (peso_mt1 * hasb_mt1) - (peso_mt2 * hasb_mt2) - (peso_mt3 * hasb_mt3) - (peso_mt4 * hasb_mt4) - (peso_mt5 * hasb_mt5))
                                    peso_inv += ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))
                                    has_mt4 = True
                                    hasb_mt4 += 1
                                    peso_inv += peso_mt4
                                    print(f"Você comprou com sucesso uma has_mt4 por {preco_mt4}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 5:
                    qty_compra = 1
                    print(f"Preço total da compra: {qty_compra * preco_mt5}")
                    resposta = input("Tem certeza que deseja continuar? [S/N] ")
                    if resposta == "s" or resposta == "S":
                        if qty_compra * preco_mt5 > saldo:
                            print("Saldo insuficiente.")
                            time.sleep(1)
                        else:
                            if var_controle == True:
                                print("Peso insuficiente.")
                                time.sleep(2)
                            else:
                                if var_controle == False:
                                    saldo -= qty_compra * preco_mt5
                                    has_mt5 = True
                                    hasb_mt5 += 1
                                    peso_inv += peso_mt5
                                    print(f"Você comprou com sucesso uma has_ct5 por {preco_mt5}.")
                                    print(f"Saldo atual: {saldo}")
                                    time.sleep(2)
                                    os.system('cls')
                                    return saldo # Retorna o saldo atualizado
                                else:
                                    print("Não é possível comprar mais de 1 colete do mesmo tipo.")
                                    time.sleep(2)
                    else:
                        print("Operação cancelada.")
                        print("Saldo atual: ", saldo)
                        time.sleep(2)
                        os.system('cls')

                elif resposta == 9:
                    print("Voltando...")
                    time.sleep(2)
                    os.system('cls')
                    interface_usuario()

        elif resposta == 9:
            print("Voltando...")
            time.sleep(2)
            os.system('cls')
            interface_usuario()

def inventario():
    fim_jogo()
    resposta = 0
    fim_jogo()
    global qty_inv_analgesico, qty_inv_atadura, qty_inv_Cogumelos, qty_inv_faixa, qty_inv_kit_grande, qty_inv_kit_pequeno, qty_inv_Maconha, qty_inv_Opium, qty_inv_Skank, qty_inv_Speed, peso_analgesico, peso_atadura, peso_Cogumelos, peso_ct1, peso_ct2, peso_ct3, peso_ct4, peso_ct5, peso_faixa, peso_inv, peso_kit_grande, peso_kit_pequeno, peso_Maconha, peso_mt2, peso_mt1, peso_mt3, peso_mt4, peso_mt5, peso_t1, peso_t2, peso_t3, peso_t4, peso_t5, peso_Opium, peso_Skank, peso_Speed
    while resposta != 9:
        if tutorial == True and dia != 0:
            print("--------------------------------")
            print("Tutorial: Esse é seu inventário, aqui você pode conferir suas drogas, medicamentos, armas, imóveis e negócios.")
        print("----------------------------------------")
        print("Seu inventário:")
        print("[1] - Ver drogas")
        print("[2] - Ver medicamentos")
        print("[3] - Ver armas")
        print("[4] - Ver imóveis")
        print("[5] - Ver negócios")
        print("[9] - Voltar")
        print("----------------------------------------")
        resposta = input("Para onde deseja ir? ")
        fim_jogo()
        if resposta.isnumeric() == False:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(2)
            os.system('cls')
            break
        else:
            resposta = int(resposta)
        if dia == 0 and resposta!= 9 and type(resposta) == int:
            print("Você está no dia 0 e não pode fazer isso!")
            print("Para jogar você precisa iniciar o primeiro dia.")
            print("Insira 9 para ir para o próximo dia e começar o jogo.")
            time.sleep(3)
            os.system('cls')
        elif resposta < 1 or resposta > 9:
            print("Por favor insira um valor numérico dentro dos limites.")
            time.sleep(1)
            os.system('cls')
            time.sleep(2)
        if resposta == 1:
            fim_jogo()
            os.system('cls')
            interface_usuario2()
            while resposta != 3:
                print("----------------------------------------")
                print("Suas drogas: ")
                print(f"Espaço total: {(peso_alterar + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))):.2f}")
                print(f"Espaço disponível: {peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5)):.2f}kg")
                print(f"Opium: {(qty_inv_Opium*peso_Opium):.2f}kg [{qty_inv_Opium}x{peso_Opium}kg]")
                print(f"Maconha: {(qty_inv_Maconha*peso_Maconha):.2f}kg [{qty_inv_Maconha}x{peso_Maconha}kg]")
                print(f"Speed: {(qty_inv_Speed*peso_Speed):.2f}kg [{qty_inv_Speed}x{peso_Speed}kg]")
                print(f"Skank: {(qty_inv_Skank*peso_Skank):.2f}kg [{qty_inv_Skank}x{peso_Skank}kg]")
                print(f"Cogumelos: {(qty_inv_Cogumelos*peso_Cogumelos):.2f}kg [{qty_inv_Cogumelos}x{peso_Cogumelos}kg]")
                print("----------------------------------------")
                print("[1] - Comprar")
                print("[2] - Vender")
                print("[3] - Voltar")
                print("----------------------------------------")
                resposta = input("O que deseja comprar? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 3:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    resposta = 0
                    qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos = compra_Opium(qty_mercado_Opium, saldo, qty_mercado_Maconha, qty_mercado_Speed, qty_mercado_Skank, qty_mercado_Cogumelos)  # Atualiza o saldo e a quantidade disponível no mercado
                elif resposta == 2:
                    resposta = 0
                    venda_Opium()
                elif resposta == 3:
                    break
        elif resposta == 2:
            fim_jogo()
            resposta = 0
            os.system('cls')
            interface_usuario2()
            while resposta != 2:
                print("--------------------------------")
                print("Seus medicamentos: ")
                print(f"Espaço total: {(peso_alterar + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))):.2f}")
                print(f"Espaço disponível: {peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5)):.2f}kg")
                print("Analgesicos: ", qty_inv_analgesico)
                print("Faixa: ", qty_inv_faixa)
                print("Atadura: ", qty_inv_atadura)
                print("Kit Pequeno: ", qty_inv_kit_pequeno)
                print("Kit Grande: ", qty_inv_kit_grande)
                print("--------------------------------")
                print("[1] - Usar medicamentos")
                print("[2] - Voltar")
                print("--------------------------------")
                resposta = input("O que deseja fazer? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 9:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    resposta = 0
                    while resposta != 9:
                        print("--------------------------------")
                        print("[1] - Analgésicos")
                        print("[2] - Faixa")
                        print("[3] - Atadura")
                        print("[4] - Kit Pequeno")
                        print("[5] - Kit Grande")
                        print("[9] - Voltar")
                        print("--------------------------------")
                        resposta = input("O que deseja usar? ")
                        if resposta.isnumeric() == False:
                            print("Por favor insira um valor numérico dentro dos limites.")
                            time.sleep(2)
                        else:
                            resposta = int(resposta)
                        if resposta < 1 or resposta > 9:
                            print("Por favor insira um valor numérico dentro dos limites.")
                            time.sleep(2)
                        elif vida == vida_max:
                            print("Sua vida já está no máximo, você não usou nada.")
                        else:
                            if resposta == 1:
                                if qty_inv_analgesico > 0 and cd_analgesico == False:
                                    qty_inv_analgesico -= 1
                                    if vida + hp_analgesico > vida_max:
                                        vida = vida_max
                                    else:
                                        vida += hp_analgesico
                                    print("Você utilizou com sucesso 1 analgésico.")
                                    time.sleep(1)
                                    cd_analgesico = True
                                else:
                                    print("Você não possui analgésicos para utilizar ou está em tempo de recarga.")
                                    time.sleep(2)
                            elif resposta == 2:
                                if qty_inv_faixa > 0 and cd_faixa == False:
                                    qty_inv_faixa -= 1
                                    if vida + hp_faixa > vida_max:
                                        vida = vida_max
                                    else:
                                        vida += hp_faixa
                                    print("Você utilizou com sucesso 1 faixa.")
                                    time.sleep(1)
                                    cd_faixa = True
                                else:
                                    print("Você não possui faixa para utilizar ou está em tempo de recarga.")
                                    time.sleep(2)
                            elif resposta == 3:
                                if qty_inv_atadura > 0 and cd_atadura == False:
                                    qty_inv_atadura -= 1
                                    if vida + hp_atadura > vida_max:
                                        vida = vida_max
                                    else:
                                        vida += hp_atadura
                                    print("Você utilizou com sucesso 1 atadura.")
                                    time.sleep(1)
                                    cd_atadura = True
                                else:
                                    print("Você não possui atadura para utilizar ou está em tempo de recarga.")
                                    time.sleep(2)
                            elif resposta == 4:
                                if qty_inv_kit_pequeno > 0 and cd_kit_pequeno == False:
                                    qty_inv_kit_pequeno -= 1
                                    if vida + hp_kit_pequeno > vida_max:
                                        vida = vida_max
                                    else:
                                        vida += hp_kit_pequeno
                                    print("Você utilizou com sucesso 1 kit pequeno.")
                                    time.sleep(1)
                                    cd_kit_pequeno = True
                                else:
                                    print("Você não possui kit pequeno para utilizar ou está em tempo de recarga.")
                                    time.sleep(2)
                            elif resposta == 5:
                                if qty_inv_kit_grande > 0 and cd_kit_grande == False:
                                    qty_inv_kit_grande -= 1
                                    if vida + hp_kit_grande > vida_max:
                                        vida = vida_max
                                    else:
                                        vida += hp_kit_grande
                                    print("Você utilizou com sucesso 1 kit grande.")
                                    cd_kit_grande = True
                                    time.sleep(1)
                                else:
                                    print("Você não possui kit grande para utilizar ou está em tempo de recarga.")
                                    time.sleep(2)

                            elif resposta == 9:
                                print("Voltando...")
                                time.sleep(2)
                                os.system('cls')
                                break
                    inventario()
                else:
                    break
            inventario()
        elif resposta == 3:
            fim_jogo()
            resposta = 0 
            while resposta != 9:
                resposta = 0
                os.system('cls')
                interface_usuario2()
                print("----------------------------------------")
                print("[1] - Armas")
                print("[2] - Coletes")
                print("[3] - Mochilas")
                print("[9] - Voltar")
                resposta = input("O que deseja fazer? ")
                if resposta.isnumeric() == False:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                else:
                    resposta = int(resposta)
                if resposta < 1 or resposta > 9:
                    print("Por favor insira um valor numérico dentro dos limites.")
                    time.sleep(2)
                elif dia == 0:
                    print("Você não pode fazer isso no dia 0.")
                elif resposta == 1:
                    while True:
                        resposta = 0
                        print("----------------------------------------")
                        print("Suas armas:")
                        print(f"Espaço total: {(peso_alterar + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))):.2f}")
                        print(f"Espaço disponível: {peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5)):.2f}kg")
                        if has_t1 == True:
                            print(f"T1: Possui | {peso_t1}kg.")
                        else:
                            print(f"T1: Não possui.")
                        if has_t2 == True:
                            print(f"T2: Possui | {peso_t2}kg.")
                        else:
                            print(f"T2: Não possui.")
                        if has_t3 == True:
                            print(f"T3: Possui | {peso_t3}kg.")
                        else:
                            print(f"T3: Não possui.")
                        if has_t4 == True:
                            print(f"T4: Possui | {peso_t4}kg.")
                        else:
                            print(f"T4: Não possui.")
                        if has_t5 == True:
                            print(f"T5: Possui | {peso_t5}kg.")
                        else:
                            print(f"T5: Não possui.")
                        print("----------------------------------------")
                        resposta = input("Pressione enter para voltar. ")
                        time.sleep(1)
                        break
                elif resposta == 2:
                    while True:
                        resposta = 0
                        print("----------------------------------------")
                        print("Seus coletes:")
                        print(f"Espaço total: {(peso_alterar + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))):.2f}")
                        print(f"Espaço disponível: {peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5)):.2f}kg")
                        if has_ct1 == True:
                            print(f"T1: Possui | {peso_ct1}kg.")
                        else:
                            print(f"T1: Não possui.")
                        if has_ct2 == True:
                            print(f"T2: Possui | {peso_ct2}kg.")
                        else:
                            print(f"T2: Não possui.")
                        if has_ct3 == True:
                            print(f"T3: Possui | {peso_ct3}kg.")
                        else:
                            print(f"T3: Não possui.")
                        if has_ct4 == True:
                            print(f"T4: Possui | {peso_ct4}kg.")
                        else:
                            print(f"T4: Não possui.")
                        if has_ct5 == True:
                            print(f"T5: Possui | {peso_ct5}kg.")
                        else:
                            print(f"T5: Não possui.")
                        print("----------------------------------------")
                        resposta = input("Pressione enter para voltar. ")
                        time.sleep(1)
                        break
                elif resposta == 3:
                    while True:
                        resposta = 0
                        print("----------------------------------------")
                        print("Suas mochilas:")
                        print(f"Espaço total: {(peso_alterar + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5))):.2f}")
                        print(f"Espaço disponível: {peso_alterar - ((peso_Opium * qty_inv_Opium) + (peso_Maconha * qty_inv_Maconha) + (peso_Speed * qty_inv_Speed) + (peso_Skank * qty_inv_Skank) + (peso_Cogumelos * qty_inv_Cogumelos) + (peso_analgesico * qty_inv_analgesico) + (peso_atadura * qty_inv_atadura) + (peso_faixa * qty_inv_faixa) + (peso_kit_pequeno * qty_inv_kit_pequeno) + (peso_kit_grande * qty_inv_kit_grande) + (peso_t1 * hasb_t1) + (peso_t2 * hasb_t2) + (peso_t3 * hasb_t3) + (peso_t4 * hasb_t4) + (peso_t5 * hasb_t5) + (peso_ct1 * hasb_ct1) + (peso_ct2 * hasb_ct2) + (peso_ct3 * hasb_ct3) + (peso_ct4 * hasb_ct4) + (peso_ct5 * hasb_ct5)) + ((peso_mt1 * hasb_mt1) + (peso_mt2 * hasb_mt2) + (peso_mt3 * hasb_mt3) + (peso_mt4 * hasb_mt4) + (peso_mt5 * hasb_mt5)):.2f}kg")
                        if has_mt1 == True:
                            print(f"T1: Possui | Fornece: {peso_mt1}kg.")
                        else:
                            print(f"T1: Não possui.")
                        if has_mt2 == True:
                            print(f"T2: Possui | Fornece: {peso_mt2}kg.")
                        else:
                            print(f"T2: Não possui.")
                        if has_mt3 == True:
                            print(f"T3: Possui | Fornece: {peso_mt3}kg.")
                        else:
                            print(f"T3: Não possui.")
                        if has_mt4 == True:
                            print(f"T4: Possui | Fornece: {peso_mt4}kg.")
                        else:
                            print(f"T4: Não possui.")
                        if has_mt5 == True:
                            print(f"T5: Possui | Fornece: {peso_mt5}kg.")
                        else:
                            print(f"T5: Não possui.")
                        print("----------------------------------------")
                        resposta = input("Pressione enter para voltar. ")
                        time.sleep(1)
                        break
        elif resposta == 9:
            print("Voltando...")
            time.sleep(1)
            break

def fim_jogo2():
    while True:
        if tutorial == True and dia != 0:
            print("--------------------------------")
            print("Tutorial: Esse é o fim do jogo!")
            print("Tutorial: Aqui você encontrará duas pontuações finais: pontuação final e pontuação final + inventário.")
            print("Tutorial: A pontuação final é seu saldo, menos a dívida com o agiota multiplicada por cinco, menos os pontos de vida perdidos multiplicados por 1000. ")
            print("Tutorial: A pontuação final + inventário leva em conta o preço dos itens que você possuia no inventário, como armas, coletes, drogas, imóveis, etc.")
            print("Tutorial: Na maioria dos menu utilizados no jogo, o valor 9 é utilizado para voltar ao menu anterior.")
        print("----------------------------------------")
        print("Fim do jogo!")
        print("----------------------------------------")
        print(f"Saldo: {saldo}")
        print(f"Saldo no banco: {saldo_banco}")
        print(f"Total de dinheiro no inventário: ${total_dinheiro_inv}")
        print(f"Débito total: ${debito_agiota}")
        if debito_agiota > 0:
            print("----------------------------------------")
            print("Como você não pagou o agiota, o valor final foi multiplicado por 5 e descontado da sua pontuação.")
            print(f"Débito final: ${debito_agiota * 5}")
        if vida != 100:
            print("----------------------------------------")
            print("Como sua vida está abaixo de 100, você perderá $1000 a cada 1 ponto de vida perdido.")
            print(f"Desconto por vida: ${(100 - vida)*1000}")
        print("----------------------------------------")
        print(f"Pontuação final: ${(saldo + saldo_banco - (debito_agiota * 5)) - ((100-vida)*1000)}")
        print(f"Pontuação final (+$ inventário): ${(saldo + saldo_banco + total_dinheiro_inv) - ((debito_agiota * 5) + ((100-vida)*1000)) }")
        print("----------------------------------------")
        resposta = input("Deseja ver seu inventário? [S/N]")
        if resposta == "S" or resposta == "s":
            print("----------------------------------------")
            print("Drogas no inventário: ")
            print(f"Opium: {qty_inv_Opium}")
            print(f"Maconha: {qty_inv_Maconha}")
            print(f"Speed: {qty_inv_Speed}")
            print(f"Skank: {qty_inv_Skank}")
            print(f"Cogumelos: {qty_inv_Cogumelos}")
            print("----------------------------------------")
            print("Armas no inventário: ")
            print(f"T1: {has_t1}")
            print(f"T2: {has_t2}")
            print(f"T3: {has_t3}")
            print(f"T4: {has_t4}")
            print(f"T5: {has_t5}")
            print("----------------------------------------")
            print("Coletes no inventário: ")
            print(f"T1: {has_ct1}")
            print(f"T2: {has_ct2}")
            print(f"T3: {has_ct3}")
            print(f"T4: {has_ct4}")
            print(f"T5: {has_ct5}")
            print("----------------------------------------")
            print("Mochilas no inventário: ")
            print(f"T1: {has_mt1}")
            print(f"T2: {has_mt2}")
            print(f"T3: {has_mt3}")
            print(f"T4: {has_mt4}")
            print(f"T5: {has_mt5}")
            print("----------------------------------------")
            resposta = input("Pressione enter para voltar.")
            os.system('cls')

def fim_jogo():
    if vida < 0 or dia > max_dias:
        total_dinheiro_inv = ( (hasb_t1*preco_t1) + (hasb_t2*preco_t2) + (hasb_t3*preco_t3) + (hasb_t4*preco_t4) + (hasb_t5*preco_t5) ) + ( (hasb_ct1*preco_ct1) + (hasb_ct2*preco_ct2) + (hasb_ct3*preco_ct3) + (hasb_ct4*preco_ct4) + (hasb_ct5*preco_ct5) ) + ( (hasb_mt1*preco_mt1) + (hasb_mt2*preco_mt2) + (hasb_mt3*preco_mt3) + (hasb_mt4*preco_mt4) + (hasb_mt5*preco_mt5) )
        total_dinheiro_inv += qty_inv_Opium * preco_Opium
        total_dinheiro_inv += qty_inv_Maconha * preco_Maconha
        total_dinheiro_inv += qty_inv_Speed * preco_Speed
        total_dinheiro_inv += qty_inv_Skank * preco_Skank
        total_dinheiro_inv += qty_inv_Cogumelos * preco_Cogumelos
        fim_jogo2()


#Fim do jogo + Pontuação
while dia < max_dias:
    os.system("cls")
    interface_usuario()
    if vida <= 0.00000000000000001:
        fim_jogo()
