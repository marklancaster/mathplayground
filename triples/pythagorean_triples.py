import math
import argparse

# Playing around with generating Pythagorean Triples 
# Inspired by https://www.youtube.com/watch?v=QJYmyhnaaek

def find_triples(upperbound, lowest_terms=True):
    """Tries n^2 combinations and returns unique pythagorean triples"""
    triples = []
    for u in range(1, upperbound+1):
        for v in range(1,upperbound+1):
            z = complex(u, v) ** 2
            a = int(z.real)
            b = int(z.imag)
            c = int(math.sqrt(a**2 + b**2))
            if a > 0 and b > 0 and c > 0:
                if lowest_terms:
                    triple = [i//math.gcd(a, b, c) for i in [a, b, c]]
                else:
                    triple = [a, b, c]    
                triple.sort()
                triples.append(tuple(triple))
    triples = list(set(triples))
    triples.sort()
    return triples

def write_triples(triples, filename="triples"):
    """outputs triples to a csv"""
    print(f"storing file to {filename}")
    with open(filename, 'w') as f:
        for a, b, c in triples:
            f.write(f"{a}, {b}, {c}\n")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="performs n^2 combinations", type=int, default=100)
    parser.add_argument("-f", "--filename", help="output filename")
    parser.add_argument("-a", "--all", help="find all triples, rather than those in lowest terms", action="store_true")
    parser.add_argument("-v", "--verbose", help="prints output to console", action="store_true")
    args = parser.parse_args()
    lowest_terms = False if args.all else True
    triples = find_triples(args.n, lowest_terms)
    if args.verbose:
        print(triples)
        print(f"found {len(triples)} sets of triples")
    if args.filename:
        write_triples(triples, filename=f"{args.filename}.csv")
