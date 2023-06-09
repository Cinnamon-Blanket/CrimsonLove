label chapter4_day7_route1:
    scene black
    with fade
    centered "Day 21 - Sunday 21st January."
    pause 1.0

    scene bg bedroom day
    with fade
    play music hareka_theme fadein 1.0 fadeout 1.0 loop
    show hareka arbiter alt messy eyes_closed normal
    my "Hey... Wake up."
    harekai "Mm..."
    "She shoves me away."
    my "Look, I already let you sleep in later because we don't have work."
    my "We have plans today, remember."
    show hareka arbiter alt messy eyes_closed smile
    harekai "I remember..."
    "She sighs, sitting up and rubbing her eyes."
    show hareka arbiter alt messy smile
    harekai "Good morning."
    my "Good morning."
    my "Did you sleep well?"
    harekai "Yeah..."
    my "Good."
    "She stands up."
    harekai "My hair is a mess again..."
    my "To be honest, I like your hair down."
    harekai "Oh?"
    show hareka arbiter alt messy eyes_closed smile
    harekai "Well then."
    pause 0.5
    show hareka arbiter alt hair_down eyes_closed normal
    "She unties her hair and quickly brushes through it."
    my "I like it."
    show hareka arbiter alt hair_down smile
    harekai "Thanks."
    harekai "Let's get breakfast."
    my "Okay!"

    scene bg kitchen day
    show hareka arbiter alt hair_down smile
    with fade
    "We head to the kitchen, and she makes the usual toast."
    "I notice she's a lot more fidgety than usual."
    my "Are you excited?"
    harekai "Of course I am!"
    my "Well, I'm glad you are."
    "We finish our breakfast and get ready to leave, then return to the kitchen."
    harekai "I packed up a picnic here, see."
    "She shows me the basket."
    my "Oh! That'll be nice!"
    harekai "Yep!"
    harekai "Well then, let's go!"
    
    scene bg park
    play music love_theme fadein 1.0 fadeout 1.0 loop
    show hareka arbiter alt hair_down eyes_closed smile
    with fade
    "We arrive at the park."
    "We walk around for a while, chatting about anything, and enjoying the beautiful scenery."
    "Eventually, we stop and sit down on a bench."
    harekai "The weather is so nice."
    my "Yeah... I would never have expected this from January."
    "She looks at me and smiles."
    show hareka arbiter alt hair_down smile
    harekai "I'm so glad to be here with you, Alex."
    my "Oh-"
    "That caught me off guard."
    my "Really...?"
    harekai "Of course."
    "I smile back."
    my "I'm glad to be here with you too, Hareka."
    "So we sit, soaking up the abnormally warm sunlight for a while."
    show hareka arbiter alt hair_down eyes_closed smile
    with fade
    "{b}{u}A while later...{/u}{/b}"
    "She stands up, grabbing the picnic basket, and we set up on the bench."
    "The grass is too damp to sit on, unfortunately."
    "She unloads the food."
    my "Mm, this looks delicious! Did you make it all yourself?"
    show hareka arbiter alt hair_down smile
    harekai "Yep!"
    my "Wow..."
    harekai "I have much more motivation to cook now that I can taste the things I'm cooking!"
    my "Haha, good."
    "We eat the food, while chatting about lots of different topics."
    "It's relaxing. I'm enjoying myself, and it seems like she is, too."
    "Eventually, we finish the food, and we tidy everything away, placing the basket on the ground."
    "She looks up to the sky, inhaling deeply."
    show hareka arbiter alt hair_down smile
    harekai "This is so beautiful."
    my "Yeah, it is..."
    scene black
    with fade
    "I close my eyes too."
    "We sit here for a moment of bliss."
    "No distractions, no worries."
    "Just the two of us."
    "Just..."
    harekai "I want to stay like this forever."
    my "Hm?"
    scene bg park
    show hareka arbiter alt hair_down eyes_closed smile
    with fade
    "I open my eyes."
    "She giggles."
    show hareka arbiter alt hair_down smile
    harekai "I'd love to stay with you forever and ever~!"
    my "Oh..."
    my "I'd like to stay with you, too."
    "We both laugh."
    harekai "Thank you."
    my "You're welcome."
    "So we sit, enjoying this moment, completely isolated from the busy City for a while."
    "{b}{u}A while later...{/u}{/b}"
    "Eventually, we stand up."
    my "Ready to head back now? It's beginning to get cold."
    harekai "Ah, yeah, good idea."
    "We pack up our things and head home."

    scene bg bedroom day
    play music hareka_theme fadein 1.0 fadeout 0.5 loop
    show hareka arbiter alt hair_down smile
    with fade
    "We arrive home. Hareka puts the picnic stuff back where it belongs, we wash the pots together, then head to the bedroom."
    my "Did you enjoy that?"
    harekai "Yeah, I really did!"
    my "Good!"
    "We both smile at each other."
    "Genuine smiles of pure happiness."
    my "Back to normal tomorrow, though..."
    show hareka arbiter alt hair_down eyes_closed smile
    harekai "Yeah..."
    harekai "I feel reinvigorated, though."
    my "Oh?"
    harekai "Like I can take on anything life throws at me this coming week."
    my "Aw, that's lovely. I'm glad you feel that way."
    my "I do too, kinda..."
    show hareka arbiter alt hair_down smile
    harekai "We can make it!"
    my "Yeah!"
    scene bg bedroom evening
    show hareka arbiter alt hair_down eyes_closed smile
    with fade
    "We went back to doing our own thing, winding down for a while. Eventually, evening arrives."
    my "Well, the day is ending, huh."
    "Hareka sighs happily."
    harekai "I'm so happy..."
    my "I'm glad."
    show hareka arbiter alt hair_down smile
    harekai "Let's get to bed. We need to save energy for tomorrow."
    my "Yeah, good idea."
    "We get ready for bed."
    my "Goodnight, Hareka."
    harekai "Goodnight!"
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter5_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter4_day7_route1_end:
        "Day 21 (Chapter 4 - Day 7) complete!"
        "{b}Carry on option is not available due to Chapter Completion.{/b}"
        "Chapter selection.":
            jump chapter_select