class LDPCDecoder:
    """
    LDPC Belief Propagation Decoder using bipartite Tanner graph parity verification.
    """
    def __init__(self, H):
        self.H = H
        self.m = len(H)
        self.n = len(H[0])

    def decode(self, received_bits, max_iters=10):
        bits = list(received_bits)
        for _ in range(max_iters):
            syndromes = []
            for r in range(self.m):
                s = sum(self.H[r][c] * bits[c] for c in range(self.n)) % 2
                syndromes.append(s)
            if all(s == 0 for s in syndromes):
                return bits, True

            unsatisfied = [0] * self.n
            for r in range(self.m):
                if syndromes[r] == 1:
                    for c in range(self.n):
                        if self.H[r][c] == 1:
                            unsatisfied[c] += 1
            max_viol = max(unsatisfied)
            if max_viol == 0:
                break
            for c in range(self.n):
                if unsatisfied[c] == max_viol:
                    bits[c] ^= 1
                    break
        return bits, False
