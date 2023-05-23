label chapter2_day1:
    scene black
    with fade
    centered "Day 36 - Monday 5th February"
    pause 1.0
    ###
    scene bg living room day
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    with fade
    "I wake up."
    "It's another day."
    "I sit up, stretching."
    show mora arbiter no_coat normal
    with moveinleft
    mora "Good morning."
    my "Good morning Mora..."
    "I stand up."
    mora "Breakfast is almost ready for you."
    my "Ah, thanks..."
    my "I'll be there in a sec."
    mora "Okay."
    hide mora
    with moveoutleft
    "She heads back into the kitchen."
    "I stretch, sighing in relief."
    "The sofa is so cramped..."
    "I should probably ask to move into a guest bedroom or something."
    
    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    "I head into the kitchen."
    "A plate of baked beans on toast is waiting for me."
    my "Ah, yum..."
    "I sit down."
    my "Are you not gonna have anything today?"
    mora "I had mine before you."
    mora "You overslept a bit, but I kept it warm for you."
    my "Oh..."
    my "Thank you."
    my "Am I gonna be late?"
    mora "No. You know I wouldn't let you sleep in {i}that{/i} late."
    mora "You should still hurry up, though."
    my "Ah, okay..."
    "I eat quicker."
    "It's already been over a month since we met..."
    "We've become significantly more comfortable with each other."
    "She's still really formal and serious, but I've made some good progress with getting to know her."
    "It's slow but steady."
    "I finish my food."
    my "Thanks for that."
    mora "You'd better get ready. I'll finish up cleaning in here, then we'll go."
    my "Yeah, okay."

    scene bg bathroom
    with fade
    "I head to the bathroom to get ready."
    "I get dressed into my work uniform, then brush my hair and clean my teeth."
    "I check in the mirror."
    "I look good, I think."
    mora "Are you ready?"
    "She calls."
    my "Yep!"
    "I reply, finishing up and heading out."

    scene bg living room day
    with fade
    show mora arbiter normal
    "I enter the room."
    mora "Are you ready?"
    my "Yep."
    my "Do I look okay?"
    mora "Hm."
    show mora arbiter eyes_closed normal
    "She straightens my collar and brushes off a couple spots of dirt."
    show mora arbiter normal
    mora "Now you do."
    my "Ahaha, good."
    "I've learned she's very attentive to the small details."
    "Hence, I ask her for advice on looks a lot."
    "She can see issues that even I can't see."
    "It's helpful."
    mora "Let's go then."
    my "Mhm."

    scene bg stage
    play music stage_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal
    "We arrive at work."
    mora "I'll be over in the corner."
    mora "As usual, if you need anything, just call me."
    my "I never do usually... but thanks!"
    mora "Mhm."
    hide mora
    with moveoutleft
    "She heads to the corner and gets out her laptop."
    "She's taken a habit of doing her own work while I'm doing mine."
    show eli work eyes_closed normal
    with moveinright
    eli "Good morning Alex!"
    my "Ah, good morning Eli!"
    my "What's the list of jobs for today?"
    show eli work normal
    eli "Well, stage maintenance is coming up."
    my "Ahh..."
    my "What a pain."
    eli "Also, as you know, Artificial Interspace had to reschedule their concert..."
    my "Yeah. Did they decide on a date yet?"
    eli "They said they want to move it to February 14th!"
    my "February 14th?"
    eli "Yep!"
    show eli work eyes_closed normal
    eli "That's Valentine's Day!"
    eli "I bet we'll get a lot of couples coming for a stage date, hehe~"
    my "Wow..."
    my "Yeah, that'll be great for traction..."
    "I look down."
    show eli work normal
    eli "Well, let's get to work!"
    my "Yeah..."
    my "Let's do a good job today!"
    eli "Mhm!"
    hide eli
    with moveoutright
    "Right..."
    "I forgot."
    "Valentine's Day is coming up."
    "I still need to... do something about that..."
    "I shake the thought away, for now."
    "Gotta focus on work."
    "{b}{u}A few hours later...{/u}{/b}"
    "The day goes by easily."
    "There's never really any issues... Other than minor technical faults which are easily fixable..."
    "I pack up, then head to Mora."
    show mora arbiter eyes_closed normal
    my "Hey, Mora, I'm done now."
    mora "..."
    show mora arbiter normal
    mora "Oh."
    my "Were you daydreaming again?"
    mora "Yeah."
    "I chuckle."
    "She's been doing that a lot recently."
    my "Shall we head off?"
    mora "Yes."
    "She packs away her laptop, then we leave."

    scene bg living room day
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal
    my "Finally home..."
    mora "I'll begin dinner preparations."
    my "Yeah, thanks."

    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    mora "Here you go."
    "She hands me a plate of chicken pie, diced potatoes and mushy peas."
    my "Thanks..."
    "Mora sits down next to me, and we eat in comfortable silence."

    scene bg living room night
    with fade
    show mora arbiter no_coat normal
    mora "It's getting late. You should go to bed now."
    my "Ah yeah..."
    my "Goodnight, Mora."
    mora "Goodnight."
    scene bg living room dark
    with flash
    "She turns off the light."
    hide mora
    with moveoutright
    "She heads to her room."
    "I curl up onto the sofa."
    "Another day complete..."
    "I lay here, in the dark, my thoughts racing."
    "The past week or so has been the same thing, every night."
    "I can never sleep properly anymore."
    "I can't stop thinking..."
    "I'm not thinking about loads of things."
    "I'm just thinking of one thing."
    "One thing that won't go away, no matter how hard I try to block it."
    "My feelings for..."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter2_day2_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter2_day1_end:
        "Day 36 (Chapter 2 - Day 1) complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter2_day2