""". Implemente una clase “factura” que tenga un importe correspondiente al total
de la factura pero de acuerdo a la condición impositiva del cliente (IVA
Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal
condición. """

from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def factory_method(self, total):
        pass
    
class IvaResponsable(Creator):
    def factory_method(self, total):
        return FacturaIvaResponsable(total)

class IvaNoInscripto(Creator):
    def factory_method(self, total):
        return FacturaIvaNoInscripto(total)

class IvaExento(Creator):
    def factory_method(self, total):
        return FacturaIvaExento(total)

class Factura(ABC):
    def __init__(self, total):
        self.total = total

    @abstractmethod
    def operacion(self):
        pass

class FacturaIvaResponsable(Factura):
    def operacion(self):
        print("factura para cliente con IVA responsable")
        print("total:", self.total)
        print("impuestos (IVA 21%):", self.total * 0.21)

class FacturaIvaNoInscripto(Factura):
    def operacion(self):
        print("factura para cliente con IVA no inscripto")
        print("total:", self.total)
        print("impuestos (IVA 0%): 0")

class FacturaIvaExento(Factura):
    def operacion(self):
        print("factura para cliente con IVA exento")
        print("total:", self.total)
        print("impuestos (IVA Exento): 0")

if __name__ == "__main__":
    responsable_iva = IvaResponsable()
    factura_iva_responsable = responsable_iva.factory_method(1520)
    factura_iva_responsable.operacion()

    n_inscripto_iva = IvaNoInscripto()
    factura_iva_no_inscripto = n_inscripto_iva.factory_method(1400)
    factura_iva_no_inscripto.operacion()

    exento_iva = IvaExento()
    factura_iva_exento = exento_iva.factory_method(800)
    factura_iva_exento.operacion()
