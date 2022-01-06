
define s = Character("{b}Sakuya{/b}", color=gui.text_color, ctc="ball")

## `menu` keyword is not used here. Its purpose is only to crosscheck.

## parche al español creado por adam @adam3752YT  github.com/weebcoderuwu

label start:
    call scene1 from _call_scene1
    call scene2 from _call_scene2
    call scene3 from _call_scene3
    return

label scene1:  ############################################################################################# SCENE 1 ##
    python:
        quick_menu = False
        save_name = "Day 1 - On Bed With Sakuya"
    hide screen main_menu
    scene sakuyabed1
    show smslogo:
        align(0.89, -0.05)
    show artist_sig:
        align(1.0, 0.0)
    with Dissolve(1.0)
    # Animation and stuff.
    hide smslogo with Dissolve(0.4)
    hide artist_sig with Dissolve(0.4)
    
    pause 1
    
    $ quick_menu = True
    
    window show Dissolve(0.2)
    s "..."
    
    pause 0.5
    
    play music bedsong  # Might want to delete this.
    
    s "Hola."
    
    s "Parece que querias terminarlo todo.."
    
    scene sakuyabed6 with Dissolve(1)
    
    s "Menos mal que vine en el ultimo momento."
    
    s "Me alegra que puedas estar conmigo hoy."
    
    show screen choice2("Por que me salvaste?", "No se supone que lo fuera a hacer", "scene1choice1", "scene1choice1", 1103, 407, 1049, 524)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:  # Day1choice1
        "por que me salvaste?":  #x="735"  y="271"
            pass
        
        "No se supone que lo fuera a hacer":  #x="699"  y="349"
            pass
            
label scene1choice1:
    
    hide screen choice2 with Dissolve(0.2)
            
    scene sakuyabed1 with Dissolve(1)
    
    s "Bueno, nunca quise entrometerme."
    
    s "Creeme , Te habria dejado solo y nunca habria interferido."
    
    pause 0.5
    
    s "Pero..."
    
    s "Alguien que te ha estado observando un poco sintió que, en el fondo, en realidad no querías que terminara.."
    
    pause 0.5
    ## asd
    s "Era débil, pero tu alma estaba pidiendo ayuda, rogando por otra oportunidad en la vida."
    
    scene sakuyabed5 with Dissolve(1)
    
    s "¡Así que, naturalmente, me ofrecí como voluntaria para ayudar!"
    
    scene sakuyabed6 with Dissolve(1)
    
    s "Independientemente, estoy aquí para ti."
    
    show screen choice1("Que quieres de mi?", "scene1choice2", 1091, 152)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:  # Day1choice2
        "Que quieres de mi?":  #x="727"  y="101"
            pass

label scene1choice2:
    
    hide screen choice1 with Dissolve(0.2)
    
    scene sakuyabed3 with Dissolve(1)
    
    s "Yo solo quiero una cosa."
    
    s "Que te mejores."
    
    scene sakuyabed1 with Dissolve(1)
    
    s "Mas específicamente, Quiero que duermas un poco. Se ve que no lo sueles hacer, Lo puedo ver con tan solo mirar a tus ojos ."
    
    show screen choice1("No puedo dormir", "scene1choice3", 366, 471)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:  # Day1choice2
        "No puedo dormir":  #x="244"  y="314"
            pass
    
label scene1choice3:
    
    hide screen choice1 with Dissolve(0.2)

    pause 0.5
    
    s "Hmm..."
    
    pause 0.5
    
    s "Se lo dificil que es tener sueño."

    scene sakuyabed3 with dissolve
    
    s "Solo quiero que recuerdes esto."
    
    scene sakuyabed1 with dissolvepp
    
    s "Lo que hiciste en el pasado, no importa ahora."
    
    s "Lo que sea que creas que va a pasar en el futuro, Tampoco importa aqui."
    
    scene sakuyabed3 with dissolve
    
    s "Nada importa ahora mismo ."
    
    scene sakuyabed6 with dissolve
    
    s "La unica cosa que importa ahora mismo, Es cerrar tus ojos, y dormir lo suficiente."
    
    scene sakuyabed3 with dissolve
    
    s "Eso es todo, nada más importa excepto que tú duermas."
    
    scene sakuyabed6 with dissolve
    
    s "Yo de hecho tambien estoy cansada, !Fue un trabajo divertido pero realmente deberia dormir ahora "
    
    scene sakuyabed3 with dissolve
    
    s "Asi que descansare aqui contigo."
    
    scene sakuyabed1 with dissolve
    
    s "seuramente te des cuenta de que, cuanto mas intentas dormir, mas te cuesta cerrar los ojos."
    
    s "Uno no deveria \"intentar\" dormir, deveria ser tan natural como caminar."
    
    s "Una vez que te dejes ir y dejes de pensar, estoy segura de que descubrirás que es mucho más fácil dormir un poco.."
    
    scene sakuyabed3 with dissolve
    
    s "con eso dicho, tomate todo el tiempo que necesites."
    
    s "Puedes solo mirarme si eso te ayuda a dormir."
    
    scene sakuyabed6 with dissolve
    
    s "Siempre que estés listo."
    
    scene sakuyabed5 with dissolve
    
    s "Estoy a tu lado."
    
    scene black with Dissolve(1)
    stop music fadeout 1  ## Additional
    $ save_name = "Day 2 - Cooking With Sakuya"
    
    s "ven aquiii~ necesito que me ayudes con algo!"
    
    play music cookingsong
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "Hey, ahi estas!"
    
    s "Parece que has descansado vien."
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "Solo con mirar tus ojos."
    
    show screen choice2("Todo gracias a ti.", "Realmente lo necesitaba.", "scene1choice4a", "scene1choice4b", 1382, 203, 74, 224)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Todo gracias a tí.":  # x="921"  y="135"
            
            scene sakuyacooking1 with Dissolve(1)
            
            s "Me alegro de haber podido ayudar, dormir lo sufuciente es esencial para el dia a dia!"
        
        "Realmente lo necesitaba.":  # x="49"  y="149"
        
            scene sakuyacooking1 with Dissolve(1)
            
            s "Bueno, apuesto a que lo hiciste!, Parecías estar al borde de la muerte."
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "Bueno, eso probablemente no sea una exajeracion."

label scene1choice4a:
    
    hide screen choice2
    
    scene sakuyacooking1 with Dissolve(1)
            
    s  "dormir lo suficiente es fundamental para el dia a dia!"
    
    jump scene1choice4
    
label scene1choice4b:
    
    hide screen choice2
    
    scene sakuyacooking1 with Dissolve(1)
            
    s "Bueno, apuesto a que lo hiciste! Parecías estar al borde de la muerte."
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "Bueno, probablemente eso no sea una exageración de todos modos.."
    
label scene1choice4:
    
    scene sakuyacooking3 with dissolve
    
    s "De todos modos, es bueno que haya sucedido."
    
    s "¡Esta tarea que voy a hacer que hagas requiere que te mantengas alerta!"
    
    show screen choice1("Que vamos a hacer?", "scene1choice5", 1353, 189)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Que vamos a hacer?":  #x="902"  y="126"
            pass
            
label scene1choice5:
    
    hide screen choice1 with Dissolve(0.2)
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "Voy a hacer que hagas algo de comida!"
    
    scene sakuyacooking2 with Dissolve(1)
    
    s "Mas especificamente..."
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "Vas a hacer ensalada de fruta!"
    
    show screen choice2("Nunca he hecho esto antes.", "Me gusta la fruta!", "scene1choice6a", "scene1choice6b", 1316, 161, 131, 176)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Nunca he hecho esto antes.":  # x="877"  y="107"
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "Hmm, ¿es así??"  # So Nanoka??
            
            scene sakuyacooking1 with Dissolve(1)
            
            s "Bueno, no te preocupes por eso!"
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "Mis cuchillos siempre están afilados como una navaja, por lo que harán la mayor parte del trabajo por ti."
            
        "Me gusta la fruta!":  # x="87"  y="117"
            
            s "Es bueno oir eso!"
            
            s "Tambien me gusta la fruta!"
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "Puedes hasta hacer te con fruta."
            
label scene1choice6a:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyacooking4 with Dissolve(1)
            
    s "Hmm, es así?"  # So Nanoka??
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "Bueno, no te preocupes por eso!"
    
    scene sakuyacooking4 with Dissolve(1)
    
    s 
    "Mis cuchillos siempre están afilados como una navaja, por lo que harán la mayor parte del trabajo por ti."
    
    jump scene1choice6
    
label scene1choice6b:
    
    hide screen choice2 with Dissolve(0.2)
    
    s "Eso es bueno oirlo!"
            
    s "Tambien me gusta la fruta!"
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "Puedes hasta hacer te con fruta."
    
label scene1choice6:
            
    scene sakuyacooking1 with Dissolve(1)
            
    s "Bueno, en cualquier caso, comencemos."
            
    s "Toma este cuchillo."
            
    s "Voy a tirar estas frutas al aire y tú haces todo lo posible para cortarlas."
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "No te preocupes si no crees que puedas cortar la fruta a tiempo."
    
    scene sakuyacooking3 with Dissolve(1)
    
    s "Digamos que te daré todo el tiempo que necesites."
    
    scene sakuyacooking1 with dissolve
    
    s "¡Aquí vamos! Corta esta fruta!"
    
    # Fruit button screen
    # Note:
    #   - All fruits are align(0.5, 0.5)  // Use its exact coordinate and size
    #   - Order: banana, orange, apple
    #   - When clicked, do hpunch and play sound "cutstuff.ogg"
    #   - Dissolve(1) for fruit comes in.
    
    show screen fruit_screen("fruits.png", "scene1banana", 557, 252)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
label scene1banana: # banana_cut
    
    play sound cutstuff
    with hpunch
    hide screen fruit_screen with Dissolve(0.2)
    
    scene sakuyacooking2 with dissolve
    
    s "Buen trabajo!"
    
    scene sakuyacooking3 with dissolve
    
    s "Aqui viene la siguiente!"
    
    show screen fruit_screen("orange.png", "scene1orange", 470, 126)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
label scene1orange: # orange_cut
    
    play sound cutstuff
    with hpunch
    hide screen fruit_screen with Dissolve(0.2)
    
    scene sakuyacooking1 with dissolve
    
    s "Aqui viene la ultima!"
    
    show screen fruit_screen("apple.png", "scene1apple", 530, 165)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
label scene1apple: # apple_cut
    
    play sound cutstuff
    with hpunch
    hide screen fruit_screen with Dissolve(0.2)
    
    scene sakuyacooking3 with dissolve
    
    s "Maravilloso!"
            
    scene sakuyacooking1 with dissolve
    
    s "Ahora mézclalo todo en ese cuenco y pásamelo!"
    
    scene sakuyasalad1 with dissolve
    
    s "Vamos a ver que tas sabe esto!"
    
    scene sakuyasalad2 with dissolve
    
    s "Delicioso!"
    
    s "Sabe aún mejor, especialmente porque lo hiciste tú!"
    
    scene sakuyacooking1 with dissolve
    
    s "Bueno, espero que todo el proceso haya sido agradable para ti.."
    
    s "Pero..."
    
    scene sakuyacooking4 with dissolve
    
    s "También había otro punto en esto.."
    
    scene sakuyacooking3 with dissolve
    
    s "Es posible que tengas algunos problemas en ti vida."
    
    s "Este tipo de cosas que van pasando por tu mente, No importa que tan duro lo intentes."
    
    s "Pensamientos de \"qué pasaría si\", arrepentimiento de elecciones pasadas, ansiedad por el futuro..."
    
    scene sakuyacooking4 with dissolve
    
    s "Es bastante molesto cuando eso sucede, ¿no?"
    
    s "Sin embargo..."
    
    scene sakuyacooking3 with dissolve
    
    s "Estoy dispuesto a apostar que no estabas pensando en esas cosas mientras estabas ocupado cortando esa fruta conmigo, ¿verdad?"
    
    scene sakuyacooking2 with dissolve
    
    s "Es importante mantener la mente ocupada con actividades saludables como estas."
    
    scene sakuyacooking1 with dissolve
    
    s "¡Funciona de maravilla para combatir esos pensamientos desagradables y, en general, es excelente para tu bienestar!"
    
    scene sakuyacooking2 with dissolve
    
    s "Espero que esto te haya servido de algo.."
    
    scene sakuyacooking1 with dissolve
    
    s "¡Eso es todo lo que tengo que decir por ahora!"
    
    s "¡Hasta mañana! ¡Cuídate!"
    
    stop music fadeout 1
    
    scene black with Dissolve(1)
    
    pause 0.5
    
    $ save_name = "Day 3 - Sakuya's Experiment"
    
    scene smstea with Dissolve(1)
    
    play music teasong
    
    s "¡Bienvenido de nuevo!"
    
    s "Pude terminar mis tareas del día antes de lo habitual, ¡así que decidí llamarte aquí!"
    
    s "So, it's your third day here so far."
    
    s "Espero que te haya gustado esta humilde mansión.."
    
    show screen choice1("¿Esta es tu habitación?", "scene1choice7", 320, 197)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "¿Esta es tu habitación?":  # x="213"  y="131"
            pass

label scene1choice7:
    
    hide screen choice1 with Dissolve(0.2)

    s "¡Porque?, si!"
    
    s "Esta es de hecho mi habitación."
    
    s "¡Nada es mejor que venir aquí con una buena taza de té después de un largo día de arduo trabajo!"
    
    scene sakuyatea2 with Dissolve(1)
    
    s "Pero debes estar preguntándote por qué te traje aquí."
    
    s "Necesito hacer un pequeño experimento contigo."
    
    s "Eres un ser humano bastante peculiar, todos en la mansión, incluso la señora, sienten curiosidad por ti."
    
    scene sakuyatea6 with Dissolve(1)
    
    s "Por lo tanto, como Head Maid de esta mansion, es mi deber satisfacer estas necesidades."
    
    scene sakuyatea4 with Dissolve(1)
    
    s "¡Espero que no te importe!"
    
    s "¡Nunca haría nada que te haga sentir incómodo!"
    
    show screen choice2("Cualquier cosa por ti", "Estoy un poco nervioso.", "scene1choice8a", "scene1choice8b", 150, 171, 1364, 189)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Cualquier cosa por ti":  # x="100"  y="114"
            
            scene sakuyatea6 with Dissolve(1)
            
            s "Por que, ¡gracias!"
            
            s "Me alegro de que hayas depositado tu confianza en mi."
            
        "Estoy un poco nervioso.":  # x="909"  y="126"  - In script, ignores the following dialogues
            
            scene sakuyatea3 with Dissolve(1)
            
            s "¿Es eso así?"
            
            scene sakuyatea2 with Dissolve(1)
            
            s "Bueno, puedes confiar en mí en este, estarás completamente seguro."
    
label scene1choice8a:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea6 with Dissolve(1)
              
    s "Por que, ¡gracias!"
    
    s "Me alegro de que hayas depositado tu confianza en mí."
    
    jump scene1choice8
    
label scene1choice8b:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea3 with Dissolve(1)
            
    s "¿Es eso así?"
    
    scene sakuyatea2 with Dissolve(1)
    
    s "Bueno, puedes confiar en mí en este, estarás completamente seguro."
    
label scene1choice8:
    
    scene sakuyatea2 with Dissolve(1)
    
    s "Ahora, acércate."
    
    stop music fadeout 2
    
    s "Quiero que te acuestes en mi regazo."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    play music laying_down_song_re
    
    s "Espero que haya suficiente amortiguación a tu gusto.."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Es simple"
    
    s "Solo contesta estas preguntas por mí y te daré un perfil extenso que coincide con quien eres."
    
    s "Puede ayudarte a entenderte mejor a ti mismo."
    
    scene sakuyaquiz4 with Dissolve(1)
    
    s "Solo sé tan honesto como puedas."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "No hay respuesta incorrecta!"
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Ahora, comencemos."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "pregunta numero 1:"
    
    s "por que odias vivir?"  # player: *Big shock* O.O
    
    show screen choice3("Duele estar vivo", "No puedo hacer frente a mi pasado", "Mi futuro es extremadamente sombrío", "scene1choice9", "scene1choice9", "scene1choice9", 1233, 125, 1230, 249, 1250, 362)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Duele estar vivo":  # x="822"  y="83"
            pass
            
        "No puedo hacer frente a mi pasado":  # x="820"  y="166"
            pass
            
        "Mi futuro es extremadamente sombrío":  # x="833"  y="241"
            pass
    
label scene1choice9:
    
    hide screen choice3 with Dissolve(0.2)
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Ya veo...."
    
    s "Siguiente pregunta:"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "¿Qué es lo que más piensas?"
    
    show screen choice3("Sigo pensando en errores pasados.", "Sigo pensando en el futuro incierto", "No pienso en absoluto.", "scene1choice10", "scene1choice10", "scene1choice10", 1133, 125, 1130, 249, 1150, 362)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Sigo pensando en errores pasados.":  # x="822"  y="83"
            pass
            
        "Sigo pensando en el futuro incierto":  # x="820"  y="166"
            pass
        
        "No pienso en absoluto..":  # x="833"  y="241"
            pass
    
label scene1choice10:
    
    hide screen choice3 with Dissolve(0.2)
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Ya veo..."
    
    s "Solo unas pocas preguntas más."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "¿Por qué lo hiciste?"
    
    show screen choice3("Me lo dijeron.", "No tenía otra opción.", "No pertenecía a ningún otro lugar.", "scene1choice11", "scene1choice11", "scene1choice11", 1386, 123, 1325, 248, 1290, 353)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Me lo dijeron.":  # x="924"  y="82"
            pass
            
        "No tenia otra opcion.":  # x="883"  y="165"
            pass
            
        "No pertenecía a ningún otro lugar.":  # x="860"  y="235"
            pass

label scene1choice11:
    
    hide screen choice3 with Dissolve(0.2)

    scene sakuyaquiz5 with Dissolve(1)
    
    s "¡Lo estás haciendo muy bien hasta ahora! ¡Casi estámos allí!"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "¿A quién culpas de todo?"
    
    show screen choice3("a mi mismo", "a el mundo", "a nadie", "scene1choice12", "scene1choice12", "scene1choice12", 1452, 123, 1412, 251, 1428, 356)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "a mi mismo":  # x="968"  y="82"
            pass
            
        "a el mundo":  # x="941"  y="167"
            pass
            
        "a nadie":  # x="952"  y="237"
            pass
            
label scene1choice12:
    
    hide screen choice3 with Dissolve(0.2)
            
    scene sakuyaquiz3 with Dissolve(1)
    
    s "¡Muy bien! ¡Última pregunta!"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "¿Dónde le gustaría ser enterrado?"
    
    show screen choice3("bajo un arbol", "Debajo De Un Pequeño Ataúd En Una Mansión.", "Déjame pudrirme en el suelo", "scene1choice13", "scene1choice13", "scene1choice13", 1404, 123, 1247, 249, 1320, 357)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "bajo un arbol":  # x="936"  y="82"
            pass
            
        "Debajo De Un Pequeño Ataúd En Una Mansión.":  # x="831"  y="166"
            pass
            
        "Déjame pudrirme en el suelo":  # x="880"  y="238"
            pass

label scene1choice13:
    
    hide screen choice3 with Dissolve(0.2)

    scene sakuyaquiz4 with Dissolve(1)
    
    s "¡Bueno, gracias!"
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "Ahora tengo suficiente información."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Esto es lo que pienso."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Eres una persona ansiosa por naturaleza."
    
    s "Tiene sus esperanzas y aspiraciones, pero necesita un buen empujón o dos en la dirección correcta para lograrlas."
    
    s "Tienes mucha tristeza en tu corazón. Necesitas algo o alguien que te ayude a dejar de dejar que tus penas se acumulen en ti."
    
    s "A menudo se queman muchos puentes, pero solo por necesidad."
    
    s "Necesitas aprender a perdonarte, a veces eres demasiado duro contigo mismo."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "¿Qué piensas?"
    
    s "Bastante preciso, ¿verdad?"
    
    show screen choice2("Es preciso.", "No exactamente...", "scene1choice14", "scene1choice14", 1401, 177, 149, 170)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Es preciso.":  # x="934"  y="118"
            pass
        
        "No exactamente...":  # x="99"  y="113"
            pass
    
label scene1choice14:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Bueno, es gracioso que digas eso."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "La verdad es que lo inventé todo."
    
    s "Iba a darte esa respuesta sin importar la opción que elijas."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Creo que para entender quién eres realmente, tendría que pasar más tiempo contigo y llegar a conocerte mejor."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "Lo cual estoy más que feliz de complacer."
    
    show screen choice2("Estoy confuso...", "¿Cuál era el punto?", "scene1choice15", "scene1choice15", 1386, 186, 108, 179)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Estoy confuso...":  # x="924"  y="124"
            pass
            
        "¿Cuál era el punto?":  # x="72"  y="119"
            pass
    
label scene1choice15:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyaquiz4 with Dissolve(1)
    
    s "Bueno, para ser honesta, ¡solo quería que descansaras en mi regazo!"
    
    s "Ehehehe!"
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Aparte de eso, hice esto para probarte algo."
    
    s "Que realmente no importa lo que yo u otras personas te perciban como."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Siempre eres libre de moldear tu propio destino."
    
    s "Solo importan aquellos que te aceptan por lo que eres y lo que quieres hacer."
    
    show screen choice2("No me gusta quien soy.", "Nadie me acepta.", "scene1choice16", "scene1choice16", 117, 176, 1349, 194)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "No me gusta quien soy.":  # x="78"  y="117"
            pass
            
        "Nadie me acepta.":  # x="899"  y="129"
            pass
    
label scene1choice16:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Bueno, lo creas o no, me siento identificado."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "No siempre fui como la persona que ves ante ti."
    
    s "Me sentía sola y aislada de los demás."
    
    s "Incluso cuando trabajaba en esta mansión, seguía siendo bastante cruel con los humanos, e incluso con los que me rodeaban."
    
    s "Pensé \"Mientras tenga una cama para dormir, no necesito nada más\"."
                                                              
    s "Al final del día, sólo pensaba en mí."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Pero, como estoy seguro de que sabes, estaba resolviendo un incidente."
    
    s "Había una enorme e inusual cantidad de lirios araña rojos creciendo por todas partes."
    
    s "Bueno, resumiendo la historia..."
    
    s "Me di cuenta, después de ese incidente, que las cosas que hacemos, importan."
    
    s "Incluso las acciones más pequeñas, más insignificantes que hago, también importan."
    
    s "Tengo un impacto en la gente, grande o pequeño, y eso acabará teniendo un impacto en mí, me dé cuenta o no."
    
    scene sakuyaquiz3 with Dissolve(1)
    
    s "Así que, a partir de entonces, quise ser cálido y amable con los que me rodeaban."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "Bueno, la mayor parte."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Algunas personas realmente necesitan un buen \"regañando\" antes de que puedas poner algo de sentido común en ellos."
    
    s "Sé amable hasta que llegue el momento de no serlo"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Creo que es un buen lema para vivir."
    
    s "Sólo quiero que entiendas esto."
    
    scene sakuyaquiz3 with Dissolve(1)
    
    s "Al igual que nunca fue demasiado tarde para mí para cambiar mis costumbres, ¡tampoco es demasiado tarde para cambiar las tuyas!"
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Es decir, para las cosas que quieres cambiar."
    
    s "Siempre habrá partes de nosotros que no cambiaríamos por nada de el mundo."
    
    scene sakuyaquiz3 with Dissolve(1)
    
    s "¡Y eso está muy bien!"
    
    s "Sólo tenemos que rodearnos de aquellos que nos quieren por lo que somos."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Pero, por supuesto, si no tienes a nadie, también está bien."
    
    s "Ser capaz de recorrer tu propio camino por ti mismo es toda una virtud."
    
    s "Y en el camino, puede que encuentres lo que buscas o a quien buscas desde el principio."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "Que conste que te acepto por lo que eres y por lo que quieres ser."
    
    scene sakuyaquiz4 with Dissolve(1)
    
    s "Estoy aquí para ti, siempre."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Bueno, eso es todo lo que tengo que decir."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Puedes seguir acostado en mi regazo todo el tiempo que quieras."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Cuando estés preparado, podemos pasar al día siguiente."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Pero, tómate el tiempo que necesites."
    
    s "Yo te tengo."
    
    scene sakuyaquiz4 with Dissolve(1)
    
    scene black with Dissolve(1)
    
    stop music fadeout 2
    
    pause 2.0
    
    return


label scene2:  ############################################################################################# SCENE 2 ##
    
    $ save_name = "Day 4 - Fishing With Sakuya"
    
    scene sakuyafishing1 with dissolve
    
    play music fishing_song
    
    s "¡Hagamos algo diferente hoy!"
    
    s "Esta mansión tiene un gran lago que la rodea."
    
    s "¡Y quién sabe qué clase de criaturas acechan en él!"
    
    scene sakuyafishing2 with dissolve
    
    s "Es el momento perfecto para ir a pescar, diría yo."
    
    show screen choice1("Necesitas algo de ayuda!", "scene2choice1", 945, 257)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Necesitas algo de ayuda!":  # x="630"  y="171"
            pass

label scene2choice1:
    
    hide screen choice1 with Dissolve(0.2)

    scene sakuyafishing1 with dissolve
    
    s "Por supuesto!."
    
    scene sakuyafishing2 with dissolve
    
    s "No te traería aquí sólo para mirar."
    
    s "La pesca se parece mucho a la vida real."
    
    s "Cuando pique, encontrará cierta resistencia."
    
    scene sakuyafishing1 with dissolve
    
    s "Naturalmente, hay que luchar contra la marea."
    
    s "De lo contrario, perderás lo que tanto te costó conseguir."
    
    scene sakuyafishing2 with dissolve
    
    s "Por supuesto, a veces nos resulta demasiado difícil aguantar, así que debemos soltarlo e intentarlo de nuevo."
    
    scene sakuyafishing1 with dissolve
    
    s "No hay que avergonzarse de ello."
    
    scene sakuyafishing2 with dissolve
    
    s "Piensa en algo que hayas querido o intentado conseguir en la vida."
    
    s "¿Te has encontrado con algunas dificultades en el camino? Seguro que sí."
    
    scene sakuyafishing1 with dissolve
    
    s "Casi todo lo que vale la pena hacer en la vida va a ser difícil de una manera u otra."
    
    s "¿Te defiendes o lo dejas pasar?"
    
    s "¿Lo intentas de nuevo o intentas coger otra cosa?"
    
    scene sakuyafishing2 with dissolve
    
    s "no hay decisión equivocada, cualquiera está bien."
    
    scene sakuyafishing1 with dissolve
    
    s "La única decisión equivocada es no tomar ninguna."
    
    scene sakuyafishing2 with dissolve
    
    with hpunch
    
    s "*SNAP*"
    
    scene sakuyafishing1 with dissolve
    
    stop music fadeout 1
    
    s "¡Oh, Dios! ¡Parece que ya tenemos algo!."
    
    scene iydcl with Dissolve(1)
    
    play music catchfishsong
    
    s "Hnnnnng, esto es realmente difícil, ¡no estoy seguro de poder hacerlo!"
    
    show screen choice2("¡¡¡PUEDES HACERLO!!!", "¡¡CREO EN TI!!", "scene2choice2", "scene2choice2", 66, 171, 42, 279)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "¡¡¡PUEDES HACERLO!!!":  # x="44"  y="114"
            pass
            
        "¡¡CREO EN TI!!":  # x="28"  y="186"
            pass

label scene2choice2:
    
    hide screen choice2 with Dissolve(0.2)

    s "Jaja, ¡gracias!"
    
    s "Pero aún así, es realmente..."
    
    scene sakuyafrogwater with dissolve
    
    with hpunch
    
    s "¡Ooooh! ¡¡¡Puedo sentir que algo vieneiiiii!!!"
    
    show screen choice2("¡¡SIGUE ADELANTE!! ¡¡YA CASI LLEGAS!!", "PASE LO QUE PASE, ¡ESTOY AQUÍ PARA TI!", "scene2choice3", "scene2choice3", 150, 287, 150, 437)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "¡¡SIGUE ADELANTE!! ¡¡YA CASI LLEGAS!!":  # x="100"  y="191"
            pass
            
        "PASE LO QUE PASE, ¡ESTOY AQUÍ PARA TI!":  # x=""  y=""
            pass 
            
label scene2choice3:
    
    hide screen choice2 with Dissolve(0.2)
    
    with hpunch
    
    s "Haaaaaaaaaaaaaaaaah!"
    
    scene iyde9o with dissolve
    
    s "Woah!!!"
    
    stop music fadeout 1
    
    s "¿Qué es esta cosa?"
    
    scene sakuyafishing3 with Dissolve(1)
    
    play music fishing_song
    
    s "Bueno, gracias por tus palabras de ánimo."
    
    s "No estoy seguro de haber podido hacerlo sin ti."
    
    show screen choice2("¡Podrías haberlo hecho!", "Fue divertido!", "scene2choice4a", "scene2choice4a", 818, 546, 890, 651)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "¡Podrías haberlo hecho!":  # x="545"  y="364"
            
            scene sakuyafishing4 with dissolve
            
            s "Jaja, puede que sea así."
            
            s "Pero, fue divertido, ¿no?"
            
            scene sakuyafishing3 with dissolve
            
            s "¿No es agradable animar a alguien en quien crees, y viceversa?"
            
            s "Definitivamente creo que sí."
            
        "Fue divertido!":  # x="593"  y="410"
            
            s "De hecho... ¡Seguro que fue bonito animar y apoyar a la persona que apoyas!"
            
label scene2choice4a:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyafishing4 with dissolve
            
    s "Jaja, puede que sea así."
    
    s "Pero, fue divertido, ¿no?"
    
    scene sakuyafishing3 with dissolve
    
    s "¿No es agradable animar a alguien en quien crees, y viceversa?"
    
    s "Definitivamente creo que sí."
    
    jump scene2choice4

label scene2choice4b:
    
    hide screen choice2 with Dissolve(0.2)
    
    s "De hecho... ¡Seguro que fue bonito animar y apoyar a la persona que apoyas!"
            
label scene2choice4:
    
    scene sakuyafishing4 with dissolve
    
    s "Siempre es bueno tener aunque sea una sola persona que te apoye."
    
    s "Ahora..."
    
    s "¿Qué opinas de comer ancas de rana?"
    
    show screen choice2("No estoy seguro de eso.", "¡Suena delicioso!", "scene2choice5a", "scene2choice5b", 746, 662, 764, 548)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "No estoy seguro de eso.":  # x="497"  y="441"
            
            s "Hmm, está bien, a veces, es natural estar inseguro sobre este tipo de cosas."
            
            scene sakuyafishing3 with dissolve
            
            s "Pero te aseguro que si lo cocinara, probablemente sería una de las mejores cosas que hayas probado en toda tu vida."
            
        "¡Suena delicioso!":  # x="509"  y="365"
            
            scene sakuyafishing3 with dissolve
            
            s "Oh, ¿realmente lo crees?."
            
            s "Apuesto a que no te decepcionará."
            
label scene2choice5a:
    
    hide screen choice2 with Dissolve(0.2)
    
    s "Hmm, está bien, a veces, es natural estar inseguro sobre este tipo de cosas."
            
    scene sakuyafishing3 with dissolve
    
    s "Pero te aseguro que si lo cocinara, probablemente sería una de las mejores cosas que hayas probado en toda tu vida."
    
    jump scene2choice5
    
label scene2choice5b:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyafishing3 with dissolve
            
    s "¿De verdad lo crees?"
    
    s "Apuesto a que no te decepcionará."
    
label scene2choice5:
            
    scene sakuyafishing4 with dissolve
    
    s "Dicho esto, esta es una rana muy inusual."
    
    s "Mi señora tiene afinidad por este tipo de criaturas interesantes."
    
    s "Sabías que incluso tenía un chupacabras como mascota?"
    
    s "Se lo enseñaré primero y dejaré que ella decida lo que quiere hacer con él."
    
    scene sakuyafishing3 with dissolve
    
    s "Me pregunto cómo deberíamos llamarlo..."
    
    scene sakuyafishing4 with dissolve
    
    s "Hmmm...."
    
    s "¡Ya lo tengo!"
    
    s "Su nombre deveria ser..."
    
    scene sakuyafishing3 with dissolve
    
    s "Henry."
    
    scene sakuyafishing4 with dissolve
    
    s "Es un bonito nombre, ¿no crees?"
    
    show screen choice6
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Es un gran nombre!":  # x="-3"  y="341"
            pass
            
        "No se me podría haber ocurrido un nombre mejor":  # x="413"  y="368"
            pass
            
        "¡Me encanta el nombre!":  # x="522"  y="240"
            pass
            
        "¡Al ama le encantará el nombre!":  # x="485"  y="427"
            pass
            
        "Es el nombre perfecto.":  # x="980"  y="426"
            pass
            
        "Creo que llamaré a nuestro hijo Henry.":  # x="513"  y="3"
            pass
            
label scene2choice6:
            
    hide screen choice6 with Dissolve(0.2)
            
    scene sakuyafishing3 with dissolve
    
    s "Hehehe!"  # Ehe te nandayo!
    
    scene black with Dissolve(1)
    
    stop music fadeout 1
    
    $ save_name = "Day 5 - Pool Time With Sakuya"
    
    pause 2
    
    play music poolambeince 
    
    s "No puedo recordar la última vez que estuve en uno de estos..."
    
    scene sakuyapoolside4 with Dissolve(1)
    
    s "Ah, hace tiempo que no vengo por aquí."
    
    scene sakuyapoolside3 with dissolve
    
    s "Sabes, este lugar tiene algo de historia detrás."
    
    s "Aunque no fue hace tanto tiempo, siento una extraña nostalgia por ello."
    
    scene sakuyapoolside4 with dissolve
    
    s "Supongo que a veces no podemos evitar rememorar el pasado."
    
    scene sakuyapoolside3 with dissolve
    
    s "¿Qué te parece? ¿te gustaría saber más sobre esta zona?"
    
    show screen choice2("¡Claro!", "Prefiero sumergirme.", "scene2choice7a", "scene2choice7b", 1373, 434, 1382, 278)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "¡Claro!":  # x="915"  y="289"
            
            scene sakuyapoolside4 with Dissolve(1)
            
            s "¡Genial! Estoy encantado de explicarlo"
            
            s "Fue poco después del incidente de las flores del que hablé antes."
            
            s "Mi señora fue convencida de participar en un plan muy extravagante."
            
            scene sakuyapoolside3 with dissolve
            
            s "¿El plan? Nada menos que llevar una misión furtiva a la Luna."
            
            scene sakuyapoolside4 with dissolve
            
            s "Hemos tenido nuestra cuota de resolución de incidentes y de aventuras."
            
            s "Así que, naturalmente, no tuvimos ningún problema en complacerlos, esto también fue emocionante para nosotros."
            
            scene sakuyapoolside1 with Dissolve(1)
            
            s "Sin embargo, era complicado, teníamos que construir una especie de cohete a la luna, nos faltaban referencias de cómo debería funcionar y ser."
            
            scene sakuyapoolside4 with dissolve
            
            s "Por suerte, pude conseguir las referencias perfectas gracias a una revista que conseguí en una tienda de lo más curiosa."
            
            scene sakuyapoolside3 with Dissolve(1)
            
            s "¡Deberías haber visto la cara de la señora Patchouli! Estaba extasiada."
            
            scene sakuyapoolside2 with dissolve
            
            s "Finalmente, gracias a los esfuerzos de todos, llegamos a la luna."
            
            scene sakuyapoolside3 with dissolve
            
            s "El tiempo era perfecto, las olas eran hermosas y la brisa fresca en la cara se sentía celestial."
            
            s "Así que, cuando llegó la hora de volver a casa, Patchouli ayudó a montar esta piscina cubierta para que pudiéramos llevarnos un poco de la luna cuando volviéramos a casa."
            
            scene sakuyapoolside4 with dissolve
            
            s "Así que, cuando llegó la hora de volver a casa, Patchouli ayudó a montar esta piscina cubierta para que pudiéramos llevarnos un poco de la luna cuando volviéramos a casa."
            
            s "Pero ya sabes..."
            
            scene sakuyapoolside3 with Dissolve(1)
            
            s "Hicimos esta piscina cubierta después de la lucha en la luna, pero nunca tuve la oportunidad de nadar en ella."
            
            scene sakuyapoolside4 with dissolve
            
            s "Así que... basta de hablar."
            
        "Prefiero sumergirme.":  # x="921"  y="185"
            
            s "¡Estoy de acuerdo!"
            
            scene sakuyapoolside4 with dissolve
            
            s "De todos modos, puedes preguntarme cuando quieras más adelante."
            
label scene2choice7a:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyapoolside4 with Dissolve(1)
            
    s "¡Genial! Estoy encantado de explicarlo."
    
    s "Fue poco después del incidente de las flores del que hablé antes."
    
    s "Mi señora fue convencida de participar en un plan muy extravagante."
    
    scene sakuyapoolside3 with dissolve
    
    s "¿El plan? Nada menos que llevar una misión furtiva a la Luna."
    
    scene sakuyapoolside4 with dissolve
    
    s "Hemos tenido nuestra cuota de resolución de incidentes y de aventuras."
    
    s "Así que, naturalmente, no tuvimos ningún problema en complacerlos, esto también fue emocionante para nosotros."
    
    scene sakuyapoolside1 with Dissolve(1)
    
    s "Sin embargo, era complicado, teníamos que construir una especie de cohete a la luna, nos faltaban referencias de cómo debería funcionar y ser."
    
    scene sakuyapoolside4 with dissolve
    
    s "Por suerte, pude conseguir las referencias perfectas gracias a una revista que conseguí en una tienda de lo más curiosa."
    
    scene sakuyapoolside3 with Dissolve(1)
    
    s "¡Deberías haber visto la cara de la señora Patchouli! Estaba extasiada."
    
    scene sakuyapoolside2 with dissolve
    
    s "Finalmente, gracias a los esfuerzos de todos, llegamos a la luna."
    
    scene sakuyapoolside3 with dissolve
    
    s "El tiempo era perfecto, las olas eran hermosas y la brisa fresca en la cara se sentía celestial."
    
    s "¡Mi señora incluso hizo un viaje alrededor de la luna!"
    
    scene sakuyapoolside4 with dissolve
    
    s "Así que, cuando llegó la hora de volver a casa, Patchouli ayudó a montar esta piscina cubierta para que pudiéramos llevarnos un poco de la luna cuando volviéramos a casa."
    
    s "Pero usted sabe..."
    
    scene sakuyapoolside3 with Dissolve(1)
    
    s "Hicimos esta piscina cubierta después de la lucha en la luna, pero nunca tuve la oportunidad de nadar en ella."
    
    scene sakuyapoolside4 with dissolve
    
    s "Así que... basta de hablar."
    
    jump scene2choice7
    
label scene2choice7b:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "Estoy de acuerdo!"
            
    scene sakuyapoolside4 with dissolve
    
    s "De todos modos, puedes preguntarme cuando quieras más adelante."
    
label scene2choice7:
    
    scene sakuyapoolside3 with Dissolve(1)
    
    s "Vamos a entrar de lleno."
    
    scene sakuyapool1 with dissolve
    
    s "¿Le gusta nadar?"
    
    s "Sé que la piscina puede ser un poco pequeña, pero..."
    
    show screen choice2("Es divertido", "Solo por que estas aqui", "scene2choice8", "scene2choice8", 818, 488, 696, 393)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu: 
        "Es divertido":  # x="545"  y="325"
            pass
        "Solo por que estas aqui":  # x="464"  y="262"
            pass
            
label scene2choice8:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyapool4 with Dissolve(1)
    
    s "¡Ja! Me alegro de oírlo."
    
    scene sakuyapool1 with dissolve
    
    s "Bueno, de cualquier manera..."
    
    scene sakuyapool3 with Dissolve(1)
    
    s "Es importante probar cosas nuevas y descubrir cosas sobre uno mismo a través de estas actividades."
    
    scene sakuyapool4 with Dissolve(1)
    
    s "For example, let's take what we just did right now. Swimming."
    
    s "¿Lo disfrutaste? ¿Fue divertido? ¿Se te dio bien? ¿Qué aspectos te gustaron o te disgustaron?"
    
    scene sakuyapool1 with dissolve
    
    s "Evidentemente, no tienes que escribir un ensayo cada vez que pruebes algo nuevo."
    
    s "Pero el mero hecho de probar algo nuevo, sobre todo si se sale de la zona de confort, y hacer una simple reflexión sobre estas cuestiones puede ser muy beneficioso para uno mismo a largo plazo."
    
    scene sakuyapool4 with Dissolve(1)
    
    s "Es posible que encuentre nuevas pasiones o aficiones que, en última instancia, pueden ser una fuente de felicidad para usted."
    
    #pause 1
    
    s "Como ya sabrás, algunas personas especulan con la posibilidad de que haya sido un gran cazador de vampiros en una vida pasada, ¡y no creo que eso sea tan malo!"
    
    scene sakuyapool1 with dissolve
    
    s "..."
    
    scene sakuyapool3 with dissolve
    
    s "..."
    
    s "Acércate"
    
    # Camera zoom 2x for 1 second
    scene sakuyapool3:
        zoom 1.0 align(0.5, 0.5)
        ease 1.0 zoom 2.0
    pause 1.0
        
    scene sakuyapool4 with Dissolve(1):
        zoom 2.0 align(0.5, 0.5)
    
    s "Bésame."
    
    # Reset camera back for 1 second
    scene sakuyapool4:
        zoom 2.0 align(0.5, 0.5)
        ease 1.0 zoom 1.0
    pause 1.0
    
    scene sakuyapool3 with dissolve
    
    s "Oh, pero espera."
    
    stop music fadeout 2
    
    s "Hablando de natación.."
    
    scene sakuyapool6 with dissolve
    
    play music drownsong
    
    s "¿Sabías que, aparentemente, ahogarse es una de las peores formas de morir?"
    
    scene sakuyapool5 with dissolve
    
    s "Yo no estoy tan seguro, diría que hay formas mucho peores de morir."
    
    s "Parece que vas a tener que averiguarlo por mí."
    
    show screen choice2("No me hagas sufrir", "¡Ya no quiero morir!", "scene2choice9a", "scene2choice9b", 713, 538, 675, 422)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "No me hagas sufrir":  # x="475"  y="322"
            
            s "Bueno, me alegro de haber podido ayudarte con eso, pero.."
            
        "¡Ya no quiero morir!":  # x="450"  y="281"
            
            s "Lo siento, pero, como he dicho, me imagino que esto va a ser bastante agonizante por tu parte."
            
            s "Sin embargo, está bien...."
    
label scene2choice9a:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "Bueno, me alegro de haber podido ayudarte con eso, pero.."
    
    jump scene2choice9
    
label scene2choice9b:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "Lo siento, pero, como he dicho, me imagino que esto va a ser bastante agonizante por tu parte."
            
    s "Sin embargo, está bien...."
    
label scene2choice9:
            
    s "Tal y como yo lo veo, estabas perdido de todos modos.."
    
    scene sakuyapool8 with Dissolve(1)
    
    s "Ahora que me he divertido contigo, podría convertirte en una deliciosa comida para la señora.."
    
    s "Hace tiempo que ella y la hermana no comen carne."
    
    scene sakuyapool7 with dissolve
    
    s "Muere."
    
    scene black with Dissolve(1)
    
    scene sakuyawater1 with Dissolve(1)
    
    s "..."
    
    scene sakuyawater2 with dissolve
    
    pause 1
    
    scene black with Dissolve(1)
    
    pause 2
    
    stop music fadeout 1
    
    pause 1
    
    return
    
label scene3:  ############################################################################################# SCENE 3 ##
    
    $ save_name = "Day 6 - Farewell"
    
    scene sakuyatea2 with Dissolve(1)
    
    play music teasong
    
    s "Bueno, me disculpo si te he asustado así."
    
    scene sakuyatea4 with dissolve
    
    s "Sólo quería divertirme un poco!."
    
    show screen choice2("Tienes una idea rara de diversion", "No hay problema.", "scene3choice1a", "scene3choice1b", 1233, 164, 150, 155)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Tienes una idea rara de diversion":  # x="822"  y="109"
            
            scene sakuyatea5 with dissolve
            
            s "Jaja, bueno, ¡eso es sólo una cosa de mí!"
            
            scene sakuyatea6 with dissolve
            
            s "Espero que haya un millón de cosas más que te gusten de mí por lo demás."
            
        "No hay problema.":  # x="100"  y="103"
            
            scene sakuyatea3 with dissolve
            
            s "¿Ah, sí?"
            
            scene sakuyatea4 with dissolve
            
            s "¡Esto es tan dulce!"
            
            scene sakuyatea2 with dissolve
            
            s "Eres genial".
    
label scene3choice1a:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea5 with dissolve
            
    s "Jaja, bueno, ¡eso es sólo una cosa de mí!"
    
    scene sakuyatea6 with dissolve
    
    s "Espero que haya un millón de cosas más que te gusten de mí por lo demás."
    
    jump scene3choice1
    
label scene3choice1b:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea3 with dissolve
            
    s "¿Ah, sí?"
    
    scene sakuyatea4 with dissolve
    
    s "¡Esto es muy dulce!"
    
    scene sakuyatea2 with dissolve
    
    s "Eres genial."
    
label scene3choice1:
    
    scene smstea with dissolve
    
    s "Pero aún así..."
    
    scene sakuyasad2 with dissolve
    
    s "Me gustaría compensarte por tus problemas, pero..."
    
    scene sakuyasad with dissolve
    
    s "Hoy es mi último día aquí, tengo que irme."
    
    s "Un alborotador que supuestamente vino del cielo está causando un gran alboroto en Gensokyo."
    
    scene sakuyasad2 with dissolve
    
    s "Quiero ir a investigarlo, estoy seguro de que lo entiendes."
    
    s "Sin embargo, mi señora estará aquí, está muy interesada en conocerte para tus últimos días aquí."
    
    scene sakuyatea3 with dissolve
    
    #Sakuya'
    s "Espero que se comporte con usted. Puede ser un poco difícil de manejar."
    
    scene sakuyatea2 with Dissolve(1)
    
    stop music fadeout 1

    s "Pero..."
    
    scene sakuyacheek1 with dissolve
    
    play music finalsong
    
    s "Muchas gracias por estar aquí conmigo."
    
    s "Me lo he pasado muy bien."
    
    s "Y espero volver a verte alguna vez."
    
    s "Sé que fue difícil para ti antes de venir aquí..."
    
    s "Así que espero que estos últimos días conmigo te hayan ayudado, aunque sea un poco."
    
    show screen choice2("Te extrañaré", "Gracias por todo.", "scene3choice2a", "scene3choice2b", 107, 189, 1424, 210)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Te extrañaré":  # x="71"  y="126"
            
            s "Yo también te extrañaré..."
            
            s "Prometamos vernos de nuevo, está bien?"
            
        "Gracias por todo.":  # x="949"  y="140"
    
            s "No, Gracias por todo."
            
            s "Estoy contenta de haber ayudado."
            
            s "Yo también necesitaba esto."
            
label scene3choice2a:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "No, Gracias por todo..."
            
    s "Prometamos vernos de nuevo, está bien?"
    
    jump scene3choice2

label scene3choice2b:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "No, Gracias por todo."
            
    s "Estoy contenta de haber ayudado."
    
    s "Yo también necesitaba esto."

label scene3choice2:
            
    s "Cuídate por mí, ¿de acuerdo?"
    window hide Dissolve(0.2)
    $ quick_menu = False
    
    scene sakuyacheek2 with dissolve
    
    pause 8
    
    stop music fadeout 2
    
    scene black with Dissolve(2)
    
    return
