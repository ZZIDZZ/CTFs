from Crypto.Util.number import long_to_bytes, bytes_to_long, GCD, getPrime, isPrime

def nextPrime(prime):
    if isPrime(prime):
        return prime
    else:
        return nextPrime(prime+1)




primes = [2822637605335640168948453689, 621031330492050523448709463, 68591325640662633521085799, 27235435252936086045324877, 1046827780659574653190811, 2827284264406615278140899, 983130318051001095366163, 276605575392575538677717, 7056425513524146322679, 335329231052772772727, 4606579003333269820243, 1025638279567545039811, 50835016989181692187, 60841287451007424323, 485731221401402993, 717998288941160551, 6366831362026956353320338406831804137016295564701287500398906588168531606205409992030871221038687312905611170844270814947407148127555721286436763532356187]

n = 991780332070847898144930172913707154337428968947289369950557418182205916671610439120415358846651351930506089582472303042933616371165128107548726642508866988284488166396083880240510413080431759514941229838260223120292397812794508537379728621988207944460296809293569542376203

while True: 
    p = getPrime(128)
    q = nextPrime(7*p)
    r = nextPrime(p*q)
    s = nextPrime(q*r)
    nb = p*q*r*s
    print(GCD(nb, n))