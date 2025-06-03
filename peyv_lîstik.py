from kurdish_python import *

class PeyvLîstik:
    def __init__(self):
        self.peyv = ferheng({
            "mal": "ev",
            "kîç": "kız", 
            "kurê": "oğul",
            "bav": "baba",
            "dayik": "anne",
            "birêz": "pirinç",
            "nan": "ekmek",
            "av": "su",
            "agir": "ateş",
            "êvar": "akşam",
            "sibe": "sabah",
            "rojbûn": "gündüz",
            "şev": "gece",
            "stêr": "yıldız",
            "heyv": "ay",
            "rojê": "güneş",
            "bahoz": "rüzgar",
            "baranê": "yağmur",
            "berf": "kar",
            "gul": "çiçek",
            "dar": "ağaç",
            "çiya": "dağ",
            "çem": "nehir",
            "deryê": "deniz",
            "kitêb": "kitap",
            "pirtûk": "kitap",
            "qelem": "kalem",
            "mêze": "masa",
            "kursî": "sandalye",
            "reng": "renk",
            "sor": "kırmızı",
            "kesk": "yeşil",
            "şîn": "mavi",
            "zer": "sarı",
            "reş": "siyah",
            "spî": "beyaz"
        })
        
        self.xal = 0  # puan
        self.bersivên_rast = 0  # doğru cevaplar
        self.giştî_pirs = 0  # toplam sorular
        
    def lîstikê_nû(self):
        nivîs("=" * 50)
        nivîs("🎮 LÎSTIKA PEYVAN - کەڵێنەی وشەکان 🎮")
        nivîs("=" * 50)
        nivîs("Wateya peyvên kurdî bi tirkî bibêje!")
        nivîs("Ji bo derketin 'der' binivîse.\n")
        
        while rastî:
            # Peyvek bi tesadûfî hilbijêre
            peyva_kurdî = hilbijartin(lîste(self.peyv.keys()))
            peyva_tirkî = self.peyv[peyva_kurdî]
            
            # Pirsê bike
            nivîs(f"📝 Pirs {self.giştî_pirs + 1}")
            nivîs(f"Peyva '{peyva_kurdî}' bi tirkî çi ye?")
            
            bersiv = bixwîne("Bersiva te: ").strip().lower()
            
            # Kontrola derketinê
            if bersiv == "der":
                self.dawiya_lîstikê()
                break
                
            # Kontrola bersivê
            if bersiv == peyva_tirkî.lower():
                nivîs("✅ Rast e! +10 xal")
                self.xal += 10
                self.bersivên_rast += 1
            else:
                nivîs(f"❌ Şaş e! Bersiva rast: {peyva_tirkî}")
                
            self.giştî_pirs += 1
            
            # Rewşa niha nîşan bide
            nivîs(f"💰 Xal: {self.xal}")
            nivîs(f"📊 Rast: {self.bersivên_rast}/{self.giştî_pirs}")
            nivîs("-" * 30)
            
            # Dixwaze bidomîne?
            berdewam = bixwîne("Ji bo berdewamiyê Enter bike ('der' ji bo derketin): ")
            if berdewam.lower() == "der":
                self.dawiya_lîstikê()
                break
                
    def dawiya_lîstikê(self):
        nivîs("\n" + "=" * 50)
        nivîs("🎯 LÎSTIK QEDIYA!")
        nivîs("=" * 50)
        
        if self.giştî_pirs > 0:
            rêjeya_serkeftinê = girtik((self.bersivên_rast / self.giştî_pirs) * 100, 1)
            
            nivîs(f"📊 Encamên te:")
            nivîs(f"   • Giştî Pirs: {self.giştî_pirs}")
            nivîs(f"   • Bersivên Rast: {self.bersivên_rast}")
            nivîs(f"   • Bersivên Şaş: {self.giştî_pirs - self.bersivên_rast}")
            nivîs(f"   • Rêjeya Serkeftinê: %{rêjeya_serkeftinê}")
            nivîs(f"   • Giştî Xal: {self.xal}")
            
            # Nirxandina serkeftinê
            if rêjeya_serkeftinê >= 80:
                nivîs("🏆 Pir baş! Zanîniya te ya kurdî gelek xweş e!")
            elif rêjeya_serkeftinê >= 60:
                nivîs("👍 Baş e! Berdewam bike!")
            elif rêjeya_serkeftinê >= 40:
                nivîs("📚 Ne xerab e! Hinekî din dixebite!")
            else:
                nivîs("💪 Destpêka baş e! Bi pratîkê baştir dibî!")
        else:
            nivîs("Tu pirs nehat bersivdan.")
            
        nivîs("\nSpas! Bi xatirê te! 🙏")

def menuya_sereke():
    while rastî:
        nivîs("\n" + "🌟" * 20)
        nivîs("LÎSTIKA PEYVAN KURDÎ")
        nivîs("🌟" * 20)
        nivîs("1️⃣  Lîstikê Nû Dest Pê bike")
        nivîs("2️⃣  Lîsteya Peyvan Nîşan bide") 
        nivîs("3️⃣  Derkeve")
        
        hilbijardin = bixwîne("\nHilbijardina xwe bike (1-3): ").strip()
        
        if hilbijardin == "1":
            lîstik = PeyvLîstik()
            lîstik.lîstikê_nû()
        elif hilbijardin == "2":
            lîsteya_peyvan_nîşan_bide()
        elif hilbijardin == "3":
            nivîs("Bi xatirê te! Heta careke din! 👋")
            break
        else:
            nivîs("❌ Hilbijardineke şaş! Ji kerema xwe 1, 2 an 3 hilbijêre.")

def lîsteya_peyvan_nîşan_bide():
    peyv = ferheng({
        "mal": "ev", "kîç": "kız", "kurê": "oğul", "bav": "baba", "dayik": "anne",
        "birêz": "pirinç", "nan": "ekmek", "av": "su", "agir": "ateş", "êvar": "akşam",
        "sibe": "sabah", "rojbûn": "gündüz", "şev": "gece", "stêr": "yıldız", "heyv": "ay",
        "rojê": "güneş", "bahoz": "rüzgar", "baranê": "yağmur", "berf": "kar", "gul": "çiçek",
        "dar": "ağaç", "çiya": "dağ", "çem": "nehir", "deryê": "deniz", "kitêb": "kitap",
        "pirtûk": "kitap", "qelem": "kalem", "mêze": "masa", "kursî": "sandalye",
        "reng": "renk", "sor": "kırmızı", "kesk": "yeşil", "şîn": "mavi", 
        "zer": "sarı", "reş": "siyah", "spî": "beyaz"
    })
    
    nivîs("\n📚 LÎSTEYA PEYVAN")
    nivîs("=" * 40)
    nivîs("KURDÎ          →    TIRKÎ")
    nivîs("-" * 40)
    
    for kurdî, tirkî in peyv.items():
        nivîs(f"{kurdî:15} → {tirkî}")
    
    bixwîne("\nJi bo berdewamiyê Enter bike...")

def serhêl():
    """Serhêl = Başlık"""
    nivîs("🌟" * 60)
    nivîs("           بەخێر هاتن - Bi xêr hatin")
    nivîs("        LÎSTIKA PEYVAN - وشە یارییەکە")  
    nivîs("🌟" * 60)
    nivîs("Ev lîstikek e ku tu yê peyvên kurdî fêr bibî!")
    nivîs("Bu oyunda Kürtçe kelimeleri öğreneceksin!")
    nivîs("")

# Lîstikê dest pê bike
if __name__ == "__main__":
    try:
        serhêl()
        menuya_sereke()
    except KeyboardInterrupt:
        nivîs("\n\n👋 Lîstik hate girtin. Bi xatirê te!")
    except Exception as xeta:
        nivîs(f"❌ Xetayek derket: {xeta}")