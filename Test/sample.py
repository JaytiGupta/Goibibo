from faker import Faker

fake = Faker(locale="en_US")

print(fake.name())
print(fake.first_name())
print(fake.last_name())
print(fake.company_email())
print(fake.company())
print(fake.unique.numerify('###-###-####'))
