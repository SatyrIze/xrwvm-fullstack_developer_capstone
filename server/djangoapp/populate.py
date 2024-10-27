import os
import sys
import django

# Add the server directory to the Python path
server_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(server_dir)

# Set up Django's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproj.settings')
django.setup()

from djangoapp.models import CarMake, CarModel

def initiate():
    # First, create car makes
    makes_data = [
        {
            "name": "Toyota",
            "description": "Japanese multinational automotive manufacturer known for reliability and quality."
        },
        {
            "name": "Honda",
            "description": "Japanese automobile manufacturer known for fuel efficiency and innovation."
        },
        {
            "name": "Ford",
            "description": "American multinational automaker known for trucks and muscle cars."
        },
        {
            "name": "BMW",
            "description": "German luxury vehicle manufacturer known for performance and technology."
        },
        {
            "name": "Mercedes-Benz",
            "description": "German luxury automobile manufacturer known for premium vehicles and innovation."
        }
    ]

    # Create CarMake instances
    for make_data in makes_data:
        make, created = CarMake.objects.get_or_create(
            name=make_data["name"],
            defaults={"description": make_data["description"]}
        )
        print(f"{'Created' if created else 'Retrieved'} car make: {make.name}")

    # Create CarModel instances for each make
    models_data = [
        # Toyota Models
        {
            "make": "Toyota",
            "name": "Camry",
            "type": "SEDAN",
            "year": 2023
        },
        {
            "make": "Toyota",
            "name": "RAV4",
            "type": "SUV",
            "year": 2023
        },
        # Honda Models
        {
            "make": "Honda",
            "name": "Civic",
            "type": "SEDAN",
            "year": 2023
        },
        {
            "make": "Honda",
            "name": "CR-V",
            "type": "SUV",
            "year": 2023
        },
        # Ford Models
        {
            "make": "Ford",
            "name": "F-150",
            "type": "SUV",
            "year": 2023
        },
        {
            "make": "Ford",
            "name": "Mustang",
            "type": "SEDAN",
            "year": 2023
        },
        # BMW Models
        {
            "make": "BMW",
            "name": "3 Series",
            "type": "SEDAN",
            "year": 2023
        },
        {
            "make": "BMW",
            "name": "X5",
            "type": "SUV",
            "year": 2023
        },
        # Mercedes-Benz Models
        {
            "make": "Mercedes-Benz",
            "name": "C-Class",
            "type": "SEDAN",
            "year": 2023
        },
        {
            "make": "Mercedes-Benz",
            "name": "GLE",
            "type": "SUV",
            "year": 2023
        }
    ]

    # Create CarModel instances
    for model_data in models_data:
        make = CarMake.objects.get(name=model_data["make"])
        model, created = CarModel.objects.get_or_create(
            car_make=make,
            name=model_data["name"],
            defaults={
                "type": model_data["type"],
                "year": model_data["year"]
            }
        )
        print(f"{'Created' if created else 'Retrieved'} car model: {model.name} ({model.car_make.name})")

if __name__ == "__main__":
    print("Starting database population...")
    initiate()
    print("Database population completed!")
