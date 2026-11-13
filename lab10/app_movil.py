class SuscripcionExpiradaError(Exception):
    """Se lanza cuando se intenta usar una función Pro sin membresía activa."""
    pass


class PuntosInsuficientesError(Exception):
    """Se lanza cuando el usuario intenta gastar más gemas de las que tiene."""
    pass


class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True):
        if gemas < 0:
            raise ValueError("La cantidad inicial de gemas no puede ser negativa.")
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a ganar debe ser mayor a cero.")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a gastar debe ser mayor a cero.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError("No tienes suficientes gemas para realizar esta operación.")
        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(self, username: str, meses_suscripcion: int, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True):
        if meses_suscripcion <= 0:
            raise ValueError("Los meses de suscripción inicial deben ser mayores a cero.")
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion == 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("Tu suscripción Pro ha expirado. Renueva para descargar contenido offline.")
        return f"Descargando contenido offline para el usuario Pro: {self.username}"