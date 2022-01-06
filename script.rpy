
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
    #*para el tiempo*
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
    ## esta scripteado es normal xdd
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
    
    s "Well, thanks for your words of encouragement."
    
    s "I'm not sure I could've done it without you."
    
    show screen choice2("You Totally Could Have!", "It Was Fun!", "scene2choice4a", "scene2choice4a", 818, 546, 890, 651)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "You Totally Could Have!":  # x="545"  y="364"
            
            scene sakuyafishing4 with dissolve
            
            s "Haha, that may be so."
            
            s "But, it was fun, wasn't it?"
            
            scene sakuyafishing3 with dissolve
            
            s "Doesn't it feel nice to cheer for someone you believe in, and vise versa?"
            
            s "I definetly think so."
            
        "It Was Fun!":  # x="593"  y="410"
            
            s "Indeed! I'm sure it was nice cheering and supporting for the person you support!"
            
label scene2choice4a:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyafishing4 with dissolve
            
    s "Haha, that may be so."
    
    s "But, it was fun, wasn't it?"
    
    scene sakuyafishing3 with dissolve
    
    s "Doesn't it feel nice to cheer for someone you believe in, and vise versa?"
    
    s "I definetly think so."
    
    jump scene2choice4

label scene2choice4b:
    
    hide screen choice2 with Dissolve(0.2)
    
    s "Indeed! I'm sure it was nice cheering and supporting for the person you support!"
            
label scene2choice4:
    
    scene sakuyafishing4 with dissolve
    
    s "It's always good to have even just one person supporting you."
    
    s "Now..."
    
    s "What do you think of eating frog legs?"
    
    show screen choice2("I'm Not Sure About That.", "Sounds Delicious!", "scene2choice5a", "scene2choice5b", 746, 662, 764, 548)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "I'm Not Sure About That.":  # x="497"  y="441"
            
            s "Hmm, that's okay, sometimes, it's only natural to be unsure about these kinds of things."
            
            scene sakuyafishing3 with dissolve
            
            s "But I assure you, if I were to cook it, it would probably be one of the best things you have ever tasted in your entire life."
            
        "Sounds Delicious!":  # x="509"  y="365"
            
            scene sakuyafishing3 with dissolve
            
            s "Oh, you really think so?"
            
            s "I bet I won't dissapoint you!"
            
label scene2choice5a:
    
    hide screen choice2 with Dissolve(0.2)
    
    s "Hmm, that's okay, sometimes, it's only natural to be unsure about these kinds of things."
            
    scene sakuyafishing3 with dissolve
    
    s "But I assure you, if I were to cook it, it would probably be one of the best things you have ever tasted in your entire life."
    
    jump scene2choice5
    
label scene2choice5b:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyafishing3 with dissolve
            
    s "Oh, you really think so?"
    
    s "I bet I won't dissapoint you!"
    
label scene2choice5:
            
    scene sakuyafishing4 with dissolve
    
    s "That said, this is a most unusual frog."
    
    s "My mistress has an affinity for these kinds of intresting creatures."
    
    s "Did you know she even had a pet chupacabra?"
    
    s "I'll show it to her first and let her decide what she wants to do with it."
    
    scene sakuyafishing3 with dissolve
    
    s "I wonder what we should call it..."
    
    scene sakuyafishing4 with dissolve
    
    s "Hmmm...."
    
    s "I got it!"
    
    s "His name shall be..."
    
    scene sakuyafishing3 with dissolve
    
    s "Henry."
    
    scene sakuyafishing4 with dissolve
    
    s "That's a nice name, don't you think?"
    
    show screen choice6
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "It's A Great Name!":  # x="-3"  y="341"
            pass
            
        "I Couldn't Have Come Up With A Better Name Myself":  # x="413"  y="368"
            pass
            
        "I Love The Name!":  # x="522"  y="240"
            pass
            
        "The Mistress Will Love The Name!":  # x="485"  y="427"
            pass
            
        "It's The Perfect Name.":  # x="980"  y="426"
            pass
            
        "I Think I'll Name Our Kid Henry.":  # x="513"  y="3"
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
    
    s "I can't remember the last time I was in one of these..."
    
    scene sakuyapoolside4 with Dissolve(1)
    
    s "Ah, it's been a while since I was down here."
    
    scene sakuyapoolside3 with dissolve
    
    s "You know, this place has got some history behind it."
    
    s "Even though it wasn't that long ago, I feel oddly nostalgic about it."
    
    scene sakuyapoolside4 with dissolve
    
    s "I guess we can't help but remicense over the past sometimes."
    
    scene sakuyapoolside3 with dissolve
    
    s "What do you think? Would you like to know more about this area?"
    
    show screen choice2("Sure!", "I'd Rather Just Dive In!", "scene2choice7a", "scene2choice7b", 1373, 434, 1382, 278)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Sure!":  # x="915"  y="289"
            
            scene sakuyapoolside4 with Dissolve(1)
            
            s "Great! I'm happy to explain it."
            
            s "It was a small while after the flower incident I was talking about earlier."
            
            s "My mistress was convinced to take part in a very outlandish plan."
            
            scene sakuyapoolside3 with dissolve
            
            s "The plan? None other than to take a stealth mission to the moon."
            
            scene sakuyapoolside4 with dissolve
            
            s "We've had our fair share of solving incidents and going on adventures."
            
            s "So naturally, we had no problem obliging, this was exciting for us as well."
            
            scene sakuyapoolside1 with Dissolve(1)
            
            s "It was tricky though, we had to build some kind of rocket to the moon, we lacked references as to what should one function and look like."
            
            scene sakuyapoolside4 with dissolve
            
            s "Thankfully, I was able to procure the perfect references thanks to a magazine I obtained from a most curious shop."
            
            scene sakuyapoolside3 with Dissolve(1)
            
            s "You should've seen the look on lady Patchouli's face! She was ecstatic!"
            
            scene sakuyapoolside2 with dissolve
            
            s "Eventually, thanks to everyone's efforts, we finally make it to the moon."
            
            scene sakuyapoolside3 with dissolve
            
            s "The weather was perfect, the waves were beautiful and the cool breeze on you face felt heavenly."
            
            s "My mistress even took a trip around the moon!"
            
            scene sakuyapoolside4 with dissolve
            
            s "So, when it was time to go home, Patchouli helped set up this indoor pool so we could take a bit of the moon with us when we got back home."
            
            s "But you know..."
            
            scene sakuyapoolside3 with Dissolve(1)
            
            s "We made this indoor pool after the fight on the moon, but I never got a chance to actually swim in it!"
            
            scene sakuyapoolside4 with dissolve
            
            s "So... enough talk."
            
        "I'd Rather Just Dive In!":  # x="921"  y="185"
            
            s "Fair enough!"
            
            scene sakuyapoolside4 with dissolve
            
            s "You can ask me anytime later on anyways."
            
label scene2choice7a:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyapoolside4 with Dissolve(1)
            
    s "Great! I'm happy to explain it."
    
    s "It was a small while after the flower incident I was talking about earlier."
    
    s "My mistress was convinced to take part in a very outlandish plan."
    
    scene sakuyapoolside3 with dissolve
    
    s "The plan? None other than to take a stealth mission to the moon."
    
    scene sakuyapoolside4 with dissolve
    
    s "We've had our fair share of solving incidents and going on adventures."
    
    s "So naturally, we had no problem obliging, this was exciting for us as well."
    
    scene sakuyapoolside1 with Dissolve(1)
    
    s "It was tricky though, we had to build some kind of rocket to the moon, we lacked references as to what should one function and look like."
    
    scene sakuyapoolside4 with dissolve
    
    s "Thankfully, I was able to procure the perfect references thanks to a magazine I obtained from a most curious shop."
    
    scene sakuyapoolside3 with Dissolve(1)
    
    s "You should've seen the look on lady Patchouli's face! She was ecstatic!"
    
    scene sakuyapoolside2 with dissolve
    
    s "Eventually, thanks to everyone's efforts, we finally make it to the moon."
    
    scene sakuyapoolside3 with dissolve
    
    s "The weather was perfect, the waves were beautiful and the cool breeze on you face felt heavenly."
    
    s "My mistress even took a trip around the moon!"
    
    scene sakuyapoolside4 with dissolve
    
    s "So, when it was time to go home, Patchouli helped set up this indoor pool so we could take a bit of the moon with us when we got back home."
    
    s "But you know..."
    
    scene sakuyapoolside3 with Dissolve(1)
    
    s "We made this indoor pool after the fight on the moon, but I never got a chance to actually swim in it!"
    
    scene sakuyapoolside4 with dissolve
    
    s "So... enough talk."
    
    jump scene2choice7
    
label scene2choice7b:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "Fair enough!"
            
    scene sakuyapoolside4 with dissolve
    
    s "You can ask me anytime later on anyways."
    
label scene2choice7:
    
    scene sakuyapoolside3 with Dissolve(1)
    
    s "Let's hop right in!"
    
    scene sakuyapool1 with dissolve
    
    s "So, do you enjoy swimming?"
    
    s "I know the pool might be a bit small, but..."
    
    show screen choice2("It's Fun!", "Only Because You're Here.", "scene2choice8", "scene2choice8", 818, 488, 696, 393)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu: 
        "It's Fun!":  # x="545"  y="325"
            pass
        "Only Because You're Here.":  # x="464"  y="262"
            pass
            
label scene2choice8:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyapool4 with Dissolve(1)
    
    s "Hah! Glad to hear it."
    
    scene sakuyapool1 with dissolve
    
    s "Well, either way..."
    
    scene sakuyapool3 with Dissolve(1)
    
    s "It's important to try new things, and to discover things about yourself through these activities."
    
    scene sakuyapool4 with Dissolve(1)
    
    s "For example, let's take what we just did right now. Swimming."
    
    s "Did you enjoy it? Was it fun? Were you good at it? What aspects of it did you like or dislike?"
    
    scene sakuyapool1 with dissolve
    
    s "Obviously, you don't have to write an essay every time you try something new."
    
    s "But simply just trying something new, especially if it's a bit out of your comfort zone, and doing some simple reflecting on such matters can be highly beneficial to yourself in the long run."
    
    scene sakuyapool4 with Dissolve(1)
    
    s "You may find some new passions or hobbies which can ultimately be a source of happiness for you."
    
    #pause 1
    
    s "As you may know, some people speculate I may have been a great vampire hunter in a past life, and I don't think that's so bad!"
    
    scene sakuyapool1 with dissolve
    
    s "..."
    
    scene sakuyapool3 with dissolve
    
    s "..."
    
    s "Come closer"
    
    # Camera zoom 2x for 1 second
    scene sakuyapool3:
        zoom 1.0 align(0.5, 0.5)
        ease 1.0 zoom 2.0
    pause 1.0
        
    scene sakuyapool4 with Dissolve(1):
        zoom 2.0 align(0.5, 0.5)
    
    s "Kiss me."
    
    # Reset camera back for 1 second
    scene sakuyapool4:
        zoom 2.0 align(0.5, 0.5)
        ease 1.0 zoom 1.0
    pause 1.0
    
    scene sakuyapool3 with dissolve
    
    s "Oh, but wait."
    
    stop music fadeout 2
    
    s "Speaking of swimming.."
    
    scene sakuyapool6 with dissolve
    
    play music drownsong
    
    s "Did you know that, apparently, drowning is one of the worst ways to die?"
    
    scene sakuyapool5 with dissolve
    
    s "I'm not so sure myself, I'd say there's a lot worse ways to die."
    
    s "Looks like you're gonna have to find out for me."
    
    show screen choice2("Don't Make Me Suffer", "I Don't Want To Die Anymore!", "scene2choice9a", "scene2choice9b", 713, 538, 675, 422)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Don't Make Me Suffer":  # x="475"  y="322"
            
            s "Well, I'm glad I was able to help you out with that, but.."
            
        "I Don't Want To Die Anymore!":  # x="450"  y="281"
            
            s "Sorry, but, like I said, I'd imagine this is going to be quite agonizing on your end."
            
            s "That's okay though..."
    
label scene2choice9a:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "Well, I'm glad I was able to help you out with that, but.."
    
    jump scene2choice9
    
label scene2choice9b:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "Sorry, but, like I said, I'd imagine this is going to be quite agonizing on your end."
            
    s "That's okay though..."
    
label scene2choice9:
            
    s "The way Ya veo it, you were a goner anyways."
    
    scene sakuyapool8 with Dissolve(1)
    
    s "Now that I've had my fun with you, I might as well turn you into a delectable meal for the mistress."
    
    s "It's been a while since she and the sister have had meat."
    
    scene sakuyapool7 with dissolve
    
    s "Die."
    
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
    
    s "Well, I do apologize if I scared you like that."
    
    scene sakuyatea4 with dissolve
    
    s "I just wanted to have a little bit of fun!"
    
    show screen choice2("You Have A Weird Idea Of Fun!", "It's No Problem!", "scene3choice1a", "scene3choice1b", 1233, 164, 150, 155)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "You Have A Weird Idea Of Fun!":  # x="822"  y="109"
            
            scene sakuyatea5 with dissolve
            
            s "Haha, well, that's just one thing about me!"
            
            scene sakuyatea6 with dissolve
            
            s "I hope there's a million other things you do like about me otherwise."
            
        "It's No Problem!":  # x="100"  y="103"
            
            scene sakuyatea3 with dissolve
            
            s "Oh really!?"
            
            scene sakuyatea4 with dissolve
            
            s "That's so sweet!"
            
            scene sakuyatea2 with dissolve
            
            s "You're so cool."
    
label scene3choice1a:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea5 with dissolve
            
    s "Haha, well, that's just one thing about me!"
    
    scene sakuyatea6 with dissolve
    
    s "I hope there's a million other things you do like about me otherwise."
    
    jump scene3choice1
    
label scene3choice1b:
            
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea3 with dissolve
            
    s "Oh really!?"
    
    scene sakuyatea4 with dissolve
    
    s "That's so sweet!"
    
    scene sakuyatea2 with dissolve
    
    s "You're so cool."
    
label scene3choice1:
    
    scene smstea with dissolve
    
    s "Still though..."
    
    scene sakuyasad2 with dissolve
    
    s "I would like to make it up to you for your troubles, but..."
    
    scene sakuyasad with dissolve
    
    s "Today is my last day here, I have to go now."
    
    s "Some trouble maker who supposedly came from heaven is causing quite a ruckus in gensokyo."
    
    scene sakuyasad2 with dissolve
    
    s "I want to go investigate it, I'm sure you understand."
    
    s "My mistress will be here though, she's very interested in meeting you for your last few days here."
    
    scene sakuyatea3 with dissolve
    
    #Sakuya'
    s "I hope she behaves herself around you! She can be quite a handful!"
    
    scene sakuyatea2 with Dissolve(1)
    
    stop music fadeout 1

    s "But..."
    
    scene sakuyacheek1 with dissolve
    
    play music finalsong
    
    s "Thank you so much for being here with me."
    
    s "I had a really good time."
    
    s "And I hope to see you again sometime."p
    
    s "I know it was hard for you before you came here..."
    
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
