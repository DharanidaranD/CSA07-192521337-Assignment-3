"""Iterative DNS resolution through root, TLD and authoritative servers."""
SERVERS = {
    "root": {"in.": "tld-in", "com.": "tld-com"},
    "tld-in": {"ac.in.": "ns-ac"},
    "tld-com": {"example.com.": "ns-example"},
    "ns-ac": {"simats.ac.in.": "ns-simats"},
    "ns-simats": {"results.simats.ac.in.": "10.20.30.40"},
    "ns-example": {"www.example.com.": "93.184.216.34"},
}
cache = {}

def resolve(name):
    if name in cache:
        return cache[name], 0
    server, queries = "root", 0
    while True:
        queries += 1
        # TODO 1: Look in SERVERS[server] for the longest key that name ends with. If
        # the value looks like an IP address (it contains a digit), cache it and
        # return (ip, queries); otherwise continue with that server
        best_key = max((k for k in SERVERS[server] if name.endswith(k)), key=len)
        target = SERVERS[server][best_key]
        if any(ch.isdigit() for ch in target):
            cache[name] = target
            return target, queries
        server = target

if __name__ == "__main__":
    for n in ("results.simats.ac.in.", "www.example.com.", "results.simats.ac.in."):
        ip, q = resolve(n)
        print(f"{n:<24} {ip:<15} queries sent: {q}")
