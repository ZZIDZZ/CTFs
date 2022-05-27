import sys
try:
	import gmpy2
except ImportError:
	print("Install gmpy2 first to run this program")
	sys.exit()

n = 22137488924207093504183186376443859354835785288991574895837282856676380333738904817378987602944695031790398977517963663188182768618582293974130000616654073692880016626337212611367911355027582654703844826924570146595499912979842088796649142154729705099839663641410978509728139288489186370983295576433616915932105195836048439384445932510770489960550942000762850153890730931519963897130306064982573466415891762853633985789258880867626664885905269371598527645106795355720311075334667739668502166294845275812517045520286298640555830704003935106536119129047997911190041677443831537446579531149960766948750034327251653223877
n = hex(n)
e = 3
cipher = 26480272848384180570411447917437668635135597564435407928130220812155801611065536704781892656033726277516148813916446180796750368332515779970289682282804676030149428215146347671350240386440440048832713595112882403831539777582778645411270433913301224819057222081543727263602678819745693540865806160910293144052079393615890645460901858988883318691997438568705602949652125 
import gmpy2
 
#f = open('cipher','rb')
#cipher = int(f.read().encode('hex'),16)
with gmpy2.local_context(gmpy2.context(), precision=800) as ctx:
 ctx.precision += 800
 root = gmpy2.cbrt(cipher)

try:
	print(int(root))
except AttributeError:
	print(bytes.fromhex(str('%x' % + int(root))).decode('utf-8'))