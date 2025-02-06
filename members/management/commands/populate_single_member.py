from members.models import Member
import random
from faker import Faker

fake = Faker()
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

# Example date in YYYY-MM-DD format
dob = '1980-01-01'  # Correct format

member = Member(
    first_name=fake.first_name(),
    last_name=fake.last_name(),
    dob=dob,  # Using correct date format
    address=fake.street_address(),
    address2=fake.secondary_address(),
    city=fake.city(),
    state=random.choice(states),
    zip_code=fake.zipcode()[:5],  # Use only the first 5 characters
    phone=fake.phone_number()[:10],  # Ensure phone number fits the max_length
    email=fake.unique.email(),  # Ensure unique email
    ssn=fake.ssn(),
    status=fake.boolean()
)

# Save the entry
member.save()
print("Member saved successfully!")