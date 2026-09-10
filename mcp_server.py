import sys
import json
from client import LDPCDecoder

def main():
    H_default = [
        [1, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 1]
    ]
    decoder = LDPCDecoder(H_default)
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "decode":
            dec, ok = decoder.decode(params.get("bits", []), params.get("max_iters", 10))
            res = {"decoded": dec, "success": ok}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
