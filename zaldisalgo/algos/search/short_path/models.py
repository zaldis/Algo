from dataclasses import dataclass


@dataclass
class Edge:
    start: int
    end: int
    cost: int

    def reversed(self) -> 'Edge':
        return Edge(self.end, self.start, self.cost)

