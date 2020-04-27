from constants import USERS
user_list = []
for user in range(len(USERS)):
    if 'email' in USERS[user]:
        email = USERS[user].get('email')
        if email != '':
            for i in USERS[user]:
                user_list.append(USERS[user][i])
        else:
            USERS[user]['email'] = "This user did not provide an e-mail"
            for i in USERS[user]:
                user_list.append(USERS[user][i])
    else:
        for i in USERS[user]:
            user_list.append(USERS[user][i])
        user_list.append('This user did not provide an e-mail')
for l in user_list:
    print(l, end="\n")


def get_transformed_users():
    users = []
    for user in USERS:
        if user.get('email'):
            users.append({
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'email': user['email']
            })
        else:
           users.append({
               'first_name': user['first_name'],
               'last_name': user['last_name'],
               'email': 'This user did not provide e-mail'
           })
    return users

def get_users_comp():
    users_comp = 
    print(users_comp)
print(get_users_comp())

