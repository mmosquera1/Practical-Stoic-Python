import random

practices = [
    {
        'Despertate': 'Ya descansaste suficiente. Hora de levantarse y aprovechar el día que tenés por delante. No duermas más de lo que tu cuerpo necesita.',
    },
    {
        'Hacé tu cama':'Luego de despertarte, hacé tu cama. Empezá el día con momentum al completar una tarea tan simple, y te vas a dar cuenta que ese momentum te acompaña durante el día.',
    },
    {
        'Mira un amanecer': 'De vez en cuando, hacete un tiempo para despertar antes del amanecer, y experimentá completamente la hermosa vista que te regala el cielo. Mientras estás en eso, pensá acerca de tu lugar en el Universo.',
    },
    {
        'Memento mori': 'Recuerda que podrías dejar la vida ahora mismo. No hay garantías de que vayas a presenciar otro amanecer, o sentir otro beso, otro abrazo. Usa esta oportunidad sabiamente.'
    },
    {
        'Premeditatio malorum': 'Empezá tu día revisando tu calendario, imaginá cómo puede salir mal tu día. Pensá en cómo se van a sentir, cómo podes ser avergonzado. Ahora considerá cómo podrías responder a estos infortunios, suavizar el golpe.'
    },
    {
        'Revisá tus impresiones': 'Poné cada impresión que tengas a prueba con tu criterio, principalmente preguntate: esto está o no en mi control? Y si no lo está, entonces no tenés que preocuparte. Preguntate por qué tenés esa impresion. Si es en un área específica, empezá a contar esos incidentes cuando aparecen.'
    },
    {
        'Preparate para los indeseables': 'Es inevitable, cualquier día te vas a encontrar con personas insufribles. Considerá cómo podés manejarlos, mentalmente hacé una imagen de no perder la cordura, de cómo vas a preservar tu serenidad y mantener tu altura. Admití que vos también tenés tus faltas y que a veces las escondes mejor que otras. Imagina que ese día alguien más esta respirando hondo para lidiar con vos.'
    },
    {
        'Prepara tus herramientas': 'Memoriza los quotes, máximas y principios de tu sistema de creencias que te mantiene centrado. Dejá copias de Meditaciones, Manual de Epicteto y aquello que te sea inspirativo y de apoyo a mano. Revisalos a diario.'
    },
    {
        'Pausa, evalua y luego decide': 'Frente a una fuerte impresión y/o emoción, respira hondo y toma una pausa, sé conciente de que lo que te afecta es tu propia impresión del evento, evalúa si amerita una respuesta de tu parte, y luego toma una decisión.'
    },
    {
        'Aplicá el tenedor estoico': 'Ante todas las cosas aplicá el tenedor y preguntate: ¿esta cosa está en mi poder? Las cosas que pasan por tu cabeza, las impresiones que consentis, las acciones que tomás, los pensamientos que formas y el ejercicio de tu voluntad, todas estas controlas completamente. Pero los resultados de tu esfuerzo, en su mayor parte, no están en tu control. Podés hacerlo correcta y prudentemente, y aún así no obtener recompensa.'
    },
    {
        'Usa la cabeza': 'Seguí la naturaleza, la razón, la lógica. Si los hechos cambian, tú te adaptas. Si no tenés suficiente información, conseguís más.'
    },
    {
        'Usa la perspectiva de un tercero': 'Para tener una mirada más objetiva, ayuda dar un paso hacia atrás y mirar tus obstáculos como si fueras una parte desinteresada, pero empática. ¿La persona en ese rol estaría preocupada por vos? ¿O imaginaría que sos capaz de resolverlo sin problemas?'
    },
    {
        'Apoya tu comunidad': '¿Qué podés hacer para ayudar en la preservación de tu especie? Vivir acorde a la naturaleza incluye tratar a tus vecinos como hermanos, como brazos. Hechos para trabajar uno al lado del otro en pos del bien común.'
    },
    {
        'Considerá los peores escenarios posibles': 'Tomate 10 minutos para imaginar que perdiste la vista en un accidente. Tu hijo ante una enfermedad. Tu reputación en un gran y dramático episodio de pánico. Tu vida. Lo que sea que te tenga más asustado actualmente. Caminá cada paso de ese episodio, sin saltear un minuto. ¿Qué vas a hacer? ¿Cómo vas a manejarlo? Si te sucede, ya no vas a estar debilitado por el shock del evento.'
    },
    {
        'Retirate dentro del ser': 'La próxima vez que necesites aliviarte; busca un lugar tranquilo y considera que está realmente en tu control, nada que te suceda puede lastimarte a menos que vos elijas que te lastime, el cambio es natural e inevitable y memento mori, el segundero del reloj no para por nadie.'
    },
    {
        'Elegí bien tu compañía': 'Asociate con personas que te ayuden a mejorar. Rodeate de gente que usa la cabeza. Evita la gente que saca lo peor de vos, que te arrastra a malos hábitos.'
    },
    {
        'Usa humor autocrítico': 'Es una forma elegante de mostrar que tu autoestima es lo suficientemente fuerte como para aceptar golpes sin perder el sentido del humor.'
    },
    {
        'Deja que hable el otro': 'Pasar tiempo hablando de vos es aburrido e inútil. Asique deja que el otro cuente su historia, tenemos dos orejas y una boca por una razón.'
    },
    {
        'Vive de forma simple': 'El propósito en la vida no es consumir lo mejor de todo. Es alcanzar el "areté", es el autocumplimiento a través de la excelencia de carácter. El sabio buscará sacar de su vida todo lo que no contribuya a sus metas, porque todo lo que no ayuda es, en el mejor de los casos, una distracción. Identifica y remueve de tu vida una distracción ahora mismo.'
    },
]

def addPractice():
    practice = input("Por favor ingresá tu práctica de preferencia: ")
    practices.append(practice)
    print(f"La práctica '{practice}' se añadió correctamente.")

def selectPractice():
    listPractices()
    try:
        chosenPractice = int(input("Elegí la práctica que desees hacer: "))
        if chosenPractice >= 0 and chosenPractice < len(practices):
            print(practices[chosenPractice])
        else:
            print(f"La práctica con el número {chosenPractice} no fue encontrada.")
    except:
        print(f"Práctica inválida. Por favor intentalo nuevamente.")

def selectRandom():
    selected_practice = random.choice(practices)
    print(selected_practice)

def listPractices():
    if not practices:
        print(f"La lista de prácticas está vacía.")
    else:
        print(f"Prácticas disponibles: ")
        for index, practice in enumerate(practices):
            print(f"Práctica #{index}. {practice}")
            ###Práctica # 1. Levántate


def deletePractice():
    listPractices()
    try:
        practiceToDelete = int(input("Elegí el número de práctica para eliminar."))
        if practiceToDelete >= 0 and practiceToDelete < len(practices):
            practices.pop(practiceToDelete)
            print(f"Práctica {practiceToDelete} fue eliminada correctamente.")
        else:
            print(f"La práctica con el número {practiceToDelete} no fue encontrada.")
    except:
        print("Práctica inválida. Por favor intentá de nuevo.")

#Definir una funcion que permita al usuario ver cuantas prácticas hizo a lo largo de los días. Que lo felicite si viene en una racha.

if __name__ == "__main__":
    ###Crea un loop para correr la app:
    print("Bienvenido a Estoico Práctico!")
    while True:
        print("\n")
        print("Cuál práctica estoica te gustaría hacer hoy?")
        print("-----------------------------------------")
        print("1. Añade una práctica.")
        print("2. Selecciona una práctica.")
        print("3. Selecciona una práctica aleatoria.")
        print("4. Lista todas las prácticas.")
        print("5. Eliminar una práctica.")
        print("6. Salir.")

        choice = input("Ingresá tu elección: ")
        if(choice == "1"):
            addPractice()
        elif(choice == "2"):
            selectPractice()
        elif(choice == "3"):
            selectRandom()
        elif(choice == "4"):
            listPractices()
        elif(choice == "5"):
            deletePractice()
        elif(choice == "6"):
            break
        else:
            print("Elección inválida. Por favor ingresá una de las opciones desplegadas más arriba.")

print("Hasta la próxima, estoico! 👋👋")