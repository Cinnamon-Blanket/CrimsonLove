label chapter3_day11:
    scene black
    with fade
    centered "Day 11 - Thursday 11th January."
    pause 1.0

    scene bg bedroom day
    play music hareka_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter no_coat smile at left
    show interface arbiter normal at right
    with fade
    "I wake up."
    "The two girls are staring at me."
    "I sit up, yawning."
    hareka "Good morning..."
    my "Good morning."
    show interface arbiter eyes_closed normal
    interface "..."
    hareka "Today is Thursday 11th January."
    hareka "Today's weather is 94\% chance of rain."
    my "To be expected..."
    "I stand up."
    my "Breakfast?"
    hareka "Yes, let's go."

    scene bg kitchen day
    show hareka arbiter no_coat smile at left
    show interface arbiter normal at right
    with fade
    "We enter the kitchen."
    "I sit down and Hareka makes my toast."
    "I eat it."
    interface "Do you cook for her every day?"
    hareka "Yes. Nutrition is important."
    interface "Well, for humans, yes."
    hareka "Yes..."
    my "I have been feeling a lot healthier since Hareka took me, to be honest."
    my "She's been looking after me very well."
    show hareka arbiter no_coat eyes_closed smile
    hareka "I'm glad you think that..."
    interface "At least you're doing one thing right."
    show hareka arbiter no_coat eyes_closed normal
    hareka "..."
    my "Hey, that's rude!"
    interface "I'm not sorry."
    "Ugh..."
    "This is gonna be hard to get used to."

    scene bg bedroom day
    show hareka arbiter no_coat smile at left
    show interface arbiter normal at right
    with fade
    hareka "Would you like to play some chess today?"
    my "Yeah, that'd be nice!"
    "We set up the chess set."
    interface "Chess..."
    my "Would you like to play, Interface?"
    show interface arbiter eyes_closed normal
    interface "I do not have time for such trivial activities."
    "I shrug."
    my "Your loss."
    "I've learned it's better to not give people like her the time of day."
    "I won't let her ruin our fun."
    "{b}{u}An hour later...{/u}{/b}"
    show interface arbiter normal
    "There were a fair share of wins and loses this time."
    "The Interface had been watching us the whole time, hoping we wouldn't notice, probably."
    hareka "You're getting better at this. Well done."
    my "Thank you!"
    "We put the chess set away and I grab another book."
    "I sit on the bed and she sits on the desk."
    interface "What are you doing now?"
    hareka "This is the part of the day where she usually reads for a while, and I catch up on my own work."
    interface "Oh. So you {i}do{/i} do work here?"
    show hareka arbiter no_coat eyes_closed normal
    hareka "Of course I do. I'm not a slacker."
    interface "Good."
    "The tension between them is quite high. I can feel it myself."
    "I don't know what grudges they hold but they'd better settle down..."
    "{b}{u}A couple of hours later...{/u}{/b}"
    show hareka arbiter no_coat smile
    hareka "Would you like lunch now, Alex?"
    "I look up from the book."
    my "Oh, yeah, that'd be nice."
    "I bookmark my current point and then we head to the kitchen."

    scene bg kitchen day
    show hareka arbiter no_coat smile at left
    show interface arbiter normal at right
    with fade
    "Hareka makes me a wrap this time."
    hareka "A ham and cheese wrap."
    my "Oh, thanks!"
    "I eat it happily."
    show interface arbiter eyes_closed normal
    interface "..."
    show hareka arbiter no_coat normal
    hareka "Is something wrong?"
    show interface arbiter normal
    interface "No."
    hareka "Thought so."

    scene bg bedroom day
    show hareka arbiter no_coat smile at left
    show interface arbiter normal at right
    with fade
    "We return to the bedroom."
    "I continue reading, and Hareka continues working."
    "The Interface watches my every move."
    scene bg bedroom evening
    show hareka arbiter no_coat smile at left
    show interface arbiter normal at right
    with fade
    "{b}{u}A few hours later...{/u}{/b}"
    "We've been mainly keeping to ourselves these past few hours."
    "It's finally approaching dinner time."
    "Hareka shuts off her laptop and stands up."
    hareka "Are you ready for dinner now?"
    my "Yep!"
    "I put the book away. I'll finish the bit of that left tomorrow."

    scene bg kitchen day
    show hareka arbiter no_coat smile at left
    show interface arbiter eyes_closed normal at right
    with fade
    interface "Are you going to cook together again?"
    my "Yeah, I think so."
    my "Does that bother you?"
    show interface arbiter normal
    interface "Of course not."
    my "Good."
    hareka "Let's begin!"
    my "Okay!"
    "{b}{u}Half an hour later...{/u}{/b}"
    "We're finished."
    "I sit at the table to eat."
    "It's a fishcake with diced potatoes and mushy peas."
    my "It's delicious!"
    hareka "Great!"
    "I eat contendedly."
    show interface arbiter eyes_closed normal
    interface "You both have a proper routine, don't you?"
    show hareka arbiter no_coat eyes_closed smile
    hareka "Yeah... We seem to be falling into a rhythm."
    my "I agree... It's nice though!"
    hareka "Yeah, it is."
    show interface arbiter normal
    interface "Good for you."
    "She seems a bit... pouty."
    "Is she jealous of our bond??"
    "Wow..."
    "It's definitely affecting her in some way, and she's not doing a good job of hiding me."
    "It takes a lot to hide lies from me."
    "As a compulsive liar myself..."

    scene bg bedroom night
    show hareka arbiter no_coat smile at left
    show interface arbiter normal at right
    interface "It's your bedtime now, right?"
    my "Yep..."
    "I get into bed."
    my "Goodnight, Hareka. Goodnight, Interface."
    hareka "Goodnight. Sleep well."
    interface "Goodnight."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter3_day12_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter3_day11_end:
        "Day 11 (Chapter 3 - Day 11) complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter3_day12