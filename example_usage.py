from client import LDPCDecoder

def main():
    print("=== Testing LDPC Belief Propagation Decoder ===")
    H = [
        [1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 1]
    ]
    ldpc = LDPCDecoder(H)
    transmitted = [0, 0, 0, 0, 0, 0]
    corrupted = [1, 0, 0, 0, 0, 0]
    decoded, ok = ldpc.decode(corrupted)
    print("Corrupted:", corrupted)
    print("Decoded:  ", decoded, "Success:", ok)
    assert ok and decoded == transmitted
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
