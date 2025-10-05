from django.contrib.auth.models import User
try:
    # Check if user already exists and delete if it does
    if User.objects.filter(username='anigrezda@hotmail.com').exists():
        User.objects.filter(username='anigrezda@hotmail.com').delete()
    # Create new superuser
    User.objects.create_superuser(
        username='anigrezda@hotmail.com',
        email='anigrezda@hotmail.com',
        password='Ptk123456%'
    )
    print("Superuser created successfully!")
except Exception as e:
    print(f"Error creating superuser: {str(e)}")