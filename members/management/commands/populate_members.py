from django.core.management.base import BaseCommand
from members.models import Member
from faker import Faker
import random
import re

class Command(BaseCommand):
    help = 'Populate the database with dummy member data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

        for _ in range(100):  # Generate 20 dummy members
            # Generate a clean phone number without special characters
            raw_phone = fake.phone_number()
            clean_phone = re.sub(r'\D', '', raw_phone)  # Remove all non-numeric characters
            formatted_phone = clean_phone[:10]  # Limit to 10 characters to fit typical U.S. phone number format

            Member.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                dob=fake.date_of_birth(minimum_age=18, maximum_age=90),
                address=fake.street_address(),
                address2=fake.secondary_address(),
                city=fake.city(),
                state=random.choice(states),
                zip_code=fake.zipcode()[:5],  # Use only the first 5 characters
                phone=formatted_phone,  # Use the formatted phone number
                email=fake.unique.email(),  # Ensure unique emails
                ssn=fake.ssn(),
                status=fake.boolean()
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 100 dummy data entries'))