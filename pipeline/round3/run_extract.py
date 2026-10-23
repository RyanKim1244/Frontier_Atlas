import json, os, re, glob, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ptx_extract import extract, macros_from, SRC
ULA = os.path.join(SRC, "davidaustinm_ula", "src")
AC = os.path.join(SRC, "mitchkeller_applied-combinatorics", "source")
um = {"1-1": ["linear-systems"], "1-2": ["linear-systems"], "1-3": ["linear-systems"], "1-4": ["linear-systems"],
      "2-1": ["vectors-plane", "matrices"], "2-2": ["matrices"], "2-3": ["vector-spaces"], "2-4": ["basis-dimension"], "2-5": ["linear-maps", "matrices"], "2-6": ["linear-maps"],
      "3-1": ["matrices", "linear-maps"], "3-2": ["basis-dimension"], "3-3": ["basis-dimension"], "3-4": ["determinants"], "3-5": ["vector-spaces"],
      "4-1": ["eigen"], "4-2": ["eigen"], "4-3": ["diagonalization"], "4-4": ["diagonalization", "eigen"], "4-5": ["markov-chains", "eigen"],
      "5-1": ["linear-systems", "matrices"], "5-2": ["eigen"],
      "6-1": ["inner-products"], "6-2": ["inner-products"], "6-3": ["inner-products"], "6-4": ["inner-products"], "6-5": ["inner-products"],
      "7-1": ["spectral-theorem"], "7-2": ["spectral-theorem"], "7-3": ["svd", "spectral-theorem"], "7-4": ["svd"], "7-5": ["svd"]}
def ula_title(k):
    f = os.path.join(ULA, f"section{k}.xml")
    if not os.path.exists(f): return k.replace("-", ".")
    m = re.search(r"<title>(.*?)</title>", open(f, encoding="utf8").read(), re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else k
ufiles = [(os.path.join(ULA, "exercises", f"exercises{k}.xml"), v, k.replace("-", ".") + " " + ula_title(k)) for k, v in um.items()]
ula, sk1 = extract(ufiles, macros_from(os.path.join(ULA, "bookinfo.xml")), "Understanding Linear Algebra", "Austin, Understanding Linear Algebra", "https://understandinglinearalgebra.org/")
am = {"strings": (["counting"], "Strings, sets and binomial coefficients"), "induction": (["counting", "sequences"], "Induction"), "basics": (["counting", "pigeonhole"], "Combinatorial basics"),
      "graphs": (["graph-basics", "graph-coloring"], "Graph theory"), "graphalgorithms": (["graph-basics"], "Graph algorithms"), "posets": (["set-systems"], "Partially ordered sets"),
      "inclusion-exclusion": (["counting"], "Inclusion–exclusion"), "genfunction": (["generating-functions"], "Generating functions"), "recurrence": (["generating-functions", "sequences"], "Recurrence equations"),
      "probability": (["probability-basics", "random-variables"], "Probability"), "ramsey": (["ramsey", "probabilistic-method"], "Applying probability to combinatorics"),
      "networkflow": (["cycles-matchings"], "Network flows"), "flowapplications": (["cycles-matchings"], "Combinatorial applications of network flows"), "polya": (["groups", "counting"], "Pólya's enumeration theorem")}
afiles = [(os.path.join(AC, f"s_{k}_exercises.ptx"), v[0], v[1]) for k, v in am.items()]
ac, sk2 = extract(afiles, macros_from(os.path.join(AC, "macros.ptx")), "Applied Combinatorics", "Keller & Trotter, Applied Combinatorics", "https://www.appliedcombinatorics.org/")
json.dump(ula + ac, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "textbook_raw.json"), "w"), ensure_ascii=False, indent=0)
print("ULA", len(ula), sk1, "| AC", len(ac), sk2)
