from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

def positive_integer_with_max_digits(max_digits):
    return [
        MinValueValidator(0), # Asegura que sea un número positivo
        MaxValueValidator(10**max_digits - 1) # Asegura que no tenga más de `max_digits` dígitos
    ]

def validate_observaciones(max_length):
    return [
        MaxLengthValidator(max_length, message=f'Las observaciones no pueden exceder los {max_length} caracteres')
    ]


