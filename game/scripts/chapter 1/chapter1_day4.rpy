label chapter1_day4:
    scene black
    with fade
    centered "Day 4 - Thursday 4th January."
    pause 1.0
    if mora_almost_kill == True:
        jump chapter1_day4_moraalmostkill
    ###
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    scene bg living room day
    with fade
    "It's a new day."
    "I sit up, yawning and stretching."
    "Mora enters."
    show mora arbiter normal
    with moveinright
    mora "Good morning."
    my "Good morning!"
    my "I'm going to work today again, right?"
    mora "That's right."
    mora "Get ready. I'll make breakfast."
    my "Thanks..."
    hide mora
    with moveoutleft
    "She heads into the kitchen."
    "I straighten myself up ready for work."
    "Then I head into the kitchen to her."

    scene bg kitchen day
    with fade
    show mora arbiter normal
    my "Mm, smells yummy!"
    mora "It's eggs on toast, this morning."
    my "Yum..."
    "I sit down at the counter, just as she finishes preparing the food."
    "She hands me my plate."
    my "Thank you!"
    mora "There's no need to thank me."
    "She sits down next to me."
    "We eat."
    "When we're done, she washes the plates."
    mora "All done."
    mora "Are you ready to go?"
    my "Yeah."
    mora "Let's go then."

    scene bg stage
    play music stage_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal at left
    show eli work eyes_closed normal at right
    "We arrive at work."
    "Eli is waiting for me."
    eli "Good morning!"
    my "Good morning!"
    eli "Guess what~?"
    my "What? You seem happier than even normal..."
    eli "Ehehe."
    eli "I'm just excited!"
    my "Why?"
    eli "Well..."
    eli "The Artificial Interspace are here again!"
    my "Woah!"
    my "Why??"
    eli "They said they want to hold another show here!!"
    my "Wow..."
    my "Are they backstage?"
    eli "Mhm!"
    my "I'll go talk to 'em!"
    eli "Oki doki!"
    eli "We'll continue preparing for now!"
    my "Yep!"
    hide eli
    with moveoutright
    show mora arbiter normal at center
    with move
    "I turn to Mora."
    my "Hey, Mora, I'd love for you to meet these girls!"
    mora "I don't have a choice, anyways... I have to follow you..."
    my "I'm sure you'll love them! They're a bunch of cuties!"
    "I chuckle."
    "Her glare remains unchanged."
    "I sigh, shaking my head."
    my "Come on, let's go."

    scene bg backstage
    with fade
    show amari casual normal at t_xpos(250)
    show angela casual normal at t_xpos(650)
    show zena newstudent normal at t_xpos(1000)
    show mora arbiter normal at t_xpos(-150)
    "We head backstage, where the girls are waiting."
    my "Hello~!"
    show angela casual talk
    angela "Oh, hello again!"
    angela "It's nice to see you again!"
    my "Likewise!"
    zena "..."
    mora "..."
    my "Eh-"
    "Zena and Mora are giving each other death stares..."
    "..."
    "Come to think of it-"
    my "Zena are you an Arbiter?!"
    "I blurt out."
    "To my surprise, she actually replies."
    show zena newstudent talk
    zena "Yes."
    my "Wha-"
    my "So you and Mora are work colleagues?!"
    show mora arbiter eyes_closed normal
    mora "...Technically."
    my "Ah..."
    my "That's where the tense atmosphere comes from..."
    show zena newstudent eyes_closed talk
    zena "It just isn't very often that colleagues meet, even inside of work."
    my "Oh... I see... Must be awkward for you both then, huh."
    "They both nod."
    my "I see..."
    show angela casual eyes_closed talk
    angela "Zena is my Arbiter."
    angela "We kind of forced her into becoming an idol with us, hahaha."
    my "Wow..."
    my "It's such a small world..."
    show amari casual eyes_closed normal
    amari "Right~?"
    my "Yeah..."
    my "Uh, anyways, what are you all doing here?"
    my "I heard you were planning on doing another show here?"
    show angela casual talk
    angela "Oh, right!"
    angela "Yeah, we're planning to at the end of the month!"
    my "Really? So soon?"
    angela "Yeah..."
    show amari casual talk
    amari "We really loved the feel of the stage! We wanna use it more often!"
    amari "If... That's okay..."
    my "No, I'd love that!"
    amari "Yay~!"
    "I smile."
    show zena newstudent normal
    zena "Of course, we'd have to figure out more in-depth details, but I have a rough schedule of how much we'll use the stage."
    "She hands me a document."
    my "Oh wow, you're prepared..."
    show angela casual eyes_closed normal
    angela "Arbiters can be rather useful..."
    my "Ahaha, I bet they can be."
    "I glance at Mora."
    show mora arbiter normal
    mora "Whatever it is you're thinking, {i}no.{/i}"
    my "Aw... I didn't even say anything!"
    mora "Hmph."
    "Me and Angela chuckle."
    "I give the timetable a quick glance over."
    my "Okay, this looks fine, but I'll have to cross-check with the booking system..."
    my "If that's okay, then we're all set!"
    show amari casual eyes_closed normal
    amari "Yay!"
    show angela casual talk
    angela "I look forward to it!"
    "Zena turns to Mora."
    zena "So, it is a possibility our paths may cross again."
    show mora arbiter eyes_closed normal
    mora "Indeed."
    zena "I look forward to it."
    show mora arbiter normal
    mora "I don't."
    zena "Of course you don't..."
    mora "Shouldn't you get back to work, Alex?"
    my "Eh, okay then."
    my "I look forward to working with you girls!"
    angela "Same!"
    show amari casual eyes_closed talk
    amari "Goodbye!"
    zena "Bye."

    scene black
    with fade
    centered "{b}{u}A few hours later...{/u}{/b}"

    scene bg stage
    with fade
    "It's finally the end of the work day."
    "I did well today."
    "I gather my stuff and head to Mora."
    show mora arbiter normal
    mora "Ready to go?"
    my "Mhm."
    "We say goodbye and leave."

    scene bg living room day
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    with fade
    show mora arbiter normal
    "We return."
    mora "I shall make us dinner."
    my "Yeah, that'll be great... Thanks..."
    mora "Okay then."
    hide mora
    with moveoutleft
    "She leaves."
    "{b}{u}20 minutes later...{/u}{/b}"
    mora "It's done!"
    "She calls from the kitchen."
    "I stand up."
    "My stomach grumbles."

    scene bg kitchen day
    with fade
    show mora arbiter normal
    "I enter the kitchen."
    "My food is waiting for me."
    my "Thanks..."
    mora "..."
    my "Yeah. I know."
    "I smile to myself."
    "I take a seat. She does the same."
    "Today's meal is cheesy pasta and garlic bread."
    "Water too, of course."
    "At least she's helping me keep on top of my hydration..."
    "I feel a lot better recently..."
    "We eat."
    "{b}{u}10 minutes later...{/u}{/b}"
    "We're finished."
    "She grabs the plates, and washes them."
    "I stand up, brushing off stray crumbs."
    my "That was delicious."
    my "I love all cheesy meals."
    mora "Noted."
    my "Haha... You don't have to cook anything in particular for me."
    my "Thank you though!"

    scene bg living room night
    with fade
    show mora arbiter normal
    "We enter the room."
    "It's late now."
    my "I think I'll head to bed again..."
    mora "Okay. Sleep well."
    my "Thanks..."
    my "Goodnight."
    mora "Goodnight."
    hide mora
    with moveoutright
    "She leaves."
    "I curl up on the sofa, falling asleep immediately again..."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter1_day5_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter1_day4_end:
        "Day 4 complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter1_day5
label chapter1_day4_moraalmostkill:
    play music mora_theme fadein 0.5 fadeout 0.5 loop
    scene bg living room day
    with fade
    "I wake up."
    "It's a new day..."
    "I stand up, stretching."
    "Mora walks in shortly after."
    show mora casual ponytail normal
    mora "Good morning..."
    my "Good morning."
    my "Did you sleep at all?"
    mora "No."
    mora "I already told you not to worry."
    my "Eh... I can't help it."
    mora "Well."
    mora "I'm making breakfast."
    my "Okay..."
    my "I'll call into work again."
    mora "Okay."
    hide mora
    with moveoutleft
    "I grab the phone and dial work again."
    "{b}{u}10 minutes later...{/u}{/b}"
    mora "Breakfast is done!"
    "She calls from the kitchen."

    scene bg kitchen day
    with fade
    show mora casual ponytail normal
    "I enter the kitchen."
    "Breakfast is waiting for me."
    mora "It's eggs on toast today."
    my "Yum..."
    "I take a seat."
    "She sits next to me."
    "We eat."
    "It's still rather awkward between us..."
    "She doesn't seem as scared of me now, at least..."
    "I hope I can redeem myself."
    "I'll try my best...!"
    hide mora
    "{b}{u}5 minutes later...{/u}{/b}"
    show mora casual ponytail normal
    "We finish our food."
    "Mora grabs the plates and washes them."
    "We then return to the room."

    scene bg living room day
    with fade
    show mora casual ponytail normal
    my "Hey, Mora, I was wondering..."
    mora "What?"
    my "Could we go out somewhere today?"
    my "Like... A park or something?"
    my "Since I don't have work..."
    mora "I don't see why not."
    mora "Let me get dressed."
    my "Is your uniform dry now?"
    mora "It has been washed and dried, yes."
    my "Good."
    mora "I will be back shortly."
    hide mora
    with moveoutright
    "Mora leaves."
    "I straighten myself up, ready to leave."
    "I should probably grab my stuff from my home, if I'm moving here..."
    "Like clothes and stuff..."
    "{b}{u}A few minutes later...{/u}{/b}"
    show mora arbiter normal
    with moveinright
    "Mora returns."
    mora "Ready to go?"
    my "Yep!"
    mora "Let's go, then."

    scene bg park
    with fade
    show mora arbiter normal
    "We arrive at a nearby park."
    "The weather is actually fairly nice, for January, ignoring the cold wind."
    "We walk around quietly for a while, just taking in the scenery."
    "It's nice..."
    "Eventually, my legs get tired."
    "We sit down on a bench."
    show mora arbiter eyes_closed normal
    "Mora closes her eyes, taking some deep breaths."
    "I decide to do the same."
    my "This is so refreshing..."
    mora "Yes..."
    "We stay like this for a while, just taking in the moment."
    "It's the calmest I've been in a while."
    "Mora seems really relaxed too."
    "I'm glad about that."
    "After a while, I stand up."
    my "Should we get something to eat?"
    show mora arbiter normal
    mora "Like what?"
    my "There's a nice cafe near here..."
    mora "Okay then. We'll get lunch there."
    my "Yay!"
    "She stands up too."
    "We head to the cafe."
    
    scene bg restaurant a
    with fade
    show mora arbiter normal
    "We enter the cafe."
    "It's not too busy, thank goodness."
    "We take a seat."
    mora "This place seems..."
    my "Cozy?"
    mora "Yes, I suppose."
    my "Yeah, it's a nice place..."
    my "The staff are really friendly, and the food is great..."
    my "In my opinion at least, haha."
    "We grab a menu."
    mora "There's a lot of different foods here..."
    my "Yeah, that's one reason they're so popular!"
    my "We're lucky not many people are here, usually it's so packed..."
    my "Partly due to the sheer amount of options of dining here..."
    mora "I see..."
    mora "Well, I'd like to order the jacket potato with cheese and beans, and a glass of water."
    my "Wow that was quick-"
    my "Well uh..."
    "I scan the menu."
    my "I'll have the same!"
    mora "Really?"
    my "Yeah... I love jacket potato!"
    mora "Oh."
    mora "Noted."
    my "Haha..."
    "I call a waiter over, and they take our order."
    "While we're waiting, I decide to try to converse with her, to get to know her better."
    menu chapter1_day4_moraalmostkill_menu1:
        "What are your hobbies?" if not mora_hobbies_unlock:
            $ mora_hobbies_unlock = True
            my "Hey, Mora, what are your hobbies?"
            mora "I don't really have any..."
            my "Really?!"
            mora "Yeah."
            my "Wow..."
            mora "I suppose I enjoy reading."
            my "Ah, that's a start!"
            my "I like reading too!"
            mora "Oh."
            jump chapter1_day4_moraalmostkill_menu1
        "What does your job entail?" if not mora_job_unlock:
            $ mora_job_unlock = True
            my "Hey, what exactly does your job entail?"
            my "I've been curious for a while..."
            my "It feels more like you're a host than an Arbiter..."
            show mora arbiter eyes_closed normal
            mora "Sigh..."
            mora "Do you really want to know?"
            my "Yeah..."
            show mora arbiter normal
            mora "Fine."
            mora "My job is to keep an eye on you, to monitor if you're a threat to us, and if I find any threats, to report them."
            mora "Part of that role involves making sure you are well looked after."
            mora "If I don't look after you, you may end up turning against me, and trying to run away, or..."
            show mora arbiter eyes_closed normal
            mora "..."
            my "Ah."
            my "I think I understand."
            my "Well... Thank you for being honest with me. It helps."
            mora "Mhm."
            jump chapter1_day4_moraalmostkill_menu1
        "Do you enjoy your work?" if not mora_workenjoy_failed_unlock:
            $ mora_workenjoy_failed_unlock = True
            my "Do you enjoy your work, Mora?"
            "I ask out of curiosity."
            "She looks up at me."
            mora "I am not allowed to answer that."
            my "Ah-"
            my "Aw..."
            my "Okay then."
            "I got quickly shot down on that one..."
        "Done.":
            pass
    "Finally, our food arrives."
    "I thank the waiter, and we dig in."
    show mora arbiter eyes_closed normal
    mora "This is delicious..."
    my "Yeah, it is!"
    my "This place is the best!"
    mora "Mm..."
    "She eats slower than normal, savouring the flavour perhaps?"
    "I'm glad she's enjoying it, either way."
    "I'm enjoying mine too!"
    "It's been a long time since I've been here..."
    "I never had much time before..."
    "Now I do!"
    "I'm also doing a good job at redeeming myself, I think!"
    "She seems a lot more relaxed now. I really am glad."
    "We finish our food."
    show mora arbiter normal
    mora "That was great..."
    mora "Thank you."
    my "It-"
    my "AH-"
    "..."
    "DID SHE JUST THANK ME?!"
    "For the first time..."
    "No way."
    "Usually it wouldn't be a big deal, but she always seemed to hate being thanked, and never once thanked me."
    "It's weird hearing her say it..."
    "Not that I'm ungrateful."
    "I smile."
    my "You're welcome, Mora."
    my "Should we go back now?"
    mora "Mhm."
    "We leave."
    
    scene bg living room day
    with fade
    show mora arbiter normal
    "We return."
    my "That was nice."
    mora "Mhm."
    my "Thank you for taking me out."
    show mora arbiter eyes_closed normal
    mora "..."
    mora "There is no need to thank me."
    mora "I'm going to get back to work now."
    hide mora
    with moveoutleft
    "She heads to the table."
    my "Don't fall asleep again!"
    "I laugh."
    "{b}{u}A couple of hours later...{/u}{/b}"
    "I've been sitting on the sofa, watching more TV."
    "Mora has been super focused on her work."
    "No sleeping today, haha."
    "I stand up, heading over to her."
    show mora arbiter no_coat normal
    mora "What is it?"
    "She looks up at me."
    my "I'm a bit hungry..."
    mora "I'll make dinner."
    my "No-"
    my "You don't have to make anything..."
    my "I can cook myself, you know."
    my "Plus, you've already treated me once today."
    my "Why don't I cook something for you this time around?"
    mora "Okay."
    "Wow... I'd expected her to be a bit more humble about it..."
    my "What would you like?"
    mora "I don't mind."
    my "Eh... I'll make you a surprise then!"

    scene bg kitchen day
    with fade
    "I head into the kitchen."
    my "Right... Let's see what we've got here..."
    "I grab a few different ingredients from a few cupboards."
    "Time to get to work."
    "{b}{u}30 minutes later...{/u}{/b}"
    my "Dinner is done!"
    "I call out to her."
    show mora arbiter no_coat normal
    with moveinright
    "Mora enters the kitchen."
    mora "That smells nice."
    my "I\'m glad you think so!"
    "She sits down at the counter."
    "I hand her the plate."
    my "I made spaghetti bolognaise!"
    mora "Thank you."
    my "You're welcome!"
    "She takes a bite."
    "I eagerly await her reaction."
    show mora arbiter no_coat eyes_closed normal
    mora "It's nice."
    my "Oh!"
    my "I'm glad you think so!"
    "I internally squeal."
    "She liked it!"
    mora "Yes."
    "I sit down next to her with my own plate."
    "I try some."
    "It's a little spicy, but not too much."
    "It's soft and rich."
    "The flavours blend together well."
    "It's great..."
    "We both enjoy our meal."
    "When done, I stand up."
    my "I'll wash the plates this time, too."
    show mora arbiter no_coat normal
    mora "Oh."
    mora "Okay. Thank you."
    my "Look at you, thanking me all the time now..."
    my "How hypocritical..."
    "I say half jokingly."
    "She sighs."
    "I chuckle."
    mora "I'm going to continue working now."
    my "Okay!"
    hide mora
    with moveoutright
    "She heads back into the room."
    "I wash the plates and put everything away, and then head into the room myself."

    scene bg living room night
    with fade
    "{b}{u}A couple of hours later...{/u}{/b}"
    "It's been a few hours."
    "I've watched more TV, and she continued working."
    "Finally, I switch off the TV, and head to where Mora is sat."
    show mora arbiter no_coat normal
    my "It's about my bedtime again..."
    mora "Okay."
    mora "Would you like me to leave?"
    my "No, it's okay, I was just letting you know."
    mora "Okay."
    mora "I'll stay quiet when I pack away."
    my "Thank you..."
    my "Goodnight!"
    mora "Goodnight."
    hide mora
    "I head back to the sofa and curl up, closing my eyes."
    "Sleep soon comes."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter1_day5_avail = True
    scene black
    with fade
    centered "End of day."
    jump chapter1_day4_end