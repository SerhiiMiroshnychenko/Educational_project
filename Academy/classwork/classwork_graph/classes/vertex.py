class Vertex:

    def __init__(self, key: int) -> None:
        self._id = key
        self.connected_to: Dict["Vertex", int] = {}
        self._color = "white"
        self._predecessor = None
        self._distance = 0

    def get_color(self) -> str:
        return self._color

    def set_color(self, color) -> None:
        self._color = color

    def get_distance(self) -> int:
        return self._distance

    def set_distance(self, distance: int) -> None:
        self._distance = distance

    def get_previous(self) -> Optional["Vertex"]:
        return self._predecessor

    def set_previous(self, previous: Optional["Vertex"]) -> None:
        self._predecessor = previous

    def add_neighbor(self, nbr, weight=0) -> None:
        self.connected_to[nbr] = weight

    def __str__(self) -> str:
        return f"{self._id} connected to: {[x.get_id() for x in self.connected_to]}"

    def get_connections(self) -> Tuple["Vertex"]:
        return tuple(self.connected_to.keys())

    def get_id(self) -> int:
        return self._id