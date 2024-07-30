import random
import string

Department_Name = input('Enter your Department name: ').lower()
Department_list = [ 'Marketing', 'Accounting', 'FinOps']
Department_list_case_variation = [Dept.lower()for Dept in Department_list]

if Department_Name in Department_list_case_variation:
    print('Random EC2 name Generator script can be used by your Department ')
    No_of_EC2_Instances = int(input('Please enter how many EC2 instances you want: '))
    print('List of EC2 instance names:')
    for i in range(No_of_EC2_Instances):
        Random_Character = ''.join(random.choices(string.ascii_letters, k=3))
        Random_Number = ''.join(random.choices(string.digits, k=3))
        Random_EC2_Instance_Name = Department_Name + '-' + Random_Character + Random_Number
        print(Random_EC2_Instance_Name)
else:
    print("You can't use the EC2 name Generator")
