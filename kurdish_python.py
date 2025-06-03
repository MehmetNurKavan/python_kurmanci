import math
import random
import datetime
import os
import json
import re
import threading
import time
from pathlib import Path
import csv
import sys
from functools import reduce as _reduce

def nivîs(*args, **kwargs):
    return print(*args, **kwargs)
def bixwîne(prompt=""):
    return input(prompt)
def dirêjî(obj):
    return len(obj)
def rêzek(*args):
    return range(*args)
def jimartin(iterable):
    return sum(iterable)
def mezin(iterable):
    return max(iterable)
def piçûk(iterable):
    return min(iterable)
def nirxAbsolut(x):
    return abs(x)
def girtik(number, ndigits=None):
    return round(number, ndigits)
def hêz(base, exp):
    return pow(base, exp)
def rêzker(iterable, key=None, reverse=False):
    return sorted(iterable, key=key, reverse=reverse)
def vegerî(seq):
    return reversed(seq)
def celeb(obj):
    return type(obj)
def rast(obj):
    return bool(obj)
def hejmar(obj):
    return int(obj)
def hejmarKoma(obj):
    return float(obj)
def rêzok(obj):
    return str(obj)
def lîste(obj=None):
    return list() if obj is None else list(obj)
def duplet(obj=None):
    return tuple() if obj is None else tuple(obj)
def kom(obj=None):
    return set() if obj is None else set(obj)
def ferheng(obj=None):
    return dict() if obj is None else dict(obj)
def jimartinHerêmê(value, iterable):
    if hasattr(iterable, 'count'):
        return iterable.count(value)
    return sum(1 for x in iterable if x == value)
def heryek(iterable):
    return all(iterable)
def hinji(iterable):
    return any(iterable)
def rêzik(start, stop=None, step=1):
    if stop is None:
        return enumerate(start)
    return enumerate(start, stop)
def zipKirin(*iterables):
    return zip(*iterables)

def parzûn(function, iterable):
    return map(function, iterable)

def parçeKirin(s, sep=None):
    return s.split(sep)

def berak(value=None):
    return value

# Yeni eklenen kavramlar
def veger(value):
    """Kürtçe 'return' karşılığı"""
    return value

def şkestin():
    """Kürtçe 'break' karşılığı - döngüyü kır"""
    pass  # Bu özel kullanım gerektiriyor

def derbas():
    """Kürtçe 'continue' karşılığı - geç"""
    pass  # Bu özel kullanım gerektiriyor

def derxistin():
    """Kürtçe 'pass' karşılığı"""
    pass

def têkilî():
    """Kürtçe 'assert' karşılığı"""
    pass

def del_kirin(obj):
    """Kürtçe 'del' karşılığı"""
    del obj

def global_gişti(var_name):
    """Kürtçe 'global' karşılığı"""
    return globals()[var_name]

def local_herêmî(var_name):
    """Kürtçe 'local' karşılığı"""
    return locals().get(var_name)

def import_kirin(module_name):
    """Kürtçe 'import' karşılığı"""
    return __import__(module_name)

def from_ji_import(module_name, item_name):
    """Kürtçe 'from ... import' karşılığı"""
    module = __import__(module_name, fromlist=[item_name])
    return getattr(module, item_name)

rastî = True
çalak = False
vala = None

# Xeta (Exception) handling için yeni kavramlar
def têkoşîn(func, *args, **kwargs):
    """Kürtçe 'try' karşılığı - tê koşîn (deneme yapmak)"""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return None, e

def girtinXeta(func, xeta_cure, xeta_func=None):
    """Kürtçe 'except' karşılığı - xeta girtin"""
    try:
        return func()
    except xeta_cure as e:
        if xeta_func:
            return xeta_func(e)
        return e

def dawî(func):
    """Kürtçe 'finally' karşılığı"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        finally:
            pass
    return wrapper

def xetaAvêtin(xeta, mesaj=""):
    """Kürtçe 'raise' karşılığı"""
    raise xeta(mesaj)

class RêzokAlîkar:
    @staticmethod
    def mezin(s):
        return s.upper()
    @staticmethod
    def piçûk(s):
        return s.lower()
    @staticmethod
    def sernav(s):
        return s.title()
    @staticmethod
    def yekemaMezinHerf(s):
        return s.capitalize()
    @staticmethod
    def guhertin(s, old, new):
        return s.replace(old, new)
    @staticmethod
    def parçeKirin(s, sep=None):
        return s.split(sep)
    @staticmethod
    def hevketin(sep, iterable):
        return sep.join(iterable)
    @staticmethod
    def destPêKirin(s, prefix):
        return s.startswith(prefix)
    @staticmethod
    def qedandin(s, suffix):
        return s.endswith(suffix)
    @staticmethod
    def dîtin(s, sub):
        return s.find(sub)
    @staticmethod
    def jêkêşîn(s):
        return s.strip()
    @staticmethod
    def jêkêşînÇep(s):
        return s.lstrip()
    @staticmethod
    def jêkêşînRastê(s):
        return s.rstrip()

class LîsteAlîkar:
    @staticmethod
    def zêdekirin(lst, item):
        lst.append(item)
        return lst
    @staticmethod
    def dirêjKirin(lst, iterable):
        lst.extend(iterable)
        return lst
    @staticmethod
    def têxistin(lst, index, item):
        lst.insert(index, item)
        return lst
    @staticmethod
    def rakirin(lst, item):
        lst.remove(item)
        return lst
    @staticmethod
    def derxistin(lst, index=-1):
        return lst.pop(index)
    @staticmethod
    def pakKirin(lst):
        lst.clear()
        return lst
    @staticmethod
    def kopîKirin(lst):
        return lst.copy()
    @staticmethod
    def paşxistin(lst):
        lst.reverse()
        return lst
    @staticmethod
    def rêzkirin(lst, key=None, reverse=False):
        lst.sort(key=key, reverse=reverse)
        return lst
    @staticmethod
    def rêzik(lst, value):
        return lst.index(value)
    @staticmethod
    def mezin(lîste):
        return max(lîste)
    @staticmethod
    def piçûk(lîste):
        return min(lîste)

class KomAlîkar:
    @staticmethod
    def zêdekirin(s, item):
        s.add(item)
        return s
    @staticmethod
    def rakirin(s, item):
        s.remove(item)
        return s
    @staticmethod
    def rakêşin(s, item):
        s.discard(item)
        return s
    @staticmethod
    def yekbûnê(s1, s2):
        return s1.union(s2)
    @staticmethod
    def hevparî(s1, s2):
        return s1.intersection(s2)
    @staticmethod
    def taybetî(s1, s2):
        return s1.difference(s2)
    @staticmethod
    def cudayîyaHemûyan(s1, s2):
        return s1.symmetric_difference(s2)
    @staticmethod
    def komêjêrîn(s1, s2):
        return s1.issubset(s2)
    @staticmethod
    def komêjorîn(s1, s2):
        return s1.issuperset(s2)
    @staticmethod
    def têkili(s1, s2):
        return s1.isdisjoint(s2)

class FerhengAlîkar:
    @staticmethod
    def mifteyan(d):
        return d.keys()
    @staticmethod
    def nirxên(d):
        return d.values()
    @staticmethod
    def tiştên(d):
        return d.items()
    @staticmethod
    def wergirtin(d, key, default=None):
        return d.get(key, default)
    @staticmethod
    def derxistin(d, key, default=None):
        return d.pop(key, default)
    @staticmethod
    def derxistinaTiştê(d):
        return d.popitem()
    @staticmethod
    def nûBike(d, other):
        d.update(other)
        return d
    @staticmethod
    def pakKirin(d):
        d.clear()
        return d
    @staticmethod
    def kopîKirin(d):
        return d.copy()
    @staticmethod
    def xwerû(d, key, default):
        return d.setdefault(key, default)

class HejmarîAlîkar:
    @staticmethod
    def karekê(x):
        return math.sqrt(x)
    @staticmethod
    def jêrîn(x):
        return math.floor(x)
    @staticmethod
    def jorîn(x):
        return math.ceil(x)
    @staticmethod
    def log(x, base=math.e):
        return math.log(x, base)
    @staticmethod
    def xweşiLog(x):
        return math.log(x)
    @staticmethod
    def sin(x):
        return math.sin(x)
    @staticmethod
    def kos(x):
        return math.cos(x)
    @staticmethod
    def tan(x):
        return math.tan(x)
    pi = math.pi
    e = math.e

class RastgehîAlîkar:
    @staticmethod
    def rastgehî():
        return random.random()
    @staticmethod
    def hejmarêRastgehî(a, b):
        return random.randint(a, b)
    @staticmethod
    def hilbijartin(sequence):
        return random.choice(sequence)
    @staticmethod
    def tevlîKirin(lst):
        random.shuffle(lst)
        return lst
    @staticmethod
    def nimûne(population, k):
        return random.sample(population, k)

class DemZemanAlîkar:
    @staticmethod
    def niha():
        return datetime.datetime.now()
    @staticmethod
    def îro():
        return datetime.date.today()
    @staticmethod
    def formaDemê(dt, format_str):
        return dt.strftime(format_str)
    @staticmethod
    def xwendinaDemê(date_string, format_str):
        return datetime.datetime.strptime(date_string, format_str)
    @staticmethod
    def dîrok(year, month, day):
        return datetime.date(year, month, day)
    @staticmethod
    def dem(hour=0, minute=0, second=0):
        return datetime.time(hour, minute, second)
    @staticmethod
    def nîşanaDemê(dt=None):
        if dt is None:
            dt = datetime.datetime.now()
        return dt.timestamp()

class PelAlîkar:
    @staticmethod
    def vekirin(filename, mode='r', encoding='utf-8'):
        return open(filename, mode, encoding=encoding)
    @staticmethod
    def heye(rê):
        return os.path.exists(rê)
    @staticmethod
    def pelE(rê):
        return os.path.isfile(rê)
    @staticmethod
    def peldankE(rê):
        return os.path.isdir(rê)
    @staticmethod
    def rakirin(rê):
        return os.remove(rê)
    @staticmethod
    def peldankêRakirin(rê):
        return os.rmdir(rê)
    @staticmethod
    def peldankêÇêkirin(rê):
        return os.mkdir(rê)
    @staticmethod
    def navguhertin(old_path, new_path):
        return os.rename(old_path, new_path)
    @staticmethod
    def rêyaKarêWergirtin():
        return os.getcwd()
    @staticmethod
    def guherînaPeldankê(rê):
        return os.chdir(rê)
    @staticmethod
    def lîsteyaPeldankê(rê='.'):
        return os.listdir(rê)
    @staticmethod
    def rê(*args):
        return os.path.join(*args)

class JsonAlîkar:
    @staticmethod
    def barkirin(fp):
        return json.load(fp)
    @staticmethod
    def barkirinaMetnê(s):
        return json.loads(s)
    @staticmethod
    def derxistin(obj, fp):
        return json.dump(obj, fp, ensure_ascii=False, indent=2)
    @staticmethod
    def derxistinaMetnê(obj):
        return json.dumps(obj, ensure_ascii=False, indent=2)

class RêzokKarAlîkar:
    @staticmethod
    def rêzokêKarê(target, args=()):
        return threading.Thread(target=target, args=args)
    @staticmethod
    def destPêKirin(thread):
        thread.start()
        return thread
    @staticmethod
    def hevketin(thread):
        thread.join()
        return thread
    @staticmethod
    def kilit():
        return threading.Lock()
    @staticmethod
    def bûyer():
        return threading.Event()
    @staticmethod
    def semafor(value=1):
        return threading.Semaphore(value)

class DemAlîkar:
    @staticmethod
    def xew(seconds):
        return time.sleep(seconds)
    @staticmethod
    def dem():
        return time.time()

class CsvAlîkar:
    @staticmethod
    def xwendinaCSV(filename, delimiter=',', encoding='utf-8'):
        rows = []
        with open(filename, 'r', encoding=encoding, newline='') as file:
            reader = csv.reader(file, delimiter=delimiter)
            for row in reader:
                rows.append(row)
        return rows
    @staticmethod
    def nivîsanaCSV(filename, data, delimiter=',', encoding='utf-8'):
        with open(filename, 'w', encoding=encoding, newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerows(data)

class RegexAlîkar:
    @staticmethod
    def lêgerîn(pattern, string):
        return re.search(pattern, string)
    @staticmethod
    def gişDîtin(pattern, string):
        return re.findall(pattern, string)
    @staticmethod
    def parçeKirin(pattern, string):
        return re.split(pattern, string)
    @staticmethod
    def guhertin(pattern, repl, string):
        return re.sub(pattern, repl, string)
    @staticmethod
    def topBikin(pattern, string):
        return re.match(pattern, string)

xeta = Exception
xetaNirxê = ValueError
xetaCureyê = TypeError
xetaKilîtê = KeyError
xetaIndexê = IndexError
xetaPelêNehatDîtin = FileNotFoundError
xetaDestûrê = PermissionError

rêzok_alîkar = RêzokAlîkar()
lîste_alîkar = LîsteAlîkar()
kom_alîkar = KomAlîkar()
ferheng_alîkar = FerhengAlîkar()
hejmarî_alîkar = HejmarîAlîkar()
rastgehî_alîkar = RastgehîAlîkar()
demzeman_alîkar = DemZemanAlîkar()
pel_alîkar = PelAlîkar()
json_alîkar = JsonAlîkar()
rêzokkar_alîkar = RêzokKarAlîkar()
dem_alîkar = DemAlîkar()
csv_alîkar = CsvAlîkar()
regex_alîkar = RegexAlîkar()

def xew(seconds): 
    return time.sleep(seconds)
def dem():
    return time.time()
def jêkêşîn(s):
    return s.strip()
def parçeKirin(s, sep=None):
    return s.split(sep)
def hevketin(sep, iterable):
    return sep.join(iterable)
def guhertin(s, old, new):
    return s.replace(old, new)
def dîtin(s, sub):
    return s.find(sub)
def perDestPêKirin(s, prefix):
    return s.startswith(prefix)
def biQediya(s, suffix):
    return s.endswith(suffix)
def mezin(s):
    return s.upper()
def piçûk(s):
    return s.lower()
def sernav(s):
    return s.title()
def kopîKirin(obj):
    if hasattr(obj, 'copy'):
        return obj.copy()
    else:
        import copy
        return copy.copy(obj)
def pakKirin(obj):
    if hasattr(obj, 'clear'):
        obj.clear()
    return obj

karekê = math.sqrt
jêrîn = math.floor
jorîn = math.ceil
log = math.log
xweşilog = math.log
sin = math.sin
kos = math.cos
tan = math.tan
pi = math.pi
e = math.e
rastgehî = random.random
hejmarêRastgehî = random.randint
hilbijartin = random.choice
tevlîKirin = random.shuffle

def eger(condition, then_func, else_func=None):
    if condition:
        return then_func()
    elif else_func:
        return else_func()
def na(condition):
    return not condition
def hemû(*conditions):
    return all(conditions)
def hinekjî(*conditions):
    return any(conditions)
def nav(item, container):
    return item in container
def nahewîne(item, container):
    return item not in container
def wekhev(a, b):
    return a == b
def neWekhev(a, b):
    return a != b
def rêzandin(iterable):
    return enumerate(iterable)
def girêdan(*iterables):
    return zip(*iterables)
def xerîtekirin(fonk, iterable):
    return map(fonk, iterable)
def parzûn(fonk, iterable):
    return filter(fonk, iterable)
def kêmkirin(fonk, iterable):
    return _reduce(fonk, iterable)
def mezintir(a, b):
    return a > b
def piçûktir(a, b):
    return a < b
def mezinyanwekhev(a, b):
    return a >= b
def piçûkyanwekhev(a, b):
    return a <= b