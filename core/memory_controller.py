class MemoryController:

    def __init__(
        self,
        sram_size_kb=256,
        bandwidth_gb_per_sec=32
    ):

        self.sram_size_kb = sram_size_kb

        self.bandwidth_gb_per_sec = bandwidth_gb_per_sec

        self.sram_hits = 0
        self.dram_accesses = 0
        self.memory_stalls = 0

    def access_data(self, size_kb):

        # ===== FULL SRAM HIT =====
        if size_kb <= self.sram_size_kb:

            self.sram_hits += 1

        # ===== PARTIAL SRAM + DRAM =====
        else:

            sram_fraction = (
                self.sram_size_kb / size_kb
            )

            dram_fraction = 1 - sram_fraction

            self.sram_hits += sram_fraction

            self.dram_accesses += dram_fraction

            self.memory_stalls += dram_fraction * 0.5

    def stats(self):

        total = (
            self.sram_hits +
            self.dram_accesses
        )

        if total == 0:
            hit_rate = 0
        else:
            hit_rate = (
                self.sram_hits / total
            ) * 100

        return {

            "sram_hits":
                round(self.sram_hits, 2),

            "dram_accesses":
                round(self.dram_accesses, 2),

            "memory_stalls":
                round(self.memory_stalls, 2),

            "hit_rate_percent":
                round(hit_rate, 2)
        }