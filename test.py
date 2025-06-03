from kurdish_python import *

nivîs("=" * 50)
nivîs("Python a Kurmancî")
nivîs("=" * 50)
nivîs("Hewalno çawa ni?")

# Fonksiyona Hejmarîyê
nivîs("\n--- Fonksiyona Hejmarîyê ---")
nivîs(f"24 karekê: {karekê(24)}")
nivîs(f"4.1 jêrîn: {jêrîn(4.1)}")
nivîs(f"2.4 jorîn: {jorîn(2.4)}")
nivîs(f"5^3: {hêz(5, 3)}")
nivîs(f"Pi: {pi}")
nivîs(f"E: {e}")
nivîs(f"|-7| = {nirxAbsolut(-7)}")
nivîs(f"3.7 girtik = {girtik(3.7)}")
nivîs(f"3.3 girtik = {girtik(3.3)}")
nivîs(f"Sin(pi/2): {hejmarî_alîkar.sin(hejmarî_alîkar.pi/2)}")
nivîs(f"Log(10): {hejmarî_alîkar.log(10)}")
nivîs(f"Karekê 25: {hejmarî_alîkar.karekê(25)}")
nivîs(f"Jêrîn 3.7: {hejmarî_alîkar.jêrîn(3.7)}")
nivîs(f"Jorîn 3.1: {hejmarî_alîkar.jorîn(3.1)}")
nivîs(f"XweşîLog(20): {hejmarî_alîkar.xweşiLog(20)}")
nivîs(f"Kos(pi): {hejmarî_alîkar.kos(hejmarî_alîkar.pi)}")
nivîs(f"Tan(pi/4): {hejmarî_alîkar.tan(hejmarî_alîkar.pi/4)}")

# Kom
nivîs("\n--- Kom ---")
nivîs("Kom [1,2,2,3]:", kom([1,2,2,3]))
nivîs("Kom 'çawa ni?':", kom("çawa ni?"))

# Lîste
nivîs("\n--- Lîste ---") 
liste_min = lîste([5, 2, 8, 1, 9])
nivîs("lîste: ", liste_min)
nivîs("Jimartin: ", jimartin([5, 2, 8]))
nivîs("Dirêjî: ", dirêjî(liste_min))
nivîs("lîsta rast: ", rêzker(liste_min))
nivîs("lîste xhar: ", lîste(vegerî(liste_min)))

# Lîste Alîkar
listek = [4, 2, 7]
nivîs("Serê xwe:", listek)
nivîs("Zêdekirin:", lîste_alîkar.zêdekirin(listek, 9))
nivîs("Dirêjkirin:", lîste_alîkar.dirêjKirin(listek, [1, 5]))
nivîs("Têxistin li indexê 1:", lîste_alîkar.têxistin(listek, 1, 99))
nivîs("Rakirin 2:", lîste_alîkar.rakirin(listek, 2))
derketî = lîste_alîkar.derxistin(listek)
nivîs("Derxistin (dawi):", derketî)
nivîs("Piştî derxistin:", listek)
nivîs("Pak kirin:", lîste_alîkar.pakKirin(listek))
listek1 = [3, 6, 1]
kopî = lîste_alîkar.kopîKirin(listek1)
nivîs("Kopiya listê:", kopî)
nivîs("Paşxistin:", lîste_alîkar.paşxistin(kopî))
nivîs("Rêzkirin:", lîste_alîkar.rêzkirin(kopî))
nivîs("Indexê 6:", lîste_alîkar.rêzik(kopî, 6))
nivîs(f"Mezin: {lîste_alîkar.mezin(liste_min)}")
nivîs(f"Piçûk: {lîste_alîkar.piçûk(liste_min)}")

# Rêzok Alîkar
nivîs("\n--- Rêzok ---")
rêzok = "salav ji te Ali"
nivîs("Herfan mezin:", rêzok_alîkar.mezin(rêzok))
nivîs("Herfan piçûk:", rêzok_alîkar.piçûk(rêzok))
nivîs("Sernav:", rêzok_alîkar.sernav(rêzok))
nivîs("Yekem herf mezin:", rêzok_alîkar.yekemaMezinHerf(rêzok))

nivîs("Guhertin (Ali → Rojhat):", rêzok_alîkar.guhertin(rêzok, "Ali", "Rojhat"))
nivîs("Parçe kirin:", rêzok_alîkar.parçeKirin(rêzok))
nivîs("Hevketin:", rêzok_alîkar.hevketin("-", ["slav", "ji", "te"]))

nivîs("Dest pê dike bi 'slav':", rêzok_alîkar.destPêKirin(jêkêşîn(rêzok), "slav"))
nivîs("Qedandine bi 'ji':", rêzok_alîkar.qedandin(jêkêşîn(rêzok), "ji"))
nivîs("Dîtina 'te':", rêzok_alîkar.dîtin(rêzok, "te"))

nivîs("Jêkêşîn:", f"[{rêzok_alîkar.jêkêşîn(rêzok)}]")
nivîs("Jêkêşîn çep:", f"[{rêzok_alîkar.jêkêşînÇep(rêzok)}]")
nivîs("Jêkêşîn rastê:", f"[{rêzok_alîkar.jêkêşînRastê(rêzok)}]")

# Regex Alîkar
nivîs("\n--- Regex Alîkar ---")
text = "Navê min Armanç e û ez di Amedê dijîm."
nivîs(regex_alîkar.lêgerîn("Armanç", text))
nivîs(regex_alîkar.gişDîtin(r"\b\w{5}\b", text))
nivîs(regex_alîkar.parçeKirin(r"\s", text))
nivîs(regex_alîkar.guhertin("Amedê", "Diyarbakir", text))
nivîs(regex_alîkar.topBikin("Navê", text))

# CSV Alîkar
nivîs("\n--- CSV Alîkar ---")
data = [
    ["Nav", "Temen", "Bajar"],
    ["Rojhat", "25", "Amed"],
    ["Zîn", "30", "Mêrdîn"]
]
csv_alîkar.nivîsanaCSV("veriler.csv", data)
nivîs("Pelê CSV hate nivîsandin!")

veriler = csv_alîkar.xwendinaCSV("veriler.csv")
for rêz in veriler:
    nivîs(hevketin(" | ", rêz))

# Ferheng
nivîs("\n--- Ferheng ---")
ferheng_min = ferheng({"nav": "Ahmad", "temen": 25, "şar": "Diyarbakır"})
nivîs("Ferheng: ", ferheng_min)
nivîs("Kilît: ", lîste(ferheng_alîkar.mifteyan(ferheng_min)))
nivîs("Nirxên: ", lîste(ferheng_alîkar.nirxên(ferheng_min)))

# Rastgehî Alîkar
nivîs("\n--- Rastgehî Alîkar ---")
nivîs(f"Rastgehî (0-1): {rastgehî_alîkar.rastgehî()}")
nivîs(f"Hejmarê Rastgehî (1-100): {rastgehî_alîkar.hejmarêRastgehî(1, 100)}")
lîste_rastgehî = lîste([1, 2, 3, 4, 5])
nivîs(f"Hilbijartin {lîste_rastgehî} -> {rastgehî_alîkar.hilbijartin(lîste_rastgehî)}")
nivîs("Hilbijartin:", rastgehî_alîkar.hilbijartin(lîste_rastgehî))
nivîs("Tevlî kirin:", rastgehî_alîkar.tevlîKirin(kopîKirin(lîste_rastgehî)))
nivîs("Nimûne:", rastgehî_alîkar.nimûne(lîste_rastgehî, 3))

# Têkoşîn/Xeta Handling
nivîs("\n--- Têkoşîn û Xeta Girtin ---")

def xetaLîBike():
    return 10 / 0

netice, xeta = têkoşîn(xetaLîBike)
if xeta:
    nivîs(f"Xeta hat girtin: {xeta}")
else:
    nivîs(f"Netice: {netice}")


nivîs("*"*50),
x = 10
y = 5

eger(
    mezintir(x, y), 
     lambda: nivîs("x mezin e"), 
     lambda: nivîs("x mezin nîne"),
     )

nivîs(f"Hemû rast in? {hemû(True, True, True)}")       # True
nivîs(f"Hinek rast in? {hinekjî(False, True, False)}") # True
nivîs(f"'a' nav 'abc'de ye? {nav('a', 'abc')}")           # True
nivîs(f"'z' nahewîne 'abc'de ye? {nahewîne('z', 'abc')}") # True
for index, item in rêzandin(["zer", "spî", "reş"]):
    nivîs(f"{index}: {item}")
navn = ["Ali", "Veli"]
temen = [23, 34]
for nav, t in girêdan(navn, temen):
    nivîs(f"{nav} - {t} salî")
rêz = [1, 2, 3, 4]

# her yê ducar bikin
result = list(xerîtekirin(lambda x: x * 2, rêz))
nivîs(f"2x: {result}")

# tenê yên ku ji 2 mezin in
filtered = list(parzûn(lambda x: mezintir(x, 2), rêz))
nivîs(f">2: {filtered}")
ciwan = [1, 2, 3, 4]
cem = kêmkirin(lambda x, y: x + y, ciwan)
nivîs(f"Kom: {cem}")
