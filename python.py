
clients = [

{

    'username': 'CAMERON',
    'age': 25,
    'friends': ['Laine', 'Noah', 'Ren'],
    

},
{

    'username': 'LAINE',
    'age': 25,
    'friends': ['Cameron', 'Noah', 'Ren'],
    
},
{

    'username': 'REN',
    'age': 25,
    'friends': ['Laine', 'Noah', 'Cameron'],
    
},
]


for client in clients:
    print(client['username'])
    
    print(client['age'])
    print()

    for friend in client['friends']:
        print(friend)
        print()