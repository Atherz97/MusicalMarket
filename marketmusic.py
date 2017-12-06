from bittrex import Bittrex
import os, sys, time
import simpleaudio as sa
api = Bittrex(None, None)

class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# fetch markets
print("fetching markets...")
markets = api.get_markets()
print(" - done")

# read config
print("reading config...")
c = open("marketmusic.conf","r").readlines()
currency = []
for i in range(0,5):
    t = c[i].replace("\n","")
    currency.append(t)
    print(" - currency added: "+t)
print(" - done")

# get current market values
i = 1
s = ""
print("\nchoose a coin:")
for coinpair in currency:
    currentTick = api.get_ticker(coinpair)["result"]
    c = colors.ENDC
    unit = "BTC"
    if coinpair == "BTC-DASH":
        c = colors.BLUE
    if coinpair == "USDT-BTC":
        c = colors.YELLOW
        unit = "USD"
    if coinpair == "BTC-BCC":
        c = colors.GREEN
    if coinpair == "BTC-LTC":
        c = colors.BOLD
    print(s + c + str(i) + ". " + coinpair + " (" + str(currentTick["Last"]) + " " + unit + ") " + colors.ENDC)
    i = i + 1

choice = int(input("(input 1-5)"))-1

currentCoin = currency[choice]
lastPrice = 0

# coin sound loop -- play appropriate sound whenever order made
while 1 == 1:
    price = int(float(api.get_ticker(currentCoin)["result"]["Last"]*100000000))
    
    # analyze sound
    diff = price - lastPrice
    
    files = ["G.wav","Gs.wav","A.wav","As.wav","B.wav","c.wav","cs.wav","d.wav","ds.wav","e.wav","f.wav","fs.wav","g.wav","gs.wav","a.wav","as.wav","b.wav","cc.wav","ccs.wav","dd.wav","dds.wav","ee.wav","ff.wav","ffs.wav"]  
    i = price % len(files) 
    sound = sa.WaveObject.from_wave_file(files[i])

    if (diff != 0):
        sound.play()
        c = colors.RED
        if diff > 0:
            c = colors.GREEN
        print(c + str(price) + colors.ENDC)

    lastPrice = price
    time.sleep(0.2)
