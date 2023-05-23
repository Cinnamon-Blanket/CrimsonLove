label chapter3_day8:
    scene black
    with fade
    centered "Day 8 - Monday 8th January."
    pause 1.0

    scene bg bedroom day
    play music hareka_theme fadein 0.5 fadeout 0.5 loop
    show hareka arbiter smile
    with fade
    hareka "Good morning."
    my "Good morning."
    show hareka arbiter eyes_closed smile
    hareka "Today is Monday 8th January."
    hareka "Today's weather is-"
    my "High rain? Haha."
    show hareka arbiter smile
    hareka "95\% chance."
    my "Knew it."
    hareka "Today is also our second week."
    my "Oh yeah... Today's like, the anniversary I met you, haha."
    hareka "Anniversary..."
    hareka "I suppose."
    hareka "Let's get breakfast sorted."
    my "Okay!"

    scene bg kitchen day
    show hareka arbiter smile
    with fade
    "She makes my toast."
    "I eat."
    show hareka arbiter eyes_closed smile
    hareka "I struggled to stay awake last night..."
    my "What?!"
    my "Wow... What is happening to you?"
    hareka "I'm not worried."
    show hareka arbiter smile
    hareka "If I'm becoming human somehow..."
    my "No... That's impossible."
    hareka "How do you know? You didn't create me!"
    my "True... It just doesn't {i}seem{/i} very plausible."
    my "Maybe you should get checked out."
    hareka "I'm fine!"
    hareka "In fact, I've never felt better!"
    my "Eh..."
    "Well, as long as she's happy..."
    "It doesn't make any sense though. How can someone born as an AI become human???"
    "So quickly too??"
    "This is giving me a headache..."

    scene bg bedroom day
    show hareka arbiter smile
    with fade
    hareka "Would you like to play chess today? I was unable to play with you yesterday..."
    my "Oh, yeah, I forgot about that."
    my "Yeah, let's play!"
    "{b}{u}An hour later...{/u}{/b}"
    "She won the majority of the matches, of course, but I won a couple too!"
    hareka "You're getting better at this. Well done!"
    my "Thanks... I do feel like I'm finally starting to see progress."
    hareka "I told you so!"
    "We laugh."
    my "Right, I'll read a bit more now, and you can do your work."
    hareka "Mhm."
    "I put the chess set away and grab a new book."
    "Hareka sits down at the laptop and I sit on the bed."
    "We begin our activities."
    "{b}{u}An hour later...{/u}{/b}"
    hareka "Would you like lunch now?"
    my "Yes please!"
    hareka "Okay."

    scene bg kitchen day
    show hareka arbiter smile
    with fade
    "We enter the kitchen."
    "She makes me a sandwich."
    hareka "Here you go, egg cress sandwich."
    my "Ooh, something different!"
    hareka "Do you like egg cress?"
    my "Yep!"
    "I eat it."
    my "It's nice!"
    show hareka arbiter eyes_closed smile
    hareka "Good."
    "I finish it, and put the plate in the dishwasher."
    my "Thanks, that was nice."
    show hareka arbiter smile
    hareka "You're welcome."

    scene bg bedroom day
    show hareka arbiter smile
    with fade
    "We head back to the room, and return to our activities."
    "{b}{u}A couple of hours later...{/u}{/b}"
    "I finish the book."
    "I put it back on the shelf and grab another one."
    hareka "You're a rather fast reader."
    my "Yeah... I just get completely absorbed by the story."
    hareka "What was the last book about?"
    my "Some girl who got lost in a creepy woods and had help from a friendly spirit."
    hareka "Ooh..."
    my "Do you read?"
    hareka "Books? Not really."
    show hareka arbiter eyes_closed smile
    hareka "I don't have time for that kind of stuff."
    my "Oh... What a shame."
    "I sit back down. She returns to her work, and I begin reading the first chapter."
    scene bg bedroom evening
    show hareka arbiter smile
    with fade
    "{b}{u}An hour later...{/u}{/b}"
    hareka "It's time for dinner."
    my "Okay!"

    scene bg kitchen day
    show hareka arbiter smile
    with fade
    "We begin making dinner."
    "It's becoming a sort of common thing for me to help out. Not that I mind at all."
    "It's actually fun being able to do something together... in my opinion..."
    "We end up making egg fried rice and chicken, with a bit of mild store-bought curry sauce."
    "I sit down to eat."
    my "It's nice, being able to cook together, don't you think?"
    hareka "Yes, I agree."
    my "We've grown our trust in each other a lot over this past week..."
    hareka "Yes."
    my "Do you trust me?"
    show hareka arbiter eyes_closed smile
    hareka "Yes..."
    hareka "Do you trust me?"
    my "Yes."
    my "I'm not entirely sure why, but I've started feeling things towards you..."
    "Why am I opening up all of a sudden?"
    "It just feels... right."
    show hareka arbiter smile
    "She laughs a bit."
    hareka "What sort of \"things\"?"
    my "Uh... I'd like to be friends with you, I guess..."
    "I look away, embarrassed."
    "Why did I say that?!"
    hareka "Oh..."
    hareka "That would be nice. I've never had a friend before."
    my "Really?"
    hareka "They say we shouldn't get close to our targets..."
    hareka "But I don't see you as a threat at all, to be honest."
    hareka "At least, not to me."
    "I briefly flash back to what happened in the bath."
    "I feel a pang of guilt."
    "She really doesn't know how dangerous I can be when I get emotional..."
    my "I'll try not to be dangerous."
    hareka "You don't need to try, haha."
    my "Yeah..."
    "I avert my eyes."
    hareka "Anyways, finish your food before it gets cold."
    my "Oh, right..."
    "I finish the meal."

    scene bg bedroom night
    show hareka arbiter smile
    with fade
    hareka "Time for bed."
    my "Yep..."
    "I get into bed, sinking into the mattress."
    my "This bed is so comfy..."
    hareka "Good."
    my "Goodnight Hareka."
    hareka "Goodnight."
    window hide
    play music chapter1_theme fadein 0.5 fadeout 0.5 loop
    $ chapter3_day9_avail = True
    scene black
    with fade
    centered "End of day."
    menu chapter3_day8_end:
        "Day 8 (Chapter 3 - Day 8) complete!"
        "Would you like to return to the chapter selection screen, or carry onto the next day?"
        "Chapter selection.":
            jump chapter_select
        "Carry on.":
            jump chapter3_day9