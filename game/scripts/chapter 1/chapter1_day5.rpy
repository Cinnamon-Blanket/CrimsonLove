label chapter1_day5:
    scene black
    with fade
    centered "Day 5 - Friday 5th January."
    pause 1.0
    if mora_almost_kill == True:
        jump chapter1_day5_moraalmostkill
    ###
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    scene bg living room day
    with fade
    "It's another new day."
    "I stand up, stretching."
    "I head towards the window."
    "It's actually rather nice weather today..."
    "For January, at least..."
    "The sky is cloudy, but it looks calm."
    "It's probably still freezing outside though."
    "Mora enters."
    show mora arbiter no_coat normal
    with moveinright
    mora "Good morning."
    my "Good morning Mora!"
    mora "I will make breakfast for you."
    my "Okay!"
    hide mora
    with moveoutleft
    "She heads into the kitchen."
    "I follow."

    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    "I sit down at the counter, watching her prepare my food."
    "Eventually it's done."
    "She hands me the plate and sits down next to me with her food."
    "We eat in silence."
    "When done, she washes the plates, and we get ready to leave for work."
    
    scene bg stage
    play music stage_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal at left
    show eli work eyes_closed normal at right
    "We arrive at work."
    eli "Good morning, Alex!"
    my "Good morning Eli!"
    show eli work normal
    eli "There's a lot to do today."
    my "Ah, okay."
    my "I'll do my best!"
    eli "Yep!"
    hide eli
    show mora arbiter normal at center
    with move
    "I turn to Mora."
    my "Well, best get to work then!"
    mora "Yes, you should."
    mora "Good luck."
    my "Ah... Thanks!"
    "It feels odd hearing her say that."
    "Not that I'm complaining."
    hide mora
    "{b}{u}A few hours later...{/u}{/b}"
    "Work goes by easily."
    "No problems today."
    "I pack up and head to Mora."
    show mora arbiter normal
    mora "Ready to go?"
    my "Yep!"
    "We head out."
    
    scene bg city afternoon
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal
    "The sky has cleared up, and although it's still freezing, it's still nice."
    my "Hey, Mora?"
    mora "What?"
    my "If I'm going to live with you, I need to pick up my stuff from my apartment..."
    show mora arbiter eyes_closed normal
    mora "You do not {i}need to{/i} move in with me."
    my "Well, maybe... But wouldn't it be easier?"
    my "My house is so far away, and it'd be more convenient for the both of us."
    my "Is that okay?"
    mora "..."
    show mora arbiter normal
    mora "It's fine."
    my "Yay."
    my "We'll have to take the train to my house. I have a pass but you'll have to buy your ticket."
    mora "That's fine."
    my "Okay."
    my "Let's go then!"
    mora "Mhm."
    
    scene bg train day
    with fade
    show mora arbiter eyes_closed normal
    "We sit down."
    mora "Train rides are so expensive..."
    "I laugh."
    my "Yeah... It can be pretty expensive."
    my "Especially considering how far away I live."
    mora "How do you cope..."
    my "I have a pass. One time payment every year to get anywhere with this company."
    my "Yeah, the payment is expensive, but you only gotta do it once, so it ends up cheaper in the long run."
    my "It all adds up..."
    show mora arbiter normal
    mora "I suppose so."
    mora "Perhaps it is the best idea for you to move in, then."
    my "Yeah, haha."
    hide mora
    "{b}{u}An hour later...{/u}{/b}"
    show mora arbiter normal
    "The train announcer announces my stop, finally."
    "We head off."
    
    scene bg futon room
    with fade
    show mora arbiter normal
    "We enter my apartment."
    "It's a lot smaller than hers."
    mora "This is where you live?"
    my "Yeah."
    mora "It only has two rooms..."
    my "Yeah well, I don't have much need for more than that."
    mora "Fair enough."
    my "I'll grab my stuff."
    mora "Okay."
    "I head to the cupboard and grab a suitcase, unzipping it and laying it flat."
    "I then begin packing my clothes from the wardrobe."
    mora "Do you need help?"
    my "Ah, that'd be great!"
    "She helps pass me things, and I put them into the suitcase."
    "With the both of us sharing the work, it doesn't take long."
    "Finally, I zip up the suitcase."
    my "I'll sort out quitting the rental later on."
    my "My payment isn't due for a while, so I don't need to worry."
    mora "Are you sure?"
    my "Yeah."
    my "Let's go back now!"
    mora "Okay."
    "I grab the suitcase, and we leave."
    
    scene bg train evening
    with fade
    show mora arbiter normal
    "We get back onto the train."
    "It's getting rather late now, and I can tell we're both tired."
    my "Hey..."
    my "Do you wanna get dinner out today?"
    my "Since it's pretty late, and it'd be a nice change of pace."
    mora "Oh."
    mora "If you want to, sure."
    my "Okay then!"
    my "I know of a nice place in the city."
    my "We can go there!"
    mora "Okay."
    
    scene bg restaurant a
    with fade
    show mora arbiter normal
    "We enter the cafe."
    "We take a seat, and look at the menu."
    mora "There's a lot of different foods here..."
    my "Yeah, that's one reason they're so popular!"
    my "We're lucky not many people are here, usually it's so packed..."
    my "Partly due to the sheer amount of options of dining here..."
    mora "I see..."
    mora "It looks like a nice place."
    my "It is!"
    my "In my opinion at least, ahaha."
    "We both give our orders to the waiter, and wait patiently for our food."
    hide mora
    "{b}{u}30 minutes later...{/u}{/b}"
    show mora arbiter normal
    "Eventually, our food arrives."
    "It doesn't take too long."
    "We thank the waiter, and dig in."
    mora "This is..."
    show mora arbiter eyes_closed normal
    mora "..."
    my "Do you like it?"
    mora "Yes."
    my "Good!"
    show mora arbiter normal
    mora "It has been ages since I've been to a cafe."
    my "Same..."
    my "I missed this place."
    mora "Why did you stop coming?"
    my "Ah... Work got in the way, I suppose."
    my "I had a lot of late nights from concerts and such."
    my "It's rather quiet this beginning part of the year, though, luckily."
    my "Why did you stop?"
    mora "Well."
    mora "I suppose for a similar reason. Work got in the way."
    my "Ah, I see."
    my "What made you agree to do this kind of work, then?"
    my "Looking after me, and making sure I don't cause trouble..."
    mora "Well, I didn't agree to it."
    mora "Arbiters are usually given tasks such as taking down large corporations who pose a threat, not ordinary people..."
    mora "However, you and Angela are a special case."
    my "Oh?"
    my "Yeah, Zena is an Arbiter too, I remember..."
    my "What's so special about us?"
    mora "I cannot disclose that."
    mora "Not until this is over, anyways."
    my "Ah, okay... Fair enough."
    "At least she's willing to talk about it now."
    mora "My job is to keep an eye on you, to monitor if you're a threat to us, and if I find any threats, to report them."
    mora "Part of that role involves making sure you are well looked after."
    mora "If I don't look after you, you may end up turning against me, and trying to run away, or..."
    mora "Killing me."
    my "Ah, I see..."
    my "Well, thank you for explaining it to me."
    mora "Mhm."
    "We finish our food and I pay the bill."
    my "Ready to head back now?"
    mora "Yes. Let's go."
    
    scene bg living room night
    with fade
    show mora arbiter eyes_closed normal
    "We return home."
    mora "Finally home..."
    my "Are you tired?"
    show mora arbiter normal
    mora "A bit."
    my "We should both head to bed, probably."
    my "I'll unpack in the morning."
    "I place my suitcase in a corner, out of the way."
    mora "Okay then."
    mora "Goodnight."
    my "Goodnight!"
    hide mora
    with moveoutright
    "She heads to her room."
    "I lay down on the sofa, pulling the blanket over me."
    "Today was a nice day..."
    "I fall asleep rather quickly."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    scene black
    with fade
    centered "End of day."
    $ chapter2_avail = True
    menu chapter1_day5_end:
        "Day 5 complete!"
        "{b}Carry on option is not available due to Chapter Completion.{/b}"
        "Chapter selection.":
            jump chapter_select
label chapter1_day5_moraalmostkill:
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    scene bg living room day
    with fade
    "I wake up."
    "It's another new day."
    mora "Good morning."
    my "Huh-"
    "I turn around."
    show mora arbiter no_coat normal
    "Mora is sitting at the table."
    my "Ah, good morning Mora."
    my "I didn't realise you were still in here, haha."
    mora "It's fine."
    my "Have you been working all night?"
    mora "Yes."
    mora "I had a lot to catch up on."
    my "But sleep is important..."
    mora "I'm fine."
    mora "Do not worry."
    my "You've already passed out once..."
    mora "..."
    mora "{i}I'm fine.{/i}"
    my "If you say so..."
    mora "I'll make breakfast."
    my "Okay."
    
    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    "We enter the kitchen."
    "I sit down and watch as she prepares the breakfast."
    "She moves so gracefully..."
    "A few minutes later, it's done, and she passes me a plate."
    my "Thanks!"
    mora "Seriously. Stop thanking me for being a decent human being."
    my "Haha..."
    "She sits down next to me."
    "We eat."
    "When finished, she washes the dishes, and we return back to the room."
    
    scene bg living room day
    with fade
    show mora arbiter no_coat normal
    my "So, what should we do today?"
    mora "Unfortunately, I have to keep working."
    my "No way..."
    my "They really make you do that much??"
    mora "It's a load of reports I have been putting off, and they piled up."
    mora "It's entirely my fault."
    my "Ah..."
    my "A fellow procrastinator..."
    mora "I apologise for the inconvenience to you."
    my "Oh no, it's fine!"
    my "I'm just worried about you."
    mora "There's no need to. I'll be fine."
    my "Okay then... If you're sure..."
    hide mora
    "She sits back at the table, beginning to type away."
    "I feel sorta bad for her..."
    "Oh well. If she says she's fine, then I'll have to trust her."
    "I sit down on the couch, turning on the TV."
    "Time to continue that show..."
    "{b}{u}A few hours later...{/u}{/b}"
    "It's been a few hours now."
    "I finished one season already."
    "It comes up to lunchtime."
    show mora arbiter no_coat normal
    with moveinleft
    mora "Hey."
    my "Hm?"
    "I look up."
    "She passes me a plate with a sandwich on it."
    mora "I made you some lunch."
    my "Ah... Thank you!"
    mora "..."
    my "Oops."
    mora "Well, at least you're grateful."
    mora "Not many people are."
    my "True..."
    my "I suppose it's a bit of a habit, haha..."
    mora "It's not the worst habit to have, being polite."
    my "That's true."
    "I chuckle."
    my "Did you make yourself something to eat too?"
    mora "Of course."
    "I look behind me."
    "Her sandwich is at the table beside her laptop."
    my "I see. Good."
    mora "I do look after myself, you know."
    my "I know... I was just checking."
    mora "Well, I've already told you, you don't need to worry."
    my "It's instinct..."
    mora "Well then."
    mora "Enjoy your lunch."
    hide mora
    "She returns to the table."
    "I take a bite of the sandwich."
    "It's cheese filled. My favourite."
    "I eat it rather quickly."
    scene bg living room night
    with flash
    "{b}{u}A few more hours later...{/u}{/b}"
    "Mora stands up."
    show mora arbiter no_coat normal
    mora "I'm going to make dinner now."
    my "Ah, okay!"
    hide mora
    "She shuts off her laptop, and heads to the kitchen."
    "I turn off the TV and follow her."
    
    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    "I take a seat, and watch her prepare dinner."
    "She works so swiftly..."
    "I'm jealous of how productive she is..."
    "In a short amount of time, the preparation is done."
    "She hands me a plate of crispy sausages, fries and baked beans."
    "She sits down next to me."
    my "Mm... You're so focused all the time. How do you do it?"
    mora "I have to be."
    my "Oh..."
    "We eat."
    "It's delicious, as usual."
    my "You're a great cook, you know."
    mora "Really?"
    my "Yeah. I love your food."
    my "I'm serious."
    mora "Oh..."
    mora "Well, thank you."
    "I chuckle."
    my "{i}No need to thank me for being a decent human being, Mora.{/i}"
    "I say jokingly."
    mora "Hah..."
    "Did she just..."
    "Wow."
    hide mora
    "{b}{u}10 minutes later...{/u}{/b}"
    show mora arbiter no_coat normal
    "We finish eating, and she washes the pots."
    "We return to the room."
    
    scene bg living room night
    with fade
    show mora arbiter no_coat normal
    mora "I need to return to work now."
    my "Okay. I'll finish this TV show I'm watching."
    mora "Enjoy that."
    my "Thanks..."
    "I can't really say \"enjoy your work\" haha..."
    my "Good luck with your work."
    "I decide on that."
    mora "Thank you."
    hide mora
    "She returns to the laptop and boots it back up."
    "I turn on the TV and continue watching my show."
    "{b}{u}A couple of hours later...{/u}{/b}"
    "Finally done."
    "That finale was... so sad..."
    "I had to stop myself from bawling..."
    "I turn off the TV, turning to Mora."
    show mora arbiter no_coat eyes_closed normal
    my "Mora?"
    mora "..."
    "Did she fall asleep again?"
    "I tap her shoulder."
    show mora arbiter no_coat normal
    mora "What-"
    "She looks up at me."
    mora "..."
    my "You were falling asleep, weren't you?"
    mora "..."
    "I sigh."
    my "You'd better get to bed."
    my "Sleeping like that will hurt your back and stuff..."
    my "Plus, you need good {i}quality{/i} sleep, by the looks of it."
    mora "But my work-"
    my "Your work can wait."
    my "It'll still be there in the morning, no?"
    mora "Sigh."
    mora "I suppose..."
    my "I don't wanna have to look after {i}you{/i} after everything..."
    mora "Fine."
    mora "I'll go to bed."
    mora "Let me finish off first."
    my "Fine, but be quick."
    my "I need to get to bed myself, y'know..."
    "She finishes off typing some stuff up."
    "Finally, she shuts off the laptop, putting it aside."
    "She stands up."
    mora "Goodnight."
    my "Goodnight, Mora."
    hide mora
    with moveoutright
    "She leaves."
    "I sigh in relief."
    "She's clearly not getting enough sleep..."
    "I hope she can now..."
    "I curl up on the sofa, underneath the blanket."
    "It's warm."
    "Time for my own sleep..."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    scene black
    with fade
    centered "End of day."
    jump chapter1_day5_end