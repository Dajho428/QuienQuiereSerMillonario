import random


class Pregunta():
    def __init__(self, idPregunta):
        self.idPregunta = idPregunta

    def crearPreguntas(self, dificultad, categoria):

        if dificultad == 'Facil':
            if categoria == 'Entretenimiento':
                """
                preguntas = ['¿Quien fue el cantante de QUEEN?',
                             ' ¿A que grupo pertenece la cancion ¨Smells Like Teen Spirit¨?',
                             ' ¿A que pelicula pertenece el personaje ¨Jack Sparrow¨?']
                preguntasDic = {'¿Quien fue el cantante de QUEEN?': ['A. James Hetfield ', 'B. Roger Waters',
                                                                     ' C. John Lennon', 'D. Freddy Mercury', 'D'],
                                ' ¿A que grupo pertenece la cancion ¨Smells Like Teen Spirit¨?': ['A. Nirvana',
                                                                                                  'B. Metallica',
                                                                                                  'C. Artic Monkeys',
                                                                                                  'D. The Rolling Stones',
                                                                                                  'A'],
                                ' ¿A que pelicula pertenece el personaje ¨Jack Sparrow¨?': ['A. Harry Potter',
                                                                                            ' B. Piratas del Caribe',
                                                                                            'C. Los Pinguinos de Madagascar',
                                                                                            'D. El señor de los anillos',
                                                                                            'B']
                                }
                preguntaAux = random.choice(preguntas)
                preguntaAux2 = (preguntasDic[preguntaAux])"""
                pregunta1 = ['¿Quien fue el cantante de QUEEN?', 'A. James Hetfield ', 'B. Roger Waters',
                             ' C. John Lennon', 'D. Freddy Mercury', 'D']
                pregunta2 = [
                    ' ¿A que grupo pertenece la cancion ¨Smells Like Teen Spirit¨?,A. Nirvana,B. Metallica    C. Artic Monkeys    D. The Rolling Stones',
                    'A']
                pregunta3 = [' ¿A que pelicula pertenece el personaje ¨Jack Sparrow¨?', 'A. Harry Potter',
                             ' B. Piratas del Caribe', 'C. Los Pinguinos de Madagascar', 'D. El señor de los anillos',
                             'B']

                # ' ¿Como se llama el villano de la pelicula el ¨Rey Leon¨?\n A. Simba      B. Wall-e       C. Scar     D. Pumba',#C
                # ' ¿Como se llama el protagonista de ¨Spiderman¨?\n A. Peter Parker    B. Harry Osborn     C. Tony Stark       D. Octopus',#A
                # ' ¿Nombra la serie de anime, cuyo persona principal es de nombre ¨Goku¨?\n A. Los caballeros de Zoodiaco      B. One Piece    C. Death Note    D. Dragon Ball',#D
                # ' ¿Mediante cual plataforma se puede ver la serie ¨La Casa de Papel¨?\n A. Youtube    B. DisneyPlus       C.Netflix       D.ClaroVideo',#C
                # ' ¿Famoso grupo de rock britanico cuyo nombre traducido al español da como significado ¨los escarabajos¨?\n A.The Beatles     B. The Who      C. The Cure     D. Aterciopelados',#A
                # ' ¿Que artista colombiano fundo la fundacion ¨Pies Descalzos¨? \n A. Juanes   B. Carlos Vives      C. Shakira      D. Maluma',#C
                # ' ¿Cual es la red social mas utilizada en los ultimos tiempos?\n A. Hi5      B. MySpace      C. Messenger    D. Facebook'#D

                return list[pregunta1,pregunta2,pregunta3]
            else:  # DEPORTES
                preguntas = [
                    ' ¿Campeon del Mundial de futbol del año 2014?\nA.Era gol de Yepes    B.España    C. Alemania     D.Brasil',
                    # C
                    ' ¿Cuantos puntos vale un tiro libre en el baloncesto?\nA. 3    B. 5    C. 0    D. 1',  # D
                    ' ¿Que jugador del mundo que ha ganado mas copas del mundo junto a su equipo?\nA. Pele    B. Maradona     C. Zinedine Zidane      D. Messi',
                    # A
                    ' ¿QUe jugador es considerado el mejor jugador Basquetbolista de todos los tiempos?\nA. Lebron James      B. Stephen Curry    C. Allen Iverson    D. Michael Jordan',
                    # D
                    ' ¿Cada cuantos años se celebran los juegos olimpicos?\nA. 2  B. 4    C. 6    D. 1',  # B
                    ' ¿Que equipo de futbol ha ganado mas mundiales hasta el momento?\nA. Brasil      B.Alemania      C. Uruguay      D.Francia',
                    # A
                    ' ¿Clavadista Colombiano reconocido por tener dos records Guinness?\nA. Michael Phleps    B. Orlando Duque    C. James Rodiguez       D. Ninguno de los anteriores',
                    # B
                    ' ¿En que pais nacio el futobolista Lionel Messi?\nA. España   B. Chile     C. Mexico     D. Argentina',
                    # D
                    ' ¿Pais con mas medallas olimpicas?\nA. Sudafrica     B. Ecuador      C. Estados Unidos      D. Colombia',
                    # C
                    ' ¿Ciclista colombiano en obtener los titulos del giro de Italia y el tour de France?\nA. Egan Bernal    B. Nairoman     C. SupermanLopez     D. Rogoberto Uran'
                    # A
                ]
                return preguntas
        elif dificultad == 'Medio':
            if categoria == 'Geografia':
                preguntas = [
                    ' ¿Cuál es el rió más largo del mundo?\nA. Amazonas   B. Nilo     C. Rio Amarillo     D.Yangtse',
                    # A
                    ' ¿Qué país es el segundo más grande del mundo en términos de población?\nA. China    B. Rusia    C. India    D. Indonesia',
                    # C
                    ' ¿Cuántos continentes hay en la Tierra?\nA. 5    B. 6    C. 3    D.  7',  # B
                    ' ¿Dónde desemboca el río Amazonas?\nA. Oceano Pacifico   B. Oceano Atlantico     C. Mar Caribe   D. Mar Muerto',
                    # B
                    ' ¿En qué país puedes visitar Machu Picchu?\nA. Ecuador   B. Argentina    C.Peru      D. Chile',
                    # C
                    ' ¿En qué cordillera se encuentra el Monte Everest?\nA. Himalaya      B. Andes    C. Central      D. Pirineos',
                    # A
                    ' ¿Cuál es la ciudad más antigua del mundo?\nA. Roma      B. Jerusalen        C. Vietnam      D. Damasco',
                    # D
                    ' ¿Cuál es el principal río que recorre el Gran Cañón de Estados Unidos?\nA. Colorado      B. Oregon      C. Roble    D. Nilo',
                    # A
                    ' ¿Cuál es el país más grande de Sudamérica?\nA. Argentina     B. Chile   C. Colombia     D. Brasil',
                    # D
                    ' ¿De qué país es capital la ciudad de Viena?\nA. Australia      B.Austria   C.Andorra   D.Belgica',
                    # B
                    ' ¿Cuál es el país más pequeño de Suramérica?\nA. Bolivia    B.Guyana Francesa   C.Surinam   D. Peru'
                    # C
                ]
                return preguntas
            else:  # CULTURA
                preguntas = [
                    ' ¿Cuándo terminó la II Guerra Mundial?\nA.1429  B.1945  C.1947  D.1965',  # B
                    ' ¿Quién es el padre del psicoanálisis?\nASigmund Freud   B.Carl Gustav Jung  C.Skinner   D. Kant',
                    # A
                    ' ¿Cuál es el libro sagrado de los musulmanes?\nA.La Biblia   B.El Talmud     C. El Necronomicon  D.El Coran',
                    # D
                    ' ¿En qué país se usó la primera bomba atómica?\nA.Rusia  B.Estados Unidos    C.Japon     D.Corea',
                    # C
                    ' ¿Cuál fue el primer hombre en ir a la luna?\nA.Louis Armstrong    B.Michael Armstrong   C.Neil Armstrong    D.Apolo',
                    # C
                    ' Actualmente, ¿cuál es el país más grande del mundo?\nA.Rusia    B.Japon     C.Estados Unidos    D.China',
                    # A
                    ' ¿Cuál es el nombre de la lengua oficial de la República Popular de China?\nA.Chino  B.Arabe     C. Japones      D.Mandarin',
                    # D
                    ' ¿Qué planeta es conocido como “planeta rojo”?\nA.Saturno    B.Marte     C.Venus     D.Tierra',
                    # B
                    ' ¿Cómo se llama la civilización que construyó el Machu Picchu en Perú?\nA.Inca   B.Aztecas   C. Mayas    D.Embera',
                    # A
                    ' ¿Cuál es el animal más grande que habita la Tierra?\nA. Elefante   B.Jirafa    C.Ballena Azul  D.Orca',
                    # C
                    ' ¿Quién está encargada del servicio de inteligencia de los Estados Unidos?\nA.FBI   B.CIA   C.Servicio Secreto      D.Departamento Justicia'
                    # B
                ]
                return preguntas
        elif dificultad == 'Dificil':
            if categoria == 'Ciencia':
                preguntas = [
                    ' ¿Qué científico propuso las tres leyes del movimiento?\nA.Albert Einstein  B.Manuel Elkin Patarroyo    C.Heisenberg    D.Isaac Newton',
                    # D
                    ' ¿Cuál es el elemento químico más abundante en la corteza terrestre?\nA.Nitrogeno    B.Carbono   C.Oxigeno   D.Hidrogeno',
                    # C
                    ' ¿Cómo se denomina al resultado de una multiplicación?\nA.Producto   B.Resultado     C.Multiplo      D.Igualdad',
                    # A
                    ' ¿Qué se le agrega al hierro para hacer acero?\nA.Oxigeno    B.Carbono   C.Nitrogeno     D.Zinc',
                    # B
                    ' ¿Cuál es el único mamífero que puede volar?\nA.Murcielago   B.Avestruz  C.Aquila    D.Condor',
                    # A
                    ' ¿Cómo se denomina a los animales que nacen de un  huevo?\nA.Hueviparos  B.ViviParos     C.Oviparos      D.Ociviparos',
                    # C
                    '  ¿Cuántos corazones tienen los pulpos?\nA.1 B.2 C.3 D.0',  # C
                    ' El proceso por el que una célula se divide para formar dos células hijas se llama: \nA.Segregacion  B.Meiosis   C.Nucleoplasmosis   D.Mitosis',
                    # D
                    ' La información genética en las células se localiza:\nA.Nucleo   B.Membrana  C.Citoplasma    D.Ribosoma',
                    # A
                    ' ¿Con qué respira una ballena?\nA.Por la piel   B.Pulmones  C.Branquias     D.Ninguna',  # B
                    ' Los cromosomas están formados por:\nA.ADN  B.Proteinas C.ARN   D.Ninguno',  # A
                    ' La columna más a la derecha de la tabla periódica esta compuesta por:\nA.Haluros   B.Minerales     C.Alcalinos     D.Gases Nobles',
                    # D
                    ' ¿Qué inventó Alfred Nobel, el que da nombre a los famosos premios?\nA.La dinamita  B.La penicilina     C.La bomba Atomica  D. Ninguna',
                    # A
                    ' ¿Cuál es la principal función de los globulos rojos?\nA.Combatir enfermedades  B.Coagular la sangre    C.Desoxigenar la sangre     D.Llevar oxigeno',
                    # D
                    ' ¿Qué tipo de radiación te produce quemaduras?\nA.Rayos X   B.Ultravioleta  C.Infrarroja    D.Electromagnetica',
                    # B
                    ' ¿A que reino pertenecen las levaduras?\nA.Animal   B.Vegetal   C.Fungi     D.Monera'  # Funji
                ]
                return preguntas
            else:  # ARTE Y LITERATURA
                preguntas = [
                    ' ¿En que museo está la Mona Lisa?\nA.Museo del Prado     B.British Museum    C.Louvre    D.Galeria Uffizi',
                    # C
                    ' ¿En que siglo nació Van Gogh?\nA.XIX    B.XX    C.XVII  D.XVIII',  # A
                    ' ¿En que siglo se inició el Renacimiento?\nA.XVI     B.XIV   C.XV    D.XIII',  # C
                    ' ¿Cuál de estas no es una de las 7 maravillas del mundo antiguo?\nA.Templo de Artemisa    B.Gran Piramide de Giza     C.Faro de Alejandria    D.Partenon',
                    # D
                    ' ¿En qué estilo de pintura se clasifica El grito de Edvard Munch?\nA.Surrealismo     B.Expresionismo     C.Impresionismo     D.Ninguna',
                    # C
                    ' ¿Qué novelista y poeta ha sido apodado «Príncipe de los Ingenios»?\nA.Dante Alighieri   B.Miguel de Cervantes   C.William Shakespeare   D.Ninguno',
                    # B
                    ' ¿Cuándo surge el arte pop?\nA.FInales del siglo XX      B.Mediados del siglo XX     C.Principios del siglo XXI  D.Ninguno',
                    # A
                    ' ¿Quién fue descrito como «el más grande hombre de letras alemán»?\nA.Heinrich Heine     B.Friedrich Schiller    C.Johan Wolfang von goethe    D.Ninguno',
                    # C
                    ' ¿Donde nacio el escritor Julio Cortazar?\nA.Chile   B.Uruguay   C.Ecuador   D.Argentina',  # D
                    ' ¿Autor de la celebrada historieta Mafalda?\nA.Quino    B.Garcia Marquez    C.Coelho    D.Cortazar',
                    # A
                    ' ¿Cuanto mide el "David" de Miguel Angel?\nA.2.80 metros     B.5 metros      C.6 metros      D. 7 metros',
                    # B
                    ' ¿Cual es el origen de la musica Rock?\nA.Jazz   B.Hip Hop   C.Baladas   D. Blues',  # D
                    ' ¿A que pintor le pertenece la obra "El Grito"\nA.Picasso    B.Frida     C.Edvard Munch      D.Gandhi',
                    # C
                    ' ¿Autor de la trilogia "El señor de los anillos"?\nA.Tolkien    B.Marlon Brandon    C.Rowling   D.Ninguno',
                    # A
                    ' ¿Como murio Vincent Van Gogh?\nA.Cancer    B.Accidente     C.Suicidio      D.Ataque Cardiaco',
                    # C
                    ' ¿CUal es la obra mas famosa de Charles Dickens?\nA.Oliver Twist     B.Cancion de Navidad    C.Historias de dos ciudades     D.David Copperfield'
                    # A
                ]
                return preguntas
