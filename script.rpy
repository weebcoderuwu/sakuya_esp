
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
    
    s "parece que querias terminarlo todo.."
    
    scene sakuyabed6 with Dissolve(1)
    
    s "Good thing I came in at the last second."
    
    s "me alegra que puedas estar conmigo hoy."
    
    show screen choice2("por que me salvaste?", "I Wasn't Supposed To Make It...", "scene1choice1", "scene1choice1", 1103, 407, 1049, 524)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:  # Day1choice1
        "por que me salvaste?":  #x="735"  y="271"
            pass
        
        "I Wasn't Supposed To Make It":  #x="699"  y="349"
            pass
            
label scene1choice1:
    
    hide screen choice2 with Dissolve(0.2)
            
    scene sakuyabed1 with Dissolve(1)
    
    s "Well, I never meant to intrude."
    
    s "Trust me, I would have left you alone and never interfered."
    
    pause 0.5
    
    s "But..."
    
    s "Someone who's been watching you for a small bit sensed that, deep down, you didn't actually want it to end."
    
    pause 0.5
    
    s "It was faint, but your soul was crying for help, begging for another chance at life."
    
    scene sakuyabed5 with Dissolve(1)
    
    s "So I naturally volunteered to help!"
    
    scene sakuyabed6 with Dissolve(1)
    
    s "Regardless, I'm here for you."
    
    show screen choice1("What Do You Want From Me?", "scene1choice2", 1091, 152)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:  # Day1choice2
        "What Do You Want From Me?":  #x="727"  y="101"
            pass

label scene1choice2:
    
    hide screen choice1 with Dissolve(0.2)
    
    scene sakuyabed3 with Dissolve(1)
    
    s "I only want one thing."
    
    s "For you to get better."
    
    scene sakuyabed1 with Dissolve(1)
    
    s "More specifically, I want you to get some sleep. It looks like you hardly got any, I can tell just from looking at your eyes."
    
    show screen choice1("I Can't Sleep", "scene1choice3", 366, 471)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:  # Day1choice2
        "I Can't Sleep":  #x="244"  y="314"
            pass
    
label scene1choice3:
    
    hide screen choice1 with Dissolve(0.2)

    pause 0.5
    
    s "Hmm..."
    
    pause 0.5
    
    s "I know how hard it is to get some sleep."

    scene sakuyabed3 with dissolve
    
    s "I just want you to remember this."
    
    scene sakuyabed1 with dissolve
    
    s "What you did in the past, doesn't matter right now."
    
    s "Whatever you may think is going to happen in the future, doesn't matter right now either."
    
    scene sakuyabed3 with dissolve
    
    s "Nothing else matters right now."
    
    scene sakuyabed6 with dissolve
    
    s "The only thing that matters right now, is you closing your eyes, and getting a proper amount of sleep in."
    
    scene sakuyabed3 with dissolve
    
    s "That's it, nothing else matters except for you sleeping."
    
    scene sakuyabed6 with dissolve
    
    s "I myself am quite tired too, it was fun work but I could really use some sleep now!"
    
    scene sakuyabed3 with dissolve
    
    s "So I'll rest right here with you."
    
    scene sakuyabed1 with dissolve
    
    s "You may notice the more you try to sleep, the harder it gets to actually get some shut eye."
    
    s "One shouldn't \"try\" to sleep, it should just fall upon them as natural as walking."
    
    s "Once you let go and stop thinking, I'm sure you'll find that it's much easier to get some shut eye."
    
    scene sakuyabed3 with dissolve
    
    s "That said, take all the time you need."
    
    s "You can even just look at me if it helps you sleep."
    
    scene sakuyabed6 with dissolve
    
    s "Whenever you're ready."
    
    scene sakuyabed5 with dissolve
    
    s "I'm right beside you."
    
    scene black with Dissolve(1)
    stop music fadeout 1  ## Additional
    $ save_name = "Day 2 - Cooking With Sakuya"
    
    s "Come heeeere~ I need you to help me with something!"
    
    play music cookingsong
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "Hey, there you are!"
    
    s "You seem rather well rested."
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "Just from looking at your eyes, anyways."
    
    show screen choice2("It's All Thanks To You.", "I Really Needed It.", "scene1choice4a", "scene1choice4b", 1382, 203, 74, 224)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "It's All Thanks To You.":  # x="921"  y="135"
            
            scene sakuyacooking1 with Dissolve(1)
            
            s "I'm just glad I could've helped, getting enough sleep is paramount to your daily activities!"
        
        "I Really Needed It.":  # x="49"  y="149"
        
            scene sakuyacooking1 with Dissolve(1)
            
            s "Well I bet you did! You looked like you were on the verge of death."
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "Well, that's probably not an exaggeration anyways."

label scene1choice4a:
    
    hide screen choice2
    
    scene sakuyacooking1 with Dissolve(1)
            
    s "I'm just glad I could've helped, getting enough sleep is paramount to your daily activities!"
    
    jump scene1choice4
    
label scene1choice4b:
    
    hide screen choice2
    
    scene sakuyacooking1 with Dissolve(1)
            
    s "Well I bet you did! You looked like you were on the verge of death."
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "Well, that's probably not an exaggeration anyways."
    
label scene1choice4:
    
    scene sakuyacooking3 with dissolve
    
    s "At any rate, it's good that it happened."
    
    s "This task I'm gonna have you do requires you to stay sharp!"
    
    show screen choice1("What Are We Gonna Do?", "scene1choice5", 1353, 189)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "What Are We Gonna Do?":  #x="902"  y="126"
            pass
            
label scene1choice5:
    
    hide screen choice1 with Dissolve(0.2)
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "I'm gonna have you make some food!"
    
    scene sakuyacooking2 with Dissolve(1)
    
    s "More specifically..."
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "You're gonna make a fruit salad!"
    
    show screen choice2("I've Never Done This Before.", "I Like Fruits!", "scene1choice6a", "scene1choice6b", 1316, 161, 131, 176)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "I've Never Done This Before.":  # x="877"  y="107"
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "Hmm, Is that so?"  # So Nanoka??
            
            scene sakuyacooking1 with Dissolve(1)
            
            s "Well, don't worry about it!"
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "My knives are always razor sharp, so they'll do most of the work for you."
            
        "I Like Fruits!":  # x="87"  y="117"
            
            s "That's great to hear!"
            
            s "I like fruits too!"
            
            scene sakuyacooking4 with Dissolve(1)
            
            s "You can even make tea with fruit."
            
label scene1choice6a:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyacooking4 with Dissolve(1)
            
    s "Hmm, Is that so?"  # So Nanoka??
    
    scene sakuyacooking1 with Dissolve(1)
    
    s "Well, don't worry about it!"
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "My knives are always razor sharp, so they'll do most of the work for you."
    
    jump scene1choice6
    
label scene1choice6b:
    
    hide screen choice2 with Dissolve(0.2)
    
    s "That's great to hear!"
            
    s "I like fruits too!"
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "You can even make tea with fruit."
    
label scene1choice6:
            
    scene sakuyacooking1 with Dissolve(1)
            
    s "Well, at any rate, let's get started."
            
    s "Take this knife."
            
    s "I'm gonna throw these fruits in the air, and you do your best to chop them."
    
    scene sakuyacooking4 with Dissolve(1)
    
    s "Don't worry if you don't think you can cut the fruit in time."
    
    scene sakuyacooking3 with Dissolve(1)
    
    s "Let's just say I'll give you all the time you need."
    
    scene sakuyacooking1 with dissolve
    
    s "Here we go! Cut this fruit up!"
    
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
    
    s "Great job!"
    
    scene sakuyacooking3 with dissolve
    
    s "Here's the next one!"
    
    show screen fruit_screen("orange.png", "scene1orange", 470, 126)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
label scene1orange: # orange_cut
    
    play sound cutstuff
    with hpunch
    hide screen fruit_screen with Dissolve(0.2)
    
    scene sakuyacooking1 with dissolve
    
    s "Last one coming right up!"
    
    show screen fruit_screen("apple.png", "scene1apple", 530, 165)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
label scene1apple: # apple_cut
    
    play sound cutstuff
    with hpunch
    hide screen fruit_screen with Dissolve(0.2)
    
    scene sakuyacooking3 with dissolve
    
    s "Wonderful!"
            
    scene sakuyacooking1 with dissolve
    
    s "Now mix it all up in that bowl and hand it to me!"
    
    scene sakuyasalad1 with dissolve
    
    s "Let's see how this tastes!"
    
    scene sakuyasalad2 with dissolve
    
    s "Delicious!"
    
    s "It tastes even better especially because you made it!"
    
    scene sakuyacooking1 with dissolve
    
    s "Well, I hope that whole process was enjoyable for you."
    
    s "But..."
    
    scene sakuyacooking4 with dissolve
    
    s "There was also another point to this."
    
    scene sakuyacooking3 with dissolve
    
    s "You may have had some troubles in your life."
    
    s "The kind of things that just keep running through your head, no matter how hard you try."
    
    s "\"What If\" thoughts, regretting past choices, anxious about the future..."
    
    scene sakuyacooking4 with dissolve
    
    s "It's quite annoying when that happens, isn't it?"
    
    s "However..."
    
    scene sakuyacooking3 with dissolve
    
    s "I'm willing to bet that you weren't thinking about such things while you were busy cutting up that fruit with me, were you?"
    
    scene sakuyacooking2 with dissolve
    
    s "It's important to keep your mind occupied with healthy acitvities such as these."
    
    scene sakuyacooking1 with dissolve
    
    s "It works wonders towards fighting those nasty thoughts, and in general is great for your well being!"
    
    scene sakuyacooking2 with dissolve
    
    s "I hope this was of some use to you."
    
    scene sakuyacooking1 with dissolve
    
    s "That's all I have to say for now!"
    
    s "See you tomorrow! Take care!"
    
    stop music fadeout 1
    
    scene black with Dissolve(1)
    
    pause 0.5
    
    $ save_name = "Day 3 - Sakuya's Experiment"
    
    scene smstea with Dissolve(1)
    
    play music teasong
    
    s "Welcome back!"
    
    s "I was able to finish my chores for the day earlier than usual, so I decided to call you here!"
    
    s "So, it's your third day here so far."
    
    s "I hope you've taken a liking to this humble mansion."
    
    show screen choice1("Is This Your Room?", "scene1choice7", 320, 197)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Is This Your Room?":  # x="213"  y="131"
            pass

label scene1choice7:
    
    hide screen choice1 with Dissolve(0.2)

    s "Why yes!"
    
    s "This is indeed my room."
    
    s "Nothing's better than coming here with a nice cup of tea after a long day of  hard work!"
    
    scene sakuyatea2 with Dissolve(1)
    
    s "But you must be wondering why I brought you here."
    
    s "I need to perform a little experiment with you."
    
    s "You're quite a peculiar human, everyone around the mansion, even the mistress is curious about you."
    
    scene sakuyatea6 with Dissolve(1)
    
    s "Therefore, as the Cheif Head Maid of this mansion, it's my duty to satisfy these needs."
    
    scene sakuyatea4 with Dissolve(1)
    
    s "I hope you won't mind though!"
    
    s "I'd never do anything that makes you feel uncomfortable!"
    
    show screen choice2("Anything For You", "I'm A Little Nervous.", "scene1choice8a", "scene1choice8b", 150, 171, 1364, 189)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Anything For You":  # x="100"  y="114"
            
            scene sakuyatea6 with Dissolve(1)
            
            s "Why, thank you!"
            
            s "I'm glad you have your trust placed in me."
            
        "I'm A Little Nervous.":  # x="909"  y="126"  - In script, ignores the following dialogues
            
            scene sakuyatea3 with Dissolve(1)
            
            s "Is that so?"
            
            scene sakuyatea2 with Dissolve(1)
            
            s "Well, you can trust me on this one, you'll be completely safe."
    
label scene1choice8a:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea6 with Dissolve(1)
            
    s "Why, thank you!"
    
    s "I'm glad you have your trust placed in me."
    
    jump scene1choice8
    
label scene1choice8b:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyatea3 with Dissolve(1)
            
    s "Is that so?"
    
    scene sakuyatea2 with Dissolve(1)
    
    s "Well, you can trust me on this one, you'll be completely safe."
    
label scene1choice8:
    
    scene sakuyatea2 with Dissolve(1)
    
    s "Now, come closer."
    
    stop music fadeout 2
    
    s "I want you to lay down on my lap."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    play music laying_down_song_re
    
    s "I hope there's enough cushioning to your liking."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "It's simple"
    
    s "Just answer these questions for me, and I'll give you an extensive profile that matches who you are."
    
    s "It may help you understand yourself better."
    
    scene sakuyaquiz4 with Dissolve(1)
    
    s "Just be as honest as you possibly can."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "There is no wrong answer!"
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Now, let's begin."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Question number 1:"
    
    s "Why do you hate living?"  # player: *Big shock* O.O
    
    show screen choice3("It Hurts To Be Alive", "I Can't Cope With My Past", "My Future Is Extremly Bleak", "scene1choice9", "scene1choice9", "scene1choice9", 1233, 125, 1230, 249, 1250, 362)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "It Hurts To Be Alive":  # x="822"  y="83"
            pass
            
        "I Can't Cope With My Past":  # x="820"  y="166"
            pass
            
        "My Future Is Extremly Bleak":  # x="833"  y="241"
            pass
    
label scene1choice9:
    
    hide screen choice3 with Dissolve(0.2)
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "I see..."
    
    s "Next question:"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "What do you think about the most?"
    
    show screen choice3("I Keep Thinking About Past Mistakes.", "I Keep Thinking About The Uncertain Future", "I Don't Think At All.", "scene1choice10", "scene1choice10", "scene1choice10", 1133, 125, 1130, 249, 1150, 362)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "I Keep Thinking About Past Mistakes.":  # x="822"  y="83"
            pass
            
        "I Keep Thinking About The Uncertain Future":  # x="820"  y="166"
            pass
        
        "I Don't Think At All.":  # x="833"  y="241"
            pass
    
label scene1choice10:
    
    hide screen choice3 with Dissolve(0.2)
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "I see..."
    
    s "Just a few more questions."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Why did you do it?"
    
    show screen choice3("I Was Told To.", "I Had No Other Choice.", "I Didn't Belong Anywhere Else.", "scene1choice11", "scene1choice11", "scene1choice11", 1386, 123, 1325, 248, 1290, 353)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "I Was Told To.":  # x="924"  y="82"
            pass
            
        "I Had No Other Choice.":  # x="883"  y="165"
            pass
            
        "I Didn't Belong Anywhere Else.":  # x="860"  y="235"
            pass

label scene1choice11:
    
    hide screen choice3 with Dissolve(0.2)

    scene sakuyaquiz5 with Dissolve(1)
    
    s "You're doing great so far! We're almost there!"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Who do you blame for it all?"
    
    show screen choice3("Myself", "The World", "No One", "scene1choice12", "scene1choice12", "scene1choice12", 1452, 123, 1412, 251, 1428, 356)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Myself":  # x="968"  y="82"
            pass
            
        "The World":  # x="941"  y="167"
            pass
            
        "No One":  # x="952"  y="237"
            pass
            
label scene1choice12:
    
    hide screen choice3 with Dissolve(0.2)
            
    scene sakuyaquiz3 with Dissolve(1)
    
    s "Very good! Last question!"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Where would you like to be buried?"
    
    show screen choice3("Under A Tree", "Under A Small Coffin In A Mansion.", "Let Me Rot Into The Ground", "scene1choice13", "scene1choice13", "scene1choice13", 1404, 123, 1247, 249, 1320, 357)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Under A Tree":  # x="936"  y="82"
            pass
            
        "Under A Small Coffin In A Mansion.":  # x="831"  y="166"
            pass
            
        "Let Me Rot Into The Ground":  # x="880"  y="238"
            pass

label scene1choice13:
    
    hide screen choice3 with Dissolve(0.2)

    scene sakuyaquiz4 with Dissolve(1)
    
    s "Well, thank you!"
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "I have enough information now."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Here's what I think."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "You're a naturally anxious person."
    
    s "You have your hopes and aspirations, but you need a good push or two in the right direction to achieve them."
    
    s "You have a lot of sadness in your heart. You need something or someone to help you stop letting your sorrows build up in you."
    
    s "You often burn a lot of bridges, but only out of necessity."
    
    s "You need to learn to forgive yourself, you're too harsh on yourself sometimes."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "What do you think?"
    
    s "Pretty accurate, right?"
    
    show screen choice2("It's Accurate.", "Not Exactly...", "scene1choice14", "scene1choice14", 1401, 177, 149, 170)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "It's Accurate.":  # x="934"  y="118"
            pass
        
        "Not Exactly...":  # x="99"  y="113"
            pass
    
label scene1choice14:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "Well, funny you should say that."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "The truth is, I made it all up!"
    
    s "I was going to give you that response no matter what option you picked."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "I think to understand who you really are, I'd have to hang out with you more, and get to know you better."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "Which I'm more than happy to oblige by."
    
    show screen choice2("I'm Confused...", "What Was The Point?", "scene1choice15", "scene1choice15", 1386, 186, 108, 179)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "I'm Confused...":  # x="924"  y="124"
            pass
            
        "What Was The Point?":  # x="72"  y="119"
            pass
    
label scene1choice15:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyaquiz4 with Dissolve(1)
    
    s "Well, to be honest, I just wanted you to rest on my lap!"
    
    s "Ehehehe!"
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "That aside, I did this to prove something to you."
    
    s "That it doesn't really matter what I or other people perceive you as."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "You're always free to shape your own fate, your own destiny."
    
    s "Only those who accept you for who you are and what you want to do matter."
    
    show screen choice2("I Don't Like Who I Am.", "No One Accepts Me.", "scene1choice16", "scene1choice16", 117, 176, 1349, 194)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "I Don't Like Who I Am.":  # x="78"  y="117"
            pass
            
        "No One Accepts Me.":  # x="899"  y="129"
            pass
    
label scene1choice16:
    
    hide screen choice2 with Dissolve(0.2)
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Well, believe it or not, I can relate."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "I wasn't always like the person you see before you."
    
    s "I felt lonely and isolated from other people."
    
    s "Even when I was working in this mansion, I was still rather cruel to humans, and even to those around me."
    
    s "I thought, \"As long as I have a bed to sleep on, I don't need anything else.\""
                                                              
    s "At the end of the day, I thought of only myself."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "But, as I'm sure you know, I was out solving an incident."
    
    s "There was a huge and unusual amount of Red Spider Lilies growing everywhere."
    
    s "Well, long story short..."
    
    s "I realized, after that incident, that the things you and I do, matter."
    
    s "Even the smallest, most minor actions I do, matter as well."
    
    s "I have an impact on people, big or small, and that will eventually come around to have an impact on me, whether I realize it or not."
    
    scene sakuyaquiz3 with Dissolve(1)
    
    s "So, from then on I wanted to be warm and kind to those around me."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "Well, for the most part."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Some people really need a good \"scolding\" before you can put some sense into them."
    
    s "Be nice until it's time to not be nice"
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "I think that's a fine motto to live by."
    
    s "I just want you to understand this."
    
    scene sakuyaquiz3 with Dissolve(1)
    
    s "Just like how it was never too late for me to change my ways, it's never too late to change yours either!"
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "That is, for the stuff you want to change."
    
    s "There's always going to be parts of us that we wouldn't change for the world."
    
    scene sakuyaquiz3 with Dissolve(1)
    
    s "And that's just fine!"
    
    s "We just need to surround ourselves with those who love us for who we are."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "But of course, if you have no one, that's fine too."
    
    s "Being able to walk your own path by yourself is quite a virtue."
    
    s "And along the way, you may find what or who you're looking for all along."
    
    scene sakuyaquiz5 with Dissolve(1)
    
    s "Just for the record, I accept you for who you are, and for who you want to be."
    
    scene sakuyaquiz4 with Dissolve(1)
    
    s "I'm here for you, always."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Well, that's all I have to say."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "You can keep laying down in my lap for as long as you want."
    
    scene sakuyaquiz1 with Dissolve(1)
    
    s "Whenever you're ready, we can move on to the next day."
    
    scene sakuyaquiz2 with Dissolve(1)
    
    s "But, take as much time as you need."
    
    s "I've got you."
    
    scene sakuyaquiz4 with Dissolve(1)
    
    scene black with Dissolve(1)
    
    stop music fadeout 2
    
    pause 2.0
    
    return


label scene2:  ############################################################################################# SCENE 2 ##
    
    $ save_name = "Day 4 - Fishing With Sakuya"
    
    scene sakuyafishing1 with dissolve
    
    play music fishing_song
    
    s "Let's do something different today!"
    
    s "This mansion has quite a large lake surrounding it."
    
    s "And who knows what kind of creatures lurk in it!"
    
    scene sakuyafishing2 with dissolve
    
    s "It's the perfect time to go fishing, I'd say."
    
    show screen choice1("Do You Need Some Help?", "scene2choice1", 945, 257)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "Do You Need Some Help?":  # x="630"  y="171"
            pass

label scene2choice1:
    
    hide screen choice1 with Dissolve(0.2)

    scene sakuyafishing1 with dissolve
    
    s "Of course!"
    
    scene sakuyafishing2 with dissolve
    
    s "I wouldn't bring you here just to watch."
    
    s "Fishing is a lot like real life."
    
    s "When you catch a bite, you will encounter some resistance."
    
    scene sakuyafishing1 with dissolve
    
    s "Naturally, you should fight back against the tide."
    
    s "Otherwise you'll lose what you worked so hard for."
    
    scene sakuyafishing2 with dissolve
    
    s "Of course, sometimes it's too hard for us to hang on, so we must let go and try again."
    
    scene sakuyafishing1 with dissolve
    
    s "There is no shame in that."
    
    scene sakuyafishing2 with dissolve
    
    s "Think back to something you wanted to, or tried to achieve in life."
    
    s "Did you encounter some hardships along the way? I bet you did."
    
    scene sakuyafishing1 with dissolve
    
    s "Almost everything in life worth doing is going to be hard one way or another."
    
    s "Do you fight back, or let it go?"
    
    s "Do you try again, or try to catch something else?"
    
    scene sakuyafishing2 with dissolve
    
    s "There is no wrong descision, any one is fine."
    
    scene sakuyafishing1 with dissolve
    
    s "The only wrong descision is not making one at all."
    
    scene sakuyafishing2 with dissolve
    
    with hpunch
    
    s "*SNAP*"
    
    scene sakuyafishing1 with dissolve
    
    stop music fadeout 1
    
    s "Oh my! Looks like we got something already!"
    
    scene iydcl with Dissolve(1)
    
    play music catchfishsong
    
    s "Hnnnnng, this thing is really tough, I'm not sure if I can do it!"
    
    show screen choice2("YOU CAN DO IT!!!", "I BELIEVE IN YOU!!", "scene2choice2", "scene2choice2", 66, 171, 42, 279)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "YOU CAN DO IT!!!":  # x="44"  y="114"
            pass
            
        "I BELIEVE IN YOU!!":  # x="28"  y="186"
            pass

label scene2choice2:
    
    hide screen choice2 with Dissolve(0.2)

    s "Haha, thank you!"
    
    s "But still, it's really really..."
    
    scene sakuyafrogwater with dissolve
    
    with hpunch
    
    s "Ooooh! I can feel something comiiiiiing!!!"
    
    show screen choice2("KEEP GOING!! YOU'RE ALMOST THERE!!", "NO MATTER WHAT HAPPENS, I'M HERE FOR YOU!!!", "scene2choice3", "scene2choice3", 150, 287, 150, 437)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "KEEP GOING!! YOU'RE ALMOST THERE!!":  # x="100"  y="191"
            pass
            
        "NO MATTER WHAT HAPPENS, I'M HERE FOR YOU!!!":  # x=""  y=""
            pass 
            
label scene2choice3:
    
    hide screen choice2 with Dissolve(0.2)
    
    with hpunch
    
    s "Haaaaaaaaaaaaaaaaah!"
    
    scene iyde9o with dissolve
    
    s "Woah!!!"
    
    stop music fadeout 1
    
    s "What is this thing?"
    
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
            
    s "The way I see it, you were a goner anyways."
    
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
    
    s "And I hope to see you again sometime."
    
    s "I know it was hard for you before you came here..."
    
    s "So I hope that these past few days with me have helped you, even for just a bit."
    
    show screen choice2("I'll Miss You", "Thank You For Everything.", "scene3choice2a", "scene3choice2b", 107, 189, 1424, 210)
    
    pause
    pause
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)
    
    menu:
        "I'll Miss You":  # x="71"  y="126"
            
            s "I'll miss you too..."
            
            s "Let's promise to see each other again, alright?"
            
        "Thank You For Everything.":  # x="949"  y="140"
    
            s "No, thank you for everything."
            
            s "I'm glad to have helped."
            
            s "I needed this too."
            
label scene3choice2a:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "I'll miss you too..."
            
    s "Let's promise to see each other again, alright?"
    
    jump scene3choice2

label scene3choice2b:
            
    hide screen choice2 with Dissolve(0.2)
    
    s "No, thank you for everything."
            
    s "I'm glad to have helped."
    
    s "I needed this too."

label scene3choice2:
            
    s "Take care of yourself for me, okay?"
    window hide Dissolve(0.2)
    $ quick_menu = False
    
    scene sakuyacheek2 with dissolve
    
    pause 8
    
    stop music fadeout 2
    
    scene black with Dissolve(2)
    
    return
