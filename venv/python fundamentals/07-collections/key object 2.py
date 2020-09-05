sda = {
    'tutor': {
        'name': 'Fabricio',
        'language': 'pt-BR'
    },
    'students': [
        {'name': 'Keio',
         'language': 'ee-ET'
         },
        {'name': 'Andres',
         'language': 'ee-ET'
         },
        {'name': 'Ahmed',
         'language': 'Bangladeshi'
         }
    ]
}

print(sda)
print(sda['students'].pop(0))
print(sda)
print(sda.pop('students'))
print(sda)
print(sda.pop('organizer', None))

print('organizer' in sda)
print('tutor' in sda)