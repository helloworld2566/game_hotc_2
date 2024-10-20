
label ep_1:
    scene mc_room_morning 
    scene 1
    y "As I woke up, I feel guilty and ashamed about my past actions."
    y "I realize that I need to seek help and therapy to control my desires."
    y "I can't continue behaving like this."
    y "I need help."
    y "I should start planning to visit a therapist soon."
    y "Or maybe, these feelings are completely natural."
    y "Maybe, there’s nothing wrong with them."
    y "I should just consult a therapist."
    y "I should date someone my age. I’m sure that will help me."
    scene 2
    y "I should check Tinder once."
    scene 3
    pause
    scene 4
    pause 
    scene 5
    y "This one looks nice."
    y "Her name is Emma."

    scene black with dissolve
    centered"Over the chat"
    scene 6
    play sound "SendText.ogg"
    y "Hey! I hope this isn't too random, but I saw your profile and thought I'd say hi."
    play sound "SendText.ogg"
    "Emma" "Hi! Not random at all. Nice to meet you! How's your day going?"
    play sound "SendText.ogg"
    y "Nice to meet you too! My day’s going pretty well, thanks. How about yours?"
    play sound "SendText.ogg"
    "Emma" "It’s been good, just finished some work and now relaxing with a book. What about you?"
    play sound "SendText.ogg"
    y "I just wrapped up a photography session. Trying to unwind a bit now. What book are you reading?"
    play sound "SendText.ogg"
    "Emma" "That sounds cool! I'm reading 'The Night Circus.' Have you heard of it?"
    play sound "SendText.ogg"
    y "Yeah, I've heard great things about it! Is it as good as they say?"
    play sound "SendText.ogg"
    "Emma" "It’s really captivating. I’m hooked! Do you like to read?"
    play sound "SendText.ogg"
    y "I do! Mostly thrillers and sci-fi. Any recommendations for me?"
    play sound "SendText.ogg"
    "Emma" "If you like thrillers, you should check out 'Gone Girl.' It’s a page-turner!"
    play sound "SendText.ogg"
    y "I've seen the movie, but I bet the book is even better. Thanks for the tip!"
    play sound "SendText.ogg"
    "Emma" "Definitely! The book has so much more detail. Do you have a favorite book or author?"
    play sound "SendText.ogg"
    y "I’m a big fan of Stephen King. His stories always keep me on the edge of my seat."
    play sound "SendText.ogg"
    "Emma" "Stephen King is great! His writing is so intense."
    play sound "SendText.ogg"
    y "Absolutely. By the way, do you enjoy any hobbies besides reading?"
    play sound "SendText.ogg"
    "Emma" "I love painting and hiking. How about you?"
    play sound "SendText.ogg"
    y "I’m into photography and playing the guitar. Maybe I could show you some of my photos sometime?"
    play sound "SendText.ogg"
    "Emma" "That sounds fun! I’d love to see them."
    play sound "SendText.ogg"
    y "Great! Maybe we could meet up for coffee sometime? I know a cozy café downtown."
    play sound "SendText.ogg"
    "Emma" "That sounds nice. I’d be up for that!"
    play sound "SendText.ogg"
    y "Awesome! How about Saturday afternoon at 'Bean There, Done That'?"
    play sound "SendText.ogg"
    "Emma" "Perfect! I’ve heard good things about that place."
    scene 7
    y "Excellent! Looking forward to it, Emma."
    "Emma" "Me too [y]! See you on Saturday!"
    y "See you!"
    scene 8
    y "thinking I can’t believe I pulled it off."
    y "Maybe I got the rizz. Hahaha"
    jump hallway1

label hallway1:
    show hallway_morning
    menu:
        "Go to the [cr_name]'s room":
            scene b_sis_morning
            y "[cr_name] is not here I should check the living room."
            jump hallway1
        
        "Go to the [lu_name]'s room":
            scene l_sis_morning
            y "[lu_name] is not here. I should check the living room."
            jump hallway1

        "Go to the bedroom":
            scene mc_room_morning
            y "I should go check the living room."
            jump hallway1
        
        "Go to the bathroom":
            scene bathroom_morning
            y "I should go check the living room."
            jump hallway1
        
        "Go to the living room":
            jump living_room_morning1

label living_room_morning1:
    scene living_morning
    pause
    scene 9
    y"My [cr], [cr_name] is sitting on the couch watching TV."
    scene 10
    y "She is my [cr], [cr_name]."
    y "She went to university 4 years ago. Now she’s back."
    y "She has started working as a lawyer just like [m]."
    y "She will be living with us now."
    y "I have to be careful with her though. She’s got a naughty attitude."
    y "{i}I'll just sit next to her for a minute and then I'll go read a book or something.{/i}"
    scene 11
    cr_name "Hello, [y]. How are you?"
    y "Hello. I’m good [cr_name]."
    scene 12
    cr_name "Come here, give me a hug."
    scene 13
    cr_name "You have no idea how much I love you and how much I missed you."
    y "I missed you too."
    scene 14
    y "{i}She is hot though, even if she's not my type.{/i}"
    y "{i}She smells good.{/i}"
    y "{i}Her skin feels smooth and soft. I wish I could touch it more.{/i}"
    y "{i}But I can't, obviously.{/i}"
    scene 15
    "My [cr] suddenly turns to face me, catching me off guard."
    scene 16 with vpunch
    cr_name "Oh my god, [y], is that what I think it is?!"
    y "Umm... No, it's not what you think it is. It's just a stomach ache or something."
    cr_name "Yeah, sure it is. Are you really that dumb? I mean, what kind of excuse is that?"
    y "I'm sorry, [cr]. I didn't mean to make you feel uncomfortable. But it's nothing serious, I promise."
    scene 17
    cr_name "Whatever you say. Just don't make me feel disgusted, alright?"
    y"{i}Damn, that was embarrassing. I guess I need to work on controlling my feelings more.{/i}"
    cr_name "Come for breakfast, [y]."
    y "I'll be there in a minute."
    scene black with fade
    centered "At the dining table"
    scene 18
    m_name "How is your new job going, dear?"
    cr_name "It's great, [m]!"
    cr_name "I'm learning so much and the team is fantastic."
    cr_name "I couldn't ask for a better place to work."
    lu_name "I heard from a friend that the company is expanding soon."
    lu_name "Maybe you could get promoted soon?"
    cr_name "Haha, yeah maybe. Fingers crossed!"
    scene 19 with dissolve
    pause
    scene mom_boobs with dissolve
    pause
    scene 19 with dissolve
    y "{i} Damn, why did I do that?{/i}"
    y "{i} That was wrong and disrespectful.{/i}"
    y "{i} I need to stop thinking about these things.{/i}"
    y "{i} I don't want to stay in the dining hall anymore and be reminded of last night.{/i}"
    scene living_morning
    menu :
        "Go to the school":
            y "I should go to the school."
            jump map1
        "Go to the kitchen":    
            y "I should go help [m] in the kitchen."
            jump kitchen
    
label kitchen:
    scene 20
    pause
    scene 21
    m_name "Hello honey. I have some urgent call to make."
    m_name "Can you help me with dishes?"
    menu:
        "Accept to help her":
            y "Don’t worry [m]. I’ll clean them."
            m_name "Thank you honey, you’re so helpful."

        "Refuse to help her":
            y "I’m sorry [m] but I’m late for school."
            m_name "No worries honey. I’ll clean them after the call."
            m_name "Good day honey."

    jump map1

label map1:
    scene map
    menu:
        "Go to the school":
            jump library_school

        "Go home":
            scene living_morning
            y "I'm already late, I should go to school"
            jump map1

label library_school:
    scene black with fade
    centered "At the school library"
    scene 22
    y "{i} I need to find a way to control these feelings before they consume me completely.{/i}"
    scene 23
    y "{i} I need to read something that helps me.{/i}"
    scene 24
    menu:
        "Book 1: Irresistible You- Mastering the Art of Romance":
            y "This shit sounds so funny."
            y "Interesting…"
            y "Maybe this book will help me get laid."
            y "I'm not sure if this book will actually help me, but it's worth a try."
        "Book 2: Make women fall in love with you":
            y " Make women fall in love with you"
            y "This book sounds interesting."
            y "Maybe this book could give me some insight on how I can improve my relations with my [m]."
            y "I hope this book will help me make a move on my [m] and [cr]."
            y "I'm not sure if this book will actually help me, but it's worth a try."
        "Book 3: The Sorcerer's Handbook: Medieval Magic and Mysticism":
            y "The Sorcerer's Handbook: Medieval Magic and Mysticism"
            y "The title sounds so fishy."
            y "Anyway this book might help me distract myself."
            y "I’ll give it a go."
            y "I'm not sure if this book will actually help me, but it's worth a try."
    scene 25
    pause
    scene 26
    y "{i} Looks like we have a new librarian now.{/i}"
    y "{i} She’s so young and beautiful.{/i}"
    y "{i} She must be a library intern.{/i}"

    scene 27
    "Librarian" "Hello, How may I help you?"
    y "I need to check out this book."
    "Librarian" "Sure.."
    menu:
        "Talk with her":
            scene 35
            y "{i}I should talk with her. She’s so beautiful.{/i}"
            y "{i}She’s definitely worth a try.{/i}"
            y "Are you new here?"
            scene 36
            "Librarian" "Yes, I just joined. Actually I’m doing internship here."
            "Librarian" "I’m also a student, here."
            y "No wonder, you’re so young."
            y "{i} and beautiful..{/i}"
            "Librarian" "Ha ha. Thank you."
            "Librarian" "Do you come here regularly."
            y "No, it’s my first time visiting library in this school."
            y "But I’ll visting regularly now since we have such pretty girl here"
            scene 37
            "Librarian" "Cheeky…"
            y "I’ll take my leave now. Ms…….."
            "Librarian" "Emily"
            y "Emily"
            y "I’m [y]"
            scene 38
            "Librarian" "Nice meeting you, [y]"
            "Librarian" "I look forward to seeing you."
            y "Bye Emily."
            jump library_chris
        "Leave":
            scene 38
            y "I should leave now."
            jump library_chris

label library_chris:
    scene 28
    ch_name"What are you doing here?"
    y "Nothing just borrowing this book."
    scene 29
    "What kind of book is this?"
    y "I don’t know. I just find the title rather interesting."
    y "Going to give it a go."
    ch_name"Haha.. Are you trying to make a move on someone?"
    scene 30
    y "Haha.. Maybe."
    y "Surely will tell you when I do."
    scene 30
    ch_name "I sure you will. You’re my best friend."
    ch_name "It’s time for classes now."
    ch_name "We should go now."
    scene 31
    ch_name "Damn bro. Those guys weren’t wrong when they were talking about how hot Ms. Alina is."
    y "Yeah bro. I was thinking the same thing."
    scene 32
    ch_name "Look at those melons bro. So big."
    ch_name "Anyone would fall for that."
    scene 33
    y "I’m already getting a hard on."
    ch_name "Me too."
    ch_name "We need to find a way to get closer with her."
    scene 34
    y "Yeah."
    scene black with fade
    centered "After school"
    jump map4

label map4:
    scene map
    menu:
        "Go to the school":
            scene school
            y "I should return home."
            jump map4

        "Go home":
            jump home1

label home1:
    scene 51
    y "Looks like nobody’s home."
    menu:
        "Hallway":
            jump hallway5
        
        "Kitchen":
            scene kitchen_evening
            y "There is no one here. I should go to the hallway."
            jump home1

label hallway5:
    scene hallway_evening
    menu:
        "Go to the [cr_name]'s room":
            scene b_sis_evening
            y "There is no one here."
            jump hallway5
        
        "Go to the [lu_name]'s room":
            scene l_sis_evening
            y "There is no one here."
            jump hallway5
        
        "Go to the bedroom":
            scene mc_room_evening
            y "I need to use the bathroom."
            jump hallway5

        "Go to [m]'s room":
            scene mom_room_evening
            y "There's no one here."
            jump hallway5

        "Go to the bathroom":
            jump b_sis_bathroom_scene

label b_sis_bathroom_scene:
    play sound 'door_open_public.mp3'
    play music 'sexy.mp3'
    scene 52
    pause
    scene 53
    pause
    scene 54
    pause
    scene 39 
    pause
    scene 40
    pause
    scene 41
    cr_name "What are you doing?" 
    cr_name "Get out right now."
    y "I’m sorry [cr]. Didn’t know you were here."
    scene 42
    cr_name "Wait…"
    scene 43
    y "{i} Fuck.. What is she thinking now?{/i}"
    y "{i} I better control myself.{/i}"
    cr_name "Did you intentionally come here bro?" 
    scene 44
    y "What? Of course not."
    y "Cover yourself, [cr]."
    scene 45
    cr_name "Why? Don’t you like what you’re seeing?"
    cr_name "Don’t you love your [cr]?"
    y "Uh.."
    cr_name "What are you thinking?"
    scene 46
    cr_name "Why don’t you remove your clothes and join me?"
    y "What? No, I’m not gonna get naked in front of you."
    scene 47
    cr_name "Are you shy?"
    cr_name "Let me remove your clothes for you."
    scene 48
    cr_name "You look too excited [y]."
    y "{i} I better leave now before I get into trouble.{/i}"
    scene 49
    pause 
    scene 50
    y "Shit. I can’t believe that just happened."
    y "I knew my [cr] loves me."
    y "She even used to help me with my sexual urges before she left for university."
    y "She hasn’t changed a bit."
    y "Maybe it’s good for me."
    y "I should take her help."
    scene black with fade
    centered "Next morning"
    jump hallway6

label hallway6:
    play music 'playfull.mp3'
    scene hallway_morning
    menu:
        "Go to the kitchen":
            jump morning_breakfast_mom_talk
        "Go to the [cr_name]'s room":
            scene b_sis_morning
            y "There is no one here. I should go for breakfast"
            jump hallway6
        
        "Go to the [lu_name]'s room":
            scene l_sis_morning
            y "There is no one here. I should go for breakfast"
            jump hallway6
        
        "Go to the bedroom":
            scene mc_room_morning
            y "I should go for breakfast."
            jump hallway6

        "Go to [m]'s room":
            scene mom_room_morning
            y "There's no one here. I should go for breakfast"
            jump hallway6

        "Go to the bathroom":
            scene bathroom_morning
            y "There's no one here. I should go for breakfast"
            jump hallway6

label morning_breakfast_mom_talk:
    scene 55
    y "{i} Dammnnn.. She looks hot{/i}"
    scene 56
    y "{i} Shitt.. I’m getting a boner.{/i}"
    y "{i} I should just focus on my food for now.{/i}"
    y "{i} I need to find a way to get close to her.{/i}"
    y "Hey, [m], can you pass me the pepper?"
    scene 57
    m_name "Sure thing, sweetie. Here you go."
    scene 61
    y "Thanks, [m]. You look really nice today. Did you change your hair?"
    scene 58
    m_name "Yes, I did. How do you like it?"
    scene 61
    y "It looks amazing on you! You're very beautiful, [m]."
    scene 59
    m_name "Aww, thank you, darling. You're so sweet."
    scene 61
    y "I meant it, [m]. You're truly gorgeous. I can't believe I never noticed it before"
    scene 62
    m_name "Well, I appreciate the compliment."
    m_name "It's been a while since I got some attention from a man."
    m_name "So, what have you been up to lately?"
    scene 61
    y "Uh, well, I've been working on a project for school."
    scene 62
    m_name "That's nice. What kind of project?"
    scene 61
    y "It's a research paper on the psychology of sexual desire."
    scene 63
    m_name "Oh, that sounds interesting. What inspired you to choose that topic?"
    scene 61
    y "Well, I've been having some issues with my own sexual desires recently, and I thought it might be helpful to learn more about them."
    scene 63
    m_name "I see. Well, I hope you find some answers."
    scene 61
    y "Thanks, [m]."
    scene 64
    m_name "Are you okay, [y]? You seem distracted.."
    y "Yeah, I'm fine. Just tired, I guess."
    m_name "Is everything alright? You can talk to me about anything."
    y "No, it's nothing serious. Just a little stress from schoolwork."
    m_name "Alright, well let me know if you need anything."
    y "Thanks, [m]."
    jump mom_talk_breakfast_before

label mom_talk_breakfast_before:
    menu:
        "Talk with [m]": 
            y "I need to talk with [m]."
            jump mom_talk_breakfast
            
        "Leave":
            scene 64
            y "I should get going now. I have a lot of work to do."
            m_name "Alright, [y]. Take care of yourself."
            y "You too, [m]."
            jump hallway2

label mom_talk_breakfast:
    menu:
        "Talk about the book":
            y "By the way, I found a book in the school library."
            m_name "Really? That sounds interesting."
            y "Yeah, I borrowed it from the library. Do you mind if I keep it here for a while?"
            m_name "Of course not. You can keep it as long as you need it."
            y "Thanks, [m]."
            jump mom_talk_breakfast

        "Talk about dating":
            scene 65
            y "Actually, I'm planning to ask a girl out tomorrow."
            m_name "That's great news! Who is she?"
            y "Her name is Emma."
            scene 66
            m_name "Oh, I remember her. She's a sweet girl. Good luck, [y]!"
            y "Thanks, [m]."
            jump mom_talk_breakfast

        "Talk with [m] about how she and dad met":
            y " Can you tell me about your love story?"
            m_name "Sure, honey. Your father and I met in college."
            scene 65
            m_name "He was a few years ahead of me, but we were both in the same classes."
            m_name "We became friends first, and our relationship grew from there."
            scene 66
            y "That's so sweet! Did you ever have any doubts about whether he was the one?"
            m_name "Of course! Everyone does."
            m_name "But ultimately, I knew that he was the man I wanted to spend the rest of my life with."
            y "That's wonderful, [m]. Thank you for sharing your story with me."
            m_name "Of course, sweetie. I'm glad you asked."
            jump mom_talk_breakfast

        "Ask [m] about her likes and dislikes in men":
            y "What qualities do you look for in a man, [m]?"
            scene 65
            m_name "Well, I always appreciated a man who was kind, respectful, and honest."
            m_name "Those are the most important qualities in any relationship."
            y "That's good advice, [m]. Thanks."
            scene 66
            m_name "Of course, honey. I'm always here to help."
            jump mom_talk_breakfast
        
        "I have nothing to ask":
            y "I have nothing to ask."
            jump mom_talk_breakfast_before

label hallway2:
    show hallway_afternoon
    menu:
        "Go to the [cr_name]'s room":
            jump b_sis_s1
        
        "Go to the [lu_name]'s room":
            scene l_sis_afternoon
            y "There is is no one here. I should go to [cr_name]'s room."
            jump hallway2

        "Go to the bedroom":
            scene mc_room_afternoon
            y "I should go to [cr_name]'s room."
            jump hallway2
        
        "Go to the bathroom":
            scene bathroom_afternoon
            y "There is is no one here. I should go to [cr_name]'s room."
            jump hallway2
        
        "Go to the living room":
            scene living_afternoon
            y "I should go to [cr_name]'s room."
            jump hallway2

label b_sis_s1:
    scene 67
    menu:
        "Get inside room and talk with her":
            scene 68
            y "Hey, [cr], what are you reading?"
            scene 69
            cr_name "Nothing, I'm just bored."
            y "Oh, really? Why don't you tell me about it?"
            cr_name "No, I don't want to."
            y "Come on, [cr_name], I won't bite."
            cr_name "You sure about that?"
            y "Yeah, totally."
            cr_name "Ok, fine, but you have to keep quiet."
            y "So anyway, where are you going tonight?"
            cr_name "Cause I'm going out with friends and thought maybe you'd tag along."
            y "Sorry, I can't. I'm meeting someone special tonight."
            cr_name "Special? Who?"
            scene 70
            y "A girl named Emma. She’s a girl from my class. Tonight is our first date."
            y "We’ve been flirting for quite some while."
            cr_name "Wow, congrats! I hope everything goes smoothly."
            y "Thanks, [cr]! I'm really excited about it too."
            cr_name "Well, don't forget to bring protection! Ha ha ha ha!"
            y "Ha ha ha ha! Funny, but I already have it."
            cr_name "Do you even know how to do it?"
            y "Are you mocking me?"
            cr_name "No, seriously, you haven't done it before?"
            y "Of course I have!"
            cr_name "How do you know that?"
            y "I watched porn. Lots of it."
            play music 'sexy.mp3'
            cr_name "You did? Wow, that's impressive!"
            y "I'm a quick learner."
            cr_name "Are you gonna do it tonight?"
            scene 71
            y "Stop…This isn’t an appropriate conversation between us."
            scene 72
            cr_name "I see someone getting uncomfortable now."
            cr_name "Do you feel shy, [y]?"
            cr_name "Want your [cr] to teach you some stuff."
            scene 71
            y "What stuff are you talking about?"
            scene 72
            cr_name "You know, stuff like making love and sex."
            cr_name "You surely don’t want to embarrass yourself in front of a girl."
            scene 73
            y "Maybe you could teach me, afterall you're my [cr]"
            y "Isn't it your duty?"
            scene 72
            cr_name "Ohh, Is it?"
            cr_name "Tell me what do you want me to do?"
            cr_name "Do you want me to suck your dick and let you fuck me?"
            scene 74
            cr_name "Looks like someone is getting excited."
            cr_name "Let’s have a look at your package. Shall we?"
            y "Wait.. Are you serious? I thought you were just teasing me."
            cr_name "Keep quiet, [y]."
            scene 75
            cr_name "Someone might hear us."
            cr_name "Surely you are excited [y]."
            scene 76
            cr_name "Do you want to see my boobs."
            scene 77
            y "Yeah.. They’re so big."
            cr_name "Why don’t you remove it yourself."
            scene 78
            cr_name "Do you like them?"
            y "Yes."
            cr_name "Now come closer let me have a closer look at your big dick."
            scene 79
            pause
            scene 80
            m_name "[cr_name]. Can you come here quickly? It’s very urgent."
            scene 81
            cr_name "Okay [y]. We have to stop this for now."
            scene 82
            cr_name "[m] is calling me. I must go otherwise we’ll get caught."
            y "But I’m about to cum now."
            cr_name "Aw. my sweet [y]."
            cr_name "You can’t do that now."
            cr_name "It’s sad we can’t do this now."
            cr_name "But remember I’m always here to help you."
            cr_name "Just come to me whenever you get horny."
            cr_name "We’ll do this again."
            cr_name "Don’t worry."
            y "Ok [cr]. I can’t wait to have sex with you."
            cr_name "Come here let me kiss you?"
            scene 83
            pause
            scene 84
            y "{i} What the hell?{/i}"
            y "{i} She’s clearly interested in me.{/i}"
            y "{i} She literally just gave me a handjob."
        "Don't disturb her":
            scene 67
            y "{i} Ok, so I shouldn't disturb her, I should leave her alone.{/i}"
            y"{i} But what if she wants me?{/i}"
            y"{i} What if she's waiting for me to make a move?{/i}"
            y" I need to talk with her."
            jump b_sis_s1
    jump hallway7

label hallway7:
    scene hallway_afternoon
    menu:
        "Go to the [cr_name]'s room":
                scene b_sis_afternoon
                y "[cr] is no one here."
                jump hallway7

        "Go to the [lu_name]'s room":
            scene l_sis_afternoon
            y "[lu] is no one here."
            jump hallway7

        "Go to [m]'s room":
            y "I need to go to my room first."
            jump hallway7

        "Go to the bedroom":
            scene mc_room_afternoon
            y "There's no one here. I should go talk with mom"
            y "{i} Maybe she can give me some advice on how to deal with my [cr].{/i}"
            y "{i} Or maybe she can help me figure out what to do next.{/i}"
            y "{i} Or maybe she can just listen to me vent about my frustrations.{/i}"
            y "{i} But what if she gets mad at me for bothering her?{/i}"
            y "{i} What if she gets angry and grounds me?{/i}"
            y "{i} But what if she understands and helps me out?{/i}"
            y "{i} I’m sure she’ll give me some guidance on how to handle this situation.{/i}"
            jump mom_s1


        "Go to the bathroom":
            scene bathroom_afternoon
            y "I don't need to use the bathroom now."
            jump hallway7

label mom_s1:
    play music 'playfull.mp3'
    scene 85
    scene 86
    m_name "So, how was your day, [y]?"
    scene 87
    y "Good, thanks. How was yours?"
    scene 88
    m_name "Pretty good, actually."
    m_name "Work was busy, but I managed to get everything done."
    m_name "How about you? Anything exciting happen?"
    y "Not really. Just hanging out with friends and studying for finals."
    m_name "Sounds like a typical day for a high school student."
    y "Yeah, pretty much."
    m_name "So, what are your plans for the weekend?"
    y "I'm not sure yet. Probably just hang out with friends and relax."
    y "Maybe go to the movies or something."
    m_name "That sounds nice."
    m_name "I might go shopping with your sister tomorrow. Want to come along?"
    y "Sorry [m], remember the project I talked about earlier."
    y "I have to work on that."
    m_name "Oh, right. That's important. Well, maybe next time."
    y "Thanks, [m]."
    scene 88
    m_name "Anytime, sweetie."
    jump mom_talk2_before

label mom_talk2_before:
    scene 88
    menu:
        "Talk with [m]":
            jump mom_talk2
        "Leave":
            scene 88
            y "I should get going now. I have a lot of work to do."
            m_name "Alright, [y]. Take care of yourself."
            y "You too, [m]."
            jump hallway3
            
label mom_talk2:
    menu:
        "Ask [m] about her favorite hobbies and interests":
            scene 87
            y "Do you have any hobbies or interests outside of work, [m]?"
            scene 88
            m_name "Yes, I enjoy gardening and cooking. They're both very relaxing activities for me."
            scene 87
            y "That's cool! I never knew you were into gardening."
            m_name "It's a passion of mine. I love being able to grow fresh produce for our meals."
            y "That's awesome, [m]. I'd love to learn more about it someday."
            m_name "I'd be happy to teach you, sweetie."
            jump mom_talk2
        "Ask [m] about her favorite movies and books":
            scene 87
            y "What are your favorite movies and books, [m]?"
            scene 88
            m_name "I love romantic comedies and historical fiction novels. They're my guilty pleasures."
            y "That's funny, those are two of my favorites too!"
            m_name "Great minds think alike, right?"
            y "Exactly!"
            scene 89
            jump mom_talk2
        "Ask mom about her favorite memories with dad":
            scene 87
            y "What are some of your favorite memories with dad, [m]?"
            m_name "There are so many! One of my favorites is when we took our honeymoon to Paris. It was such a magical trip."
            scene 88
            y "That sounds incredible! I'd love to go there someday too."
            scene 89
            m_name "I hope you do, honey. It's truly a beautiful city."
            scene 90
            y "Thanks for sharing that memory with me, [m]. I appreciate it."
            m_name "Of course, sweetie. Always here for you."
            jump mom_talk2

        "Ask [m] about her dreams and aspirations for the future":
            scene 87
            y "What are your dreams and aspirations for the future, [m]?"
            scene 88
            m_name "I've always dreamed of traveling the world and experiencing different cultures. And I hope to retire someday and live a peaceful life surrounded by nature."
            scene 89
            y "Those are wonderful goals, [m]. I hope you achieve them all."
            scene 90
            m_name "Thank you, sweetie. That means a lot."
            scene 92
            m_name "What was he trying to do just now?"
            jump mom_talk2

        "I have nothing more to ask":
            y "I should go to my room now."
            jump mom_talk2_before
            
label hallway3:
    scene hallway_night
    menu:
        "Go to the [cr_name]'s room":
            scene 93
            menu:
                "Don't disturb her":
                     y "I should let her sleep."
                "Wake her up":
                    y "She’s probably tired after what happened today."
                    y "I should just let her sleep."
                    y "Afterall, she’s said that she will let me fuck her whenever I want."
                    y "I should return to my room and sleep."
            jump mom_ms1
        
        "Go to the [lu_name]'s room":
            scene l_sis_night
            y "There is is no one here. I should go to [cr_name]'s room."
            jump hallway3

        "Go to the bedroom":
            scene mc_room_night
            y "I should go to [cr_name]'s room."
            jump hallway3
        
        "Go to the bathroom":
            scene bathroom_night
            y "There is is no one here. I should go to [cr_name]'s room."
            jump hallway3

        "Go to mom's room":
            scene mom_room_night
            y "I should go to [cr_name]'s room."
            jump hallway3


label mom_ms1:
    scene black
    centered "As I return to my room, I get a notification"
    scene 94
    play sound 'notification.mp3'
    y "Ohh it’s Emma." 
    scene black
    centered "Over the chat"
    scene 95
    "Emma" "Hey [y], I’m really sorry, but something urgent has come up."
    y "Oh no! Is everything okay?"
    "Emma" "Yeah, it’s just a family thing I need to take care of. I feel really bad about canceling
    on you."
    y "Don’t worry about it at all! Family comes first. We can always reschedule."
    "Emma" "Thanks for understanding. I was really looking forward to our coffee date."
    y "{i} I can’t believe I just got cancelled. I’m tired now. I should just return to my room and sleep.{/i}"
    scene 96
    y "What’s this strange sound coming from mom’s room?"
    scene 97
    m_name "Ahh.. I’ve been so lonely."
    scene 98 with vpunch
    m_name "I really need a man to fuck me."
    scene 99 with vpunch
    m_name "uhhh… umm……umm…."
    scene 100 with vpunch
    m_name "[y]....."
    y "{i} What!? Why is she calling my name while pleasuring herself?{/i}"
    y "{i} Does she have the same desires about me?{/i}"
    scene 101 with vpunch
    y "{i} I can’t believe this shit.{/i}"
    scene 102
    y "{i} I should return to my room before she catches me sneaking.{/i}"
    scene 103
    pause
    scene black
    centered "Next day"
    jump hallway4

label hallway4:
    scene hallway_morning
    menu:
        "Go to living room":
            jump l_sis_confession

        "Go to the [cr_name]'s room":
            scene b_sis_morning
            y "I should go to living room"
            jump hallway4
        
        "Go to the [lu_name]'s room":
            scene l_sis_morning
            y "There is is no one here. I should go to living room."
            jump hallway4

        "Go to the bedroom":
            scene mc_room_morning
            y "I should go to living room."
            jump hallway4
        
        "Go to the bathroom":
            scene bathroom_night
            y "There is is no one here. I should go to living room."
            jump hallway4

        "Go to mom's room":
            scene mom_room_night
            y "I should go to living room."
            jump hallway4


label l_sis_confession:
    scene 104
    lu_name "Good morning, [y]. Did you sleep well?"
    y "Yes, I slept well."
    menu:
        "Talk with her":
            scene 106
            y "I have a confession to make."
            scene 107
            lu_name "About what?"
            scene 106
            y "I’ve been having inappropriate thoughts about [m] and [cr]."
            scene 105
            lu_name "Oh my god! I can’t believe you would do such a thing."
            y "I know it’s wrong, but I can’t help it. I need help."
            lu_name "I understand, [y]. I’m here for you."
            scene 108
            lu_name "Do you want me to talk to [m] and [cr] about it?"
            y "No, please. I’m afraid they’ll be upset with me."
            lu_name "Don’t worry, I’ll handle it."
            y "Thank you, [lu]. I owe you one."
            lu_name "It’s ok, [m]. [fa] comes first."
            menu:
                "Continue talking with her":
                    jump l_sis_confession_cont
                "Stop talking with her":
                    jump map2
        "Do not talk with her":
            y "I should go to school now."
            jump map2

label map2:
    scene map
    menu:
        "Go to the school":
            jump playground_chris

        "Go home":
            scene living_morning
            y "I'm already late, I should go to school"
            jump map2

label l_sis_confession_cont:
    scene 108
    menu:
        "Talk about your feelings for [m] and [cr]":
            y "I’ve been feeling overwhelmed by my attraction to [m] and [cr]."
            lu_name "I understand, [y]. It’s hard when you have strong feelings for someone."
            y "Yes, it is. I’m worried they’ll reject me if I act on them."
            lu_name "Don’t worry, I’ll talk to them and explain your situation."
            y "Thank you, [lu]. I really appreciate it."
            lu_name "Of course, [fa] always comes first."
            jump l_sis_confession_cont
        "Ask her for advice on how to control my desires":
            y "Do you have any advice on how to control my desires?"
            lu_name "Yes, [y]. Try to distract yourself by focusing on other things. Exercise, hobbies, etc."
            y "That’s good advice, thank you."
            lu_name "You’re welcome, [y]. If you ever need anything, just let me know."
            y "I will, thank you."
            jump l_sis_confession_cont
        "Express my gratitude for her support and understanding":
            y "Thank you for supporting me and understanding my situation, [lu]."
            lu_name "Of course, [y]. [fa] always comes first."
            y "I appreciate it."
            lu_name "You’re welcome, [y]. Let me know if you need anything else."
            y "I will, thank you."
            lu_name "Always here for you, [y]."
            jump l_sis_confession_cont
        "Confess my feelings for her and express my interest in having a relationship with her":
            y "[lu], I have to confess something to you. I have feelings for you."
            y "Not just as a [lu], but as a woman."
            scene 109
            lu_name "[y], I know this may be difficult for you to accept, but I also have feelings for you."
            y "What do you mean?"
            scene 110
            lu_name "I’ve been attracted to you for a while now."
            lu_name "I’ve tried to ignore it, but I can’t anymore."
            y "I’m shocked, but also relieved. I’ve been struggling with these feelings for months."
            lu_name "I know, [y]. I’ve felt the same way."
            y "So what does this mean for us?"
            lu_name "I don’t know, [y]. But I think we should explore this further."
            y "I agree. I’d like to see where this goes."
            lu_name "Me too, [y]."
            y "Thank you for opening up to me, [lu]."
            lu_name "Thank you for trusting me, [y]."
            jump l_sis_confession_cont
        "Make a move on her by asking for a hug and then kissing her on the lips":
            y "Can I have a hug?"
            scene 111
            lu_name "Of course, [y]."
            scene 112
            y "I’m going to kiss you now."
            lu_name "Ok, [y]."
            jump l_sis_confession_cont
        "I have nothing to ask":
            y "I have nothing to ask."
            jump map2

label playground_chris:
    scene black
    centered"Playground"
    scene 113
    ch_name "Hey bro, what’s up?"
    scene 114
    y "Nothing much, just hanging out."
    scene 115
    ch_name "Cool. So, have you been avoiding me lately?"
    y "What do you mean?"
    ch_name "I’ve been texting you and you’ve been ignoring me."
    y "Oh, I’m sorry, Chris. Things have been crazy lately."
    ch_name "I understand. So, what’s up?"
    scene 116
    y "I’ve been dealing with some personal issues."
    ch_name "Like what?"
    y "Well, I’ve been having feelings for someone who I shouldn’t be feeling for."
    ch_name "Who is it?"
    y "My [cr] and [m]."
    scene 117
    ch_name "Wow, that's intense. Have you told anyone?"
    scene 118
    y "No, I'm not sure how they'll react."
    scene 119
    ch_name "I understand. It's a tough situation. But maybe it's worth exploring?"
    y "I'm not sure. I don't want to cause any harm or hurt anyone."
    ch_name "I get that. But maybe there's a way to navigate this carefully?"
    y "I don't know. I need to think about it."
    ch_name "Take your time, bro. We're here for you whenever you need us."
    y "Have you ever had feelings for someone in your [fa] in such way?"
    ch_name "Only me and my mom live together."
    ch_name "My father passes away when I was four years old."
    ch_name "When I reached puberty and started having a hard time,.."
    ch_name "It was my mom who taught me about sex."
    ch_name "And she also gave me handjobs and blowjobs."
    ch_name "She is a therapist and surely she's hot as hell."
    y "Wow, that's crazy. I can't imagine that."
    ch_name "Yeah, it was definitely a unique experience. But I loved it."
    y "Did your mom ever fuck you?"
    ch_name "No, but she promised to do it."
    y "Damn, that's hot."
    ch_name "Yeah, I'm looking forward to it."
    y "Do you think it's weird to have those kinds of feelings for your mom?"
    ch_name "I don't know. I guess it depends on the situation."
    ch_name "In my case, it was just part of growing up."
    y "I see. I'm still not sure what to do about my own situation."
    ch_name "Just take it slow and don't rush into anything."
    ch_name "And remember, I'm here for you."
    jump map3

label map3:
    scene map
    menu: 
        "Go to home":
            jump mom_beach_talk

        "Go to school":
            scene school
            y "I should return home"
            jump map3

label mom_beach_talk:
    scene black
    centered "Back at home"
    scene 120
    pause
    scene 121
    m_name "Hello, [y]. You're back."
    y "Hi, [m]. Yeah, I just got home from school."
    m_name "How was your day?"
    y "It was good."
    m_name "That's good to hear."
    y "Umm...[m], I have something I want to ask you."
    scene 123
    m_name "Yes, what is it?"
    y "I've been noticing that you seem a bit distant lately."
    y "Is everything alright?"
    scene 122
    m_name "Oh, it's nothing serious, [y]."
    m_name "Just some work-related stress."
    scene 123
    y "I see. Well, I wanted to ask if you would like to come with me to the beach this weekend?"
    y "It would be a nice break from everything."
    m_name "That sounds lovely, [y]. I would love to join you."
    y "Great! I'll pack some snacks and drinks, and we can leave early Sunday morning."
    m_name "Sounds perfect. I can't wait."
    y "I'm glad you're feeling better, [m]."
    m_name "Thank you, [y]. I appreciate your concern."
    y "Of course, [m]."
    m_name "Well, I'm going to finish upmaking dinner. See you later."
    y "See you later, [m]."
    y "Can I kiss you [m]?"
    m_name "Yes, you can."
    y "Thanks, [m]. I love you."
    m_name "I love you too, [y]."
    menu:
        "Kiss [m]":
            scene 124
            pause
        "Don't kiss [m]":
            jump hallway8
    jump hallway8

label hallway8:
    scene hallway_evening
    menu:
        "Go to the [cr_name]'s room":
                scene b_sis_evening
                y "There is no one here."
                jump hallway8

        "Go to the [lu_name]'s room":
            scene l_sis_evening
            y "There is no one here."
            jump hallway8

        "Go to the bedroom":
            jump room_return

        "Go to [m]'s room":
            scene mom_room_evening
            y "I should go to my room first."
            jump hallway8

        "Go to the bathroom":
            scene bathroom_evening
            y "I don't want to use the bathroom now."
            jump hallway8

label room_return:
    scene 125
    y "I should go have a look and what [m]'s doing?"
    scene black
    centered "I decide to check on my mom"
    scene 125
    y "Maybe she's masturbating again."
    y "I might find my moment to get physical with her."
    scene 126
    y "Strange noises are coming from her room today as well."
    y "I should slowly open her door."
    scene 127
    y "I have to make sure that she does not get aware of my presence."
    scene 128
    y "I see her masturbating."
    y "I should go closer." 
    scene 129
    m_name "[y], ahhh. I can't wait for you to fuck me."
    y "Dammnn. She's thinking about me."
    scene 130
    y "{i} I'm so hard right now.{/i}"
    menu:
        "Start stroking dick":
            $ got_caught_by_mom = True
            scene 131
            pause
            scene 132
            pause
            scene 133 with vpunch
            m_name "Oh my god, what are you doing?"
            y "I'm sorry, [m]. I couldn't help myself."
            m_name "That's disgusting! Go clean yourself up and leave me alone."
            y "I'm sorry, [m]. I didn't mean to upset you."
            m_name "Get out of my room!"
            y "Ok, I'll go now."
        "Leave":
            y "I should leave before I get caught."
            jump b_sis_night_bj

label b_sis_night_bj:
    scene 134
    pause
    scene 135
    cr_name "Hello, [y]."
    y "Hi, [cr]. What are you doing here?"
    scene 136
    cr_name "I came to apologize for yesterday. I shouldn't have teased you like that."
    y "It's ok, [cr]. I liked it."
    cr_name "I just wanted to make sure we're still on good terms."
    y "Of course we are."
    scene 137
    cr_name "Good. Anyway, I'll leave you alone now. Goodnight."
    y "Don't you want to get naughty again?"

    if got_caught_by_mom:
        scene 137
        cr_name "That is the reason I came here in the first place."
        cr_name "But I’m so tired right now."
        cr_name "I need to go to sleep."
        scene 138
        y "Will we be doing this some other time?"
        cr_name "We could. I don’t know to be honest."
        cr_name "Good night, [y]."
        y "Good night, [cr]."
        scene 139
        pause
    else:
        scene 140
        y "I mean you told me that we'll do it again."
        cr_name "I was just kidding. I wouldn't do that to you."
        y "Ohh come on. Now you're teasing me."
        cr_name "Are you getting excited little [y]?"
        cr_name "Do you want me to suck your cock?"
        y "Please."
        cr_name "Alright, get undressed and come here."
        scene 141
        y "Thank you, [cr_name]."
        scene 142
        cr_name "Don't mention it."
        scene 143
        pause
        scene 144
        pause
        scene 145
        pause
        scene 146
        pause

        menu:
            "Cum in her mouth":
                scene 147
                y "I'm about to cum."
                y "Take it in your mouth."
                y "I'm cumming."
                scene 147 with vpunch
                pause
                scene 148
                pause
                scene 149
                cr_name "Good boy."
                scene 150
                cr_name "Clean up and go to sleep now."
            "Cum on her face":
                scene 152
                y "I want to cum in your face."
                cr_name "No. Please cuum on my tits instead."
                scene 151 with vpunch
                y "I'm cumming."
                # She rubs my cum on her boobs.
                scene 150
                cr_name "Good night, [y]. Sweet dreams."
                y "Good night, [cr_name]."
        jump mom_room_morning
            
label mom_room_morning:
    scene black
    centered "Next morning"
    scene 153
    y "I have a session with my therapist today."
    y "I should leave now."
    scene hallway_morning
    y "I should get going"
    scene 154
    y "I should tell my [m] that I'm leaving."
    y "I also have to check whether she's mad at me for yesterday or not."
    if got_caught_by_mom:
        scene 157
        m_name "Good morning, [y]. Where are you headed?"
        y "Good morning, [m]. I'm going to meet my therapist."
        m_name "Oh, ok. How has it been going with her?"
        y "It's going well. She's helping me work through some things."
        m_name "That's good to hear. Take care and have a safe trip."
        scene 158
        y "Thank you, [m]. I will."
        scene 159
        y "I also wanted to ask you about yesterday. Are you mad at me?"
        scene 160
        m_name "No, [y]. I wasn't mad. I was just taken by surprise."
        scene 160 with vpunch
        m_name "Afterall, it wasn’t your first time masturbating in my room."
        y " You were aware of what I did last time when you were sleeping."
        scene 161
        m_name "Of course, son. I was just pretending to be asleep."
        m_name "I wanted to see how far you were willing to go with your own mother."
        y "Aren't you mad at me, [m]?"
        scene 162
        m_name "Aww... sweetheart. Why would I be mad at you?"
        m_name "I know we've been having a tough time ever since your father left us."
        m_name "You've been so lonely."
        m_name "Same has been the case with me."
        m_name "If you ever need my help you just need to ask me directly."
        m_name "I'll always help you."
        y "Thank you, [m]. I love you."
        m_name "I love you too, [y]."
        y "I'm so sorry for yesterday, [m]."
        m_name "It's ok, [y]. I understand."
        m_name "I know you've been struggling with these feelings for a while now."
        m_name "And I'm here to support you in whatever way I can."
        y "Thank you, [m]. I appreciate it."
        m_name "I'm glad we can talk openly about this."
        m_name "Is there anything else you want to discuss?"
        y "No, [m]. I just wanted to clear the air."
    else:
        scene 155
        y "Good morning, [m]."
        m_name "Good morning, [y]. Are you going somewhere?"
        y "Yes, [m]. I’m going to the therapy session today."
        m_name "Okay, have a good day honey."
        scene 156
        pause
    
    jump map5

label map5:
    scene map
    menu:
        "Go to the therapist":
            jump therapist_office_afternoon

        "Go to the school":
            scene school
            y "I should go to the therapist."
            jump map5

        "Go home":
            scene living_morning
            y "I should go to the therapist."
            jump map5

label therapist_office_afternoon:
    scene 163
    y "Hello, Ms. Jane"
    th "Hello, [y]. How are you doing today?"
    y "Good, thank you. How are you?"
    scene 164
    th "I'm doing well, thank you. So, how have things been since our last session?"
    scene 165
    y "They've been going well, actually."
    scene 166
    th "That's great to hear! What has helped you the most in managing your feelings?"
    y "Well, I've been trying to stay busy and focused on my schoolwork."
    scene 167
    th "That's a great strategy. And what about your relationships with others? How have those been?"
    scene 168
    y "I've been spending more time with my friends and family, which has been helpful."
    scene 169
    th "That's excellent. And how do you feel about your progress overall?"
    scene 170
    y "I feel like I'm making steady progress. It's a slow process, but I'm seeing improvements."
    th "That's fantastic! Keep up the good work, [y]."
    y "Thank you, Ms. Jane. I appreciate your help."
    jump therapist_office_afternoon_convo

label therapist_office_afternoon_convo:
    scene 170
    menu:
        "Ask whether you're feelings are normal.":
            y "Ms.Jane Do you think that having sexual fantasies about your family members are normal?"
            th "Yes, don't worry about it. They're completely normal."
            th "However, the most important thing in this case is consent."
            th "Who do you have sexual fantasies with in your family?"
            y "My mother and sisters."
            th "You should try to talk with them about these fantasies and see if they're willing to explore them with you."
            y "Do you think that they'll want to have sex with me?"
            th "I don't know."
            th "It's quite unprofessional of me to say this but you're actually quite handsome."
            y "If you were my mother, would you allow me to fuck you?"
            th "Haha.. I'm not sure."
            jump therapist_office_afternoon_convo

        "Ask her about her job":
            y "Do you mind if I ask you something about your job?"
            th "Of course not. Ask me anything you like"
            y "How long have you been in this job?"
            th "It's been around 13 years now."
            y "Do you like your job?"
            th "Yes, I love it."
            jump therapist_office_afternoon_convo

        "Ask about her family":
            y "Can you tell me about your family?"
            th "My husband passed away 14 years ago."
            th "I have a son who is the same age as you."
            th "His name is Chris."
            y "Chris is my friend."
            th "Oh, really? Small world."
            jump therapist_office_afternoon_convo

        "I have nothing more to ask":
            y "That's enough for today. I should leave now."
        
    jump evening_home

label evening_home:
    scene 171
    y "Dammmnnnn.. Chris’s mom is so hot."
    y "She’s so fucking hot."
    y "She also gave blowjobs to Chris."
    y "Shit. That’s so hot."
    scene 172
    y "I’m getting a boner."
    scene 171
    y "I should ask my [m] for help."
    y "She told me earlier that all I need to do is ask for help."
    scene black
    centered "Kitchen"
    scene 173
    y "[m], can you help me?"
    scene 174
    y "I’m so hard right now."
    m_name "Why do you need my help?"
    y "I’m hard because of you."
    m_name "Really?"
    y "Yes, mom. I’m so horny thinking about you."
    y "Do you want to suck my dick?"
    scene 175
    m_name "What??!!!! Are you out of your mind [y]."
    m_name "I’m your [m]."
    y "I’m sorry, [m]. I don’t know why I said that."
    y "I was zoned out."
    scene 176
    y "{i} She is really mad. I didn’t think she would respond like that.{/i}"
    y "{i} Afterall, she was masturbating saying my name.{/i}"
    scene black
    centered "Bedroom"
    scene 177
    y "Should I go have a look at what [m]’s doing today as well."
    scene black
    centered "Outside mom's room"
    scene 178
    menu:
        "Go to [m]’s bedroom":
            if got_caught_by_mom:
                scene 179
                y "It’s locked from inside."
                y "She being more careful after the last time."
            else:
                y "She’s sleeping. I should not disturb her."
                y "I’ll talk with her tomorrow."
        "Don’t go to [m]’s bedroom":
            y "I should just let her rest."
    scene black
    centered "Bedroom"
    scene 177
    y "I should just sleep for now"
    jump hallway9

label hallway9:
    scene hallway_morning
    menu:
        "Go to the [cr_name]'s room":
            scene b_sis_morning
            y "There is no one here."
            jump hallway9
        
        "Go to the [lu_name]'s room":
            scene l_sis_morning
            y "There is no one here."
            jump hallway9
        
        "Go to the bedroom":
            scene mc_room_morning
            y "I should go for breakfast."
            jump hallway9

        "Go to [m]'s room":
            scene mom_room_morning
            jump mom_room_call_therapist

        "Go to the bathroom":
            scene bathroom_morning
            y "I don't want to use the bathroom now."
            jump hallway9

label mom_room_call_therapist:
    scene 181
    y "[m] is talking to a woman. But why the phone has speaker on?"
    scene black
    centered "On the phone"
    "Woman" "[m_name], is everything well?"
    m_name "Yes, everything is good."
    "Woman" "Can’t wait to meet you guys tonight."
    m_name "I’ll make something nice for you guys for dinner."
    m_name "Ok, Jane See you."
    scene 182
    # I decide to enter mom’s room.
    m_name "Hello [y]. Good morning."
    scene 183
    y "Good morning, [m]."
    y "Are we going somewhere?"
    y "Who was on the other side of the call?"
    scene 184
    m_name "It was Jane. She’s one of my close friends."
    m_name "I have invited her to come to our house for dinner tonight."
    y "You never told me about her."
    m_name "She’s a therapist. She has a son."
    m_name "Her son is the same age as you."
    y "What’s his name?"
    m_name "Chris."
    y "And his mom is a therapist?"
    m_name "Yes."
    y "Chris is my friend and his mom is the therapist I went to talk with."
    m_name "That’s so great!! I can’t believe this."
    m_name "Go and rest now honey. I have so much work to do."
    y "Ok [m]. Is Chris coming tonight as well?"
    m_name "Yes, honey."
    y "I’ll also help you [m]."
    m_name "I really appreciate your help, [y]."
    m_name "I’m so glad you're here."
    scene 185
    m_name "It’s been hard without your dad."
    m_name "I’m not young anymore and I’ve been juggling everything by myself."
    m_name "And, I’m not sure if I’m doing that great a job anymore…"
    menu:
        "Encourage her":
            y "I miss him too. I know it’s hard, but don’t let life get to you, [m]"
            y "Everyone has bad times in their life, but don’t give up. I will always be here for you."
            m_name "It’s so good to have a man in the house."
        "Agree with her":
            y "Well, everyone gets old [m]… It’s a sad fact of life."
            m_name "What a depressing thought"
        
    jump th_evening_home_visit

label th_evening_home_visit:
    scene black
    centered "Evening"
    scene 186

    y "Hello, Chris."
    y "Hello, Ms. Jane"
    ch_name "Hello, bro."
    "Jane" "Hello, [y]"
    y "Come inside, guys."
    scene 187
    "Jane" "Wow, this place looks so different than I imagined."
    y "Do you like it?"
    "Jane" "Yes, it’s very charming."
    y "Would you like to sit down first?"
    ch_name "Yes, please."
    "Jane" "Sure, I’d love to."
    scene 188
    m_name "Hello, Ms. Jane. Welcome."
    m_name "Welcome, Chris."
    m_name "I’m so happy to see you guys again."
    ch_name "Thanks. Ms.[m_name]."
    scene 189
    m_name "[y] why don’t you take Chris to your room and have a talk?"
    m_name "I’ll call you guys when the dinner is ready."
    y "Sure [m]."
    scene black
    centered "Bedroom"
    scene 190
    ch_name "Bro, I was quite shocked to know that our mothers are close friends."
    y "Yes, Chris. I didn’t know it either."
    y "I had already met your mother earlier in the therapy session."
    ch_name "Isn’t that great?"
    scene 192
    ch_name "We are best friends."
    ch_name "And our mothers are also best friends."
    scene 191
    y "Chris you told me earlier that your mother helped you relieve your sexual urges."
    ch_name "Yes. What about it?"
    y "Nothing. I just didn’t know that your mother was so hot."
    scene 193
    ch_name "Haha. I could say the same thing about you."
    ch_name "Your [m]’s so fucking hot bro."
    ch_name "I want to fuck your [m]."
    y "What??!! What are you talking bro?"
    scene 194
    ch_name "Come on bro. She’s so hot. Anyone would want to fuck her."
    ch_name "Have you never wanted to fuck her?"
    y "I mean I want to."
    y "But she’s my mother."
    ch_name "So what."
    ch_name "The fact that she’s your mother just makes having sex with her better."
    ch_name "Both of our fathers died when we were young."
    ch_name "We must help our moms."
    ch_name "You understand that. Right?"
    y "Yes, Chris."
    ch_name "We just need to make make the right moves. And we’ll get to fuck our moms."
    ch_name "And each other’s mom."
    y "Do you really mean it, Chris?"
    ch_name "I’m dead serious about it bro."
    y "That would be so great."
    y "But how do get going with it?"
    y "How will we make them agree to fuck with us?"
    ch_name "We’ll have to come up with a plan."
    ch_name "With the both of us combined, I’m sure anything is possible."
    scene black
    centered "Dinner"
    scene 195
    m_name "Do you guys like the food?"
    scene 196
    "Jane" "Come on now, [m]. You’re embarrassing us."
    "Jane" "Like have you ever cooked bad food."
    scene 198
    m_name "Now you’re flattering me."
    scene 197
    ch_name "It’s great aunt."
    ch_name "I didn’t know you were such a good cook."
    scene 198
    m_name "Thanks, Chris."
    m_name "You should come more often to our home Chris."
    m_name "You guys should have more sleepovers."
    scene 196
    "Jane" "Yeah I was thinking exactly the same thing."
    "Jane" "You should also visit our house more often, [y]."
    scene 197
    ch_name "Yes you should."
    y "Yes, exactly."
    jump mom_son_game

label mom_son_game:
    scene black
    centered "After some time"
    scene 199
    y "[m] I’ve done the dishes."
    y "I’m going to my room now."
    scene 200
    m_name "Thank you so much honey. You’ve been so much help."
    y "No problem [m]."
    m_name "Can we talk about something honey?"
    play music 'sexy.mp3'
    scene 201
    y "Yea.. sure [m]."
    y "What is it about?"
    m_name "Actually I’ve been so lonely, since you’re father passed away."
    m_name "I just have to thank you for everything."
    scene 202
    y "I did what I could have done [m]."
    y "Why don’t you date someone?"
    y "You are so beautiful and young."
    y "Anyone would want to date you."
    y "You’re very beautiful, [m]."
    scene 203
    m_name "Aww, thank you, darling. You're so sweet."
    scene 204
    y "I meant it, [m]. You're truly gorgeous."
    m_name "Well, I appreciate the compliment. It's been a while since I got some attention from a man."
    y "Yeah, I know what you mean. Life gets pretty lonely sometimes, doesn't it?"
    scene 205
    m_name "Definitely. I mean, it's not like I'm not interested in men."
    y "Really?"
    scene 206
    m_name "Yeah, sadly I am single. All these years without sex really makes me thirsty."
    y "{i} Woah.. [m] is really drunk right now.{/i}"
    y "{i} I should take advantage of that.{/i}"
    y "Are you looking for a date or something?"
    y "With a body as hot as yours, I'm sure many men have tried hitting on you."
    y "They must have wanted to fuck your brains out"
    scene 207
    m_name "This talk isn't appropriate [y]. But still thank you."
    m_name "Do you think I'm hot?"
    scene 208
    y "You're gorgeous. You have a sexy body, nice tits, ass. I bet a lot of guys would want to fuck you"
    m_name "Stop talking like that."
    y "You don't deny it."
    y " In fact I want to fuck you myself"
    y "But I can't. Because you are my [m]."
    scene 209
    m_name "I don't blame you for wanting to fuck me. Many man have tried to fuck me."
    y "So do you want to have sex with me?"
    m_name "No"
    y "Why?"
    m_name "Because you are my [fa] and it would be immoral."
    m_name "But if you were not my [fa], then yes, I would love to have sex with you."
    y "If I wasn't your [fa], would you let me fuck you?"
    m_name "Yes."
    y "How far will you let me go? Will you let me have sex with you?"
    m_name "No, it would be too risky. People might find out and it would be bad for us."
    y "But wouldn't you want to have sex with someone? Wouldn't it feel good?"
    m_name "Maybe, but not with you. You're my [fa]. It would be wrong."
    y "But what if I told you that I loved you? What if I said that I wanted to make you happy and that I could give you everything you ever wanted?"
    m_name "No, it wouldn't work. It would be too weird."
    y "Why do you think that? Is it because of our relationship or because of what society thinks?"
    y "At least give me a chance."
    scene 210
    m_name "Alright honey, we’ll play a game and if you win I’ll let you have your way with me?"
    y "What do you mean? Are you going to let me fuck you?"
    m_name "Yes, you can fuck me tonight if you win."
    y "Okay [m], I’m ready. What’s the game?"
    m_name "You have to guess what color bra I’m wearing right now."
    m_name "If you guess correctly in two tries, then I’ll remove my bra for you."
    y "Ok"
    $ guesses_left1 = 2
    $ guesses_left2 = 2
    while guesses_left1 > 0:
        menu:
            "Red":
                $ guesses_left1 -= 1
                m_name "No, that’s wrong. You have one guess left."
            "Black":
                $ mom_challenge_1 = True
                m_name "That’s correct honey."
                y "{i} Is she really going to remove her bra?{/i}"
                y "You have to remove your bra now."
                scene 211
                m_name "Wait, honey. I’m doing it."
                scene 212
                m_name "Here you go honey." 
                scene 213
                m_name "Do you like my boobs?"
                y "Yes, I love them [m]."
                y "Can I touch them [m]?"
                m_name "Ok honey, you can touch them."
                scene 214
                m_name "Ahh.. Slowly honey. You have all the time."
                scene 215
                m_name "What are you doing honey?"
                scene 216
                m_name "Ok stop now, [y]. Do you want to keep playing this game?"
                y "Yes, [m]."
                m_name "Now you have to guess what color panties I’m wearing."
                y "What if I win?"
                m_name "Then I’ll remove my panties for you. I’ll also grant you one wish."
                y "{i} Shit.. This is my chance now. I could fuck her tonight.{/i}"
                y "I’m about to guess now."
                while guesses_left2 > 0:
                    menu:
                        "Red":
                            $ guesses_left2 -= 1
                            m_name "No, that’s wrong. You have one guess left."
                        "Black":
                            $ mom_challenge_2 = True
                            scene 217
                            m_name "That’s correct honey."
                            y "{i} She is going to get completely naked now.{/i}"
                            y "You have to remove your panties now."
                            scene 218
                            m_name "Wait, honey. I’m doing it."
                            m_name "Here you go honey."
                            scene 219 
                            m_name "What’s your wish honey?"
                            y "I want you to suck my dick."
                            m_name "Alright honey. Come closer."
                            m_name "Show it to me now."
                            scene 220
                            m_name "It’s so big it’s not even completely hard yet."
                            scene 221
                            m_name "I think it need my soft touch."
                            #Show [m] stroking my dick with her hands.
                            scene 222
                            pause
                            scene 223
                            m_name "Yeah.. I think it’s working."
                            scene 224
                            m_name "It became hard as soon as I touched it."
                            m_name "You like to have you mother touch it, huh?"
                            m_name "I think you are ready to stick that big juicy cock of yours between my soft tits."
                            m_name "What do you say, hmm?"
                            y "I say you should get it wet before you stick it between your tits."
                            y "It may be uncomfortable, if it’s not wet."
                            m_name "Umm.. where did you get that knowledge?"
                            y "I just saw it in porn."
                            m_name "Porn.."
                            m_name "What kind of porn do you watch?"
                            y "The ones where mothers fuck their own sons."
                            m_name "You’re so naughty."
                            m_name "Imagining such things with your own [m]."
                            y "Ahh.. Stop it you’re squeezing my dick too hard."
                            m_name "Fine.. So how do you want to do it."
                            y "The rough way."
                            m_name "Ohh.. you’re so naughty."
                            scene 225
                            y "I think we can go deeper than that."
                            m_name "Mhmm.."
                            scene 226
                            y "I'm sorry. I couldn't hold back. It felt too good. It was too much, [[m] name]. I can't... Aah"
                            m_name "I can't believe this! You just came in my mouth."
                            m_name "My own [y] just filled my mouth with his cum."
                            scene 227
                            cr_name "My mouth is so full of his semen."
                            scene 228
                            m_name "Fuck that was too much for me to handle."
                            y "But you did a good job."
                            scene 229
                            m_name "Ohh.."
                            y "How about we do something more bold?"
                            m_name "I thought you’d never ask?"
                            y "{i} Now is the moment of truth. Will she try to resist it?{/i}"
                            y "{i} I don’t think she wants to resist me.{/i}"
                            scene 230
                            m_name "Come over here."
                            m_name "We will finally try something new."
                            m_name "Something more spicy."
                            m_name "Something bold…"
                            scene 231
                            m_name "Something that a mother and son should never do."
                            scene 232 with vpunch
                            # m_name falls asleep
                            y "{i} I should let her rest now.{/i}"
                            $son_lost_challenge = False
                            jump game_after
                        "White":
                            $ guesses_left2 -= 1
                            m_name "No, that’s wrong. You have one try left."
            "White":
                $ guesses_left1 -= 1
                m_name "No, that’s wrong. You have one tries left."
label game_after:
    if son_lost_challenge:
        scene 233
        m_name "Well you’ve lost, [y]."
        m_name "Guess you can’t have sex with me tonight."
        m_name "I’m so tired."
        scene 234
        m_name "I’m going to my room and sleep."
        m_name "Good night, sweetie."
        y "Good night, [m]."
        scene 235
        y "{i} I fucked up. I had the chance to fuck her.{/i}"
        y "{i} She’s still drunk. I still have my chance.{/i}"
        y "{i} I stay here for some time and go to her room after sometime.{/i}"

        scene 236
        "Night"
        "Mom’s room"
        y "What the hell? Why I am standing here?"
        y "This feeling... What's this desire? This lust! It's rising up in me."
        y "I can smell [m]'s perfume from this morning."
        scene 237
        y "I want to feel her body."
        y "No! This is wrong."
        y "What the fuck is wrong with me?!"
        y "I need to go back to sleep."
        y "I need to RESIST these urges."

        menu:
            "Resist":
                y "No, this is wrong. What the hell is wrong with me?"
                y "I should just return to my room and sleep."
                scene 238
                # m_name wakes up
                m_name "Honey, what are you doing here?"
                m_name "Are you alright?"
                y "Uh, I don’t know... I, I've been feeling really strange, lately.."
                m_name "You are probably just tired and stressed out."
                m_name "Come back to bed. I will keep your company tonight, okay?"
                y "Okay [m]. Thank you."
                scene 239
                #We sleep together hugging each other.
                y "Having her near me really makes everything feel so peaceful and calm."
                y "I love her."
                #m_name is only in her bra
                scene 240
                y "{i} My face is so close to her tits.{/i}"
                y "{i} I’m getting a boner.{/i}"
                #I slowly remove her bra.
                scene 241
                pause
                scene 242
                m_name "What are you doing, honey?"
                scene 243
                y "I can’t resist anymore, [m]."
                y "You’re so hot."
                y "I have to fuck you now."
                scene 244
                m_name "You can’t do that."
                m_name "I’m your [m]."
                y "I know [m] you are very loney as well."
                y "You told me that you wanted to have sex as well."
                y "Just this one time. Let me fuck you."
                m_name "No, I can’t let you have sex with me."
                m_name "You can ask for anything beside that."
                menu:
                    "Ask for blowjob":
                        y "I want you to suck my dick."
                        scene 245
                        m_name "Alright honey. Come closer."
                        m_name "Show it to me now."
                        scene 246
                        pause
                        scene 247
                        pause
                        scene 248
                        pause
                        scene 249
                        y "You’re doing great [m]."
                        scene 50
                        pause
                        scene 251
                        pause
                        scene 252
                        menu:
                            "Cum in her mouth":
                                y "I'm about to cum."
                                y "I'm going to cum in your mouth."
                                scene 253 with vpunch
                                pause
                                scene 254 with vpunch
                                pause
                                scene 255
                                m_name "That’s digusting"
                                y "Gosh, I'm so proud of you for not wasting my sperm!"
                                m_name "Don’t talk to me like that honey. I’m your [m]."
                            "Cum on her face":
                                scene 256
                                pause
                                scene 257
                                m_name "OMG, that's disgusting!"
                                y "No problem! I'll wipe it off for you."
                                scene 258
                                m_name "Don't worry about it. I guess I liked it."
                                y "Alright."
                                scene 259
                                m_name "You may be able to get away with that once, but if you try that again, then I'm going to kick your ass!"
                                y "Sorry, mom, but that was too much for me."
                                scene 260
                                m_name "Fair enough."
                                m_name "I know that, but you still owe me one favor!"
                                y "Like what?"
                                m_name "I want you to finish the job now!"
                                y "Wait...you want me to fuck you?"
                                m_name "What? Noo…"
                                m_name "I want you to cover it completely!"
                                scene 261
                                pause
                                scene 262
                                pause
                                scene 263
                                pause
                                scene 264
                                pause
                                scene 265
                                pause
                                scene 266
                                pause
                                scene 267
                                pause
                                #I cum multiple times in her face and her face is completely covered with my cum.
                    # "Ask for boobjob":
                    #     y "I want you to give me boobjob."
                    #     m_name "Alright honey. Come closer."
                    #     m_name "Show it to me now."
                    #     #Show boobjob scene
                    #     # I eventually cum on her boobs
            "Give in":
                #I completely remove my clothes.
                scene 268
                y "I NEED TO TOUCH HER BODY!"
                y "[m_name]"
                scene 269
                m_name "Argh! Shit! You scared me."
                m_name "What are you doing here?"
                scene 270
                m_name "And why are you naked?"
                y "I came for you."
                m_name "And, what are you going to do with me, Sweetie?"
                scene 271
                y "First, I want to undress you."
                m_name "No, you can't that."
                scene 272
                #I remove her clothes.
                m_name "Stop it, Sweetie."
                scene 273
                y "Don’t you want to have sex too, [m]?"
                m_name "Yes, I want to have sex but not like this."
                scene 274
                y "Please [m]. I really need your help."
                y "Just this once."
                scene 275
                m_name "Ok honey. I can’t let you have sex with me. But I can help you with this situation."
                m_name "But I can’t let you have sex with me."
                m_name "And remember, this is only going to happen once."
                m_name "You can’t record anything without my permission, okay."
                y "Okay, [m]."
                y "{i} Can’t believe that worked.{/i}"
                scene 276
                m_name "Come closer honey."
                m_name "You have a really big dick."
                m_name "I want to suck it."
                scene 277
                y "Go ahead [m]."
                scene 278
                pause
                scene 279
                pause
                scene 280
                pause
                scene 281
                m_name "Looks like you like it the rough way."
                m_name "Alright then let’s do this."
                m_name "Start slowly then increase your pace as much as you like honey."
                m_name "I also want it rough."
                scene 282
                pause
                scene 283
                pause
                scene 284
                pause
                scene 285 
                pause
    jump morning_scene

label morning_scene:
    scene 286
    "Morning"
    "Mom’s bedroom"
    y "I can’t believe what happended last night."
    scene 287
    y "It was like a dream."
    scene 288
    y "I’m late. I must hurry up and go to school."
    scene 289
    y "Mom wake up."
    m_name "Hmm?"
    y "You need to dress up before my sisters come and find out that we fucked."
    scene 290
    m_name "You are NOT gonna fuck me?"
    m_name "It felt so nice yesterday."
    m_name "Let’s do it now, son."
    y "Not now mom."
    y "I’m late for school."
    scene 291
    m_name "Come here. Let me kiss you at least."
    m_name "Have a good day honey."
    y "I must go fast"
    jump map6

label map6:
    play music 'playfull.mp3'
    scene map
    menu:
        "Go to school":
            jump school_scene
        "Go to home":
            scene living_morning
            y "I'm late for school"
            jump map6

label school_scene:
    scene black
    centered "At lunch break"
    scene 292
    ch_name "Did you come up with any idea to have sex with each other’s mom?"
    y "No, but I’m thinking."
    y "Did you think of something?"
    scene 293
    ch_name "Yes, and for that you need to come to my home this Sunday."
    y "But I’m going to the beach with my mom this sunday."
    ch_name "Come on bro. You need to cancel that plan with your mom."
    ch_name "Otherwise, we won’t be able to have sex with my mom."
    scene 294
    y "Alright bro. Chill down."
    y "I come to your house this sunday."
    y "But right now we have to meet Ms. Alina."
    y "Remember she has called us in her office."
    y "We’ll get to see that amazing body again."
    scene 293
    ch_name "Damn it! You’re right."
    y "But don’t get too excited, bro."
    y "Ms. Alina is our teacher. We shouldn’t be getting too excited."
    scene 295
    "Ms. Alina's office"
    scene 296
    "Ms. Alina" "Do you boys know why I called you today in my office?"
    ch_name "No, Ms. Alina."
    "Ms. Alina" "First of all, lock the door boys."
    scene 297
    "Ms. Alina" "I've noticed you guys looking vulgarly at my body all the time."
    "Ms. Alina" "I'm your teacher. You shouldn't be looking at me like that."
    y "We're sorry, Ms. Alina."
    "Ms. Alina" "You should be ashamed of yourselves."
    "Ms. Alina" "You should be punished for this."
    ch_name "Punished?"
    "Ms. Alina" "Yes, punished."
    "Ms. Alina" "And I'm going to make you do it now."
    "Ms. Alina" "Take off your shirt, Chris."
    ch_name "What? No way!"
    "Ms. Alina" "Do it now or I'll call your parents."
    scene 298
    ch_name "Fine, Ms. Alina."
    ch_name "This is so humiliating."
    scene 299
    "Ms. Alina" "Now, [y], take off your shirt."
    y "But Ms. Alina..."
    "Ms. Alina" "Do it now or I'll call your parents."
    y "Fine, Ms. Alina."
    y "This is so humiliating."
    scene 300
    "Ms. Alina" "Now both of you stand up and strip down to your underwear."
    ch_name "This is so humiliating."
    y "Yes, it is."
    scene 301
    play music 'sexy.mp3'
    "Ms. Alina" "Both of you have big dicks, huh?"

    "Ms. Alina" "Now tell me honestly, what do you guys think about me?"
    scene 302
    ch_name "You have a great body, Ms. Alina."
    scene 301
    "Ms. Alina" "You are so kind, Chris."
    "Ms. Alina" "But you can be honest with me."
    ch_name "I think you have a sexy body."
    "Ms. Alina" "What do you like the most about my body?"
    ch_name "Your boobs."
    scene 303
    pause
    scene 304
    pause
    scene 305
    "Ms. Alina" "Why do you like them so much?"
    ch_name "They look so big and juicy."
    "Ms. Alina" "Do you want to see them?"
    scene 306
    pause
    scene 307 with vpunch
    "Ms. Alina" "You guys are so pathetic."
    scene 308
    "Ms. Alina" "I can’t believe you guys fell for that."
    "Ms. Alina" "Such losers."
    "Ms. Alina" "Now get dressed and get lost."
    scene 309
    ch_name "She just made a fool out of us."
    y "At least we got to see those amazing boobs."
    ch_name "Yeah, can’t deny that."
    "Ms. Alina" "Don’t you guys want to get dressed?" 
    scene 310
    "Ms. Alina" "Hurry up and leave so that I can get dressed as well."
    scene 311
    y "{i} We must take revenge for what happened here.{/i}"
    scene 312 with vpunch
    play sound 'camera_shutter.mp3'
    "Ms. Alina" "No.. What are you doing?"
    scene 313
    pause
    jump map7

label map7:
    scene map
    play music 'playfull.mp3'
    menu:
        "Go home":
            jump back_home_a_school
        "Go to school":
            scene school
            y "I’m have to return home."
            jump map7

label back_home_a_school:
    scene black
    centered "Evening"
    scene 314
    lu_name "Hey, [y]."
    lu_name "I heard that you guys went to Ms. Alina's office."
    lu_name "Did you get in trouble?"
    scene 315
    y "No, I’m fine."
    lu_name "Did you have fun?"
    y "Yes, we did."
    lu_name "Did you see something interesting?"
    y "Yes, we did."
    lu_name "Is it something that you would like to share with your [lu]?"
    y "No, I don’t think so."
    lu_name "Oh come on. Don’t be shy. Tell me what happened."
    y "Alright, I’ll tell you later."
    lu_name "Okay, I’ll wait for it."
    y "So, how was your day?"
    lu_name "Good. I spent the whole day studying."
    y "That’s good."
    lu_name "Thanks, [y]."
    lu_name "Can we watch TV now?"
    y "Sure."
    lu_name "Okay, thanks."
    scene 316
    lu_name "Bye, [y]."
    y "Bye, [lu_name]."

    scene black
    centered "Same night"
    scene 317
    pause
    scene 318
    pause
    scene 319
    y "Holy shit! I really got to see those boobs!"
    y "Now we can make her do anything we like."
    y "She humiliated us so much today."
    scene 320
    y "We must take revenge."
    y "For today I'll just sleep."
    jump hallway10

label hallway10:
    scene hallway_morning
    menu: 
        "Go to kitchen":
            jump morning_with_mom

        "Go to the [cr_name]'s room":
            scene b_sis_morning
            y "There is no one here."
            jump hallway10
        
        "Go to the [lu_name]'s room":
            scene l_sis_morning
            y "There is no one here."
            jump hallway10
        
        "Go to the bedroom":
            scene mc_room_morning
            y "I should go for breakfast."
            jump hallway10

        "Go to [m]'s room":
            scene mom_room_morning
            y "There's no one here"
            jump hallway10

        "Go to the bathroom":
            scene bathroom_morning
            y "I don't want to use the bathroom now."
            jump hallway10

label morning_with_mom:
    scene 321
    m_name "Good morning honey."
    m_name "How was your sleep?"
    y "Good. Thanks."
    scene 322
    m_name "Would you like something to eat?"
    y "No, thanks [m]."
    m_name "You’re not hungry?"
    y "No, [m]."
    y "I’m full."
    m_name "Are you sure, honey?"
    y "Yes, [m]."
    m_name "Alright, then."
    scene 323
    m_name "Do you want to fuck me?"
    y "Yes, [m]."
    scene 324
    m_name "Okay honey. But we have to wait until the weekend ends."
    m_name "Otherwise your [cr] and [lu] might find out."
    y "Yes, [m]."
    y "m_name I’m going to spend my weekend at Chris’s house."
    m_name "Yes, I’m so glad."
    m_name "Don’t forget to give my regards to Chris’s mom."
    y "Alright mom. I’m leaving now."
    m_name "Okay honey. Enjoy the weekend."
    scene 325
    scene black
    centered "Back at hallway"
    y "Good morning, [cr]."
    cr_name "Good morning."
    scene 326
    y "Did you like what we did last time?"
    cr_name "It was rough. But yes I loved it."
    scene 327
    y "Great. Because I loved it too."
    cr_name "You're so big [y]. Your cock is so big."
    y "And you're so sexy. I loved fucking you."
    cr_name "Yeah, it was fun. I never thought my brother would be so rough with me."
    y "Well, it turns out I can be very rough sometimes."
    cr_name "Yeah, I guess you can."
    cr_name "Anyway, what are you doing this weekend?"
    scene 328
    cr_name "If you’re free then we can do some fun stuff."
    y "I’m going to stay at Chris’s home until the weekend ends."
    cr_name "Anyway, I need to go to work now."
    y "Okay, I'll walk you out."
    cr_name "Thanks, [y]."
    y "No problem. Have a good day."
    cr_name "You too, bro."
    cr_name "Do you want to kiss me?"
    y "Of course I do."
    scene 329
    pause
    y "Shit I'm late for chris mom"
    jump map8

label map8:
    scene map
    menu:
        "Go to school":
            scene school
            y "I need to meet Chris' mom"
            jump map8
        
        "Go to home":
            scene hallway_morning
            y "I need to meet Chris' mom"
            jump map8
        
        "Go to Chris' mom's office":
            jump chris_mom_office

label chris_mom_office:
    scene black
    centered "Therapist Offce / Chris’s mom"
    scene 330
    "Jane" "Hello, [y]. I didn't expect you here today."
    y "Hello, aunt. Are you free right now?"
    "Jane" "Yes, honey. I'm free right now."
    scene 331
    "Jane" "Chris told me that you were gonna spend the weekend with us?"
    y "Yes, aunt."
    "Jane" "What do you want to talk about?"
    scene 333
    y "It's something very embarassing aunt. I'm not sure if I should talk about it."
    "Jane" "Don't worry, [y]. I'm always here to help you."
    "Jane" "You don't need to hesistate."
    y "The thing is I actually had intimate activities with my [m] and [cr]."
    scene 334
    "Jane" "Oh.. really? That's actually great."
    "Jane" "You're feelings are very natural."
    "Jane" "I'm glad you could help your mother."
    "Jane" "She was so lonely since you're dad passed away."
    "Jane" "She needed a strong man in her life again."
    "Jane" "I'm happy that you could be that person."
    scene 335
    y "Do you really think so, aunt?"
    scene 336
    "Jane" "Yes honey. I know what it's like to be lonely."
    "Jane" "You're uncle also passed away around the same time your father passed away."
    "Jane" "It was really hard being alone raising a child."
    "Jane" "It was Chris who helped me get through it."
    scene 225
    play music 'sexy.mp3'
    y "Did Chris have sex with you?"
    scene 337
    "Jane" "Yes, he did. He’s a wonderful boy."
    "Jane" "He made me feel so good."
    scene 331
    y "I’m glad to hear that."
    "Jane" "You’re a good boy. You're just like Chris."
    y "I know, aunt."
    "Jane" "But I’m here for you."
    "Jane" "You can come to me whenever you need someone to talk to."
    "Jane" "I’m always here for you."
    y "Thanks, aunt."
    y "Would you ever have sex with your son's friend?"
    scene 336
    "Jane" "I see where you're getting boy."
    "Jane" "You're asking whether I'd let you fuck me?"
    y "You could interpret it that way."
    "Jane" "Ha ha.. If it's you then I guess I'll be okay with you fucking me."
    "Jane" "I'm very open minded about these things."
    "Jane" "If I'm attracted to you, which I already am and you're also attracted to me, then I have no problem."
    y "I just want to help you aunt."
    "Jane" "Aw.. You're such a sweet boy."
    "Jane" "Now, go meet Chris."
    "Jane" "I'll see you at home."
    y "Alright aunt. Have a good day."
    jump chris_home_scene

label chris_home_scene:
    scene black with fade
    centered "Late the same evening, Chris's home"
    scene 338
    y "..."
    scene 339
    y "So what is your plan?"
    ch_name "We'll simply just ask her."
    ch_name "She's very open minded about these things."
    ch_name "She'll let us fuck her."
    scene 340
    y "What if she gets angry."
    ch_name "No, she won't."
    ch_name "She'll just agree to have sex with us right away."
    y "But how?"
    scene 341
    ch_name "Have a look at this?"
    y "What are these?"
    scene 342
    ch_name "These are some pills I saw online and ordered."
    ch_name "It increases the sex drive of a person."
    ch_name "It makes a person horny as hell."
    ch_name "I'll start fucking her then you join."
    ch_name "We're going give this to my mother without her knowing."
    ch_name "Then we'll make out move."
    y "That's genius bro."
    ch_name "I'm so excited about this."
    scene 343
    "Jane" "Hello, boys. Dinner's ready."
    scene black with fade
    centered "Dinner time"
    scene 344
    y "The food was great aunt."
    scene 345
    ch_name "Yes, mom. It was delicious."
    scene 346
    "Jane" "Thank you boys. I'm glad you liked it."
    scene 347
    ch_name "Mom, we're going to watch a movie tonight in my room."
    ch_name "Do you want to join us?"
    scene 348
    "Jane" "What will I do with you guys?"
    "Jane" "I'll bore you guys."
    y "Please aunt. Come with us."
    "Jane" "Alright boys. Wait for me in the room."
    "Jane" "I'll clean the dishes and come."
    "Jane" "I also have to take a bath."

    scene black with fade
    centered "Later....."
    scene 349
    y "Are you sure this is gonna work?"
    ch_name "Yes, I'm sure this will work. Don't worry."
    ch_name "We're going to watch a porn movie with her."
    ch_name "That's gonna make her horny as hell."
    scene 350
    "Jane" "Hello boys."
    y "Hello aunt."
    scene 351
    ch_name "Sit with us, mom."
    scene 352
    pause
    scene 353
    "Jane" "The scenes are very bold. What movie is this?"
    scene 354
    ch_name "Hot MILF fucked by her son and his friend."
    scene 355
    pause
    scene 356
    pause
    scene 357
    pause
    scene 358
    pause
    scene 359
    "Jane" "Ahh... What are you boys doing?"
    scene 360
    ch_name "We want to have sex with you mom."
    scene 357
    y "Well, ch_name and I were wondering if you would be interested in joining us in a threesome."
    scene 361
    "Jane" "A threesome? Are you serious?"
    y "Yes. We thought it would be fun and exciting."
    "Jane" "I don't know..."
    ch_name "Come on, mom! It'll be fun! Trust me."
    "Jane" "I don't know..."
    ch_name "Please? Just try it out. If you don't like it, we'll stop right away. No questions asked."
    "Jane" "Hmm...okay, I guess I can give it a shot."
    y "Great! Let's get started then!"
    scene 362
    y "So what do you think? Do you like the idea of being with two men?"
    scene 363
    "Jane" "I don't know...it feels a bit weird."
    scene 364
    ch_name "Don't worry, mom! We won't hurt you or anything like that!"
    ch_name "We just want to show you how good it can feel when three people share intimate moments together!"
    scene 365
    y "Exactly! There's no pressure involved here either - just pure enjoyment for everyone involved!"
    scene 366
    ch_name "Plus, who wouldn't want to experience something new like this?"
    "Jane" "I suppose you're right..."
    ch_name "So let's get started then!"
    y "Fuck yeah! Look at this beauty right here!"
    y "Damn bro, your mom is hot!"
    ch_name "I know right?"
    y "She has a nice ass and tits."
    ch_name "She is hot."
    y "Your mom is sexy as fuck bro."
    "Jane""Stop staring at my ass."
    y "Sorry aunt."
    ch_name "Don't be sorry. You know how to enjoy yourself."
    ch_name "Just relax and let us do what we do best."
    "Jane" "Fine."
    ch_name "Good girl."
    scene 367
    ch_name "Her body smells amazing."
    scene 368
    "Jane" "Ohhh...mmmhmmm...mmmhmmm...ohhh...ohhh...ohhh..."
    scene 369
    "Jane" "OHHH FUCK YESSSSSSSS!!!"
    scene 370
    y "Suck my dick, slut."
    "Jane" "Yeah.. Treat me like a slut. Please continue."
    scene 371
    y "That's more like it."
    y "You are such a slut."
    y "You are such a whore."
    scene 372
    "Jane" "Yes [y]. I am your slut."
    y "Open your mouth wide for me and suck my big cock."
    scene 373
    ch_name "I'm going to fuck you now mom."
    "Jane""Please be gentle."
    scene 374
    ch_name "Sure thing, mom."
    scene 375
    pause
    scene 376
    pause
    scene 377
    pause
    scene 378
    pause
    scene 379
    pause
    menu:
        "Cum inside her":
            scene 379
            ch_name "I'm cumming mom."
            scene 380
            "Jane" "Please don't do it inside sweetheart."
            "Jane" "I'm your mother."
            scene 379
            ch_name "Shut the fuck up and take it."
            scene 381
            pause
            scene 382
            "Jane" "What did you just do? I could get pregnant with your child."
            scene 379
            ch_name "I'm sorry mom, It was too much for me."
            ch_name "How does it feel now, mom?"
            scene 382
            "Jane" "Fuck off!"
        "Cum outside":
            scene 379
            ch_name "Fuck! I about to cum."
            scene 380
            "Jane" "Cum outsite honey. Otherwise, I'll get pregnant with your child"
            ch_name "I want to cum on your tits mom"
            scene 383
            "Jane" "Alright, honey. Spray your semen on my tits"
            scene 384
            pause

    scene 370
    y "Would you like to have some actual cock?"
    ch_name "Yeah mom, why don't you let him fuck you now?"
    "Jane" "Ok honey come here and fuck me."
    scene 385
    pause
    scene 386
    pause
    scene 387
    pause
    scene 388
    pause
    menu:
        "Cum inside her":
            scene 389
            y "I'm cumming aunt."
            scene 390
            "Jane" "I'm cumming too."
            "Jane" "No please. Don't cum inside me."
            scene 389
            y "Too late. I'm cumming inside you."
            scene 390
            "Jane" "What are you guys doing? You can't just cum inside me."
            "Jane" "I could get pregnant."
            "Jane" "Oh my god, you both just came inside me."
            "Jane" "What have you guys done?"
        "Cum  outsite":
            scene 392
            y "I'm about to cum aunt"
            scene 391
            pause
    scene 393
    "Jane" "Oh my god. I can't believe this."
    scene 394
    "Jane" "This feels so good."
    "Jane" "I'm about to cum again."
    scene 395
    ch_name "You are a dirty slut, mom"
    ch_name"I'm about to cum."
    scene 396
    ch_name "Do you want it inside or outside?"
    "Jane" "Inside."
    scene 398
    ch_name "Cumming inside your pussy, whore."
    scene 401
    "Jane" "Oh god, yes! Yes! Fill me up!"
    scene 401
    ch_name "I know you want this."
    scene 402
    "Jane" "No, I don't."
    ch_name "I love fucking you mom."
    scene 398
    "Jane" "You're just a horny teenager. It doesn't mean anything."
    ch_name "You scream like a slut with your son's cock inside you"
    "Jane" "No! Stop talking to your mother like that!"
    ch_name "You know you love it, don't you?"
    "Jane" "Of course not!"
    scene 400
    y "Then why are you moaning so hard while getting fucked by your son."
    "Jane" "He's my son. It doesn't count."
    scene 398
    ch_name "It counts."
    scene 400
    "Jane" "Stop saying that!"
    y "Common admit it bitch. You like your son fucking you."
    "Jane" "No. I hate it."
    ch_name "You love it."
    "Jane" "I don't."
    ch_name "Your body tells otherwise."
    #ch_name keeps fucking his mom until he cums inside her.
    scene 398
    pause
    scene 399
    ch_name "Then I should stop fucking"
    scene 400
    "Jane" "NO! Please don't stop. I love it when you fuck me."
    ch_name "Now say it."
    "Jane" "I love getting fucked by my son."
    ch_name "Again. Louder."
    "Jane" "I LOVE GETTING FUCKED BY MY SON!"
    ch_name "See? You like being fucked by your own son."
    "Jane" "Shut up and keep fucking me."
    scene 401
    pause
    scene 402
    pause
    scene 403
    ch_name "There you go."
    ch_name "Phew.."
    ch_name "That was great mom."
    scene 404
    "Jane" "I loved it too honey."
    y "Aunt I want to fuck your ass."
    scene 405
    "Jane" "Ok sweetie. Just be gentle. You're dick is too big."
    scene 406
    pause
    scene 407
    pause
    scene 407
    pause
    scene 409
    pause
    scene 410
    pause
    scene 411
    pause
    scene 412
    pause
    scene 413
    pause
    scene 414
    pause
    scene 415
    pause
    scene 416
    pause
    scene 417
    pause
    scene 418
    y "That was amazing aunt."
    "Jane" "You boys are so big."
    scene 419
    "Jane" "I'm so tired. I about to sleep now."
    scene 420
    ch_name "No, mom now it's time for round 2."
    scene 419
    "Jane" "I don't know what you mean."
    scene 420
    ch_name "You loved the first round. I bet you'd love this one even more."
    scene 419
    "Jane" "What are you talking about?"
    scene 420
    ch_name "Come on, mom. You know exactly what I'm talking about."
    scene 421
    y "We're going to keep fucking you aunt."
    scene 419
    "Jane" "No, please. You guys have already cum so much inside me."
    "Jane" "I'll surely get pregnant now."
    "Jane" "Are you guys tired yet?"
    "Jane" "You guys have cum inside me more than ten times."
    "Jane" "I'll surely get pregnant now."
    scene 420
    ch_name "Shut up, mom."
    y "You can now suck my cum filled dick, aunt."
    scene 423
    "Jane" "I'll never forgive you guys for this."
    scene 424
    y "That was so amazing aunt."
    scene 425
    ch_name "We love you mom."
    scene black
    centered "Next morning"
    pause
    scene 426
    pause
    scene 427
    ch_name "Common admit it bitch. You like your son fucking you."
    "Jane" "No. I hate it."
    ch_name "You love it."
    "Jane" "I don't."
    ch_name "Liar. Your body tells otherwise."
    ch_name "You are a cumslut now. "
    y "Ohh my godd… you guys are fucking like rabbits."
    y "Stop being so rough Chris."
    scene 428
    "Jane" "Don’t worry, honey. I’m enjoying it."
    scene 429
    y "I’m leaving for home now. I have some work now."
    jump map9

label map9:
    scene map
    menu:
        "Go to home":
            jump morning_home

        "Go to school":
            scene school
            y "It's weekend"
            jump map9

label morning_home:
    scene 430
    pause
    scene 431
    y "Good morning, [m]."
    m_name "Oh hi [y], I didn't expect to see you this early."
    m_name "We were just talking about how much we missed you."
    y "Thank you."
    m_name "And how's Chris and Jane?"
    y "He's fine. He's actually doing very well in school these days."
    m_name "That's great! I'm proud of him."
    y "Yeah, me too."
    m_name "So, what brings you back home so early today?"
    m_name "Weren’t you going the spend the whole weekend at Chris’s house?"
    y "I just remember I had some work to do."
    y "I’ll go to my room and get fresh."
    y "I'll take a bath."
    scene 432
    m_name "Sure honey, I'll call you when the breakfast is ready."
    y "Okay, [m]."
    scene 433
    y "Hello, mom."
    scene 434
    m_name "Oh hi [y]."
    y "I told you I had some work to do."
    m_name "Did you finish it already?"
    y "Not yet. I need to eat first."
    y "I'll work on it after breakfast."
    m_name "Okay honey, sit down. Breakfast is almost ready."
    scene 435
    y "Thank you."
    scene 436
    y "This looks delicious, mom."
    scene 437
    m_name "Thanks honey, I hope you like it."
    y "I'm sure I will."
    y "Can I ask you something?"
    m_name "Sure honey, what is it?"
    y "Do you ever miss having sex?"
    scene 438
    m_name "What kind of question is that?"
    y "I just wanted to know."
    m_name "Why do you ask?"
    y "Just curious."
    scene 439
    m_name "I guess I do sometimes."
    m_name "But I don't want to date anyone."
    y "Why not?"
    m_name "Because I'm happy with the way things are right now."
    y "But what if someone proposes you for a relationship?"
    m_name "I would say no."
    y "Why?"
    m_name "Because I'm not interested in relationships anymore."
    y "But what if that person is really good-looking and rich?"
    m_name "Still no."
    y "What if that person is me?"
    m_name "What are you talking about?"
    y "What if I propose you for a relationship?"
    m_name "Are you serious?"
    y "Yes."
    m_name "But we are related. It's wrong."
    y "I don't care about that."
    y "I just want to fuck you."
    m_name "I loved having sex with you as well."
    m_name "But you’re still so young."
    scene 440
    m_name "You can fuck me but you should date other girls also."
    y "Ok mom."
    jump chap2_end

label chap2_end:
    scene black
    centered "Meanwhile at Ms. Alina's office"
    scene 441
    "Ms. Alina" "I know what you boys want."
    scene 442
    "Ms. Alina" "But after I do this you guys have to delete that picture."
    scene 443
    y "Yes, we'll do that."
    ch_name "Yes, Ms. Alina don't worry about it."
    scene black
    centered "Thank you for playing"




