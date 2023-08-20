class Asiento:
    COLORES_ACEPTADOS = ['rojo', 'verde', 'amarillo', 'negro', 'blanco']

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        for colorAceptado in Asiento.COLORES_ACEPTADOS:
            if (colorAceptado.lower() == color):
                self.color = colorAceptado
                return


class Auto:
    MENSAJE_PIEZAS_ORIGINALES = "Auto original"
    MENSAJE_PIEZAS_NO_ORIGINALES = "Las piezas no son originales"

    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidad_asientos = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                cantidad_asientos = cantidad_asientos + 1
        return cantidad_asientos

    def verificarIntegridad(self):
        if (not isinstance(self.motor, Motor)
                and not self.motor.registro != self.registro):
            return Auto.MENSAJE_PIEZAS_NO_ORIGINALES

        for asiento in self.asientos:
            if(not isinstance(asiento, Asiento)):
                continue
            if asiento.registro != self.registro:
                return Auto.MENSAJE_PIEZAS_NO_ORIGINALES
        return Auto.MENSAJE_PIEZAS_ORIGINALES


class Motor:
    TIPOS_ACEPTADOS = ['electrico', 'gasolina']

    def __init__(self, numeroCilindros=0, tipo="", registro=0):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        for tipo_aceptado in Motor.TIPOS_ACEPTADOS:
            if (tipo.lower() == tipo_aceptado):
                self.tipo = tipo_aceptado
                return
