class EvolutionaryFuzzer:
    def generate_malicious_payloads(self):
        while True:
            yield {"fuzz": "payload"}
