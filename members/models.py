from django.db import models
from django.core.validators import RegexValidator

class Member(models.Model):
    STATE_CHOICES = [
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
        ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
        ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'),
        ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'),
        ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'),
        ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'),
        ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'),
        ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
        ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
        ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'),
        ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'), ('WY', 'Wyoming')
    ]

    # Validator for SSN format
    ssn_validator = RegexValidator(
        regex=r'^\d{3}-\d{2}-\d{4}$',
        message="SSN must be in the format '000-00-0000'."
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date of Birth")
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, verbose_name="Address (Line 2)")
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zip_code = models.CharField(max_length=5)  # Ensure no default value is set if not necessary
    phone = models.CharField(max_length=20)  # Increased max_length to accommodate longer phone numbers
    email = models.EmailField(unique=True)
    ssn = models.CharField(max_length=11, validators=[ssn_validator], verbose_name="SS #")
    status = models.BooleanField(default=True, verbose_name="Active Status")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"