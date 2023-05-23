label chapter4_day5_route1:
    scene black
    with fade
    centered "Day 19 - Friday 19th January."
    pause 1.0

    scene bg bedroom day
    play music hareka_theme fadein 0.5 fadeout 0.5 loop
    with fade
    "I slowly awaken."
    "It's morning already..."
    "I check the time. It isn't too late, that's okay. I was mostly worried about us oversleeping."
    "I stand up, stretching a bit, before going over to where Hareka is still sleeping soundly."
    "I gently shake her."
    my "Hareka?"
    show hareka arbiter alt messy eyes_closed normal
    harekai "Mm..."
    show hareka arbiter alt messy normal
    harekai "Mm."
    my "Good morning, sleepyhead."
    "She sits up, looking around."
    harekai "Did I really fall asleep...?"
    my "Yeah, you passed out, silly. I had to catch you so you didn't fall and hurt yourself."
    harekai "Oh..."
    show hareka arbiter alt messy eyes_closed normal
    "She sighs."
    harekai "Sorry..."
    my "Hey, hey, there's no need to apologise."
    harekai "It's embarrassing, though..."
    "I chuckle."
    show hareka arbiter alt messy smile
    harekai "Thank you for catching me."
    my "You're welcome."
    "It's been a while since I've seen her smile."
    "Ever since she became the new Interface..."
    "I missed it, to be honest."
    "She stands up."
    show hareka arbiter alt messy eyes_closed smile
    harekai "My hair's a mess..."
    my "Yeah well, you slept on it, it's gonna look a bit unkempt."
    my "You don't look bad or anything, though."
    harekai "Still."
    show hareka
    show hareka arbiter alt hair_down eyes_closed smile
    "She lets down her hair."
    show hareka arbiter alt hair_down smile
    harekai "Much better."
    my "Ah..."
    menu chapter4_day5_route1_menu1:
        "Tell her she looks beautiful.":
            $ hareka_affection += 5
            my "You look beautiful, Hareka."
            harekai "Ah, thank you!"
            "She laughs."
        "Don't say anything.":
            pass
    my "Well, should we get breakfast?"
    harekai "Good idea!"

    scene bg kitchen day
    show hareka arbiter alt hair_down smile
    with fade
    "We enter the kitchen, and Hareka makes us both our breakfasts."
    harekai "I won't be late for work, right?"
    my "No, you won't. I made sure not to let you oversleep."
    harekai "Ah, good."
    "We eat in comfortable silence."
    "When done, she washes the pots, then turns to me."
    harekai "Do I have time to have a quick bath?"
    my "Yeah, I think so."
    harekai "Okay. I won't be long."
    my "Okay, I'll wait for you in the bedroom."
    harekai "Thanks!"

    scene bg bedroom day
    with fade
    "She heads to the bathroom and I wait for her, reading for a bit while waiting."
    "I also keep an eye on the time. I don't want to make her late or anything."
    "{b}{u}A while later...{/u}{/b}"
    show hareka arbiter alt smile
    with moveinright
    "She returns."
    harekai "I'm back!"
    my "Ah, good."
    my "Ready to go?"
    harekai "Yeah, let's go."

    scene bg office day
    play music arbiter_office_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt normal
    with flash
    "We arrive at the office once more."
    harekai "Time to begin."
    my "Yep."
    "She gets to work."
    "Her switch in expression was so smooth though... It's almost like she has different sides depending on where she is."
    "Like she's putting on a mask..."
    "I can't help but feel a bit bad for her. She probably feels like she has to keep operating like the old Interface."
    "However, that just isn't true... It's hers now, she can change the quota..."
    "{b}{u}A few hours later...{/u}{/b}"
    "Lunchtime rolls around."
    "Hareka stands up."
    harekai "Ready to go to lunch?"
    my "Yep!"

    scene bg cafeteria day
    show hareka arbiter alt normal
    with fade
    "We head to the cafeteria."
    "Waiting in line, Mora approaches us once more."
    show hareka at left
    show mora arbiter normal at center
    harekai "What do you want now?"
    mora "You know very well what I want."
    my "Hey now, both of you, let's not start an argument..."
    "The tension is high between them, I can feel it. I don't want something starting."
    "Mora turns to me."
    mora "Keep your butt out of my fuckin' business."
    mora "You're just her slave. You have no respect from me."
    "Ouch..."
    my "That's not true!"
    show mora arbiter eyes_closed normal
    mora "You're so goddamn clueless."
    harekai "Leave, right now."
    show mora arbiter normal
    mora "No!"
    show riley arbiter normal at right
    "???" "If I were both of you right now, I'd diffuse the situation immediately."
    "Huh-"
    show mora arbiter eyes_closed normal
    show hareka arbiter alt eyes_closed normal
    "Mora & Hareka" "..."
    "I recognise this person. I think I bumped into them when I got kicked out a few days ago."
    show mora arbiter normal
    mora "Ugh. Fine."
    hide mora with dissolve
    "She leaves."
    show hareka arbiter alt normal
    harekai "Thanks."
    "???" "I didn't do it for you. I'm just doing my job."
    my "Who are you, then?"
    "The person looks at me."
    "???" "Oh."
    riley "My name is Riley. I'm a Grade 3 Arbiter in this branch."
    my "Oh..."
    my "Yeah, I think someone said there's different ranks of Arbiters..."
    my "Well, nice to meet you, I guess."
    riley "Mhm."
    riley "I'll be going now."
    hide riley with dissolve
    show hareka arbiter alt eyes_closed normal
    harekai "Sigh..."
    harekai "Let's just take our food to the office."
    my "Okay..."
    
    scene bg office day
    show hareka arbiter alt eyes_closed normal
    with fade
    "We return to the office after grabbing our food."
    "We sit down on the couch to eat."
    my "The food here is pretty nice, to be honest."
    harekai "It's okay, I guess."
    my "Your food is the best though."
    show hareka arbiter alt normal
    harekai "You think?"
    my "Yeah."
    show hareka arbiter alt eyes_closed smile
    harekai "That... Makes me a bit happy..."
    my "Good!"
    menu chapter4_day5_route1_menu2:
        "Pat her.":
            $ hareka_affection += 5
            "I pat her."
            show hareka arbiter alt blush with hpunch
            harekai "Wha- What are you doing??"
            my "Patting you."
            harekai "Ah-"
            show hareka arbiter alt eyes_closed blush
            harekai "Jeez..."
            harekai "It scared me... I thought you were gonna hurt me..."
            my "I can stop if you want. I didn't want to scare you."
            harekai "No, I..."
            show hareka arbiter alt eyes_closed blush smile
            harekai "I don't really mind... if you continue..."
            "I laugh."
            my "Okay."
            "I pat her for a moment."
            harekai "Thanks..."
            my "You're welcome."
        "Do nothing.":
            pass
    show hareka arbiter alt smile
    "We continue eating our lunch in comfortable silence."
    "When done, she sighs."
    show hareka arbiter alt eyes_closed normal
    harekai "I really don't wanna go back to work..."
    my "There's only a bit left. You can do it."
    show hareka arbiter alt eyes_closed smile
    harekai "Thank you."
    "She heads to her desk, taking a few deep breaths."
    show hareka arbiter alt normal
    harekai "Let's begin."
    "{b}{u}A few hours later...{/u}{/b}"
    "We have finished."
    show hareka arbiter alt eyes_closed normal
    "Hareka sighs in relief."
    harekai "Let's go already..."
    my "Yeah, good idea."

    scene bg bedroom evening
    play music interface_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt eyes_closed normal
    with flash
    "We return home."
    my "Hey, you look really stressed out."
    show hareka arbiter alt normal
    harekai "That's because I am."
    my "Ah..."
    menu chapter4_day5_route1_menu3:
        "Hug her.":
            $ chapter4_day5_route1_menu3_answer1 = True
            $ hareka_affection += 5
            play music hareka_theme fadein 0.5 fadeout 0.5 loop
            "I pull her into a hug."
            show hareka arbiter alt blush
            harekai "Ah-"
            my "It's okay."
            my "You got thrown into this new job very quickly, and people keep being not nice to you..."
            my "It's okay to feel stressed."
            show hareka arbiter alt blush smile
            harekai "Thanks..."
            "She holds onto me tightly."
            "We stay here for a while. Time stops during this sweet moment."
            "She's the first one to let go."
            show hareka arbiter alt eyes_closed blush smile
            harekai "Thank you... That helped."
            my "You're welcome."
            my "I'm here for you whenever you need me, okay?"
            harekai "You mean it?"
            my "Of course. I'm your friend, after all."
            show hareka arbiter alt blush smile
            harekai "Thank you so much."
            my "You're welcome."
            "We both smile."
            "My familiar warm feeling has never been stronger."
            harekai "Let's make dinner."
            my "Okay!"

            scene bg kitchen day
            show hareka arbiter alt smile
            with fade
            "We head into the kitchen and begin making dinner together."
            "We engage in casual chat while doing so."
            "It's lovely."
            "When done, we eat, continuing to chat about anything and everything."
            "It's just... relaxed and natural."
            "Hareka looks genuinely happy."
            "I'm glad she's beginning to feel better, at least a little bit."

            scene bg bedroom evening
            show hareka arbiter alt eyes_closed smile
            with fade
            "After dinner, we return to the room."
            my "Time for bed, huh."
            harekai "Yep."
            my "You really should use the bed made for you, y'know?"
            my "Sleeping at the desk is gonna be bad for your back and stuff."
            show hareka arbiter alt smile
            harekai "Ah, yeah... I keep forgetting I'm human now..."
            my "You're so silly sometimes."
            my "Anyways, I left it out from yesterday, so you can just go to bed when you're ready. I found it rather comfortable."
            harekai "Thanks..."
            "I get into bed myself."
            my "Goodnight, Hareka."
            show hareka arbiter alt eyes_closed smile
            harekai "Goodnight, Alex..."
            window hide
            $ chapter4_day6_route1_avail = True
            play music chapter1_theme fadein 0.5 fadeout 0.5 loop
            scene black
            with fade
            centered "End of day."
            menu chapter5_day5_route1_end:
                "Day 19 (Chapter 4 - Day 5) complete!"
                "Would you like to return to the chapter selection screen, or carry onto the next day?"
                "Chapter selection.":
                    jump chapter_select
                "Carry on.":
                    jump chapter4_day6_route1
        "Don't do anything.":
            $ chapter4_day5_route1_menu3_answer2 = True
            "I'm really bad at comforting people, so I end up not doing anything."
            "She sighs."
            harekai "Let's get dinner."
            my "Ah, okay..."

            scene bg kitchen day
            show hareka arbiter alt normal
            with fade
            "We head to the kitchen and make dinner."
            "She seems really out of it for the whole time."
            "We eat quietly, then head back to the bedroom."

            scene bg bedroom evening
            show hareka arbiter alt eyes_closed normal
            with fade
            my "Well, I guess it's my time to head to bed."
            harekai "Mhm."
            my "Hey... You really should use the bed made for you, y'know?"
            my "Sleeping at the desk is gonna be bad for your back and stuff."
            show hareka arbiter alt normal
            harekai "Oh, right."
            my "I left it out from yesterday, so you can just go to bed when you're ready. I found it rather comfortable."
            harekai "Thanks."
            my "You're welcome."
            "I get into bed myself."
            my "Goodnight, Hareka."
            harekai "Goodnight."
            window hide
            play music chapter1_theme fadein 0.5 fadeout 0.5 loop
            $ chapter4_day6_route1_avail = True
            scene black
            with fade
            centered "End of day."
            jump chapter5_day5_route1_end