films ={
   'Insidious':{
           'Genre':'horror',
            'rating':6.8,
             'sequel':'insidious 2'
         },
    'Sinister':{
            'Genre':'horror',
            'rating':6.2,
             'sequel':'sinister 2'

    }

}

for name,info in films.items():
    print("Film name: " + name)
    print("The film's genre is " + info['Genre'] + " and has got a rating of " + str(info['rating']) + ".\nThe upcoming sequel is " + info['sequel'].title())
    print("\n")
