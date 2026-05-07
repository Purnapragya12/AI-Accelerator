class PerformanceMetrics:

    def __init__(self):

        self.total_cycles = 0
        self.total_macs = 0

        self.clock_frequency_ghz = 1.0

    def update(self, cycles, macs):

        self.total_cycles += cycles
        self.total_macs += macs

    def throughput_tops(self):

        seconds = self.total_cycles / (
            self.clock_frequency_ghz * 1e9
        )

        if seconds == 0:
            return 0

        ops = self.total_macs * 2

        tops = ops / seconds / 1e12

        return round(tops, 4)

    def summary(self):

        return {
            "cycles": self.total_cycles,
            "macs": self.total_macs,
            "tops": self.throughput_tops()
        }