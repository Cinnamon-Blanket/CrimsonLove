label chapter4_day4:
    scene black
    with fade
    centered "Day 18 - Thursday 18th January."
    pause 1.0

    scene bg bedroom day
    play music interface_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt hair_down normal
    with fade
    "I wake up."
    harekai "Good morning. You woke up on your own today."
    my "Ah, yeah, good morning."
    "I sit up, rubbing my eyes and stretching."
    harekai "Did you sleep well?"
    my "Huh, that's the first time you asked that. Yeah, I did, thanks."
    harekai "Good."
    my "Did you?"
    harekai "Somewhat."
    harekai "Let's get breakfast."
    my "Ah, right, okay."

    scene bg kitchen day
    show hareka arbiter alt hair_down normal
    with fade
    "We head into the kitchen, and she makes both of our breakfasts, then serves and sits down next to me."
    "We eat in a cozy quiet."
    "When done, we clean up the plates, then head back to the bedroom."

    scene bg bedroom day
    show hareka arbiter alt hair_down normal
    with fade
    "We both finish getting ready for the work day."
    "She grabs a hairbrush and begins doing her hair."
    my "Have you ever thought of trying new hairstyles, Hareka?"
    show hareka arbiter alt eyes_closed normal
    harekai "Not really."
    harekai "I like my hair the way it is."
    my "Ah, fair..."
    show hareka arbiter alt hair_down normal with hpunch
    show hareka arbiter alt normal with hpunch
    "She finishes her hair-do."
    my "Okay, ready?"
    harekai "Yes. Let's go."

    scene bg office day
    play music arbiter_office_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt normal
    with flash
    "We arrive."
    "I'm getting used to the teleportation now. It doesn't feel as sickening anymore."
    "We get to work, her at the desk typing up reports and things, and me proofreading them for errors."
    "We also engage in the odd conversation through our tasks."
    "Eventually, lunchtime arrives, and we head to the cafeteria."

    scene bg cafeteria day
    show hareka arbiter alt normal
    with fade
    "We order our food and head to sit down, but just then..."
    "???" "Oi!"
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    show hareka at left
    show mora arbiter normal at center
    with fade
    "We turn around, to see a small girl in front of us."
    "Why do I feel like I know this girl, despite never meeting her before...?"
    show hareka arbiter alt eyes_closed normal
    harekai "Sigh..."
    harekai "So, we meet again, Mora."
    "Mora...?"
    mora "Indeed so."
    mora "How are you liking your new position, hm?"
    "Her tone of voice is sarcastic, almost mocking."
    show hareka arbiter alt normal
    harekai "Back off."
    harekai "Just because you're jealous of me, doesn't mean you get to ruin the life {i}I've{/i} built for myself, got it?"
    mora "You sure speak brave words for someone who could easily be annihilated by me right now."
    "!!!"
    show hareka arbiter alt eyes_closed normal
    harekai "You sure speak brave words for someone who could easily be fired on the spot for speaking to her {i}boss{/i} in such a disgusting manner."
    show mora arbiter eyes_closed normal
    mora "Ugh..."
    "Mora begins walking away."
    mora "Oh, I'd watch your back if I were you, Hareka. You never know when karma will come back to bite your ass."
    hide mora
    show hareka at center
    with fade
    "Hareka lets out a deep exhale."
    "I furrow my brows."
    my "You really managed to make some enemies, huh?"
    harekai "I told you already..."
    show hareka arbiter alt normal
    harekai "It's inevitable."
    
    scene bg office day
    play music arbiter_office_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt normal
    with fade
    "We return to the office after finishing our food."
    "We quietly get back to work. Hareka seems a lot more... detached this afternoon."
    "Sort of, lost in thought, I guess..."
    "I feel kind of bad for her. She must be feeling a mix of emotions right now."
    "I'd be terrified if I had people threatening me to my own face..."
    "Sure takes some guts to do that to your boss, though. I could never to my old boss..."
    "{b}{u}A few hours later...{/u}{/b}"
    "We finish the work day, and pack up."
    harekai "Let's go."
    my "Okay."
    
    scene bg kitchen day
    play music interface_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt eyes_closed normal
    with flash
    "We return home."
    "Dinner preparations begin, as usual."
    "She's still abnormally quiet, which makes me a bit worried."
    my "Hey, are you okay?"
    show hareka arbiter alt normal
    harekai "Oh, yeah, I'm fine."
    my "Are you sure?"
    harekai "Mhm."
    "We continue making dinner, and sit down to eat when it's done."
    show hareka arbiter alt eyes_closed normal
    "She shuts her eyes, sighing."
    my "Are you tired or something?"
    harekai "Somewhat."
    my "Why don't you go straight to sleep after this, then?"
    harekai "Mm..."
    hide hareka
    with hpunch
    stop music
    "Suddenly, she drops, and I don't have much time to react."
    menu chapter4_day4_menu1 (screen="timed_choice"):
        "Catch her.":
            $ hareka_affection += 5
            jump chapter4_day4_menu1_answer1
        "Let her fall." (auto=True,time=8.0):
            $ hareka_affection -= 5
            jump chapter4_day4_menu1_answer2
    label chapter4_day4_menu1_answer1:
        "I quickly rush forward and grab her before she hits the floor."
        my "Woah there..."
        "She's completely unconscious."
        my "Wow, you really passed out, huh..."
        "I pick her up, gently."
        my "Bedtime for you."
        
        scene bg bedroom evening
        play music hareka_theme fadein 0.5 fadeout 0.5 loop
        with fade
        "I carry her into the bedroom and place her in bed, making sure she's nicely tucked in."
        my "Goodnight, Hareka. Hopefully you enjoy this sleep in a proper bed, instead of the desk."
        "I smile to myself."
        "She looks so cute and peaceful when she's sleeping like this..."
        
        scene bg kitchen day
        with fade
        "I return to the kitchen to finish my food."
        "After that, I wrap up her plate and put it in the fridge for another day."
        "It should last..."
        "I wash up my plate and make sure everywhere is tidy, before returning to the room."
        
        scene bg bedroom evening
        with fade
        "I sit at the desk with my book, deciding to continue reading to wind down before bed."
        scene bg bedroom night
        with fade
        "Eventually, night time falls, and it's time for bed."
        "However, my bed is of course taken."
        "I grab a spare quilt and pillow from the cupboard. Lucky they were there, huh..."
        "It's probably what she's {i}supposed to{/i} use at night, but I haven't once seen her sleeping properly... She's always at the desk."
        "This night will be good for her, then."
        "I set up my makeshift bed on the floor, and snuggle under the quilt. It's actually rather comfortable still."
        "I close my eyes, quickly drifting off to sleep."
        window hide
        play music chapter1_theme fadein 0.5 fadeout 0.5 loop
        $ chapter4_day5_route1_avail = True
        scene black
        with fade
        centered "End of day."
        menu chapter4_day4_route1_end:
            "Day 18 (Chapter 4 - Day 4) complete!"
            "Would you like to return to the chapter selection screen, or carry onto the next day?"
            "Chapter selection.":
                jump chapter_select
            "Carry on.":
                jump chapter4_day5_route1
    label chapter4_day4_menu1_answer2:
        "She falls, landing on the floor with a loud thud."
        "I stare at her, concerned."
        "Luckily, she doesn't begin bleeding or anything."
        "She lays there, unconscious, and I begin to feel bad for not catching her."
        "It would've been nice to have had a warning first, though..."
        "I sigh, picking her up."
        my "Guess it's bedtime for you."
        
        scene bg bedroom evening
        play music interface_theme fadein 0.5 fadeout 0.5 loop
        with fade
        "I carry her into the bedroom and place her in bed."
        my "Goodnight, Hareka."
        
        scene bg kitchen day
        with fade
        "I return to the kitchen to finish my food."
        "After that, I wrap up her plate and put it in the fridge for another day."
        "It should last..."
        "I wash up my plate and make sure everywhere is tidy, before returning to the room."
        
        scene bg bedroom evening
        with fade
        "I sit at the desk with my book, deciding to continue reading to wind down before bed."
        scene bg bedroom night
        with fade
        "Eventually, night time falls, and it's time for bed."
        "However, my bed is of course taken."
        "I grab a spare quilt and pillow from the cupboard. Lucky they were there, huh..."
        "It's probably what she's {i}supposed to{/i} use at night, but I haven't once seen her sleeping properly... She's always at the desk."
        "I set up my makeshift bed on the floor, and snuggle under the quilt. It's actually rather comfortable still."
        "I close my eyes, quickly drifting off to sleep."
        window hide
        play music chapter1_theme fadein 0.5 fadeout 0.5 loop
        $ chapter4_day5_route2_avail = True
        scene black
        with fade
        centered "End of day."
        jump chapter4_day4_route1_end
        #menu chapter4_day4_route2_end:
            #"Day 18 (Chapter 4 - Day 4) complete!"
            #"Would you like to return to the chapter selection screen, or carry onto the next day?"
            #"Chapter selection.":
                #jump chapter_select
            #"Carry on.":
                #jump chapter4_day5_route2