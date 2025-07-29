import datetime
import random

while True:
    pasand = input("I will give you a Muhurat for your Marriage. Do you want it? (yes/no): ").lower()

    if pasand == 'yes':
        
        for i in range(3): 
            days1 = random.randint(1, 10)
            hours1 = random.randint(0, 23)

            days2 = random.randint(5, 15)
            hours2 = random.randint(0, 23)

            days3 = random.randint(16, 31)
            hours3 = random.randint(0, 23)

            muhurat_duration1 = datetime.timedelta(days=days1, hours=hours1)
            muhurat_duration2 = datetime.timedelta(days=days2, hours=hours2)
            muhurat_duration3 = datetime.timedelta(days=days3, hours=hours3)

            print(f'\nOption {i+1}: Your auspicious durations could be: ({muhurat_duration1}, {muhurat_duration2}, {muhurat_duration3})')

            if i < 2: 
                more_options = input("Do you want to see another set of muhurat options? (yes/no): ").lower()
                if more_options == 'no':
                    break

        print("\nThanks for asking...!!!")
        break 
    elif pasand == 'no':
        print("No problem! Thanks for considering......")
        break 
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")