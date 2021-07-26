import sys
import yfinance as yf

def tick(stock):
    if stock == "exit":
        return sys.exit()
    else:
        stockIn = stock + ".sa"
        acao = yf.Ticker(stockIn)
        print(f"\n** O DIVIDEND YELD DE {stockIn.upper()} é: {acao.info['dividendYield']}**\n")

def head():
    print("****************************************************")
    print("\n**** RETORNO DE DIVIDEND YELD DE TICKERS DA B3 ****")
    print("Para sair digite \'exit\'")

def error():
    print("\n!!!ERRO!!!\nDigite um código válido: (XXXX3 ou XXXX4)")

while True:
    head()
    stock = input("\nqual ticker voce deseja saber os dividendos?\nInsira o ticker aqui: \n")
    try:
        tick(stock)
    except:
        error()
