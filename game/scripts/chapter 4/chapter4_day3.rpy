label chapter4_day3:
    scene black
    with fade
    centered "Day 17 - Wednesday 17th January."
    pause 1.0

    scene black
    stop music fadeout 1.0
    with fade
    harekai "Hey... Wake up..."
    "Mm..."
    "Who is that...?"
    harekai "Hey..."
    "I feel a hand touch my head."
    "My eyes flicker open."

    scene bg bedroom day
    play music interface_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt normal
    with fade
    harekai "Good morning."
    my "Oh... Good morning..."
    "I sit up, rubbing my eyes."
    my "Is it late...?"
    harekai "No, it isn't. I just had to let you know I'm going to work soon."
    my "Oh... Okay..."
    "I stand up."
    my "Guess I should get ready then..."
    harekai "Yes, you should."
    hide hareka
    "I get dressed into some clean clothes, and then we head into the kitchen for breakfast."

    scene bg kitchen day
    show hareka arbiter alt normal
    with fade
    "I sit down at the counter, and Hareka makes me some breakfast."
    harekai "Here you go."
    my "Oh, thanks."
    harekai "You're welcome."
    "She sits down next to me with her food, and we eat quietly."
    "{b}{u}10 minutes later...{/u}{/b}"
    "We've finished."
    "We put the pots in the dishwasher and Hareka turns to me."
    harekai "Ready to go?"
    my "Yep!"
    harekai "Let's go, then."

    scene bg office day
    play music arbiter_office_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt normal
    with flash
    "We arrive at the office via teleportation."
    "I sit down on the couch. Hareka goes to her desk."
    my "So, what kind of work does being the Interface entail?"
    show hareka arbiter alt eyes_closed normal
    harekai "It's complicated."
    harekai "Many different things."
    show hareka arbiter alt normal
    harekai "You'd probably find it boring if I went in-depth, so I won't."
    my "Oh... Okay."
    "She boots up the computer."
    my "What can I do while you're working?"
    harekai "Hm..."
    harekai "You could help out a bit, if you want."
    my "Oh?"
    harekai "You could proofread these reports for me."
    harekai "It's just simply making sure there's no spelling or grammar errors."
    my "Oh, okay! Sounds simple enough."
    harekai "Good."
    "I grab the papers from her and sit back down."
    "We begin work."
    show hareka arbiter alt eyes_closed normal
    "{b}{u}An hour later...{/u}{/b}"
    "I finish."
    my "I'm done!"
    "Hareka looks up."
    show hareka arbiter alt normal
    harekai "Oh, good."
    "I pass the papers to her."
    my "I highlighted a few points, for correction, but it's all mostly okay."
    harekai "Good. Thank you."
    my "You're welcome."
    "I smile."
    my "Anything else I can do?"
    harekai "Not right now."
    my "Oh, okay. That's fine. I'll wait a bit."
    harekai "Sorry."
    my "There's no need to be sorry!"
    "I sit back down and wait patiently."
    "{b}{u}Another hour later...{/u}{/b}"
    "Hareka stands up."
    harekai "it's lunch time."
    my "Oh, yay!"

    scene bg cafeteria day
    show hareka arbiter alt normal
    with fade
    "We head to the cafeteria."
    "We order our food and sit down at a table."
    "A few people are staring."
    my "Hey, why are they staring?"
    show hareka arbiter alt eyes_closed normal
    harekai "Either because of what happened yesterday, or resentment."
    my "Oh... Sorry again about yesterday. But what do you mean by resentment?"
    harekai "I overthrew the leaders of the company. There's bound to be people who hate me for that."
    my "Oh, right..."
    my "Well, they can't touch you, right?"
    show hareka arbiter alt normal
    harekai "Wrong."
    harekai "Now I'm human, they {i}can{/i} touch me."
    my "Ah... Yeah, that's true. What are you gonna do about that?"
    harekai "I'm still thinking about it. Maybe a bodyguard."
    my "Haha... That'd be pretty cool."
    harekai "Maybe."
    "We eat our lunch quickly, and then head back to the office."

    scene bg office day
    show hareka arbiter alt normal
    with fade
    "We get back to work. I help out here and there, doing more proofreading and keeping her company."
    "Eventually, the end of the day rolls around."
    show hareka arbiter alt eyes_closed normal
    harekai "Finally done."
    "We both stand up. She shuts down the computer and heads over to me."
    my "Shall we head back?"
    show hareka arbiter alt normal
    harekai "Yep."

    scene bg kitchen day
    play music interface_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter alt normal
    with flash
    "We return home."
    "We head to the kitchen, and begin making our dinner together."
    "When it's finished, we sit down to eat."
    my "How are you liking being human, then?"
    harekai "It has its good and bad points."
    harekai "Finally being able to taste food is nice... and being free to go wherever I want... We only use teleportation now for ease, you know. I do have the directions of walking to the office from here."
    my "Ah, yeah, it is easier using teleportation."
    show hareka arbiter alt eyes_closed normal
    harekai "Having to sleep and look after myself better is rather annoying..."
    my "Well, unfortunately, that's how the human body works. We have to be... maintained, I guess."
    harekai "Yeah..."
    show hareka arbiter alt normal
    harekai "I have no regrets, though."
    "That makes me somewhat happy."
    "We finish our food, clean up, then return to the bedroom."

    scene bg bedroom evening
    show hareka arbiter alt normal
    with fade
    my "I know it's still evening, but I think I'm gonna head to bed."
    harekai "Oh, okay."
    "I get into bed, and Hareka sits at the desk."
    my "Goodnight, Hareka."
    harekai "Goodnight."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter4_day4_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter4_day3_end:
        "Day 17 (Chapter 4 - Day 3) complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter4_day4