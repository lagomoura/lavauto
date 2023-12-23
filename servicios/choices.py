from django.db.models import TextChoices


class ChoicesCategoriaMantenimiento(TextChoices):
    CAMBIAR_ACEITE_MOTOR = ("CAM", "Cambiar Aceite Motor")
    REVISAR_PASTILLA_FRENO = ("RPF", "Revisar Pastilla Freno")
    AJUSTE_CAJA_CAMBIO = ("ACC", "Ajuste Caja Cambio")
    
    
