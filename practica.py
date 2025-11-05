class Proceso:
    """Clase que representa un proceso del sistema operativo."""

    def __init__(self, pid: str, duracion: int, prioridad: int):
        if not pid:
            raise ValueError("PID no puede estar vacío.")
        if duracion <= 0:
            raise ValueError("La duración debe ser positiva.")
        self.pid = pid
        self.duracion = duracion
        self.prioridad = prioridad
        self.tiempo_restante = duracion
        self.tiempo_inicio = None
        self.tiempo_fin = None
        self.tiempo_llegada = 0

    def reiniciar(self):
        """Restablece los valores para nuevas simulaciones."""
        self.tiempo_restante = self.duracion
        self.tiempo_inicio = None
        self.tiempo_fin = None

    def __repr__(self):
        return f"{self.pid} (Duración={self.duracion}, Prioridad={self.prioridad})"