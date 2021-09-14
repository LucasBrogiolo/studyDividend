import sys
import yfinance as yf

def tick(stock):
    if stock == "exit":
        return sys.exit()
    else:
        stockIn = stock + ".sa"
        acao = yf.Ticker(stockIn)
        print(f"\n** THE DIVIDEND YELD OFF {stockIn.upper()} IS: {acao.info['dividendYield']}**\n")

def head():
    print("****************************************************")
    print("\n**** DIVIDEND YELD OF BRAZILIAN STOCKS ****")
    print("to exit type: \'exit\'")

def error():
    print("\n!!!ERROR!!!\nInsert a valid stock: (XXXX3 ou XXXX4)")

while True:
    head()
    stock = input("\nWich stock do you want to receive de DY?\nInsira o ticker aqui: \n")
    try:
        tick(stock)
    except:
        error()
