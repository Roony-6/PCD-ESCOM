
class Revision:
    def __init__(self,id_revision,vehiculo,presion_bar, tipo_vehiculo):
        
        self.id_revision = id_revision
        self.vehiculo = vehiculo
        self.presion_bar = presion_bar
        self.tipo_vehiculo = tipo_vehiculo
    
    def clasificar(self):
        """
        Clasifica el vehiculo segun la presion
        Returns:
            clasificacion: str clasificacion del vehiculo
        
        """
        if self.presion_bar < 1.59:
            return "Muy baja"
        elif self.presion_bar <= 1.92:
            return "Baja"
        elif self.presion_bar <= 2.88:
            return "Normal"
        elif self.presion_bar < 3.58:
            return "Alta"
        elif self.presion_bar >= 3.58:
            return "Peligrosa"
        
    
    def __str__(self):
        return f"id: {self.id_revision}, vehiculo: {self.vehiculo}, presion bar: {self.presion_bar}, tipo:{self.tipo_vehiculo}"
    def __repr__(self):
        return f"Revision(id='{self.id_revision}', vehiculo='{self.vehiculo}',presion_bar={self.presion_bar},tipo='{self.tipo_vehiculo}'"