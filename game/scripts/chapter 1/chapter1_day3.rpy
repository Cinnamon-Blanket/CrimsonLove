label chapter1_day3:
    scene black
    with fade
    centered "Day 3 - Wednesday 3rd January."
    pause 1.0
    if mora_push == True:
        jump chapter1_day3_morapush
    if mora_almost_kill == True:
        jump chapter1_day3_moraalmostkill
    ###
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    scene bg living room day
    with fade
    "I open my eyes."
    "The brightness is blinding. It takes a moment to adjust."
    "I sit up, stretching."
    "Just then, Mora walks in."
    show mora arbiter no_coat normal
    with moveinright
    mora "Good morning."
    my "Good morning..."
    mora "Would you like breakfast?"
    my "Yes please, I'm starving..."
    mora "Come with me."
    hide mora
    with moveoutleft
    "She heads into the kitchen."
    "I follow."

    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    mora "Sit down at the counter."
    "I take a seat."
    mora "Is buttered toast okay?"
    my "Yeah. Not too burnt. Thank you."
    "She gets out some bread, and pops it into the toaster."
    "She prepares the butter and plate ready."
    "I wait patiently."
    "Once the toast pops up, she butters it evenly."
    "She hands me the plate, and also a glass of water."
    mora "Hydration is important."
    my "Thank you."
    mora "I keep telling you. There is no need to thank me. It is simply my job."
    my "Your job involves looking after your captors?"
    show mora arbiter no_coat eyes_closed normal
    mora "..."
    "I smile."
    my "I see."
    show mora arbiter no_coat normal
    "She begins making her own breakfast, which is a bowl of weetabix with blueberries, and water."
    "She sits down next to me."
    "I take a bite of the toast."
    "It's soft, just the way I like it. I don't really like burnt toast."
    my "This is yummy."
    mora "Good."
    "We eat in silence."
    "When we finish, she grabs the plates and quickly washes them."
    "I watch, surprised at how effiecient she works."
    "So swift and smooth."
    "No stumbles or mistakes."
    "It's almost robotic..."
    mora "I'm done now."
    mora "Get ready, we're leaving soon."
    my "Huh-"
    my "Leaving? Where to?"
    mora "To work, of course."
    hide mora
    with moveoutright
    my "What-?"
    "She leaves before I can press further."
    "Huh... Am I going to work?"
    "This is one weird kidnapping scenario..."

    scene bg living room day
    with fade
    "I head back to the room."
    "I'm already dressed so..."
    "I brush my hair with my fingers, and straighten my creased clothes."
    "It's the best I can do..."
    "I check in a mirror."
    "I look a bit dishevelled but overall okay."
    "Work appropriate, at least."
    "Soon, Mora returns."
    show mora arbiter normal
    with moveinright
    mora "Right. Ready?"
    my "Yeah... Are we going to your work or mine?"
    mora "Yours."
    mora "Life will continue as normal on the outside. It's only that I'll have to follow you everywhere."
    mora "You can return to your house if you want to, but I will have to be there all of the time."
    my "Oh..."
    my "So why'd you kidnap me instead of like, asking me?"
    mora "I was forced to."
    mora "Let's go."
    my "Okay..."

    scene bg stage
    play music stage_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal
    "We arrive."
    mora "This is..."
    my "Bright, right? Haha."
    mora "I suppose."
    my "I'm a stage manager."
    mora "I know."
    my "Of course..."
    "???" "Alex!"
    my "Ah-"
    "I turn around."
    show mora arbiter normal at left
    with moveinright
    show eli work eyes_closed normal at right
    with moveinright
    eli "Good morning!"
    my "Good morning."
    my "I'm sorry about disappearing yesterday, I-"
    eli "Oh, don't worry, we got a note!"
    my "A... Note?"
    show eli work normal
    eli "Didn't you write it?"
    "I look over to Mora."
    "She nods."
    my "Ah, yeah I did."
    my "Sorry, I forgot."
    eli "Well then!"
    eli "Let's do our best today!"
    my "Mhm..."
    hide eli
    with moveoutright
    show mora arbiter normal at center
    with moveinright
    "She leaves."
    "I turn back to Mora."
    my "That's Eli, one of my colleagues."
    my "She's cheerful. It helps lift my mood all the time."
    mora "Good."
    my "Well, I'd better get to work..."
    mora "I will only watch."
    my "Okay!"
    "I begin work."
    hide mora
    "{b}{u}A few hours later...{/u}{/b}"
    "I work rather focusedly, considering what happened yesterday."
    "The day goes by rather quickly."
    "Eventually, it's the end of the day."
    "I pack up, and head to where Mora has been stood for most of the day."
    show mora arbiter normal
    my "Don't your legs get tired?"
    mora "No."
    my "Wow... I'm jealous."
    "I chuckle."
    mora "Are you done?"
    my "Yep."
    mora "Let's go."
    my "Okay."
    "We leave."

    scene bg city raining
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter eyes_closed normal
    "It's raining again."
    "It wasn't too bad this morning, but it's gotten heavier..."
    "I pull out my umbrella."
    "We begin walking, but I notice she's not walking beside me."
    my "Hey, this umbrella is big enough for the both of us, you know."
    show mora arbiter normal
    mora "I'm fine."
    my "But you're getting soaked..."
    mora "Don't worry."
    my "Eh..."
    menu chapter1_day3_menu1:
        "Give her the umbrella.":
            $ mora_affection += 2
            $ chapter1_day3_moraumbrella = True
            my "Fine."
            my "If you're gonna be stubborn..."
            "I pass the umbrella to her."
            my "Here."
            mora "What-"
            mora "No, I've already said I'm fine."
            my "I insist."
            my "I'd rather me getting soaked than you."
            mora "No."
            mora "You're getting soaked yourself now."
            mora "It only means we're both wet, which does nothing."
            my "Well then..."
            "I put the umbrella away."
            my "If you're gonna be stubborn, I'll be stubborn too."
            show mora arbiter eyes_closed normal
            mora "Sigh..."
            mora "Fine, have it your way."
            "We continue walking through the rain."
        "Ignore her.":
            my "Fine."
            my "If you're gonna be stubborn..."
            my "It's you who'll be regretting it later."
            show mora arbiter eyes_closed normal
            mora "..."
            "We continue walking through the rain."
    
    scene bg living room day
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter eyes_closed normal
    "We return back to her place."
    if not chapter1_day3_moraumbrella:
        "She stands there, soaking wet, and I do feel a bit of guilt, but it {i}was{/i} her choice..."
    my "Mind if I crash here again? My house is so far away..."
    mora "Do what you like."
    my "Thanks..."
    hide mora
    with moveoutright
    if not chapter1_day3_moraumbrella:
        "She leaves, I assume to go dry off."
    else:
        "She leaves, I assume to change out of her uniform."
    "I flop onto the couch, feeling exhausted."
    "I decide to watch a bit of TV to kill time."
    "{b}{u}An hour later...{/u}{/b}"
    show mora casual ponytail normal
    "It's been about an hour."
    "Mora came back at some point, and we've just been sitting watching the TV."
    "Just whatever show was on at the time."
    "Finally, she stands up."
    mora "I'm going to make dinner now."
    my "Ah, okay!"
    my "I'm hungry again..."
    mora "It has been a few hours since you ate."
    mora "It will be done soon."
    my "Thanks!"
    hide mora
    with moveoutleft
    "She heads into the kitchen."
    "I continue watching TV for now."
    "{b}{u}30 minutes later...{/u}{/b}"
    mora "Dinner is done!"
    "She calls from the kitchen."
    "I turn the TV off and head into the kitchen."

    scene bg kitchen day
    with fade
    show mora casual ponytail normal
    "I enter the kitchen."
    my "Mm... It smells delicious..."
    "I sit down at the counter."
    "Mora dishes up."
    mora "It's a chicken and mushroom pie with diced potatoes and baked beans."
    my "Wow..."
    mora "Enjoy."
    "I dig in."
    my "It's delicious!"
    mora "Good."
    "I eat it quickly."
    "She eats hers a bit more slowly."
    "When we're done, she serves pudding."
    mora "A triple chocolate trifle."
    my "Oh wow... I'm getting a buffet here!"
    "I chuckle."
    mora "Enjoy."
    my "Are you not gonna have any pudding?"
    mora "I am not allowed."
    my "Aw..."
    "I decide not to press further."
    "It's none of my business, really."
    "I eat the trifle happily."
    "When I'm done, she washes the plates."
    "After that, we head back into the room."

    scene bg living room night
    with fade
    show mora casual ponytail normal
    mora "It is getting dark now."
    my "Yep..."
    my "What time is it now?"
    mora "Around 8pm."
    my "Oh wow..."
    my "Usually I'd go to bed around this time..."
    my "Unless there was a late stage show, of course, haha."
    mora "Would you like to go to sleep now?"
    my "Yeah, I think I will."
    mora "Okay."
    mora "I will leave you to sleep."
    mora "I'll see you in the morning."
    my "Okay, goodnight!"
    show mora casual ponytail eyes_closed normal
    mora "Goodnight."
    hide mora
    with moveoutright
    "Mora leaves the room."
    "I curl up onto the sofa."
    "I'm so tired, I go to sleep almost immediately again..."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter1_day4_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter1_day3_end:
        "Day 3 complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter1_day4
label chapter1_day3_morapush:
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    scene bg living room day
    with fade
    "I open my eyes."
    "The brightness is blinding. It takes a moment to adjust."
    "I sit up, stretching."
    "Just then, Mora walks in."
    show mora underwear coat normal
    mora "Good morning."
    my "Ah... Good morning."
    my "Did you really sleep in just your underwear?"
    mora "Yes."
    my "{i}In January?{/i}"
    mora "..."
    my "Sigh..."
    mora "Would you like breakfast?"
    my "Yes please, I'm starving..."
    mora "Come with me."
    hide mora
    with moveoutleft
    "She heads into the kitchen."
    "I follow."

    scene bg kitchen day
    with fade
    show mora underwear coat normal
    mora "Sit down at the counter."
    "I take a seat."
    mora "Is buttered toast okay?"
    my "Yeah. Not too burnt. Thank you."
    "She gets out some bread, and pops it into the toaster."
    "She prepares the butter and plate ready."
    "I wait patiently."
    "Once the toast pops up, she butters it evenly."
    "She hands me the plate, and also a glass of water."
    mora "Hydration is important."
    my "Thank you."
    mora "I keep telling you. There is no need to thank me. It is simply my job."
    my "Your job involves looking after your captors?"
    show mora underwear coat eyes_closed normal
    mora "..."
    "I smile."
    my "I see."
    show mora underwear coat normal
    "She begins making her own breakfast, which is a bowl of weetabix with blueberries, and water."
    "She sits down next to me."
    "I take a bite of the toast."
    "It's soft, just the way I like it. I don't really like burnt toast."
    my "This is yummy."
    mora "Good."
    "We eat in silence."
    "When we finish, she grabs the plates and quickly washes them."
    "I watch, surprised at how effiecient she works."
    "So swift and smooth."
    "No stumbles or mistakes."
    "It's almost robotic..."
    mora "I'm done now."

    scene bg living room day
    with fade
    show mora underwear coat normal
    "We head back to the room."
    mora "I was going to take you to work today, but my uniform is still soaking."
    "She gives me a glare."
    my "I already said sorry..."
    my "Wait-"
    my "Work?!"
    mora "Yes."
    mora "Life will continue as normal on the outside. It's only that I'll have to follow you everywhere."
    mora "You can return to your house if you want to, but I will have to be there all of the time."
    my "Oh..."
    my "So why'd you kidnap me instead of like, asking me?"
    mora "I was forced to."
    my "Oh..."
    my "Well, can't you just get into some other clothes?"
    mora "I am not allowed to wear casual clothes outside of the house."
    my "Oh. Well that's a stupid rule."
    mora "It's still the rule."
    my "Sure..."
    my "Well..."
    my "I can always call for the day off?"
    mora "No."
    mora "Things must continue as normal."
    my "Do you not have another set of uniform?"
    mora "No."
    my "Well..."
    my "We can always stop at the laundromat on the way there?"
    my "It's still early, I think we have time."
    mora "How am I meant to get there without wearing the clothes?"
    my "Surely being out for a few minutes won't hurt?"
    show mora underwear coat eyes_closed normal
    mora "..."
    mora "I suppose..."
    my "See?"
    my "Now get dressed quickly."
    mora "Okay."
    hide mora
    with moveoutright
    "She leaves."
    "I'm already dressed so..."
    "I brush my hair with my fingers, and straighten my creased clothes."
    "It's the best I can do..."
    "I check in a mirror."
    "I look a bit dishevelled but overall okay."
    "Work appropriate, at least."
    "Soon, Mora returns."
    show mora casual coat normal
    with moveinright
    mora "I'm ready."
    "She's carrying a bag with her wet clothes in."
    my "Ah, good."
    mora "I have my Arbiter coat on at least."
    my "Yeah, so you got something!"
    my "Come on, let's go!"
    mora "Okay."

    scene bg laundromat
    with fade
    show mora casual coat normal
    "We arrive at the laundromat."
    "It isn't a long walk from her apartment."
    my "Do you know how to use it?"
    mora "Yes."
    "She puts her clothes in the tumble dryer, and puts some money in."
    "The machine starts working."
    "While waiting, we sit atop a counter."
    my "Why is your work so strict anyways?"
    show mora casual coat eyes_closed normal
    mora "It's the {i}government.{/i}"
    my "Eh... True."
    my "Do you enjoy it?"
    mora "No."
    show mora casual coat normal
    mora "Wait-"
    my "Why do you continue working there then?"
    mora "I have to."
    mora "I..."
    "She stands up."
    mora "This is an inappropriate conversation."
    my "..."
    "I thought I was getting somewhere... Fuck..."
    mora "It is done."
    "She opens the tumble dryer, and pulls out her now dry clothes."
    mora "They're warm..."
    mora "I'm going to get changed. I'll be back shortly."
    hide mora
    with moveoutright
    "She leaves to the toilets."
    "I wait patiently."
    "I can't stop thinking about what she said, though."
    "Why can't she leave? Is she in danger?"
    "I mean... They're making her do some pretty bad shit..."
    "I sigh."
    "Maybe I can help her."
    "I'll try my best!"
    "A few minutes later, she returns."
    show mora arbiter normal
    with moveinright
    mora "Much better."
    mora "Let's go to your work."
    my "Okay."
    "We exit."

    scene bg stage
    play music stage_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal
    "We arrive."
    mora "This is..."
    my "Bright, right? Haha."
    mora "I suppose."
    my "I'm a stage manager."
    mora "I know."
    my "Of course..."
    "???" "Alex!"
    my "Ah-"
    "I turn around."
    show mora arbiter normal at left
    with moveinright
    show eli work eyes_closed normal at right
    with moveinright
    eli "Good morning!"
    my "Good morning."
    my "I'm sorry about disappearing yesterday, I-"
    eli "Oh, don't worry, we got a note!"
    my "A... Note?"
    show eli work normal
    eli "Didn't you write it?"
    "I look over to Mora."
    "She nods."
    my "Ah, yeah I did."
    my "Sorry, I forgot."
    eli "Well then!"
    eli "Let's do our best today!"
    my "Mhm..."
    hide eli
    with moveoutright
    show mora arbiter normal at center
    with moveinright
    "She leaves."
    "I turn back to Mora."
    my "That's Eli, one of my colleagues."
    my "She's cheerful. It helps lift my mood all the time."
    mora "Good."
    my "Well, I'd better get to work..."
    mora "I will only watch."
    my "Okay!"
    "I begin work."
    hide mora
    "{b}{u}A few hours later...{/u}{/b}"
    "I work rather focusedly, considering what happened yesterday."
    "The day goes by rather quickly."
    "Eventually, it's the end of the day."
    "I pack up, and head to where Mora has been stood for most of the day."
    show mora arbiter normal
    my "Don't your legs get tired?"
    mora "No."
    my "Wow... I'm jealous."
    "I chuckle."
    mora "Are you done?"
    my "Yep."
    mora "Let's go."
    my "Okay."
    "We leave."

    scene bg living room day
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter eyes_closed normal
    "We return back to her place."
    my "Mind if I crash here again? My house is so far away..."
    mora "Do what you like."
    my "Thanks..."
    "I flop onto the couch, feeling exhausted."
    "I decide to watch a bit of TV to kill time."
    hide mora
    "{b}{u}An hour later...{/u}{/b}"
    show mora arbiter no_coat normal
    "It's been about an hour."
    "Mora got out of her coat at some point, and we've just been sitting watching the TV."
    "Just whatever show was on at the time."
    "Finally, she stands up."
    mora "I'm going to make dinner now."
    my "Ah, okay!"
    my "I'm hungry again..."
    mora "It has been a few hours since you ate."
    mora "It will be done soon."
    my "Thanks!"
    hide mora
    with moveoutleft
    "She heads into the kitchen."
    "I continue watching TV for now."
    "{b}{u}30 minutes later...{/u}{/b}"
    mora "Dinner is done!"
    "She calls from the kitchen."
    "I turn the TV off and head into the kitchen."

    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    "I enter the kitchen."
    my "Mm... It smells delicious..."
    "I sit down at the counter."
    "Mora dishes up."
    mora "It's a chicken and mushroom pie with diced potatoes and baked beans."
    my "Wow..."
    mora "Enjoy."
    "I dig in."
    my "It's delicious!"
    mora "Good."
    "I eat it quickly."
    "She eats hers a bit more slowly."
    "When we're done, she serves pudding."
    mora "A triple chocolate trifle."
    my "Oh wow... I'm getting a buffet here!"
    "I chuckle."
    mora "Enjoy."
    my "Are you not gonna have any pudding?"
    mora "I am not allowed."
    my "Aw..."
    "I decide not to press further."
    "It's none of my business, really."
    "I eat the trifle happily."
    "When I'm done, she washes the plates."
    "After that, we head back into the room."

    scene bg living room night
    with fade
    show mora arbiter no_coat normal
    mora "It is getting dark now."
    my "Yep..."
    my "What time is it now?"
    mora "Around 8pm."
    my "Oh wow..."
    my "Usually I'd go to bed around this time..."
    my "Unless there was a late stage show, of course, haha."
    mora "Would you like to go to sleep now?"
    my "Yeah, I think I will."
    mora "Okay."
    mora "I will leave you to sleep."
    mora "I'll see you in the morning."
    my "Okay, goodnight!"
    show mora arbiter no_coat eyes_closed normal
    mora "Goodnight."
    hide mora
    with moveoutright
    "Mora leaves the room."
    "I curl up onto the sofa."
    "I'm so tired, I go to sleep almost immediately again..."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter1_day4_avail = True
    scene black
    with fade
    centered "End of day."
    jump chapter1_day3_end
label chapter1_day3_moraalmostkill:
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    scene bg living room day
    with fade
    "I open my eyes."
    "The brightness is blinding. It takes a moment to adjust."
    "I sit up, stretching."
    "Just then, Mora walks in."
    show mora arbiter no_coat normal
    with moveinright
    mora "..."
    my "..."
    show mora arbiter no_coat eyes_closed normal
    mora "Hmph."
    hide mora
    with moveoutleft
    "She walks straight past me, into the kitchen."
    "I follow her."

    scene bg kitchen day
    with fade
    show mora arbiter no_coat normal
    "We enter the kitchen."
    mora "Are you looking for another chance to kill me?"
    my "..."
    my "Look, I'm sorry-"
    show mora arbiter no_coat eyes_closed normal
    mora "I don't want to hear it."
    my "I get it, you're upset."
    mora "Why would I not be?!"
    my "..."
    my "I'm sorry..."
    "She sighs."
    show mora arbiter no_coat normal
    mora "You do realise who you're messing with, right?"
    mora "Did you forget who I work for?"
    my "..."
    my "Ah."
    "Shit."
    mora "All it takes is one report."
    mora "You'll be arrested."
    mora "Your life will be ruined."
    my "..."
    my "I'm sorry..."
    mora "Sorry doesn't cut it."
    mora "You tried to {i}kill{/i} me."
    my "It was in the heat of the moment..."
    my "I let my emotions blind me..."
    mora "You should've known better."
    mora "{i}Look{/i} at me."
    "I now notice that she is still wearing her uniform."
    "She's still soaking."
    "Did she not even dry herself?!"
    my "Why don't you change out of your uniform?"
    my "Have you been in that all night?"
    show mora arbiter no_coat eyes_closed normal
    mora "..."
    "I sigh."
    my "You should get changed."
    my "You could get hypothermia!"
    mora "I'm fine."
    my "No you're not!"
    my "Look, I've already said sorry, okay?"
    my "I don't want you hurt really..."
    mora "..."
    show mora arbiter no_coat normal
    mora "Do you mean that?"
    my "Yes."
    my "I really am sorry."
    mora "..."
    mora "Sigh."
    mora "I suppose it doesn't matter."
    mora "Even if I did report you, I'd just be shoved onto a new subject."
    mora "Plus, you seem..."
    my "Hm?"
    show mora arbiter no_coat eyes_closed normal
    mora "..."
    mora "Never mind."
    show mora arbiter no_coat normal
    mora "Anyways, it's time for breakfast."
    mora "I'll make you some because I have to."
    my "Ah... Okay..."
    mora "Sit down at the counter."
    "I take a seat."
    mora "Is buttered toast okay?"
    my "Yeah. Not too burnt. Thank you."
    "She gets out some bread, and pops it into the toaster."
    "She prepares the butter and plate ready."
    "I wait patiently."
    "Once the toast pops up, she butters it evenly."
    "She hands me the plate, and also a glass of water."
    mora "Hydration is important."
    my "Thank you."
    mora "I keep telling you. There is no need to thank me. It is simply my job."
    my "Your job involves looking after your captors?"
    show mora arbiter no_coat eyes_closed normal
    mora "..."
    "I smile."
    my "I see."
    show mora arbiter no_coat normal
    "She begins making her own breakfast, which is a bowl of weetabix with blueberries, and water."
    "She sits down next to me."
    "I take a bite of the toast."
    "It's soft, just the way I like it. I don't really like burnt toast."
    my "This is yummy."
    mora "Good."
    "We eat in silence."
    "When we finish, she grabs the plates and quickly washes them."
    "I watch, surprised at how effiecient she works."
    "So swift and smooth."
    "No stumbles or mistakes."
    "It's almost robotic..."
    mora "I'm done now."
    my "Ah."
    "She stands up."
    my "Are you gonna get changed?"
    mora "I am not allowed to wear casual clothes outside of the house."
    my "Oh. Well that's a stupid rule."
    mora "It's still the rule."
    my "Sure..."
    my "Well..."
    my "I can always call for the day off?"
    mora "No."
    mora "Things must continue as normal."
    my "What do you mean?"
    mora "Life will continue as normal on the outside. It's only that I'll have to follow you everywhere."
    mora "You can return to your house if you want to, but I will have to be there all of the time."
    my "Oh..."
    my "So why'd you kidnap me instead of like, asking me?"
    mora "I was forced to."
    my "Oh..."
    "I sigh."
    my "Well, we're in a sticky situation here, aren't we?"
    my "Do you not have any spare uniform?"
    mora "No."
    my "Right."
    my "Well... I suppose I'm not going then."
    mora "You have to."
    my "I don't."
    my "I can just call in sick."
    my "I get sick a lot, so it won't be abnormal to them, I promise."
    show mora arbiter no_coat eyes_closed normal
    mora "Why do you care so much...? I've already said I'm fine..."
    mora "Anyone would think you didn't try to kill me."
    my "I just... want to redeem myself, I suppose."
    show mora arbiter no_coat normal
    mora "It won't work."
    my "Do you have a phone I can use?"
    mora "You can use mine."
    "She hands me her phone."
    "I key in my work's number, and call them."
    eli "Hello?"
    "Eli picks up, much to my relief."
    "I explain a fake situation of how I've been really sick and can't come in."
    eli "Oh no..."
    eli "I hope you feel better soon!"
    eli "Don't worry, we'll cover for you!"
    my "Thank you Eli."
    my "I'll be back soon!"
    eli "Hopefully!"
    eli "Stay safe~!"
    "I hang up, turning to Mora."
    my "See? Told you, it worked."
    mora "..."
    mora "Good."
    "She's probably pouty because she was wrong, haha."
    my "Well..."
    my "You should take a bath, get warmed up, and change clothes."
    my "I'll stay here, don't worry."
    show mora arbiter no_coat eyes_closed normal
    mora "You know I can't leave you here."
    my "Eh..."
    my "Do you want me to come in with you?"
    mora "Not into the bath, but in the room, yes."
    my "That's... What I meant..."
    "I look away, slightly embarrassed that she thought that."
    
    scene bg bathroom
    with fade
    show mora arbiter no_coat normal
    with moveinright
    "We enter the bathroom."
    "She turns on the fan and water switch, and gets undressed."
    show mora underwear normal
    with ease
    "She strips down to her underwear, but no further."
    "I try not to stare for too long."
    scene bg bathroom foggy
    with fade
    show mora underwear normal
    "The bathroom soon steams up."
    "When the bath finally fills up, she turns off the water, and steps into the bath."
    "I sit on the floor."
    show mora underwear eyes_closed normal
    "She lays in the bath, taking some deep breaths."
    my "Baths are so relaxing, aren't they?"
    mora "Mhm."
    my "Hey, I just noticed, you always wear those gloves, why is that?"
    mora "It's a personal thing."
    my "Oh, okay. I won't pry then."
    "Not to do with work then..."
    "I'll leave her be for now."
    "I fiddle with my fingers, waiting."
    show mora underwear normal
    mora "You look tense."
    "I look up."
    "She's staring straight at me."
    my "Oh, no, I'm not..."
    my "I'm just a bit bored..."
    mora "I apologise for boring you."
    my "Eh..."
    "I avert my eyes."
    my "It's not you... just sitting here doing nothing..."
    mora "You could always bath with me."
    my "!!!"
    "What the fuck?!"
    "She can't just suggest that out of the blue!"
    "I feel my face turning red."
    my "No! We barely know each other!"
    my "It's already weird enough, us seeing each other naked, but that's going way too far!"
    mora "I don't understand why you're uncomfortable."
    mora "However, as I've said, my job becomes a lot harder when the subject is uncomfortable."
    my "What even is your job?!"
    my "It seems like you're being {i}too{/i} nice..."
    show mora underwear eyes_closed normal
    mora "You do not have to watch me bathe."
    mora "Although I have to watch you, you do not have to watch me."
    mora "You can face the wall, or wait in the hallway, as long as I can see you."
    my "Ah-"
    "Why didn't I think of that first??"
    "It's almost like..."
    "I wanted..."
    "Ew!!!"
    "I stand up quickly, almost falling over."
    my "Fine, I'm waiting outside..."
    mora "That is fine."
    mora "Just keep within my eyesight."
    "I practically run away."

    scene black
    with fade
    centered "{b}{u}30 minutes later...{/u}{/b}"

    scene bg living room day
    with fade
    show mora casual ponytail normal
    with moveinright
    "She eventually finishes the bath, and gets dressed into some clean clothes, putting hers into the apartment's washing machine."
    "We return to the room."
    my "I bet that feels better."
    mora "A bit."
    my "Well... What should we do now?"
    mora "I have a lot of movies."
    my "Oh?"
    mora "You can watch whatever you want. I'll be doing work at the table."
    my "Oh, okay..."
    "{i}Why did part of me want her to watch with me...?{/i}"
    hide mora
    "She sits down at the table with a laptop."
    "I turn on the TV and flick through her library."
    "There's some good stuff on there..."
    "Our tastes seem kinda similar..."
    "After some contemplating, I decide on a movie, and begin watching."
    "She types away on her laptop in the background."
    "It's the first time I've seen her do anything that resembles actual work..."
    "She's more like a host, really..."
    "{b}{u}2 hours later...{/u}{/b}"
    "It's been a couple of hours."
    "The movie finishes."
    "It was really great... I was totally captivated for the whole thing."
    "I enjoyed it."
    "I check the time."
    my "1pm already..."
    "I turn to Mora."
    my "Hey, Mora-"
    my "Ah."
    show mora casual ponytail eyes_closed normal
    "She seems to have fallen asleep at the laptop."
    "I bet she couldn't sleep well in those soaked clothes..."
    "That ever-so-familiar guilty feeling washes over me."
    "I should've held back..."
    "I regret what I did."
    "But I can redeem myself."
    "I didn't kill her, that's what matters."
    "Even if... I really wanted to..."
    "I sigh."
    "Better make lunch."
    
    scene bg kitchen day
    with fade
    "I head into the kitchen."
    my "Let's see what we got here..."
    "I look through the cupboards."
    "She has a lot of really yummy ingredients..."
    "I could make a lot with all this..."
    "I grab some bread, butter, and cooked chicken slices."
    "A chicken sandwich. Lovely."
    "I prepare two sandwiches, one for me, and one for her, whenever she wakes up."
    "I also get a couple of glasses of water."

    scene bg living room day
    with fade
    "I carry my food in, placing it on the coffee table, and then place hers gently on the table next to her."
    "I then pry away the laptop so she doesn't damage it accidentally."
    "She continues sleeping."
    "She looks peaceful..."
    "It's nice to see, really."
    "With a job like hers, it must be rare to relax."
    "I sit back down on the sofa, grabbing my plate, and taking a bite."
    "The chicken is tender and nice."
    "The bread is soft."
    "It's nice."
    "I eat happily."
    "She continues sleeping."
    "{b}{u}A few hours later...{/u}{/b}"
    "It's been a few hours."
    "I watched another movie, and started a TV show I've been meaning to watch."
    "She's continued to sleep."
    "She must've been exhausted..."
    scene bg living room night
    with flash
    "{b}{u}A few more hours later...{/u}{/b}"
    "It's getting rather late now."
    "I'm a bit concerned."
    "She hasn't moved at all..."
    "I stand up, going over to where she's laying."
    show mora casual ponytail eyes_closed normal
    "I gently tap her shoulder."
    my "Mora?"
    "No response."
    "I shake her."
    my "Mora?!"
    "I'm getting a bit desperate now."
    "I shake her harder."
    mora "Mm..."
    mora "What?"
    my "Oh thank goodness..."
    show mora casual ponytail normal
    "She sits up, looking around."
    my "I was worried. You've been asleep for {i}ages.{/i}"
    mora "I... Fell asleep?"
    my "Yeah..."
    my "Are you okay?"
    "She looks up at me."
    mora "Yeah, I'm fine."
    "Her expression looks a bit shocked."
    "Did she surprise even herself??"
    my "Sure?"
    mora "Mhm."
    mora "What time is it?"
    "I check the clock."
    my "7pm."
    mora "Oh."
    mora "Shit..."
    my "Yeah..."
    my "It's been about 9 hours."
    mora "You probably want dinner."
    my "Well-"
    my "If you don't feel well-"
    mora "I'm fine."
    "She stands up, heading to the kitchen."
    my "Sigh."
    "She's so damn stubborn..."

    scene bg kitchen day
    with fade
    show mora casual ponytail normal
    with moveinright
    mora "Take a seat."
    mora "It won't be long."
    my "You really don't have to..."
    mora "Don't worry about me."
    my "If you say so..."
    "She begins making a small meal for us both."
    "{b}{u}15 minutes later...{/u}{/b}"
    mora "It's done."
    "She hands me a plate of fishcake, fries and mushy peas."
    "She sits down next to me, and we eat."
    my "Thank you..."
    mora "There's no need to-"
    my "Yeah yeah, I know."
    "I chuckle."
    mora "..."
    "We eat in silence."
    "When we're done, she washes the plates."

    scene bg living room night
    with fade
    show mora casual ponytail normal
    "We head back into the room."
    "It's rather late now."
    "I begin to feel that familiar tiredness."
    my "I really don't wanna go to bed..."
    mora "Why not?"
    my "You're not gonna sleep tonight, are you?"
    my "You slept all through today instead..."
    mora "Do not worry about me."
    mora "Sleep well."
    hide mora
    with moveoutright
    "Before I can argue, she leaves."
    "Typical."
    "I sigh."
    "Guess I'm going to sleep..."
    "I curl up on the sofa, turning on the TV for background noise."
    "Usually that helps me."
    "Tonight, unlike the last couple of nights, I don't immediately pass out."
    "I close my eyes, attempting to sleep."

    scene black
    with fade
    "I'm half conscious."
    "I was close to sleeping, but then..."
    "A phone rings."
    "I begin to wake up, but someone else answers it."
    mora "Hello?"
    "???" "Hello, Mora."
    mora "Oh."
    "She sighs."
    mora "Why are you calling this late?"
    "???" "I was wondering how you're getting along with your new captor."
    mora "..."
    mora "It's okay, I guess."
    "???" "Oh?"
    "???" "You're not as whiney as usual."
    mora "I don't want to talk about it."
    "???" "Ahaha."
    mora "Don't get any ideas in that pathetic empty head of yours."
    mora "There's nothing going on."
    "???" "Bet."
    "???" "Anyways, if everything is going fine, I'll leave you be. Goodnight~!"
    "The person hangs up."
    "Mora lets out a deep sigh."
    mora "Damn it... Why does she know so much..."
    "Footsteps."
    "I keep my eyes closed tightly."
    mora "You have no idea how important you are to me..."
    mora "Alex..."
    "A hand touches my head."
    "Only for a second."
    mora "Goodnight. Sleep well."
    "She walks away."
    "I let out a large exhale."
    "I didn't realise I was holding my breath through that..."
    "What did she mean by that...?"
    "No way..."
    "I internally groan."
    "I'm not gonna get involved in this."
    "I don't care how she feels."
    "I finally begin to slip into slumber."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter1_day4_avail = True
    scene black
    with fade
    centered "End of day."
    jump chapter1_day3_end