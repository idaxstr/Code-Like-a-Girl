password = 'python'
secret_message = 'Code Like a Girl'

user_password = input('Please enter the password: ')

while(password != user_password):
    user_password = input('Please enter the password: ')

print(secret_message)
