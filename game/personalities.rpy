﻿init 1300:

    #These are the different personality specific responses/dialogue options called through the game. These must all be defined for core personalites.

    # @_greetings - short convo used when you start a convo with someome.
    # @_sex_responses_[foreplay, oral, vaginal, anal] - exclamation used while having sex, generally vaginal.
    # @_climax_responses_[foreplay, oral, vaginal, anal] - exclamation used when a girl climaxes, with a different type for each type of sex
    # @_clothing_accept - dialogue used when you add an outfit to a girls wardrobe and she accepts it.
    # @_clothing_reject - dialogue used when you offer an outfit to a girl but she refuses it because it's too slutty.
    # @_clothing_review - dialogue used after sex when a girl checks her outfit and realises she needs to get redressed.
    # @_strip_reject - dialogue used when you try and strip a piece of clothing off of a girl but she wants it in place.
    # @_sex_accept - dialogue when you offer a sex position to a girl and she agrees because she's slutty. (Not just when you seduce them, that's below!)
    # @_sex_obedience_accept - dialogue used when you offer a sex position to a girl but she only agrees because she's obedient
    # @_sex_gentle_reject - dialouge used when you try and offer a sex position to a girl but she refuse without being angry
    # @_sex_angry_reject - dialogue used when you try and offer a sex position to a girl with a psotiion she finds ridiculously inappropriate.
    # @_seduction_response - dialogue used when you seduce a girl and she accepts
    # @_flirt_response - dialogue when you "chat with" and "flirt" with a girl.
    # @_cum_face - dialogue when you cum on a girls face.
    # @_cum_mouth - dialogue when you cum in a girls mouth
    # @_suprised_exclaim - List of random exclimations used when a character is suprised.
    # @_talk_busy - dialogue used when you've used "chat with" option too many times
    # @_improved_serum_unlock - dialogue used for the serum unlock head researcher event.
    # @_sex_strip - dialogue used when a girl strips for you (but she's not asking permission).
    # @_sex_watch - dialogue used when you're having sex in front of this girl.
    # @_being_watched - dialogue when you're having sex with the girl and being watched by another person
    # @_work_enter_greeting - dialogue used when you walk into a room at work with an employee in it.
    # @_date_seduction - dialogue used after a date when the person had a good time and wants to go back to have sex/make out/whatever.

    python:

        def relaxed_titles(the_person):
            if the_person.love < 0:
                return "Mrs." + the_person.last_name #If she doesn't like you she's much more formal.
            else:
                return the_person.name
        def relaxed_possessive_titles(the_person):
            return relaxed_titles(the_person) #If we don't have a special possessive just use their normal title.
        def relaxed_player_titles(the_person):
            return mc.name
        #Default personality is a well rounded personalty, without any strong tendencies. Default "Lily" personality.
        relaxed_personality = Personality("relaxed", #Lily style personality
        common_likes = ["skirts", "the weekend", "small talk", "the colour pink", "HR work", "supply work", "flirting","punk","pop"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "pants", "the colour yellow", "research work", "work uniforms"],
        common_sexy_dislikes = ["taking control", "doggy style sex", "showing her tits", "showing her ass", "bareback sex", "creampies"],
        titles_function = relaxed_titles, possessive_titles_function = relaxed_possessive_titles, player_titles_function = relaxed_player_titles)

        def reserved_titles(the_person):
            if the_person.love > 10:
                return the_person.name
            else:
                return "Mrs."+the_person.last_name
        def reserved_possessive_titles(the_person):
            return reserved_titles(the_person)
        def reserved_player_titles(the_person):
            return mc.name
        reserved_personality = Personality("reserved", #Mom style personality
        common_likes = ["pants", "research work", "HR work", "Mondays", "working", "makeup", "the colour blue", "conservative outfits","jazz","classical"],
        common_sexy_likes = ["missionary style sex", "kissing", "lingerie", "being submissive", "vaginal sex", "creampies", "giving tit fucks"],
        common_dislikes = ["the colour red", "marketing work", "flirting"],
        common_sexy_dislikes = ["masturbating", "giving blowjobs", "getting head", "doggy style sex", "public sex", "not wearing underwear", "not wearing anything", "bareback sex", "cum facials"],
        titles_function = reserved_titles, possessive_titles_function = reserved_possessive_titles, player_titles_function = reserved_player_titles)

        def wild_titles(the_person):
            return the_person.name
        def wild_possessive_titles(the_person):
            return wild_titles(the_person)
        def wild_player_titles(the_person):
            return mc.name
        wild_personality = Personality("wild", #Stephanie style personality
        common_likes = ["skirts", "small talk", "Fridays", "the weekend", "the colour red", "makeup", "flirting", "marketing work","heavy metal","punk"],
        common_sexy_likes = ["anal creampies", "doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "bareback sex"],
        common_dislikes = ["Mondays", "the colour pink", "supply work", "conservative outfits", "work uniforms"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "giving handjobs"],
        titles_function = wild_titles, possessive_titles_function = wild_possessive_titles, player_titles_function = wild_player_titles)

        def introvert_titles(the_person):
            return the_person.name

        def introvert_possessive_titles(the_person):
            return introvert_titles(the_person)

        def introvert_player_titles(the_person):
            return mc.name

        introvert_personality = Personality("introvert", #Stephanie style personality
        common_likes = ["conservative outfits", "research work", "punk", "working", "the colour black"],
        common_sexy_likes = ["big dicks", "kissing", "anal sex", "getting head", "giving blowjobs", "masturbating", "anal creampies", "giving tit fucks"],
        common_dislikes = ["skimpy outfits", "skirts", "HR work", "marketing work", "makeup", "flirting", "small talk", "pop"],
        common_sexy_dislikes = ["skimpy outfits", "not wearing underwear", "not wearing anything", "public sex", "lingerie"],
        titles_function = introvert_titles, possessive_titles_function = introvert_possessive_titles, player_titles_function = introvert_player_titles)

        list_of_personalities = [relaxed_personality,reserved_personality,wild_personality, introvert_personality]

        #SPECIAL PERSOANLITIES#
        def bimbo_titles(the_person):
            return the_person.name
        def bimbo_possessive_titles(the_person):
            return bimbo_titles(the_person)
        def bimbo_player_titles(the_person):
            valid_mc_titles = []
            valid_mc_titles.append(mc.name)
            valid_mc_titles.append("cutie")
            return valid_mc_titles
        bimbo_personality = Personality("bimbo", #Currently used in the head researcher event line.
        common_likes = ["skirts", "small talk", "the colour pink", "makeup", "pop"],
        common_sexy_likes = ["giving blowjobs", "missionary style sex", "being submissive", "skimpy outfits", "showing her tits", "showing her ass", "not wearing anything", "not wearing underwear", "lingerie", "cum facials"],
        common_dislikes = ["working", "research work", "work uniforms", "conservative outfits", "Mondays"],
        common_sexy_dislikes = ["taking control", "masturbating"],
        titles_function = bimbo_titles, possessive_titles_function = bimbo_possessive_titles, player_titles_function = bimbo_player_titles)

        #UNIQUE PERSONALITIES#
        def stephanie_titles(the_person):
            valid_titles = [the_person.name]
            if the_person.love > 10:
                valid_titles.append("Steph")
            return valid_titles

        def stephanie_possessive_titles(the_person):
            return "Your friend"
        def stephanie_player_titles(the_person):
            return mc.name
        stephanie_personality = Personality("stephanie", default_prefix = "wild",
        common_likes = ["pants", "research work", "Fridays", "makeup", "the colour red"],
        common_sexy_likes = ["giving blowjobs", "drinking cum","cheating on men"],
        common_dislikes = ["Mondays", "HR work", "marketing work", "conservative outfits"],
        common_sexy_dislikes = ["anal sex", "being submissive"],
        titles_function = stephanie_titles, possessive_titles_function = stephanie_possessive_titles, player_titles_function = stephanie_player_titles)


        def nora_titles(the_person):
            valid_titles = [the_person.name]
            return valid_titles

        def nora_possessive_titles(the_person):
            valid_titles = [the_person.name]
            valid_titles.append("Your old boss")
            return valid_titles

        def nora_player_titles(the_person):
            valid_titles = [mc.name]
            return valid_titles

        nora_personality = Personality("nora", default_prefix = "reserved",
        common_likes = ["pants", "working", "research work", "classical"],
        common_sexy_likes = ["vaginal sex", "skimpy uniforms", "lingerie", "masturbating"],
        common_dislikes = ["heavy metal", "HR work", "marketing work", "sports"],
        common_sexy_dislikes = ["not wearing anything", "not wearing underwear", "being submissive", "creampies"],
        titles_function = nora_titles, possessive_titles_function = nora_possessive_titles, player_titles_function = nora_player_titles)

        def alexia_titles(the_person):
            valid_titles = []
            valid_titles.append(the_person.name)
            valid_titles.append("Alex")
            return valid_titles

        def alexia_possessive_titles(the_person):
            valid_possessive_titles = []
            valid_possessive_titles.append("Your old classmate")
            return valid_possessive_titles

        def alexia_player_titles(the_person):
            valid_mc_titles = []
            valid_mc_titles.append(mc.name)
            return valid_mc_titles

        alexia_personality = Personality("alexia", default_prefix = "relaxed",
        common_likes = ["sports", "the colour yellow", "pop", "marketing work"],
        common_sexy_likes = ["doggy style sex", "bareback sex", "not wearing anything", "skimpy outfits"],
        common_dislikes = ["pants", "conservative outfits", "hiking"],
        common_sexy_dislikes = ["anal sex", "being fingered", "taking control"],
        titles_function = alexia_titles, possessive_titles_function = alexia_possessive_titles, player_titles_function = alexia_player_titles)

        def lily_titles(the_person):
            valid_titles = [the_person.name]
            if the_person.love > 15:
                valid_titles.append("Sis")

            return valid_titles
        def lily_possessive_titles(the_person):
            valid_possessive_titles = ["Your sister",the_person.title]

            if the_person.sluttiness > 60:
                valid_possessive_titles.append("Your slut of a sister")

            if the_person.sluttiness > 100:
                valid_possessive_titles.append("Your cock hungry sister")
                valid_possessive_titles.append("The family cumdump")
            return valid_possessive_titles
        def lily_player_titles(the_person):
            return mc.name
        lily_personality = Personality("lily", default_prefix = "relaxed",
        common_likes = ["skirts", "small talk", "the colour pink", "makeup"],
        common_sexy_likes = ["lingerie", "masturbating", "being submissive", "doggy style sex"],
        common_dislikes = ["working", "conservative outfits", "research work", "production work"],
        common_sexy_dislikes = ["taking control", "anal sex", "creampies"],
        titles_function = lily_titles, possessive_titles_function = lily_possessive_titles, player_titles_function = lily_player_titles)

        def mom_titles(the_person):
            valid_titles = ["Mother"]
            if the_person.love > 10:
                valid_titles.append("Mom")
            return valid_titles

        def mom_possessive_titles(the_person):
            valid_possessive_titles = ["Your mother"]
            if the_person.love > 10:
                valid_possessive_titles.append("Your mom")

            if the_person.sluttiness > 60 and the_person.love > 60:
                valid_possessive_titles.append("Your personal MILF")

            if the_person.sluttiness > 100:
                valid_possessive_titles.append("Your cock hungry mom")
                valid_possessive_titles.append("The family cumdump")
            return valid_possessive_titles

        def mom_player_titles(the_person):
            valid_player_titles = [mc.name]
            if the_person.happiness < 70:
                valid_player_titles.append(mc.name + " " + mc.last_name)

            if the_person.love > 20:
                valid_player_titles.append("Sweetheart")
                valid_player_titles.append("Sweety")
            return valid_player_titles


        mom_personality = Personality("mom", default_prefix = "reserved",
        common_likes = ["pants", "conservative outfits", "work uniforms", "HR work", "makeup"],
        common_sexy_likes = ["taking control", "being submissive", "bareback sex", "creampies"],
        common_dislikes = ["production work", "sports"],
        common_sexy_dislikes = ["anal sex", "drinking cum", "sex standing up"],
        titles_function = mom_titles, possessive_titles_function = mom_possessive_titles, player_titles_function = mom_player_titles)


        def aunt_titles(the_person):
            valid_titles = []
            valid_titles.append(the_person.name)
            valid_titles.append("Aunt " + the_person.name)
            if the_person.love > 20:
                valid_titles.append("Auntie")
            return valid_titles

        def aunt_possessive_titles(the_person):
            valid_possessive_titles = []
            valid_possessive_titles.append(the_person.name)
            valid_possessive_titles.append("Your aunt")

            if the_person.love > 20:
                valid_possessive_titles.append("Your loving aunt")


            if the_person.love > 40 and the_person.sluttiness > 60:
                valid_possessive_titles.append("Your personal MILF")

            if the_person.sluttiness > 100:
                valid_possessive_titles.append("Your cock hungry aunt")
                valid_possessive_titles.append("Your cumdump aunt")

            return valid_possessive_titles

        def aunt_player_titles(the_person):
            valid_player_titles = []
            valid_player_titles.append(mc.name)

            if the_person.love > 20:
                valid_player_titles.append("Sweetheart")
                valid_player_titles.append("Sweety")
            return valid_player_titles

        aunt_personality = Personality("aunt", default_prefix = "wild",
            common_likes = ["small talk", "the colour pink", "makeup", "flirting"],
            common_sexy_likes = ["lingerie", "skimpy outfits", "taking control"],
            common_dislikes = ["working", "hiking", "conservative outfits"],
            common_sexy_dislikes = ["public sex", "masturbating", "being fingered", "cheating on men"],
            titles_function = aunt_titles, possessive_titles_function = aunt_possessive_titles, player_titles_function = aunt_player_titles)

        def cousin_titles(the_person):
            valid_titles = []
            valid_titles.append(the_person.name)
            if the_person.love > 20:
                valid_titles.append("Cuz")

            if the_person.love < -30:
                valid_titles.append("Hellspawn")
            return valid_titles

        def cousin_possessive_titles(the_person):
            valid_possessive_titles = []
            valid_possessive_titles.append(the_person.name)
            valid_possessive_titles.append("Your cousin")
            if the_person.love > 20:
                valid_possessive_titles.append("Your cuz")

            if the_person.love < -30:
                valid_possessive_titles.append("Your bitchy cousin")

            if the_person.sluttiness > 40:
                valid_possessive_titles.append("Your cock-goth cousin")

            return valid_possessive_titles

        def cousin_player_titles(the_person):
            valid_player_titles = []
            valid_player_titles.append(mc.name)
            if the_person.love < -20:
                valid_player_titles.append("Asshat")
                valid_player_titles.append("Dickwad")
                valid_player_titles.append("Dick-for-brains")

            if the_person.love > 20:
                valid_player_titles.append("Cuz")

            if the_person.love < 0 and the_person.sluttiness > 40:
                valid_player_titles.append("Dildo")

                if the_person.obedience < 20:
                    valid_player_titles.append("Cock slave")
                    valid_player_titles.append("Slave")
            return valid_player_titles

        cousin_personality = Personality("cousin", default_prefix = "introvert",
            common_likes = ["the colour black","heavy metal","punk","makeup","skimpy outfits"],
            common_sexy_likes = ["lingerie","masturbating","taking control","getting head"],
            common_dislikes = ["small talk","flirting","working"],
            common_sexy_dislikes = ["kissing", "giving blowjobs", "bareback sex"],
            titles_function = cousin_titles, possessive_titles_function = cousin_possessive_titles, player_titles_function = cousin_player_titles)


        def get_random_personality():
            return get_random_from_list(list_of_personalities)

###############################
##### Relaxed Personality #####
###############################
# <editor-fold
label relaxed_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around."
    $ the_person.set_title("???")
    the_person.char "I guess? What do you need?"
    mc.name "I know this is strange, but I saw you and I just needed to know your name."
    "She laughs and blushes."
    the_person.char "Really? You're just saying that to impress me, aren't you."
    mc.name "Really, I really just wanted to talk to you."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person.char "Well fine, my name is [formatted_title]. It's nice to meet you..."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    "She waits expectantly for you to introduce yourself."
    return

label relaxed_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Ugh, what do you want?"
    elif the_person.happiness < 90:
        the_person.char "Hey..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title], it's good to see you."
            else:
                the_person.char "Hey there handsome, feeling good?"
        else:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title]."
            else:
                the_person.char "Hey there!"
    return

label relaxed_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm.... You're good at getting me warmed up..."
        else:
            the_person.char "Mmmm... Ah..."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Oh that's it. Mmm."
            "She purrs warmly."
        else:
            the_person.char "Oh my god..."
            "It seems like she's trying not to moan too loudly."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            if the_person.outfit.wearing_panties():
                the_person.char "Ah... If you get me any wetter I'm going to soak right through my panties."
            elif the_person.outfit.vagina_available():
                the_person.char "Good thing I'm not wearing any panties, you'd have me soaking right through them..."
            else:
                the_person.char "Oh god, if I get any wetter it's going to soak right through my clothes."
        else:
            the_person.char "I can't believe you're getting me this wet..."

    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Oh god, you might actually make me cum like this... Wow!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I wish my [so_title] knew how to touch me like this. You might actually make me cum!"
        else:
            the_person.char "Oh god... I think I might cum soon!"

    return

label relaxed_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh you know what I want [the_person.mc_title]... Ah..."
        else:
            the_person.char "Oh wow... that's... Mph!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Mmmm, that's so good. Ah..."
        else:
            the_person.char "That... that feels so good [the_person.mc_title]... So fucking good."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "God, your tongue feels so good!"

        else:
            "You're so good at that... Fuck, it's starting to drive me crazy!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "You're going to get me there [the_person.mc_title], you're going to get me to cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "My [so_title] never does this for me any more... I feel horrible, but I need this so badly!"
        else:
            the_person.char "Oh no... Oh god, you're going to make me..."
            the_person.char "Cum!"

    return

label relaxed_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, your cock feels real good inside me."
        else:
            the_person.char "Oh my god... Ah..."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Keep fucking me [the_person.mc_title], it feels fantastic!"
        else:
            the_person.char "Oh my god, that feeling..."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            "Ah, fuck me [the_person.mc_title]! Give me that big cock!"

        else:
            "[the_person.possessive_title] mumbles softly to herself."
            the_person.char "Fuck... Oh fuck... My pussy..."
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Ah! Fuck me, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Fuck me, fuck me harder! My [so_title] never fucks me like this, it feels so good!"
        else:
            the_person.char "Oh god, I think you're cock is going to make me cum soon!"

    return

label relaxed_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh fuck, you're really stretching me out!"
        else:
            the_person.char "Fuck, it feels so big... That's all of it, right? I can't take any more!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Fuck my ass [the_person.mc_title], I can take it!"
        else:
            the_person.char "Oh fuck, my poor ass..."
            "Her groan is a mixture of pain and pleasure."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Oh my poor little ass, you're going to ruin me..."
            "She doesn't seem very upset with the idea."
        else:
            "[the_person.title] bites down on her lip and growls defiantly."
            the_person.char "Oh fuck... Fuck you're big!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Oh god, keep going! Stuff my ass and make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I never let my [so_title] do this, you know? My tight ass is only for you!"
        else:
            the_person.char "I can't..."
            "She struggles to catch her breath."
            the_person.char "...I can't believe you might make me cum!"
    return


label relaxed_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh my god! I'm going to... I'm going to..."
        the_person.char "{b}Cum!{/b} Ah!"
    else:
        the_person.char "Mmmmhm!"
    return

label relaxed_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh fuck! Oh fuck, make me cum [the_person.mc_title]!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Oh my god, I'm going to cum. I'm going to cum!"
        "She closes her eyes and squeals with pleasure."
    return

label relaxed_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I'm going to cum! Ah! Fuck me [the_person.mc_title], I want to cum so badly! Ah!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Ah! I'm cumming! Oh fuck! Ah!"
    return

label relaxed_climax_responses_anal(the_person):
    if the_person.sluttiness > 80:
        the_person.char "I'm going to cum! Fuck my ass and make me cum!"
    else:
        the_person.char "Oh fuck, I think... I think I'm going to cum!"
    return

label relaxed_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
    else:
        the_person.char "Oh, it's cute! Thanks [the_person.mc_title]!"
    return

label relaxed_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Wow. I'm usually up for anything but I think that's going too far."
        else:
            the_person.char "Wow. It's a little... skimpy. I don't think I could wear that."
    return

label relaxed_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
    else:
        if the_person.sluttiness > 40:
            the_person.char "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
        else:
            the_person.char "My clothes are a mess! I'll be back in a moment, I'm going to go get cleaned up."
    return

label relaxed_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I'm sorry, but can we leave that where it is for now?"
    elif the_person.obedience < 70:
        the_person.char "Slow down there, I'll decide when that comes off."
    else:
        the_person.char "I think that should stay where it is for now."
    return

label relaxed_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person.char "I was just about to suggest the same thing."
        else:
            the_person.char "Mmm, you have a dirty mind [the_person.mc_title], I like it."
    else:
        the_person.char "Okay, we can give that a try."
    return

label relaxed_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god [the_person.mc_title], I should really say no... But you always make me feel so good, I can't say no to you."
    else:
        if the_person.obedience > 130:
            the_person.char "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
        else:
            the_person.char "I... Okay, if you really want to, lets give it a try."
    return

label relaxed_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
    else:
        the_person.char "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
    return

label relaxed_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "Wait, what? I have a [so_title], what did you think we were going to be doing?"
        "She glares at you and walks away."
    elif the_person.sluttiness < 20:
        the_person.char "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person.char "Ugh! Get away from me, I don't even want to talk to you after that."
    else:
        the_person.char "What the fuck do you think you're doing, that's disgusting!"
        the_person.char "Get the fuck away from me, I don't even want to talk to you after that!"
    return

label relaxed_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Yes [the_person.mc_title]? Do you need help relieving some stress?"
        else:
            the_person.char "Yes [the_person.mc_title]? Is there something I can help you with?"
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I know that look. Do you want to fool around a little?"
        elif the_person.sluttiness > 10:
            the_person.char "Oh, do you see something you like?"
        else:
            the_person.char "Oh, I don't really know what to say [the_person.mc_title]..."
    return

label relaxed_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
        elif the_person.sluttiness < 50:
            the_person.char "Come on, let's go find someplace quiet where we won't be interrupted."
        else:
            the_person.char "No point waisting any time then, right? Let's get to it!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "No point wasting any time, right? I hope my [so_title] won't be too jealous."
        else:
            the_person.char "I guess we could sneak away for a few minutes, but we have to make sure my [so_title] doesn't find out what we're doing."
    return

label relaxed_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "Well, there's nobody around to stop us..."
        elif the_person.sluttiness < 50:
            the_person.char "Mmm, that's a fun idea. Come on, let's get to it!"
        else:
            the_person.char "Oh [the_person.mc_title], don't make me wait!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "Don't make me wait then [the_person.mc_title]!"
        else:
            the_person.char "This is so dumb, I have a [so_title], I shouldn't be doing this..."
            "It's clear she wants to do it anyways."
    return

label relaxed_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        "[the_person.title] blushes and looks away from you awkwardly."
        the_person.char "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."

    elif the_person.sluttiness < 50:
        the_person.char "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
        "[the_person.title] smiles and gives you a wink."

    else:
        the_person.char "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
    return

label relaxed_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "If that's what you want I'm sure I could help with that [the_person.mc_title]."
        else:
            the_person.char "Thank you for the compliment, [the_person.mc_title]."
    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person.char "Well thank you [the_person.mc_title]. Don't let my [so_title] hear you say that though, he might get jealous."
            "She smiles and winks mischievously."
        else:
            the_person.char "I have a [so_title], you really shouldn't be talking to me like that..."
            "She seems more worried about being caught than flirting with you."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peak."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person.char "Hey, maybe if you buy me dinner first."
            "[the_person.title] gives you a wink and smiles."
    return

label relaxed_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Do I look cute covered in your cum, [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person.char "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
        else:
            the_person.char "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label relaxed_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person.char "Bleh, I don't know if I'll ever get use to that."
    return

label relaxed_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Mmm, your cum feels so warm. I wish you weren't wearing a condom; I bet you would feel amazing raw."
        else:
            the_person.char "Whew... I can feel how warm your cum is through the condom. It feels nice."

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Your cum is so nice and warm..."
                the_person.char "If you get me pregnant I guess I'll have to tell my [so_title] it's his."
            else:
                the_person.char "Mmm, it's so warm... I wonder if it's going to get me pregnant."
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Fuck. You need to pull out next time, okay? I have a [so_title], what if I got pregnant?"
            else:
                the_person.char "Fuck... You really shouldn't be cumming inside of me."
                "She closes her eyes and mutters to herself."
                the_person.char "What would I do if I got pregnant?"
    return

label relaxed_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Oh god yes, cum inside me!"
    else:
        the_person.char "Oh god, ah!"
    return

label relaxed_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
    the_person.char "[rando]"
    return

label relaxed_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "Hey, I'm really sorry but I've got some stuff I need to take care of. Could we catch up some other time?"
    else:
        the_person.char "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
    return

label relaxed_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "Let me get this out of the way..."
        else:
            the_person.char "Let me get this out of the way for you..."

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "This is just getting in the way..."
        else:
            the_person.char "Ah... I need to get this off."

    else:
        if the_person.arousal < 50:
            the_person.char "Let me get this worthless thing off..."
        else:
            the_person.char "Oh god, I need all of this off so badly!"

    return

label relaxed_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Holy shit, are you really doing this in front of everyone?"
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        $ the_person.change_happiness(-1)
        "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "Oh my god, you two are just... Wow..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh my god that's... Wow that looks...Hot."
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."

    return

label relaxed_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label relaxed_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        if the_person.obedience > 120:
            "[the_person.title] gives you a curt nod and then turns back to what she was doing."
        else:
            "[the_person.title] glances at you when you enters the room then looks away quickly to avoid starting a conversation."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 50:
            "[the_person.title] looks up from her work when you enter the room."
            the_person.char "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
            "She smiles and winks, then turns back to what she was doing."
        else:
            "[the_person.title] turns to you when you enter the room and shoots you a smile."
            the_person.char "Hey, good to see you!"

    else:
        if the_person.obedience < 90:
            "[the_person.title] glances up from her work."
            the_person.char "Hey, how's it going?"
        else:
            "[the_person.title] waves at you as you enter the room."
            the_person.char "Hey, let me know if you need anything [the_person.mc_title]."
    return

label relaxed_date_seduction(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
            else:
                the_person.char "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
        else:
            if the_person.love > 40:
                the_person.char "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
            else:
                the_person.char "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "I had a great time [the_person.mc_title]. My [so_title] is suppose to be out for the rest of the night with his friends so..."
                the_person.char "Would you like to swing by my place tonight?"
            else:
                the_person.char "I had such a good time tonight [the_person.mc_title]. It's been years since I had this much fun with my [so_title]."
                the_person.char "He's out with some friends tonight. Would you like to come to my place and have a drink?"
        else:
            if the_person.love > 40:
                the_person.char "I don't want this night to end. My [so_title] is out with friends, do you want to come home with me so we can spend more time together?"
            else:
                the_person.char "Tonight was fantastic. I think my [so_title] is out for the night, so we could go back to my place for a quick drink. What do you say?"
    return

label relaxed_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "Oh damn it [the_person.mc_title], I want more of you so badly!"
            else:
                the_person.char "Is that all you wanted to do? I was happy just being close to you."
        else:
            if the_person.arousal > 60:
                the_person.char "Is that really all? [the_person.mc_title], I was just getting started!"
            else:
                the_person.char "Aww, we were just getting started and you're already finished?"

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You don't want to take this any further? I thought we had a real connection."
            else:
                the_person.char "That's all? Well, maybe we can try again some other time."
        else:
            if the_person.arousal > 60:
                the_person.char "Oh my god... you've got me all out of breath..."
            else:
                the_person.char "That's all? Alright."
    return

label relaxed_sex_take_control(the_person):
    if the_person.arousal > 60:
        the_person.char "No no no, you can't just get worked up and then leave. We're finishing this, one way or another."
    else:
        the_person.char "Wait, we're just getting started! You just relax and leave this to me."
    return

label relaxed_sex_beg_finish(the_person):
    "No no no, please [the_person.mc_title] you can't stop now. I'll do whatever you want, please just let me cum!"
    return

## Role Specific Section ##
label relaxed_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] smiles mischievously."
    the_person.char "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is necessary if we want to see rapid results."
    mc.name "Go on, I'm interested."
    the_person.char "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
    the_person.char "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
    return

#</editor-fold>

################################
##### Reserved Personality #####
################################
# <editor-fold
label reserved_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around and looks at you quizzically."
    $ the_person.set_title("???")
    the_person.char "I suppose you could. How can I help you?"
    mc.name "I'm so sorry, I know this is silly but I just couldn't let you walk by without knowing your name."
    "She laughs and rolls her eyes."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person.char "Well then, I suppose I shouldn't disappoint you. You can call me [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    "[the_person.possessive_title] holds her hand out to shake yours."
    the_person.char "What about you, what's your name?"
    return

label reserved_greetings(the_person):
    if the_person.love < 0:
        the_person.char "... Do you need something?"
    elif the_person.happiness < 90:
        the_person.char "Hello..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title]."
            else:
                the_person.char "Hello, are you feeling as good as you're looking today?"
        else:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title]."
            else:
                the_person.char "Hello, I hope you're doing well."
    return

label reserved_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know just what I like, don't you?"
        else:
            the_person.char "Oh my... that feels very good, [the_person.mc_title]!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person.char "Keep doing that [the_person.mc_title]... Wow, you're good!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Oh gods above that feels amazing!"
        else:
            the_person.char "Oh lord... I could get use to you touching me like this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Touch me [the_person.mc_title], I want you to touch me!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I should feel bad... but my [so_title] never touches me this way!"
                the_person.char "I need this, so badly!"
        else:
            the_person.char "I want you to keep touching me. I never thought you could make me feel this way, but I want more of it!"

    return

label reserved_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title], you're so good to me."
        else:
            the_person.char "Oh my... that feels..."
            "She sighs happily."
            the_person.char "Good!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Yes, just like that! Mmm!"
        else:
            the_person.char "Keep doing that [the_person.mc_title], it's making me feel... very aroused."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you really know how to put that tongue of yours to good use. That feels amazing!"
        else:
            the_person.char "Oh lord... your tongue is addictive, I just want more of it!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Oh I need this so badly [the_person.mc_title]! If you keep going you'll make me climax!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I should feel bad, but you make me feel so good and my [so_title] never does this for me!"
        else:
            the_person.char "Oh sweet lord in heaven... This feeling is intoxicating!"

    return

label reserved_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I love feeling you inside of me!"
        else:
            the_person.char "Oh lord, you're so big... Whew!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person.char "Oh that feels very good, keep doing that!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! Oh god yes, fuck me!"
        else:
            the_person.char "Oh lord your... cock feels so big!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":

                the_person.char "Keep... keep going [the_person.mc_title]! I'm going to climax soon!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Keep going! My [so_title]'s tiny dick never makes me climax and I want it so badly!"
                the_person.char "I should feel bad, but all I want is your cock in me right now!"
        else:
            "[the_person.title]'s face is flush as she pants and gasps."
    return

label reserved_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you feel so big when you're inside me like this."
        else:
            the_person.char "Be gentle, it feel like you're going to tear me in half!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Give it to me, [the_person.mc_title], give me every last inch!"
        else:
            the_person.char "Oh god! Oww!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "I hope my ass isn't too tight for you, I don't want you to cum early."
        else:
            the_person.char "I don't think I will be able to walk straight after this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "You're cock feels so stuffed inside me! Keep going, I might actually climax!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "My [so_title] always wanted to try anal, but I told him it would never happen. My ass belongs to you , [the_person.mc_title]!"
        else:
            the_person.char "Oh lord, this is actually starting to feel good... I might be able to climax after all!"

    return

label reserved_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh my... I'm going to... cum!"
    else:
        the_person.char "I... Oh my god, this feeling is..."
        "She pauses and moans excitedly."
        the_person.char "So good!"
    return

label reserved_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Keep going [the_person.mc_title], you're going to make me..."
        "She barely finishes her sentence as her body shivers with pleasure."
        the_person.char "... Orgasm!"
    else:
        the_person.char "This feeling... Oh... Oh!"
        "Her eyes close and she takes a deep breath."
    return

label reserved_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "You're going to... Ah! You're going to make me climax [the_person.mc_title]!"
        "She closes her eyes as she tenses up. She freezes for a long second, then lets out a long, slow breath."
    else:
        the_person.char "Oh, I think I'm about to... Oh yes!"
    return

label reserved_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Mmmm, fuck me [the_person.mc_title], fuck my ass and make me cum!"
    else:
        the_person.char "Oh lord, I think I'm going to climax. You're going to make me cum by fucking my ass!"
    return

label reserved_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "You're too kind [the_person.mc_title]. I'll add it to my wardrobe right away."
    else:
        the_person.char "For me? Oh, I'm not use to getting gifts like this..."
    return

label reserved_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "You're too kind [the_person.mc_title], really. I don't think I can accept such a... beautiful gift from you though."
    else:
        if the_person.sluttiness > 60:
            the_person.char "It's very nice [the_person.mc_title], but I think it's a little too revealing, even for me. Maybe when I'm feeling a little more bold, okay?"
        else:
            the_person.char "Really [the_person.mc_title]? Just suggesting that I would wear something like that is a little too forward, don't you think?"
    return

label reserved_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "I'm such a mess right now [the_person.mc_title], I just have to go and get tidied up for you. I'll be back in a moment."
    else:
        if the_person.sluttiness > 40:
            the_person.char "Oh dear, my clothes are just a mess after all of that. Not that I'm complaining, of course, but I should go get tidied up. Back in a moment."
        else:
            the_person.char "Oh, I look like such a mess right now. I'll be back in a moment."
    return

label reserved_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I'm sorry [the_person.mc_title], but I think that should stay where it is for now. For modesty's sake."
    elif the_person.obedience < 70:
        the_person.char "That's going to stay right there for now. I'll decide when I want it to come off, okay?."
    else:
        the_person.char "[the_person.mc_title], I don't feel comfortable taking that off. Just leave it put."
    return

label reserved_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person.char "Good, I didn't want to be the one to suggest it but that sounds like fun."
        else:
            the_person.char "Mmm, you think we should give that a try? I'm feeling adventurous today, lets go."
    else:
        the_person.char "Oh, I know I shouldn't [the_person.mc_title]... but I think you've managed to convince me."
    return

label reserved_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I shouldn't... I really shouldn't. But I know you want me, and I think I want you too. Promise you'll make me feel good too?"
    else:
        if the_person.obedience > 130:
            the_person.char "Okay [the_person.mc_title], if that's what you want. I'll do what I can to serve you."
        else:
            the_person.char "If it were anyone other than you I'd say no [the_person.mc_title]. Don't get too use to this, okay?"
    return

label reserved_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Wait, a lady must be romanced first [the_person.mc_title]. At least get me warmed up first."
    else:
        the_person.char "This doesn't seem like the kind of thing a proper lady would do. Lets do something else, please."
    return

label reserved_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "Excuse me? I have a wonderful [so_title] and I would never dream of doing anything to betray him!"
        "She glares at you and shakes her head."
        the_person.char "I need some space, [the_person.mc_title]. I didn't think you were that kind of man."
    elif the_person.sluttiness < 20:
        the_person.char "Excuse me? Do I look like some sort of prostitute?"
        the_person.char "Get away from me, you're lucky I don't turn you into the police for that! Give me some space, I don't want to talk after that."
    else:
        the_person.char "Um, what do you think you're doing [the_person.mc_title]? That's disgusting, and certainly no way to act around a lady!"
    return

label reserved_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Hello [the_person.mc_title], is there something I can help you with? Something of a personal nature perhaps?"
        else:
            the_person.char "Hello [the_person.mc_title], is there something I can help you with?"
    else:
        if the_person.sluttiness > 50:
            the_person.char "You've got that look in your eye again. there's just no satisfying you, is there? You're lucky I'm such a willing participant."
        elif the_person.sluttiness > 10:
            the_person.char "Oh [the_person.mc_title], you always know how to make a woman feel wanted..."
        else:
            the_person.char "[the_person.mc_title], isn't that a little bit forward of you? I'm not saying no though..."
    return

label reserved_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "I don't think anyone will miss us for a few minutes. We can... get closer and see where things go."
        elif the_person.sluttiness < 50:
            the_person.char "Come on, let's go find someplace quiet then."
        else:
            the_person.char "Well then, do you want to take me right here or should we get a room?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "Well you have my attention. We should find some place private, unless you want my [so_title] to hear about us."
        else:
            the_person.char "I know I shouldn't... We need to keep it quiet, so my [so_title] doesn't find out."
    return

label reserved_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "How about we start with a little kissing and just see where it goes."
        elif the_person.sluttiness < 50:
            the_person.char "Oh [the_person.mc_title], you're going to make me blush! Come over here!"
        else:
            the_person.char "Mmm, that sounds so nice [the_person.mc_title]. Don't make me wait, get over here!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "Come here [the_person.mc_title], I want you to touch me in ways my [so_title] never does!"
        else:
            the_person.char "This is so improper."
            "She locks eyes with you, deadly serious."
            the_person.char "You can never tell my [so_title] about this, is that understood?"
            "You nod and she melts into your arms."
    return

label reserved_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Oh... I'm sorry [the_person.mc_title] but I couldn't imagine doing anything like that."

    elif the_person.sluttiness < 50:
        the_person.char "I'm sorry, but I'm just not in the mood for any fooling around right now. Maybe some other time though."

    else:
        the_person.char "Oh [the_person.mc_title], that sounds like a lot of fun, but I think we should save it for another time."
    return

label reserved_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "It would be so improper, but for you I'm sure I could arrange something special."
        else:
            the_person.char "Thank you for the compliment, [the_person.mc_title], I appreciate it."

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person.char "I'm glad you appreciate it. My [so_title] hardly even looks at me any more."
            "She spins, giving you a full look at her body."
            the_person.char "His loss, right?"
        else:
            the_person.char "[the_person.mc_title], I should remind you I have a [so_title]. We can be friendly with each other, but that's where it should end."
            "She seems more worried about maintaining appearances than she was about actually flirting with you."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title], that's so naughty of you to even think about..."
            "[the_person.title] winks at you and spins, giving you a full look at her body."
            the_person.char "How will I ever get you to contain yourself?"
        else:
            the_person.char "Please [the_person.mc_title], a woman like me likes a little romance in her relationships. At least buy me dinner first."
    return

label reserved_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Ah, that's always a pleasure, [the_person.mc_title]."
        else:
            the_person.char "Well that's certainly a lot. I hope that means I did a satisfactory job."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Oh [the_person.mc_title], what are you doing to me? I'm beginning to like looking like this!"
        else:
            the_person.char "Oh god [the_person.mc_title], could you imagine if someone saw me like this? I really should go and get cleaned up."
    return

label reserved_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Mmm, always a pleasure to taste you [the_person.mc_title]. I hope you had a good time."
        else:
            "[the_person.title] puckers her lips, obviously not happy with the taste but too polite to say anything."
    else:
        if the_person.sluttiness > 80:
            the_person.char "You're making me act like such a slut [the_person.mc_title], what would the other women think if they knew what I just did?"
        else:
            the_person.char "Well, at least there's no mess to clean up. I need to go wash my mouth out after that though."
    return

label reserved_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Oh... your seed is so close to me. Just a thin, thin condom in the way..."
        else:
            the_person.char "I can feel your seed through the condom. Well done, there's a lot of it."

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Yes, give me your seed!"
                the_person.char "If I become pregnant I can say it's my [so_title]'s. I'm sure he would believe it."
            else:
                the_person.char "Mmm, your semen is so nice and warm. I wonder how potent it is. You might have gotten me pregnant, you know."
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person.char "What would I tell my [so_title] if I got pregnant? He might not believe it's his!"
            else:
                the_person.char "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person.char "I'm in no position to be getting pregnant."
                the_person.char "Well, I suppose you have me in the literal position to get pregnant, but you know what I mean."
    return

label reserved_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Cum inside me [the_person.mc_title], fill my ass with your cum!"
    else:
        the_person.char "Oh lord, I hope I'm ready for this!"
    return

label reserved_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my!","Oh, that's not good!", "Whoa!", "Ah!", "My word!", "Oops!", "Bah!", "Dangnabbit!"])
    the_person.char "[rando]"
    return

label reserved_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I'd love to chat some more, but I've already spent far to much time getting distracted. Maybe we can catch up some other day, okay?"
    else:
        the_person.char "Sorry to interrupt, but I've got some work I really need to see to. I'd love to catch up some other time though."
    return

label reserved_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "I think I can do away with this for a few minutes..."
        else:
            the_person.char "Oh, I bet this has been in your way the whole time..."

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "I think I'm past the point of needing this..."
        else:
            the_person.char "I don't need this any more, one second!"

    else:
        if the_person.arousal < 50:
            the_person.char "One moment, I'm wearing entirely too much right now."
        else:
            the_person.char "I need this off, I want to feel you against more of me!"

    return

label reserved_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Oh my god, I can't believe you're doing that here in front of everyone. Don't either of you have any decency?"
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        $ the_person.change_happiness(-1)
        "[the_person.title] shakes her head and tries to avoid watching you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] tries to avert her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh my..."
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches quietly while you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Glad to see you two are having a good time. [the_person.mc_title], careful you aren't too rough with her."
        "[the_person.title] watches quietly while you and [the_sex_person.name] [the_position.verb]."
    return

label reserved_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "It's okay [the_person.mc_title], you don't have to be gentle with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        "[the_person.title] ignores [the_watcher.title] and keeps [the_position.verb] you."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person.char "Mmm, come on [the_person.mc_title], let's give [the_watcher.title] a show!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Being watched shouldn't... I didn't think it would feel so good!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "Maybe [the_watcher.title] is right, we shouldn't be doing this..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Oh [the_watcher.title], you shouldn't be watching me do this..."
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label reserved_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] pretends not to notice you come into the room."

    elif the_person.happiness > 130:
        "[the_person.title] smiles happily when you come into the room."
        the_person.char "Hello [the_person.mc_title], always glad to have you stop by."

    else:
        if the_person.obedience < 100:
            "You pass by [the_person.title] as you enter the room. She's absorbed by her work and only gives you a grunt and a nod."
        else:
            "You pass by [the_person.title] as you enter the room. She looks up, startled."
            the_person.char "Oh! Sorry [the_person.mc_title], I was distracted and didn't notice you come in. Let me know if you need help with anything."
    return

label reserved_date_seduction(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "[the_person.mc_title], would you like to come back home with me? I've got some wonderful wine that makes me do crazy things."
            else:
                the_person.char "You were a fantastic date [the_person.mc_title]. I know I should be getting to bed soon, but would you like to come back for a quick drink?"
        else:
            if the_person.love > 40:
                the_person.char "You're such great company [the_person.mc_title]. Would you like to come back to my place so we can spend some more time together?"
            else:
                the_person.char "I had a fantastic night [the_person.mc_title]. Before you head home would you like to share a glass of wine with me?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "[the_person.mc_title], would you like to come home with me tonight? My [so_title] is away on business and I'd love to drink some of his wine with you."
            else:
                the_person.char "This was a lot of fun. I shouldn't be out too late, but could I invite you back for a drink? My [so_title] shouldn't be home until much later."
        else:
            if the_person.love > 40:
                the_person.char "You're making me feel the same way I did when I first fell in love... Do you want to come back to my house to share one last drink?"
                the_person.char "My [so_title] won't be home until much later. I think he stays at work so late to avoid me."

            else:
                the_person.char "I had a fantastic night [the_person.mc_title], it's been so long since my [so_title] treated me this way."
                the_person.char "Would you like to share one last glass of wine at my house? My [so_title] is away on business, so I would be home all alone..."
    return

label reserved_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're done? You're going to drive me crazy [the_person.mc_title], I'm so horny..."
            else:
                the_person.char "All done? I hope you were having a good time."
        else:
            if the_person.arousal > 60:
                the_person.char "That's all? I don't know how you can stop, I'm so horny after that!"
            else:
                the_person.char "Is that all? Well, that's disappointing."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're done? Well, you could have at least thought about me."
            else:
                the_person.char "All done? Maybe we can pick this up another time when we're alone."
        else:
            if the_person.arousal > 60:
                the_person.char "I... I don't know what to say, you've worn me out."
            else:
                the_person.char "That's all you wanted? I guess we're finished then."
    return


label reserved_sex_take_control (the_person):
    if the_person.arousal > 60:
        the_person.char "I can't let you go [the_person.mc_title], I'm going to finish what you started!"
    else:
        the_person.char "Do you think you're going somewhere? We're just getting started [the_person.mc_title]."
    return

label reserved_sex_beg_finish(the_person):
    "Wait, you aren't stopping are you? Please [the_person.mc_title], I'm so close to cumming, I'll do anything!"
    return


## Role Specific Section ##
label reserved_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] nods in agreement."
    the_person.char "I think I have an idea that could really help us along. All of our testing procedures focus on human safety, but what I really need to know about are the subjective effects of our creations."
    the_person.char "With your permission, I would like to take a dose of serum myself and have you record my experience with it."
    return

#</editor-fold>

############################
##### Wild Personality #####
############################
# <editor-fold
label wild_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around and looks you up and down."
    #TODO: Have this differ based on personality
    $ the_person.set_title("???")
    the_person.char "Uh, sure? What do you want?"
    mc.name "I know this sounds crazy, but I saw you and just wanted to say hi and get your name."
    "She laughs and crosses her arms."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person.char "Yeah? Well I like the confidence, I'll say that. My name's [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    the_person.char "And what about you, random stranger? What's your name?"
    return

label wild_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Oh god, what do you want now?"
    elif the_person.happiness < 90:
        the_person.char "Hey. I hope you're having a better day than I am."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hello there [the_person.mc_title]. How can I help you, do you have anything that needs attention? Anything at all?"
            else:
                the_person.char "Hey there [the_person.mc_title], I hope this is for pleasure and not business."
        else:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title]"
            else:
                the_person.char "Hey, how's it going?"
    return

label wild_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh fuck, I love the way you touch me!"
        else:
            the_person.char "Oh... Oh fuck that feels nice!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "It feels so fucking good when you touch me like that!"
        else:
            the_person.char "Mmm, keep going [the_person.mc_title]. Just keep going."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, touch me all over. I'm your dirty slut and you can do anything you want with me!"
        else:
            the_person.char "Touch me, [the_person.mc_title], I'm all yours!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Oh fuck, I'm going to cum soon. I can feel it happening, you're getting me so close!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "The way you feel is so different from my [so_title]. For some reason your touch is the one that drives me crazy."
        else:
            the_person.char "Don't stop! You're going to make me cum - don't you dare stop!"

    return

label wild_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, I love getting some good head."
        else:
            the_person.char "Fuck me that feels real nice."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Eat me out [the_person.mc_title], your tongue feels amazing!"
        else:
            the_person.char "That feels so good, you have no idea!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, lick that pussy! Ah!"
        else:
            the_person.char "Oh god, yes! Yes!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Fuck fuck fuck, that's it right there!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "My [so_title] never eats me out like this, [the_person.mc_title]!"
                the_person.char "Make me cum my brains out and forget about him!"
        else:
            the_person.char "Don't stop! You're going to make me cum, don't you dare stop!"

    return

label wild_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh fuck, I never get tired of feeling you inside me!"
        else:
            the_person.char "Oh... Oh fuck me your cock feels nice..."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you feel so good fucking my pussy!"
        else:
            the_person.char "Ah, fuck me just like that!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "That's right, use me like your dirty little slut and fuck my pussy raw!"
        else:
            the_person.char "Oh fuck yes, fuck yes!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Fuck! I'm... You're cock is going to make me cum! I want you to make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Your cock is stretching me out, my [so_title] is never going to be enough for me after this!"
                the_person.char "Oh well, fuck him! Keep going and make me cum!"

        else:
            the_person.char "Don't stop fucking me! You're going to make me cum, I can feel it!"

    return

label wild_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Oh fuck, I'm never get use to being stretched out like this."
        else:
            the_person.char "Oh... Oh fuck my ass!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Gah! Ah! Fuck!"
        else:
            the_person.char "God, I won't be able to sit for a week after this..."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:

            the_person.char "Give it to me, fuck my asshole raw!"
        else:
            the_person.char "Ah! Why does your cock have to be so fucking big?!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "Fuck, I can't believe I'm going to cum from your cock up my ass!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Wreck my ass [the_person.mc_title], send me back to my [so_title] gaping and ruined! Ah!"

                the_person.char "I might have a [so_title], but he doesn't drive me crazy like you do [the_person.mc_title]!"
                the_person.char "Make me cum my brains out! Screw my [so_title], he's not half the man you are!"
        else:
            the_person.char "Fuck, I can't believe it but I think I'm going to cum soon!"

    return

label wild_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh fuck yes, I'm going to cum! I'm cumming!"
    else:
        the_person.char "Oh fuck, you're going to make me cum! Fuck!"
        "She goes silent, then lets out a shuddering moan."
    return

label wild_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Fuck yes, I'm going to cum! Make me cum!"
    else:
        the_person.char "Oh my god, you're good at that! I'm going to... I'm going to cum!"
    return

label wild_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Ah! More! I'm going to... Ah! Cum! Fuck!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Oh god, I'm going to... Oh fuck me! Ah!"
    return

label wild_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
        the_person.char "Ah! Mmhmmm!"
    else:
        the_person.char "Oh fucking shit, I think you're going to make me..."
        "She barely finishes her sentence before her body is wracked with pleasure."
        the_person.char "Cum!"
    return

label wild_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "You think it will look good on me? I guess that's all I need to hear then."
    else:
        the_person.char "Hey, thanks. That's a good look, I like it."
    return

label wild_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. I appreciate the thought though."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Jesus, you didn't leave much to the imagination, did you? I don't think I can wear this."
        else:
            the_person.char "There's not much of an outfit to this outfit. Thanks for the thought, but there's no way I could wear this."
    return

label wild_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Oh man, I'm a mess. I'll be back in a moment, I'm just going to get cleaned up for you."
    else:
        if the_person.sluttiness > 40:
            the_person.char "I don't think everyone else would appreciate me going around dressed like this as much as you would. I'll be back in a second, I just want to get cleaned up."
        else:
            the_person.char "Damn, everything's out of place after that. Wait here a moment, I'm just going to find a mirror and try and look presentable."
    return

label wild_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Could we leave that where it is for now, please?"
    elif the_person.obedience < 70:
        the_person.char "No, no, no, I'll decide what comes off and when, okay?"
    else:
        the_person.char "Not yet... get me a little warmed up first, okay?"
    return

label wild_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person.char "Let's do it. Once you've had your fill I have a few ideas we could try out."
        else:
            the_person.char "I was hoping you would suggest that, just thinking about it gets me excited."
    else:
        the_person.char "You want to give it a try? Okay, let's try it."
    return

label wild_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "God, what have you done to me? I should say no, but... I just want you to use me however you want, [the_person.mc_title]."
    else:
        if the_person.obedience > 130:
            the_person.char "If that's what you want to do then I'll what you tell me to do."
        else:
            the_person.char "I shouldn't... but if you want to try it out I'm game. Try everything once, right?"
    return

label wild_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet [the_person.mc_title], get me warmed up first."
    else:
        the_person.char "Wait, I just... I don't think I'm ready for this. I want to fool around, but let's keep it casual."
    return

label wild_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "What? I have a [so_title], so you can forget about doing anything like that. Ever."
        "She glares at you, then walks away."
    elif the_person.sluttiness < 20:
        the_person.char "I'm sorry, what!? No, you've massively misread the situation, get the fuck away from me!"
        "[the_person.title] glares at you and steps back."
    else:
        the_person.char "What? That's fucking disgusting, I can't believe you'd even suggest that to me!"
        "[the_person.title] glares at you and steps back."
    return

label wild_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh, I think I know what you need right now. Let me take care of you."
        else:
            the_person.char "Right now? Okay, lead the way I guess."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you're feeling as horny as me then? Come on, let's go."
            "[the_person.title] takes your hand and leads you off to find some place out of the way."
        elif the_person.sluttiness > 10:
            the_person.char "I know that look you're giving me, I think I know what you want."
        else:
            the_person.char "[mc.name], I know what you mean... Okay, I can spare a few minutes."
    return

label wild_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "Alright, let's slip away for a few minutes and you can convince me a little more."
        elif the_person.sluttiness < 50:
            the_person.char "Come on, I know someplace nearby where we can get a few minutes privacy."
        else:
            the_person.char "Oh my god. I hope you aren't planning on making me wait [the_person.mc_title], because I don't know if I can!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "Fuck, let's get this party started!"
            the_person.char "I hope you don't mind that I've got a [so_title], because I sure as hell don't right now!"
        else:
            the_person.char "God damn it, you're bad for me [the_person.mc_title]... Come on, we need to go somewhere quiet so my [so_title] doesn't find out about this."
    return

label wild_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "Well, I think you deserve a chance to impress me."
        elif the_person.sluttiness < 50:
            the_person.char "Mmm, well let's get this party started and see where it goes."
        else:
            the_person.char "Fuck, I'm glad you're as horny as I am right now. Come on, I can't wait any more!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person.char "Fuck, you know how to turn me on in ways my [so_title] never can. Come here!"
        else:
            the_person.char "You're such bad news [the_person.mc_title]... I have a [so_title], but all I can ever think of is you!"
    return

label wild_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Sorry [the_person.mc_title], I'm not really in the mood to flirt or fool around."
        "[the_person.title] shrugs unapologetically."

    elif the_person.sluttiness < 50:
        the_person.char "I'll admit it, you're tempting me, but I'm not in the mood to fool around right now. Maybe some other time though, I think we could have a lot of fun together."

    else:
        the_person.char "Shit, that sounds like a lot of fun [the_person.mc_title], but I'm not feeling it right now. Hang onto that thought and we can fool around some other time."
    return

label wild_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "You know that all you have to do is ask and it's all yours."
        else:
            the_person.char "Thank you [the_person.mc_title], I'm glad you're enjoying the view."

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person.char "Then why don't you do something about it? Come on, we don't have to tell my [so_title] anything at all, right?"
            "[the_person.title] winks and spins around, giving you a full look at her body."
        else:
            the_person.char "You're playing with fire [the_person.mc_title]. I've got a [so_title], and I don't think he'd appreciate you flirting with me."
            mc.name "What about you, do you appreciate it?"
            "She gives a coy smiles and shrugs."
            the_person.char "Maybe I do."

    else:
        if the_person.sluttiness > 50:
            the_person.char "Then why don't you do something about it? Come on, all you have to do is ask."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person.char "Well thank you, play your cards right and maybe you'll get to see a little bit more."
            the_person.char "You'll have to really impress me though, I have high standards."
    return

label wild_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "What do you think? Is this a good look [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person.char "I hope you had a good time [the_person.mc_title]. It certainly seems like you did."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm that's such a good feeling. Do you think I look cute like this?."
            "[the_person.title] runs her tongue along her lips, then smiles and laughs."
        else:
            the_person.char "Whew, glad you got that over with. Take a good look while it lasts."
    return

label wild_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Mmm, thank you [the_person.mc_title]."
        else:
            "[the_person.title]'s face grimaces as she tastes your cum in her mouth."
            the_person.char "Ugh. There, all taken care of [the_person.mc_title]."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm, you taste great [the_person.mc_title]. Was it nice to watch me take your load in my mouth?"
        else:
            the_person.char "Ugh, that's such a... unique taste."
    return

label wild_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Oh god, it's so warm. If your condom broke it would all be inside me."
        else:
            the_person.char "Oh god, I hope you buy good condoms because that's a lot of cum."
            the_person.char "But then again, maybe you're dreaming of knocking me up."

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Fuck yes, pump that cum into me! I don't care if I get pregnant, I'll just tell my [so_title] that it's his!"

            else:
                the_person.char "Mmm, give me that baby batter, pump my pussy full of it! I'll worry about being pregnant later!"
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck. [the_person.mc_title], you can't cum inside me. My [so_title] would kill me if he found out I got pregnant."
                if the_person.kids > 0:
                    the_person.char "...Again."

            else:
                the_person.char "Oh fuck, [the_person.mc_title], you can't get me pregnant. Please, I don't want to do the whole \"single mother\" thing."
    return

label wild_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Mmm, pump my ass full of your hot cum!"
    else:
        the_person.char "Oh fuck, oh fuck!"
    return

label wild_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!", "God fucking dammit!", "Son of a bitch!", "Mother fucker!", "Whoah!"])
    the_person.char "[rando]"
    return

label wild_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I've got a ton of things I need to get to, could we talk some other time [the_person.mc_title]?"
    else:
        the_person.char "Hey, I'd love to chat but I have a million things to get done right now. Maybe later?"
    return

label wild_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "One sec, I want to take something off."
        else:
            the_person.char "Ah, I'm wearing way too much right now. One sec!"

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "Why do I bother wearing all this?"
        else:
            the_person.char "Wait, I want to get a little more naked for you."

    else:
        if the_person.arousal < 50:
            the_person.char "Give me a second, I'm going to strip something off just. For. You."
        else:
            the_person.char "Ugh let me get this off. I want to feel your pressed against every inch!"
    return

label wild_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Ugh, jesus you two. Get a room or something, nobody wants to see this."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person.char "Could you two at least keep it down? This is fucking ridiculous."
        $ the_person.change_happiness(-1)
        "[the_person.title] tries to avert her gaze and ignore you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "You're certainly feeling bold today [the_sex_person.name]. At least it looks like you're having a good time..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] watches for a moment, then turns away while you and [the_sex_person.name] keep [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh wow that's hot. You don't mind if I watch, do you?"
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Come on [the_person.mc_title], [the_sex_person.name] is going to fall asleep at this rate! You're going to have to give her a little more than that."
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
    return

label wild_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "Come on [the_person.mc_title], be rough with me. I can handle it!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "I bet she just wishes she was the one being [the_position.verb]ed you."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person.char "Oh god, you need to get a little of this yourself, [the_watcher.title]!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "[the_watcher.title], I'm giving him all I can right now. Any more and he's going to break me!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "Fuck, maybe we should go somewhere a little quieter..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Ah, now this is a party! Maybe when he's done you can tap in and take a turn [the_watcher.title]!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label wild_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room. She scoffs and turns back to her work."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person.char "Hey [the_person.mc_title], down here for business or pleasure?"
            "The smile she gives you tells you which one she's hoping for."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room."
            the_person.char "Hey [the_person.mc_title], it's nice to have you stop by. Let me know if you need anything!"

    else:
        if the_person.sluttiness > 60:
            "[the_person.title] walks over to you when you come into the room."
            the_person.char "Just the person I was hoping would stop by. I'm here if you need anything."
            "She winks and slides a hand down your chest, stomach, and finally your crotch."
            the_person.char "Anything at all."
        else:
            the_person.char "Hey [the_person.mc_title]. Need anything?"
    return

label wild_date_seduction(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
            else:
                the_person.char "You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
        else:
            if the_person.love > 40:
                the_person.char "Tonight's been amazing [the_person.mc_title], I just don't want to say goodbye. Do you want to come back to my place and have a few drinks?"
            else:
                the_person.char "This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "I've had a blast [the_person.mc_title], but I'm not done with you yet. Want to come back to my place?"
                the_person.char "My [so_title] won't be home until morning, so we would have plenty of time."
            else:
                the_person.char "This might be crazy, but do you want to come back to have another drink with me?"
                the_person.char "My [so_title] is stuck at work and I don't want to be left all alone."
        else:
            if the_person.love > 40:
                the_person.char "You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
                the_person.char "My [so_title] won't be home until morning, and we have a big bed you could help me warm up."
            else:
                the_person.char "This is crazy, but would you want to have one last drink at my place? My [so_title] won't be home until morning..."
    return

label wild_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're really done? Fuck [the_person.mc_title], I'm still so horny..."
            else:
                the_person.char "That's all you wanted? I was prepared to do so much more to you..."
        else:
            if the_person.arousal > 60:
                the_person.char "Fuck, I'm so horny... you're sure you're finished?"
            else:
                the_person.char "That was a little bit of fun, I suppose."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "[the_person.mc_title], you got me so turned on..."
            else:
                the_person.char "I hope you had a good time."
        else:
            if the_person.arousal > 60:
                the_person.char "Oh god, that was intense..."
            else:
                the_person.char "Done? Good, nice and quick."
    return


label wild_sex_take_control (the_person):
    if the_person.arousal > 60:
        the_person.char "Oh hell no, you can't just get me wet and then walk away!"
    else:
        the_person.char "Are you getting bored already? Get back here, we aren't done yet!"
    return

label wild_sex_beg_finish(the_person):
    "Wait [the_person.mc_title], I'm going to cum soon and I just really need this... I'll do anything for you, just let me cum!"
    return

## Role Specific Section ##
label wild_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] smiles mischievously."
    the_person.char "Well, I've got an idea in mind. It's risky, but I think it could really push our research to a new level."
    mc.name "Go on, I'm interested."
    the_person.char "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
    the_person.char "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
    return

# </editor-fold>

#################################
##### Introvert Personality #####
#################################
# <editor-fold
label introvert_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She freezes, then turns around slowly to face you."
    $ the_person.set_title("???")
    the_person.char "What do you want?"
    mc.name "I know this is sudden, but I just saw you walking by and I felt like I needed to say hi and get your name."
    "She glances around uncomfortably."
    the_person.char "Why? Why do you want to talk to me?"
    $ the_person.change_happiness(-1)
    mc.name "I don't know yet, but there's something about you that I just couldn't turn away from."
    "She seems nervous while she thinks for a second."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person.char "My name is [formatted_title]. Is that all you wanted to know?"
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    $ the_person.change_happiness(-2)
    mc.name "Well I wanted to introduce myself too..."
    return

label introvert_greetings(the_person):
    if the_person.love < 0:
        the_person.char "... What? Spit it out."
    elif the_person.happiness < 90:
        the_person.char "..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hello [the_person.mc_title]."
            else:
                the_person.char "Hey."
        else:
            if the_person.obedience > 130:
                the_person.char "Hello."
            else:
                "[the_person.title] gives you a nod."
    return

label introvert_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "That feels nice."
        else:
            "[the_person.title]'s breathing gets louder and heavier."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "That feels really nice... Ah..."
        else:
            "[the_person.possessive_title]'s face flushes with blood as she becomes more and more aroused."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "I feel so nice when you touch me like this..."
        else:
            "[the_person.title] closes her eyes and bites her lower lip. The only sound she makes is a low, sensual growl."
    else:
        if the_person.sluttiness > 50:
            the_person.char "I think I'm going to cum soon..."
        else:
            "[the_person.title] pants and moans, her body barely under her control."

    return

label introvert_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Your tongue feels so good..."
        else:
            "[the_person.title]'s breathing gets louder and heavier."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "That's it... that's what I want."
        else:
            "[the_person.possessive_title]'s face flushes with blood as you eat her out."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Oh, my pussy... It feels so good!"
        else:
            "[the_person.title] closes her eyes and bites her lower lip. The only sound she makes is a low, sensual growl."
    else:
        if the_person.sluttiness > 50:
            the_person.char "You are going to... Make me cum!"
        else:
            "[the_person.title] pants and moans, her body barely under her control."

    return

label introvert_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Your dick feels nice."
        else:
            "[the_person.title]'s breathing gets louder and heavier as you fuck her."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "You feel so big and warm..."
        else:
            "[the_person.possessive_title]'s face flushes with blood as she becomes more and more aroused."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, my pussy feels so good with your dick inside!"
        else:
            "[the_person.title] closes her eyes and bites her lower lip. The only sound she makes is a low, sensual growl."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Your dick is going to make cum if you keep going..."
        else:
            "[the_person.title] pants and moans, her body barely under her control."

    return

label introvert_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Gah!"
        else:
            "[the_person.title]'s breathing gets louder and heavier."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Ah... I'm so stretched out..."
        else:
            "[the_person.possessive_title]'s face flushes with blood as she struggles to take your cock."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Mmm. Fuck."
        else:
            "[the_person.title] closes her eyes and grunts."
    else:
        if the_person.sluttiness > 50:
            the_person.char "My ass... I'm about to cum!"
        else:
            "[the_person.title] pants and grunts, her body barely under her control."

    return

label introvert_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "... Mmmfh!"
        "She tenses up and moans to herself."
    else:
        the_person.char "I... I think I'm going to cum!"
    return

label introvert_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh fuck, I'm cumming!"
    else:
        the_person.char "Oh... Oh! {b}Oh!{/b}"
    return

label introvert_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I'm... Cumming!"
    else:
        the_person.char "Shit..."
    return

label introvert_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Your going to make me cum! Ah!"
    else:
        the_person.char "Oh fuck, I'm..."
        "She tenses up and moans loudly."
        the_person.char "Cumming!"
    return

label introvert_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "If you like it, sure."
    else:
        the_person.char "It looks okay, I guess."
    return

label introvert_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I don't really like it. Sorry."
        "[the_person.possessive_title] shrugs."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Other people would see me in this? No, I'm not wearing that."
        else:
            the_person.char "I don't like it."
            "[the_person.possessive_title] shrugs."
    return

label introvert_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "I need to get cleaned up."
    else:
        if the_person.sluttiness > 40:
            "[the_person.title] starts to get cleaned up and dressed."
        else:
            the_person.char "Don't look at me..."
            "[the_person.title] turns her back to you while she gets put back together."
    return

label introvert_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "No, don't take that off please."

    elif the_person.love < 10:
        "[the_person.title] grabs your hand to stop you."
        the_person.char "Keep dreaming."
    else:
        "[the_person.title] grabs your hand shakes her head."
    return

label introvert_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            "[the_person.title] shrugs and nods."
            the_person.char "Sure. Sounds like it could be fun."
        else:
            "[the_person.possessive_title] smiles and nods."
    else:
        "[the_person.title] shrugs and looks away nervously."
        if the_person.love < 0:
            the_person.char "With you? Ugh, I guess..."
        else:
            the_person.char "Sure, I guess."
    return

label introvert_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        "[the_person.possessive_title] seems nervous but nods."
        the_person.char "Okay."
    else:
        if the_person.obedience > 130:
            "[the_person.possessive_title] seems shocked, but nods meekly."
            the_person.char "Okay..."
        else:
            the_person.char "I guess I could give that a try..."
    return

label introvert_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        "[the_person.possessive_title] shakes her head."
        the_person.char "Let's do something else."
    else:
        "[the_person.possessive_title] shakes her head."
        the_person.char "Let's do something else. Something less serious."
    return

label introvert_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        "[the_person.possessive_title] seems shocked. She shakes her head quickly and looks away, refusing to meet your eyes."
        the_person.char "I have a [so_title]. No. Never."
    elif the_person.sluttiness < 20:
        "[the_person.possessive_title] seems shocked. She looks away and shakes her head, stepping away from you."
    else:
        "[the_person.possessive_title] shakes her head."
        the_person.char "No way, not even a chance. Ugh."
    return

label introvert_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title] bites her lip."
            the_person.char "Is that so?"
        else:
            the_person.char "Oh... I don't know what to say..."
    else:
        if the_person.sluttiness > 50:
            the_person.char "You too? Well..."
            "[the_person.title] bites her lip."
        elif the_person.sluttiness > 10:
            the_person.char "Oh... Really?"
        else:
            "[the_person.possessive_title] seems flustered and turns her head away."
            the_person.char "Oh, really? I don't... Ah, I don't even know what to say!"
    return

label introvert_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            "[the_person.possessive_title] glances around nervously."
            the_person.char "Fine. Let's get out of here."
        elif the_person.sluttiness < 50:
            "[the_person.possessive_title] glances around."
            the_person.char "Fine. Let's get out of here."
        else:
            "[the_person.possessive_title] glances around, blushing."
            the_person.char "Fine. Should we go somewhere else...?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            "[the_person.possessive_title] glances around at the people nearby."
            the_person.char "Fine. We need to go somewhere so my [so_title] doesn't find out."
        else:
            "[the_person.possessive_title] glances around, then nods meekly."
            the_person.char "My [so_title] can never find out. Never."
    return

label introvert_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person.char "I think... Okay."
        elif the_person.sluttiness < 50:
            "[the_person.possessive_title] bites her lip and nods her approval."
        else:
            "[the_person.possessive_title] eagerly nods her approval. She seems to blush in anticipation."
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            "[the_person.possessive_title] bites her lip."
            the_person.char "Don't tell my [so_title]."
        else:
            "[the_person.possessive_title] seems conflicted. Her face is flush in anticipation but she holds herself back."
            the_person.char "I have a [so_title]. He doesn't need to know, right?"
            mc.name "It's just me and you here. You have needs and he doesn't need to know a thing."
            "Her resistance falls away completely."
    return

label introvert_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        "[the_person.possessive_title] blushes and shakes her head."
        the_person.char "Not right now."

    elif the_person.sluttiness < 50:
        the_person.char "I... No, I don't think so."

    else:
        the_person.char "Hmm..."
        "[the_person.possessive_title] takes a long moment to make up her mind."
        the_person.char "No, I don't think so [the_person.mc_title]."
    return

label introvert_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "I was thinking of you when I put this on."
        else:
            "[the_person.title] smiles and shrugs."
            the_person.char "Actions speak louder than words."
    else:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title] puts her hands behind her back and rocks her hips left and right."
        else:
            "[the_person.title] blushes and looks away."
            the_person.char "Oh... I... ah... Thanks."
    return

label introvert_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            "[the_person.title] looks you in the eye, then runs her tongue over her lips seductively."
        else:
            "[the_person.title] wipes some of your cum off her face with the back of her hand."
    return

label introvert_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Mmm. Thank you."
        else:
            the_person.char "Mmm."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm, you taste great."
        else:
            the_person.char "Ugh."
    return

label introvert_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "There's so much cum... Wow."
        else:
            the_person.char "Do you always cum this much?"

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Mmmm, I like having your cum in me. It's almost worth having to explain to my [so_title] how I got pregnant."

            else:
                the_person.char "How easily do you think I'd get pregnant? Maybe you just did."
                "She sighs and shrugs."
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh shit, wait, what if I get pregnant?"
                the_person.char "I would have to explain to my [so_title] how I got pregnant. I don't want to have to do that!"

            else:
                the_person.char "Uh, please try not to get me pregnant, okay?"
    return

label introvert_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Cum inside of me, I want it!"
    else:
        the_person.char "Ah!"
    return

label introvert_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Dicks!", "Fuck me!","Ah! Oh fuck!", "Ah!", "Holy shit!", "Fucking shit!", "God fucking dammit!", "Son of a bitch!", "Mother fucker!"])
    the_person.char "[rando]"
    return

label introvert_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I'm busy right now. Can we talk later?"
    else:
        the_person.char "Huh? Sorry, I can't talk right now."
    return

label introvert_sex_strip(the_person):
    #TODO: See if this sounds right with them just not saying anything (strong silent type)
    # if the_person.sluttiness < 20:
    #     if the_person.arousal < 50:
    #         the_person.char "One sec, I want to take something off."
    #     else:
    #         the_person.char "Ah, I'm wearing way too much right now. One sec!"
    #
    # elif the_person.sluttiness < 60:
    #     if the_person.arousal < 50:
    #         the_person.char "Why do I bother wearing all this?"
    #     else:
    #         the_person.char "Wait, I want to get a little more naked for you."
    #
    # else:
    #     if the_person.arousal < 50:
    #         the_person.char "Give me a second, I'm going to strip something off just. For. You."
    #     else:
    #         the_person.char "Ugh let me get this off. I want to feel your pressed against every inch!"
    return

label introvert_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "What the fuck..."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-3)
        "[the_person.title] shakes her head while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person.char "Right here? Really?"
        $ the_person.change_happiness(-1)
        "[the_person.title] rolls her eyes and tries to avert her gaze as you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "Right in front of me? Really?"
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] watches for a moment, then turns away while you and [the_sex_person.name] keep [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] blushes, watching you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        # the_person.char "Come on [the_person.mc_title], [the_sex_person.name] is going to fall asleep at this rate! You're going to have to give her a little more than that."
        "[the_person.title] watches excitedly while you and [the_sex_person.name] [the_position.verb]. She whispers under her breath, almost to herself."
        the_person.char "Come on, give it to her. Harder..."
    return

label introvert_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "[the_person.mc_title], I want more!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Just focus on me. Just me."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person.char "Did you know how good this feels [the_watcher.title]?"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        $ the_person.change_arousal(1)
        "[the_person.title] doesn't say anything, but she seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "We should go somewhere quiet..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        "[the_person.possessive_title] glances between you and [the_watcher.title]."
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label introvert_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] glances at you when you enter the room. She promptly ignores you and turns back to her work."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            "[the_person.title] looks up at you, blushes, then looks away."
        else:
            "[the_person.title] looks up from her work and gives you a quick nod."

    else:
        if the_person.sluttiness > 60:
            "[the_person.title] looks up briefly from her work. She bites her lip and winks."
        else:
            "[the_person.title] doesn't notice you come in and stays focused on her work."
    return

label introvert_date_seduction(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "I want you to come home with me. Want to come?"
            else:
                the_person.char "I don't normally do this. Do you want to come home with me?"
        else:
            if the_person.love > 40:
                "[the_person.title] stays close to you, before touching your arm to get your attention."
                the_person.char "I had a really good time. I... was wondering if you wanted to come home with me..."
            else:
                "[the_person.title] wrings her hands together nervously, as if working up the courage to speak."
                the_person.char "I like you, and I want you to come home with me so I don't have to say goodbye. Do you... want to?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person.char "My [so_title] isn't around. Do you want to come home with me?"
            else:
                the_person.char "I know my [so_title] wouldn't like this, but do you want to come home with me? He won't be around."
        else:
            if the_person.love > 40:
                "[the_person.title] stays close to you, before touching your arm to get your attention."
                the_person.char "My [so_title] is never around. Do you want to come home with me? I would be happy if you did..."
            else:
                "[the_person.title] wrings her hands together nervously, as if working up the courage to speak."
                the_person.char "I really like you. I have a [so_title], but I want to spend more time with you too."
                the_person.char "Do you... want to come home with me? He won't be around."
    return

label introvert_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're done? I was hoping you'd at least help me cum."
            else:
                the_person.char "All done? I thought this was going somewhere."
        else:
            if the_person.arousal > 60:
                the_person.char "Fuck, I was hoping you'd make me cum."
            else:
                "[the_person.title] stays silent but seems disappointed that you're finishing up early."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "Done? I hope it wasn't something I did, I was having a really good time..."
            else:
                the_person.char "Done? I hope it wasn't something I did wrong."
        else:
            if the_person.arousal > 60:
                "[the_person.title] stays silent, but her cheeks are flush and her breathing is heavier than normal."
            else:
                "[the_person.title] stays silent but seems glad that you're finishing up early."
    return


label introvert_sex_take_control (the_person):
    if the_person.arousal > 60:
        "[the_person.title] grabs your arm and moans aggressively."
        the_person.char "No, I'm not done yet!"
    else:
        the_person.char "You're staying here, I was just getting started!"
    return

label introvert_sex_beg_finish(the_person):
    "[the_person.title] grabs your arm and moans desperately."
    the_person.char "No, please I'm so close to cumming! I... I need you to keep going!"
    return

## Role Specific Section ##
label introvert_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    "[the_person.title] nods and listens."
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] thinks about it, then nods again."
    the_person.char "Well, I may have an idea. I think it could lead to a breakthrough."
    mc.name "Go on."
    the_person.char "Our testing procedures focus on human safety. If we put that to the side we could gain much more information about the subjective effects of our serum."
    the_person.char "I want to do is take a dose of our serum myself. I would need you to record me and ask me some questions."
    return

# </editor-fold>

###############################
###### Bimbo Personality ######
###############################
# <editor-fold
label bimbo_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around at you. She doesn't hide the way she looks your body up and down."
    $ the_person.set_title("???")
    the_person.char "Oh you're cute! Okay, cutie, what do you need?"
    mc.name "I just wanted to get your name. I saw you walking past and..."
    $ title_choice = get_random_title(the_person)
    $ formatted_title = the_person.create_formatted_title(title_choice)
    if the_person.has_large_tits():
        the_person.char "And you liked my tits? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    else:
        the_person.char "And you liked my ass? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    #the_person.char "Well then, I suppose I shouldn't disappoint you. You can call me [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(get_random_possessive_title(the_person))
    the_person.char "So what's your name?"
    return

label bimbo_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Oh, my, god... What do you want? Do I look like I want to be talking to you?"
    elif the_person.happiness < 90:
        the_person.char "Hi [the_person.mc_title]..."
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 130:
                the_person.char "Hey there [the_person.mc_title]. I mean sir! Hey there, sir!"
            else:
                the_person.char "Hey [the_person.mc_title], what are you doing here? Can I help with anything? Anything at all?"
        else:
            if the_person.obedience > 130:
                the_person.char "Hi there [the_person.mc_title], what can I do for you?"
            else:
                the_person.char "Hi there [the_person.mc_title]!"
    return

label bimbo_sex_responses_foreplay(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know just how to touch me [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly while you touch her."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Do you like touching me [the_person.mc_title]? I know I like it when you do!"
        else:
            the_person.char "Do you like touching me [the_person.mc_title]? You seem to know exactly what to do."

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! That feels really nice!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char " Mmm, you're driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better you feel when you touch me!"
                the_person.char "Make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, I might cum if you keep touching me like that!"
    return

label bimbo_sex_responses_oral(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Aww, you always know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Does my pussy taste good [the_person.mc_title]? I'll repay the favour suck your cock later!"
        else:
            the_person.char "That, like, feels so good [the_person.mc_title]!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Ah! Hehe, that's feels so good!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char "Oh wow! Mmmm, you're tongue is, like, driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum with your mouth! Make me cum, please!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better you make me feel!"
                the_person.char "He never licks my pussy though, so make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep licking my pussy like that!"
    return

label bimbo_sex_responses_vaginal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "Mmm, you know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Is your cock always this big, or are you just happy to see me? Hehe!"
        else:
            the_person.char "Am I your dirty girl [the_person.mc_title]? Because I'm having so much fun right now!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "Yes! Keep fucking me!"
            "She giggles happily, clearly having a good time."
        else:
            the_person.char "Oh wow! Mmmm, you're cock is driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew how much better your cock feels!"
                the_person.char "Oh well, I just want to cum! Make me cum! Make me cum my brains out!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep going!"
    return

label bimbo_sex_responses_anal(the_person):
    if the_person.arousal < 25:
        if the_person.sluttiness > 50:
            the_person.char "I can, like, feel every single inch of you in me! You're so big!"
        else:
            the_person.char "You're, like, {i}huge{/i} inside of me! I don't know if I can do this for very long!"

    elif the_person.arousal < 50:
        if the_person.sluttiness > 50:
            the_person.char "Fuck my ass [the_person.mc_title], fuck me it's raw and you're done with me!"
        else:
            the_person.char "Oh, it feels like you're stirring up my insides with your dick! Ah!"

    elif the_person.arousal < 75:
        if the_person.sluttiness > 50:
            the_person.char "I'm so stretched out, I think I'm starting to get the hang of this!"
            "She giggles happily, clearly proud of her accomplishment."
        else:
            the_person.char "My mind is going blank, all I can think about is your cock inside of me!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person.char "I can, like, feel it happening! Fuck my ass and make me cum [the_person.mc_title]! Do it!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh fuck! My [so_title] would be so pissed if he knew I was letting you anal me."
                the_person.char "He's been begging for it for {i}months{/i}, but I just know he wouldn't feel nearly as good inside me as you do!"

        else:
            the_person.char "Oh my god, you're... You might make me cum if you keep fucking my ass! Please make me cum!"
    return

label bimbo_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh god, I'm going to cum! All I want to do is cum [the_person.mc_title], ah!"
        "She squeals with pleasure and excitement."
    else:
        the_person.char "Oh my god, this feeling. I'm... I'm... cumming!"

    return

label bimbo_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god, make me cum [the_person.mc_title]! My mind is going blank, I just need to cum!"
    else:
        the_person.char "That feels, like, {i}so good{/i}!"
        "She closes her eyes and squeals with pleasure."
    return

label bimbo_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god I'm going to cum! Ahh, make me cum [the_person.mc_title], it's all I want right now!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person.char "Yes, yes, yes! Make me cum! Make me cum hard!"
    return

label bimbo_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh my god! I'm going to cum with your cock up my ass!"
        "She squeals loudly."
    else:
        the_person.char "Oh my god! I'm such a slut, I'm about to cum! Oh fuck!"

    return

label bimbo_clothing_accept(the_person):
    if the_person.obedience > 130:
        the_person.char "Oh that's cute! You have such a good sense of style [the_person.mc_title], this is just what I like to wear!"
    else:
        the_person.char "It's so cute! I love getting new clothes - you should see my closet at home, there's no such thing as too many shoes, right?"
    return

label bimbo_clothing_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Uh... I don't think I'm allowed to wear that. I really wish I could though, just for you!"
    else:
        if the_person.sluttiness > 60:
            the_person.char "That's not really an outfit, is it? I like something a little cuter - some heels, add a dash of pink, and a top to show off my tits!"
            "[the_person.title] looks the outfit over again for a moment and shakes her head."
            the_person.char "Yeah, this just isn't going to do it. Thanks for the thought though!"
        else:
            the_person.char "Aww, I don't think I could ever wear something like that! I wish I could though, could you imagine the looks I would get? It would be. So. Hot."
    return

label bimbo_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Hehe, you really made a mess of me. I should go get tidied up, I'm suppose to be a proper lady here!"
    else:
        if the_person.sluttiness > 40:
            "[the_person.title] looks down at herself and giggles."
            the_person.char "Hehe, I'm all messed up after that! I need to go sort this out, this outfit just doesn't work right now!"
        else:
            the_person.char "Oh darn, my outfit's all confuzzled! I'm going to go fix this up, I'll be back before you know it!"
    return

label bimbo_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "Don't you think I look cuter with it on? Leave it alone for now, okay?"
    elif the_person.obedience < 70:
        the_person.char "Oh no-no-no, I'm going to decide when that comes off. I want to see you work for it!"
    else:
        "[the_person.title] giggles and bats your hand away playfully."
        the_person.char "Not yet, there's so much fun stuff we have to do first!"
    return

label bimbo_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person.char "Oh yeah, that's one of my favorite things to do! Come on, let's do it!"
        else:
            the_person.char "Yeah, let's do it! You're so cute when you're horny, did you know that?"
    else:
        the_person.char "Oh? Oh! Yeah, lets do that!"
    return

label bimbo_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Wow that's a... does that even work? I thought... well I guess I should try it before I knock it!"
    else:
        if the_person.obedience > 130:
            the_person.char "If that's what you want, boss man, that's what you'll get!"
        else:
            the_person.char "You bring out the worst in me, you know that [the_person.mc_title]? I was a nice, respectable girl before you showed up!"
    return

label bimbo_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "No, no, no, not yet. I want you to make me wait for it a little bit, get me really begging for it."
    else:
        the_person.char "Uh, I don't think that sounds fun. Let's do something else. Come on, you pick!"
    return

label bimbo_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person.char "What? I have a [so_title], and he treats me so much better than you could EVER hope to. Understood?"
        "She rolls her eyes dramatically and walks away."
        the_person.char "Perv."
    elif the_person.sluttiness < 20:
        the_person.char "Uh, what the ACTUAL FUCK?! What do you think you're doing? Just saying that must be... illegal, or something!"
        "[the_person.title] glares at you you and walks away."
    else:
        the_person.char "Eew! No, no, no! I will NEVER do that with ANYONE! Eew!"
        "[the_person.title] shakes her head and walks away."
    return

label bimbo_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh yay, I know how to deal with this! You just relax and I'll make you feel very, very good!"
        else:
            the_person.char "All I can think about is that cute little dress I saw this morning. Oh, that's not you meant, was it..."
            "[the_person.title] giggles."
            the_person.char "Nevermind, lead the way!"
    else:
        if the_person.sluttiness > 50:
            the_person.char "Yay! I was getting so horny that I was ready to jump you in the hall!"
        elif the_person.sluttiness > 10:
            the_person.char "Hehe, I thought you had the that look in your eye. I have a sixth sense, but it's for horny guys instead of ghosts!"
        else:
            the_person.char "Oh, I don't really know what to say [the_person.mc_title]..."
    return

label bimbo_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Just make it an official order and it's all yours, boss man."
        else:
            the_person.char "Hehe, thank you, you're way too nice to me!"

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person.char "That's like, super hot to hear you say. We just can't let my [so_title] or he would flip out."
        else:
            the_person.char "Oh my god, you're so cute! My [so_title] never says things like that to me."
            "She pouts for a moment before returning to her bubbly self."

    else:
        if the_person.sluttiness > 50:
            the_person.char "You should try your luck sometimes. Maybe take me out for a drink, I get wild after I've had a few. Wild-er, I guess."
        else:
            the_person.char "Oh you, stop it! You're going to make me blush!"
    return

label bimbo_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Do I look cute covered in your cum, [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person.char "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
        else:
            the_person.char "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label bimbo_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person.char "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person.char "Bleh, I don't know if I'll ever get use to that."
    return

label bimbo_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "That condom is so stretchy! I can feel how much cum you put into it and it's, like, a lot!"
        else:
            the_person.char "Mmm, your cum is so nice and hot!"

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person.char "Oh well, my [so_title] will just take care of it, so that doesn't matter!"
            else:
                the_person.char "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person.char "Oh well, it's worth it to feel like this!"
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Oh, that's so hot... But wait, if I get pregnant what do I tell my [so_title]?"
                "She bites her lip and looks worried."
                the_person.char "We shouldn't do this too often. Next time you can cum somewhere else, okay?"
            else:
                the_person.char "Oh, that's so hot... But what do I do if I get pregnant?"
                "She bites her lip and looks worried."
                the_person.char "We shouldn't do this too often, okay? Next time you can cum, like, somewhere else, right?"
    return

label bimbo_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Give me your cum! I want you to cum in my ass! Ah!"
    else:
        the_person.char "Oh! Fuck, I hope there's room for all your cum!"
    return

label bimbo_suprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
    the_person.char "[rando]"
    return

label bimbo_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "Hi, I'm like, really sorry but I have way more stuff than you can imagine that I have to get done right now. Could we catch up later?"
    else:
        the_person.char "Hey, I'm sorry but I'm just suuuper busy right now! Hit me up later though, I'd love to chat once I get all this stupid work done!"
    return

label bimbo_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "Oh wait, I know what you want to see more of..."
        else:
            the_person.char "Ugh, all this clothing is getting in the way!"

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "I spent so much time this morning picking out this outfit, but I think you'd enjoy it more if I took it off, right?"
        else:
            the_person.char "Ah... I need to get all of this silly stuff off of me!"

    else:
        if the_person.arousal < 50:
            the_person.char "Teehee, just wait a moment and I'll strip this off for you..."
        else:
            the_person.char "Oh my god, let me strip for you [the_person.mc_title], let me be your slutty stripper!"

    return

label bimbo_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Is that, like, allowed? I thought that was illegal or something. Ugh."
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person.char "Could you two get a room or something? There are some of us here who are trying to focus and you're being very distracting."
        $ the_person.change_happiness(-1)
        "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "Wow [the_sex_person.name] you're so adventurous, I don't think I could ever do that. But it looks, like, super fun!"
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh. My. God. That is so fucking hot... Keep it up girl, you're doing great!"
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Mmm, come on [the_person.mc_title], you should do something more to her. I bet she wants it real bad. I know I do..."
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."
    return

label bimbo_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label bimbo_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] looks at you, pouts, then looks back at her work."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 40:
            "[the_person.title] looks at you when you enter the room and smiles."
            the_person.char "[the_person.mc_title]! I'm so glad you're stopping by, I've been so bored without you."
            "She pouts at you, eyes running up and down your body shamelessly."
            the_person.char "I hope you're here for something fun!"
        else:
            "[the_person.title] looks up from her work when you come into the room and smiles."
            the_person.char "[the_person.mc_title]! It's so good to see you! I've been having, like, the best day!"

    else:
        if the_person.obedience < 100:
            the_person.char "Hi [the_person.mc_title]! Do you need anything, any way I can help you?"
        else:
            the_person.char "Hi [the_person.mc_title]! Duh, I mean sir! Hi sir!"
            "[the_person.title] sticks out her tongue, then smiles and turns back to her work."

    return

label bimbo_date_seduction(the_person):
    if the_person.sluttiness > the_person.love:
        if the_person.sluttiness > 40:
            the_person.char "So [the_person.mc_title], don't you think it's time you came back home with me and we had some real fun?"
            "[the_person.title] bites her lip and puffs out her chest just a little bit."

        else:
            the_person.char "[the_person.mc_title], I swear you're driving me crazy. Do you, like, want to come home with me and just get wild?"

    else:
        if the_person.love > 40:
            the_person.char "[the_person.mc_title], I don't know how you do it but I swear you've been driving me, like, totally crazy all night."
            "[the_person.title] runs her hand along your arm and giggles."
            the_person.char "I want you to come back to my place so I can have you all to my self."
        else:
            the_person.char "Oh my god [the_person.mc_title], tonight has been so much fun. Do you want to, like, come back home with me and drink some more?"
    return

label bimbo_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "Aww darling, I was just getting close to cumming and you're done?!"
            else:
                the_person.char "That's all? Aww, I hope you had a good time with me..."
        else:
            if the_person.arousal > 60:
                "Wait, you're stopping? Aren't crazy horny right now too?"
            else:
                the_person.char "Don't you want to play with me any more? Oh well, your loss."

    else:
        if the_person.love > 40:
            if the_person.arousal > 60:
                the_person.char "You're actually done? But weren't you, like, having fun? I'm so fucking horny now..."
            else:
                the_person.char "Is that all you wanted to do? I thought guys had to, like, cum or it hurt."
        else:
            if the_person.arousal > 60:
                the_person.char "Aww, I was just getting getting warmed up!"

            else:
                the_person.char "That's it? Well, I guess that was a fun time well it lasted."
    return

## Role Specific Section ##
label bimbo_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] nods happily."
    "There's a long pause."
    mc.name "Do you know what to do?"
    the_person.char "Uh, duh! Look into the serum-stuff we make and make it better-er!"
    mc.name "Right, and do you have any idea how to actually do that?"
    "[the_person.title]'s eyebrows knit together as she tries to think."
    the_person.char "Uhm... not yet but... what if..."
    "You imagine you can see the little hamster in her head running as fast as it can."
    the_person.char "I've got it! What if you test it on me!"
    mc.name "Do you think that's a good idea!"
    the_person.char "Duh, that's why I thought of it! Come on, how bad could it be? Just let me try it! Record it or something and I'll tell you what it feels like!"
    return

# </editor-fold>

############################
#### Unique - Stephanie ####
############################
# <editor-fold
label stephanie_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Ugh... What do you need? Can we make this quick?"
    elif the_person.happiness < 90:
        the_person.char "Hey, hope you're having a better day than me. What's up?"
    else:
        if the_person.obedience > 130:
            if the_person.sluttiness > 60:
                the_person.char "Good to see you [the_person.mc_title], I hope you're here to see me about something fun."
            else:
                the_person.char "Good to see you [the_person.mc_title], how can I help?"
        else:
            if the_person.sluttiness > 60:
                the_person.char "Hey [the_person.mc_title], are you here for business or pleasure?"
                "[the_person.title] smiles playfully."
            else:
                "Hey [the_person.mc_title], what's up?"
    return

label stephanie_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Mmm, that feels nice. I bet it would feel even nicer in my mouth next time, [the_person.mc_title]."
        else:
            the_person.char "There we go, all taken care of. You can cum in my mouth next time if you want, it would make cleaning up a lot faster."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Aww, you should shoot it into my mouth next time. I love how your hot cum tastes."
            "[the_person.title] runs a finger through a puddle of your cum and then licks it clean, winking at you while she does."
        else:
            the_person.char "Oh man, you really got me covered, didn't you. I wish you would just cum in my mouth so I don't have to worry about getting cleaned up."
    return

label stephanie_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Oh god, you taste so good. Thank you for the treat [the_person.mc_title]."
        else:
            the_person.char "Mmm, thank you [the_person.mc_title]."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm, your cum tastes so great [the_person.mc_title], are you sure there isn't any more of it for me?"
            "[the_person.title] licks her lips and sighs happily."
        else:
            "[the_person.title] licks her lips and smiles at you."
            the_person.char "Mmm, that was nice."
    return

# label stephanie_cum_vagina(the_person):
#     #TODO
#     return
#
# label stephanie_cum_anal(the_person):
#     #TODO
#     return

label stephanie_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person.char "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes you and I have from our days at the lab. I wanted to ask if you think there's more we could be doing."
    "[the_person.title] smiles mischievously."
    the_person.char "I've got an idea then, I'm sure it's something you'll like."
    mc.name "What's your plan?"
    the_person.char "All of the testing that I've been doing so far focuses on not getting people killed, which is important, but I really need to know more about what subjective effects there are."
    the_person.char "I want to take a dose of serum myself and have you record the effects. You can ask me a few questions, gauge how much it affects me."
    mc.name "Do you think that's a good idea?"
    the_person.char "Nora would never let me do it, but that's why I work for you now and not for her. Come on [the_person.mc_title], this is chance to do real, proper science!"
    return

label stephanie_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "Ugh I've started to dress like Nora. Let me take some of this off."
        else:
            the_person.char "Is it getting warm in here? I need to take something off."

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "You saw more of me back at the lab, I think I can lose a little more clothing, don't you?"
        else:
            the_person.char "One second, let me take some of this off for you. Feel free to watch."

    else:
        if the_person.arousal < 50:
            the_person.char "Ugh, fuck this stupid outfit. I hope you don't mind if I take it off."
        else:
            the_person.char "Wait, I need to take this off, I want to feel you against me."

    return

# </editor-fold>

#######################
#### Unique - Lily ####
#######################
# <editor-fold

label lily_greetings(the_person):
    if the_person.love < 0:
        the_person.char "Ugh, can you tell Mom whatever you want to say to me right now? I don't want to hear it."
    elif the_person.happiness < 90:
        the_person.char "Hey [the_person.mc_title]..."
    else:
        if the_person.obedience > 130:
            if the_person.sluttiness > 60:
                the_person.char "Hey [the_person.mc_title], do you need your little sister for something?"
                "[the_person.title] crosses her arms behind her back."
            else:
                the_person.char "Hi [the_person.mc_title]."
        else:
            if the_person.sluttiness > 60:
                the_person.char "Oh hey [the_person.mc_title], I was just thinking about you."
                "[the_person.title] smiles playfully."
            else:
                the_person.char "Hey, need something?"
    return

label lily_clothing_accept(the_person):
    if the_person.obedience > 140:
        the_person.char "You're right, that looks cute! I'm glad I've got a brother with good fashion sense!"
    else:
        the_person.char "You think this would look good on me? I'll keep that in mind!"
    return

label lily_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person.char "Oh, I wish I could wear this [the_person.mc_title], but I don't think I could ever explain it to Mom if she saw."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Oh my god [the_person.mc_title]... It's hot, but there's no way I could ever actually wear it!"
        else:
            the_person.char "Oh my god [the_person.mc_title], you perv. There's no way I'm going to wear something like that!"
    return

label lily_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "Sorry [the_person.mc_title], I should really get myself dressed properly again! Just a second!"
    else:
        if the_person.sluttiness > 50:
            the_person.char "You shouldn't be looking at your sister like that [the_person.mc_title]. I'll get dressed so you won't be so distracted."
        else:
            the_person.char "Oh my god, I shouldn't be dressed like this around my own brother. Just... Just look away and give me a moment."
    return

label lily_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I wish I could let you, but I don't think I should be taking that off in front of my brother."
    elif the_person.obedience < 70:
        the_person.char "Sorry [the_person.mc_title], your little sister likes being a tease. I want to leave that on for a bit."
    else:
        the_person.char "I couldn't take that off in front of you [the_person.mc_title]. You're my brother, I'd die of embarrassment!"
    return

label lily_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            the_person.char "You're definitely my brother, I was thinking the same thing."
        else:
            the_person.char "You want to do that with your little sister [the_person.mc_title]? Well, you're lucky I'm just as perverted."
    else:
        the_person.char "Okay, let's do it. Just make sure Mom never finds out, okay?"
    return

label lily_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Oh god [the_person.mc_title], I know I shouldn't... We shouldn't be doing any of this together."
        the_person.char "But I just can't say no to you."
    else:
        if the_person.obedience > 130:
            the_person.char "If that's what my big brother needs me to do..."
        else:
            the_person.char "How do I keep letting you talk me into this? You're my brother for Gods sake..."
            "She seems conflicted for a second."
            the_person.char "Okay, just promise me Mom will never know."
    return

label lily_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet, I need to get warmed up first. Let's start out with something a little more tame."
    else:
        the_person.char "I... we can't do that [the_person.mc_title]. I'm your sister; there are lines we just shouldn't cross."
    return

label lily_sex_angry_reject(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Oh my god, what? I'm your sister you fucking pervert, how could you even talk about that to me?"
        the_person.char "Even if you're joking that's just... it's just fucked up, okay?"
    else:
        the_person.char "What the fuck [the_person.mc_title], I'm your sister! How could you think that's okay?"
        the_person.char "I... Just get out of here. You're lucky I don't want to have to explain how this happened to Mom."
    return

label lily_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "What's up [the_person.mc_title]? Do you need your little sister to pay attention to you?"
        else:
            the_person.char "What're you thinking about? You look like you're up to something."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Do you have something in mind for your innocent little sister?"
        elif the_person.sluttiness > 10:
            the_person.char "What do you mean [the_person.mc_title]? Do you want to do something together?"
        else:
            the_person.char "I... what do you mean [the_person.mc_title]?"
    return

label lily_seduction_accept_crowded(the_person):
    if the_person.sluttiness < 20:
        "[the_person.title] grabs your arm and blushes."
        the_person.char "Oh my god, you can't say things like that when there are other people around [the_person.mc_title]! let's at least find someplace quiet."

    elif the_person.sluttiness < 50:
        the_person.char "I... I mean, we shouldn't do anything like that when there are other people around. What would we do if people found out what we do together?"

    else:
        the_person.char "Oh god, that sounds so hot. I hope nobody here recognizes me!"
    return

label lily_seduction_accept_alone(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Let's just make sure nobody finds out, okay? I mean, what would my friends think if I was doing... stuff with my brother?"
    elif the_person.sluttiness < 50:
        the_person.char "I know we shouldn't, but there's nobody around to know, right? So what's the harm..."
    else:
        the_person.char "God, you're such a pervert [the_person.mc_title], taking advantage of your poor, innocent sister..."
        "[the_person.title] winks at you and holds onto your arm."
    return

label lily_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Ugh, I'm your sister [the_person.mc_title], how could you even suggest that? Gross..."

    elif the_person.sluttiness < 50:
        the_person.char "No, wait, we really shouldn't be doing this [the_person.mc_title]... What if Mom knew, or my friends knew?"
        the_person.char "It would be so embarrassing if they found out what we do sometimes."

    else:
        the_person.char "I'm sorry [the_person.mc_title], but I just don't feel like fooling around today, okay? I'm sure I'll find a way to make it up to you later."
    return

label lily_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "I know you're my brother, but it's still really hot to hear you say that."
        else:
            the_person.char "Stop it [the_person.mc_title], you're my brother and I know you're just flattering me."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Don't forget I'm your sister [the_person.mc_title], don't get too carried away. But I guess looking doesn't hurt, right?"
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person.char "Are you really checking me out? I'm your sister [the_person.mc_title], that's a little weird."
            the_person.char "But, uh... it's still nice to hear."
    return

label lily_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Oh wow, you really covered me. Do I look cute like this bro?"
        else:
            the_person.char "Oh my god, you got it all over me... You can never let Mom know about this, okay?"
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm, it feels so warm. I know it's wrong but I love being covered in your cum."
        else:
            the_person.char "Oh my god... what are we doing [the_person.mc_title], we shouldn't be doing this..."
    return

label lily_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Wow, you really needed that... I guess that's why you need a sister like me."
        else:
            the_person.char "Oh my god... Mom can never know about this [the_person.mc_title]. She'd kill us both."
    else:
        if the_person.sluttiness > 80:
            the_person.char "Mmm, who knew my brother had such good tasting cum... If I had known I would have done this with you way earlier!"
        else:
            the_person.char "I... I can't believe we just did that. We really shouldn't do it again, okay?"
    return

label lily_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Fill up that condom [the_person.mc_title], it's so close to being inside me!"
            "The thought seems to be turning her on."
        else:
            the_person.char "Oh fuck, good thing you've got a condom on. I mean, could you imagine if you had put all of that into your own sister?"

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "I know I shouldn't, but I love having my own brother's cum inside me."
                the_person.char "I guess if I you get me pregnant I'll have to say it's my [so_title]'s though, so people don't judge us."
            else:
                the_person.char "Pump me full of your hot cum, I don't care that you're my brother, I want you to get me pregnant!"
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person.char "Fuck, fuck! You can't cum in me, what if you got me pregnant? What would Mom say?"
                the_person.char "What would my [so_title] say? I don't know if I could lie to him."
            else:
                the_person.char "Oh god no, you can't cum inside me! What would I do if my own brother got me pregnant?"
                the_person.char "I'd die of embarrassment if people found out!"
    return

label lily_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Fill me up!"
    else:
        the_person.char "Oh fuck, my brother's cumming into my ass..."
        "She doesn't seem very upset by the idea."
    return

label lily_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "I feel like Mom in this outfit. One second..."
        else:
            the_person.char "Oh god, I can't believe you're making me feel this way [the_person.mc_title]."

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "I'm just going to take this off. It's nothing you haven't seen before anyways..."
        else:
            the_person.char "I know it's wrong for me to feel this way about your brother..."
            "She pauses for a second, as if gathering her confidence."
            the_person.char "But I really want to get naked right now."

    else:
        if the_person.arousal < 50:
            the_person.char "I bet you want to see more of your little sister, right? God [the_person.mc_title], you're so bad."
        else:
            the_person.char "Oh my god, I can't keep this on any longer!"

    return

label lily_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "Hey, I'd love to catch up with my big brother but I've got some work to get done. Could we chat later?"
    else:
        the_person.char "Sorry [the_person.mc_title], but I've got a ton of school work to get done. We'll have to chat later."
    return

label lily_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "Oh my god, [the_person.mc_title]! How can you do that in front of your sister?"
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        $ the_person.change_happiness(-1)
        the_person.char "I... oh my god I can't believe you're my brother..."
        "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "Oh my god, you two are just... Wow..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.possessive_title] averts her gaze, but she keeps stealing glances while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Oh my god, [the_person.mc_title], where did you learn to do that? I shouldn't be watching this, but..."
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Give it to her [the_person.mc_title], don't hold back just because I'm here."
        the_person.char "You're not nervous because your sister is watching, are you?"
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."

    return

label lily_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can play rough with your little sister."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.title], I'm having a great time. She's just jealous her brother doesn't treat her like this!"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person.char "We just love each other so much [the_watcher.title]. You understand, right?"
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh [the_person.mc_title], I know it's be wrong but being with you just feels so right!"
        $ the_person.change_arousal(1)
        "Your little sister seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], we shouldn't be doing this here. What if people talk?"
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "[the_watcher.title], I'm so glad you don't think this is too weird."
        the_person.char "I know it's suppose to be wrong, but then why does it feel so good?"
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label lily_date_seduction(the_person):
    if the_person.sluttiness > the_person.love:
        if the_person.sluttiness > 40:
            the_person.char "Hey [the_person.mc_title], wait up a sec."
            "[the_person.title] stops you before you open the front door to the house."
            the_person.char "I've had a great night, do you want to come back to my room and have some more fun?"

        else:
            the_person.char "Hey [the_person.mc_title], wait up a sec."
            "[the_person.title] stops you before you open the front door to your house."
            the_person.char "I, uh... I had a really good night with you. I know it's a little weird, but do you want to come back to my room and just hang out?"

    else:
        if the_person.love > 40:
            "[the_person.title] stops you when you get in the door. She takes your hand in hers and looks into your eyes."
            the_person.char "I had a great night. It was so nice to be with you and just pretend that we weren't... that we could be together."
            "Her hand tightens around yours."
            the_person.char "Do you want to come back to my room and just pretend a little bit longer?"

        else:
            "[the_person.title] stops you when you get inside. She takes your hand, then looks away and blushes."
            the_person.char "I had a fun time [the_person.mc_title], thanks for taking me out."
            "She hesitates for a second before continuing."
            the_person.char "If you want to come back to my room and chat for a while I wouldn't say no."
    return

# </editor-fold>

######################
#### Unique - Mom ####
######################
# <editor-fold

label mom_greetings(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 60:
            the_person.char "Hello [the_person.mc_title]. Is there anything your mother can take care of for you?"
        else:
            the_person.char "Hello [the_person.mc_title]. I hope everything is going well, if there's anything I can help with let me know."
    else:
        if the_person.sluttiness > 60:
            the_person.char "Hello [the_person.mc_title], how has your day been? I was... well, I was thinking about you, that's all."
        else:
            if time_of_day == 0 or time_of_day == 1:
                the_person.char "Good morning, [the_person.mc_title]!"
            elif time_of_day == 1 or time_of_day == 2:
                the_person.char "Good afternoon, [the_person.mc_title]!"
            else:
                the_person.char "Good evening, [the_person.mc_title]!"
    return

label mom_clothing_accept(the_person):
    if the_person.obedience > 140:
        the_person.char "Well, if you think it'll look good on me then I'm not going to argue."
        the_person.char "Thank you for the wardrobe suggestions [the_person.mc_title]."
    else:
        the_person.char "Oh that's a cute idea! I'll ask your sister about it later and see what she thinks."
    return

label mom_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person.char "I know it would make your day if I wore this for you [the_person.mc_title], but what if Lily saw me in this?"
        the_person.char "I'm sorry, I know you must be so disappointed in me."
    else:
        if the_person.sluttiness > 60:
            the_person.char "I... [the_person.mc_title], you don't think a women of my... experience could get away wearing this, do you?"
            "[the_person.possessive_title] laughs and shakes her head."
            the_person.char "No, risque stuff like this should be worn by people your sisters age!"
        else:
            the_person.char "[the_person.mc_title]! I'm your mother, I can't go walking around in something like that!"
            "[the_person.possessive_title] shakes her head and scoffs at the idea."
    return

label mom_clothing_review(the_person):
    if the_person.obedience > 130:
        the_person.char "I'm so sorry [the_person.mc_title], I'm really not looking ladylike right now. Just give me a moment to get dressed..."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title], you shouldn't be seeing your mother like this... Just give me a moment and I'll get dressed."
        else:
            the_person.char "Oh [the_person.mc_title], I'm not decent, am I? Turn around, I need to get myself covered!"
    return

label mom_strip_reject(the_person):
    if the_person.obedience > 130:
        the_person.char "I know it would make your day [the_person.mc_title], but I don't think I should take anything else off. I'm your mother, after all."
    elif the_person.obedience < 70:
        the_person.char "Not yet [the_person.mc_title]. You just need to relax and let mommy take care of you."
    else:
        the_person.char "Don't touch that [the_person.mc_title]. Could you imagine if it came off? I'm your mother, there are lines we just shouldn't cross."
    return

label mom_sex_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            the_person.char "This can't be wrong... not if I get so turned on by it, right?"
        else:
            the_person.char "Whatever you want me to do [the_person.mc_title]. I just want to make sure you're happy."
    else:
        the_person.char "Okay, lets try it. I just hope this brings us closer together as mother and son."
    return

label mom_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person.char "I know we shouldn't be doing this. I know I should say no..."
        the_person.char "But just a little more couldn't hurt, right?"
    else:
        if the_person.obedience > 130:
            the_person.char "I... We really shouldn't... But I know it would make you so happy. Okay [the_person.mc_title], let's try it"
        else:
            the_person.char "How does this keep happening [the_person.mc_title]? You know I love you but we shouldn't be doing this..."
            "[the_person.possessive_title] looks away, conflicted."
            the_person.char "I... You just have to make sure your sister never knows about this. Nobody can know..."
    return

label mom_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Not yet, I need to get warmed up first. Let's start out with something a little more tame."
    else:
        the_person.char "I... we can't do that [the_person.mc_title]. I'm your mother; there are lines we just shouldn't cross."
    return

label mom_sex_angry_reject(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Oh god, what did you just say [the_person.mc_title]? I'm your mother, how could you even think about that!"
    else:
        the_person.char "What? Oh god, I... I'm your mother [the_person.mc_title]! We can't do things like that, ever."
        "[the_person.possessive_title] turns away from you."
        the_person.char "You should go. This was a mistake. I should have known it was a mistake. I don't know what came over me."
    return

label mom_seduction_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Do you need some personal attention [the_person.mc_title]? I know how stressed you can get you."
        else:
            the_person.char "Oh well... What do you need help with [the_person.mc_title]?."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Well, how about you let your mother help you get focused again?"
        elif the_person.sluttiness > 10:
            the_person.char "What do you mean [the_person.mc_title]? Do you want to spend some time together?"
        else:
            the_person.char "I'm not sure I understand. I'm your mother, after all."
    return

label mom_seduction_accept_crowded(the_person):
    if the_person.sluttiness < 20:
        "[the_person.title] bats at your shoulder and scoffs."
        the_person.char "You can't say things like that [the_person.mc_title]! Not when we're out in public."
        "She looks around quickly to see if anyone heard you, then takes your hand in hers."
        the_person.char "Come on, we can find someplace quiet to take care of you."

    elif the_person.sluttiness < 50:
        "[the_person.title] blushes and glances around nervously, making sure nobody around you is listening."
        the_person.char "Okay, but we need to be careful. I don't think people would understand the way we show our love. Let's find someplace quiet."

    else:
        the_person.char "Oh my, [the_person.mc_title]... I think we need to take care of you right away!"
    return

label mom_seduction_accept_alone(the_person):
    if the_person.sluttiness < 20:
        the_person.char "I can't believe I'm saying this... I'll play along, as long as you promise nobody will ever know."
        mc.name "Of course Mom, I promise."
    elif the_person.sluttiness < 50:
        the_person.char "Oh [the_person.mc_title], what kind of mother would I be if I said no? Come on, let's see what we can do."
    else:
        the_person.char "Oh [the_person.mc_title], I'm so glad I make you feel that way. Come on, let's get started!"
    return


label mom_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person.char "Oh my god, what are you saying [the_person.mc_title]! I'm your mother, we certainly couldn't do anything... physical!"

    elif the_person.sluttiness < 50:
        the_person.char "I'm sorry [the_person.mc_title], but we really shouldn't be doing anything together any more. It's just... not the way we're suppose to act."

    else:
        the_person.char "I'm sorry [the_person.mc_title], I know how much you like to spend time with me, but now isn't a good time for me. I'll make it up to you though, I promise."
    return

label mom_flirt_response(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Oh [the_person.mc_title] stop, you're making your mother think some... impure thoughts."
        else:
            the_person.char "Oh stop [the_person.mc_title], it's not nice to make fun of your mother like that."
            "[the_person.possessive_title] blushes and looks away."
    else:
        if the_person.sluttiness > 50:
            the_person.char "Oh jeez... I... I don't know what to say about that [the_person.mc_title]. Thank you, I suppose."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
            the_person.char "Thank you for paying attention to someone like me."
        else:
            the_person.char "I'm your mother [the_person.mc_title], you shouldn't be complementing me on things like that."
    return

label mom_cum_face(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "Ah... is this what you like to see [the_person.mc_title]? I hope you had a good time."
        else:
            the_person.char "Oh, it's everywhere! I... I just hope you had a good time [the_person.mc_title]. I'm doing this all for you."
    else:
        if the_person.sluttiness > 70:
            the_person.char "Oh, you got it all over me. I hope that means you had a good time!"
        else:
            the_person.char "I... I don't know what to say about all this. It's so... wrong."
    return

label mom_cum_mouth(the_person):
    if the_person.obedience > 130:
        if the_person.sluttiness > 50:
            the_person.char "I guess that means I did a good job, right [the_person.mc_title]?"
        else:
            the_person.char "I... Oh I'm not sure I'm going to be able to to get use to that. I'll try for you though [the_person.mc_title]."
    else:
        if the_person.sluttiness > 70:
            the_person.char "Mmm, you taste great [the_person.mc_title]. Thank you for giving mommy such a wonderful reward."
        else:
            the_person.char "Oh [the_person.mc_title]... We really shouldn't have done that."
    return

label mom_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Give me your cum [the_person.mc_title]! I don't care if the condom works, I want to feel your seed in me!"
        else:
            the_person.char "Pump it out into that condom [the_person.mc_title], it's perfectly fine to cum in me as long as it's on!"
    elif the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person.char "Give mommy your cum, I want every last drop inside of me! Try and get mommy pregnant!"

    else:
        the_person.char "Oh [the_person.mc_title], you can't cum inside of me! You're so young and virile, it wouldn't take much to get mommy pregnant."

    return

label mom_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person.char "Cum inside of mommy's ass! I want you to give it all to me!"
    else:
        the_person.char "Oh lord, I hope I can take this!"
    return

label mom_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal < 50:
            the_person.char "I hope you don't mind if I slip this off..."
        else:
            the_person.char "I'm just going to take this off for you [the_person.mc_title]..."

    elif the_person.sluttiness < 60:
        if the_person.arousal < 50:
            the_person.char "We're all family here, right? There's nothing about me you haven't seen before."
        else:
            the_person.char "Oh [the_person.mc_title], you make me feel so young again!"
            the_person.char "I shouldn't... I know I shouldn't, but I'm going to take some more off."

    else:
        if the_person.arousal < 50:
            the_person.char "You're all worked up, I bet you want to see some more of me."
        else:
            the_person.char "I just can't keep this on any longer! I want to feel you pressed up against me!"

    return

label mom_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person.char "I'm really sorry [the_person.mc_title], but I've got some work to do right now. Could we chat later?"
        the_person.char "Maybe you can stop by for dinner and talk to me and your sister!"
    else:
        the_person.char "I'm sorry [the_person.mc_title], but I'm really busy right now. If it can wait we can talk about it later."
    return

label mom_sex_watch(the_person, the_sex_person, the_position):
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person.char "[the_person.mc_title]! I'm your mother, how can you be doing that in front of me!"
        $ the_person.change_obedience(-2)
        $ the_person.change_happiness(-1)
        "[the_person.title] looks away while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        $ the_person.change_happiness(-1)
        the_person.char "[the_person.mc_title]! Could you at least try and not do this in front of your mother?"
        "[the_person.title] tries to avert her gaze while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person.char "[the_person.mc_title], I'm... You really shouldn't be doing this here..."
        $ change_report = the_person.change_slut_temp(1)
        "[the_person.possessive_title] averts her gaze, but she keeps stealing glances while you and [the_sex_person.name] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person.char "Who taught you this [the_person.mc_title]? It certainly wasn't me..."
        $ change_report = the_person.change_slut_temp(2)
        "[the_person.title] watches you and [the_sex_person.name] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person.char "Treat her the way she deserves [the_person.mc_title]. I think you could try something a little more exciting with her."
        "[the_person.title] watches eagerly while you and [the_sex_person.name] [the_position.verb]."

    return

label mom_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person.char "I can handle it [the_person.mc_title], you can use me however you want."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person.char "Don't listen to [the_watcher.title]. I'm just taking care of my son, any way he needs!"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person.char "[the_person.mc_title], I love you so much. I hope [the_watcher.title] understands that."
        "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person.char "Oh [the_person.mc_title], I know it's be wrong but being with you just feels so right!"
        $ the_person.change_arousal(1)
        "[the_person.possessive_title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person.char "[the_person.mc_title], we shouldn't be doing this. Not here. What if people recognize us? What if they talk?"
        $ the_person.change_arousal(-1)
        $ the_person.change_slut_temp(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person.char "[the_watcher.title], I'm glad you're so supportive."
        the_person.char "People say we shouldn't do this, but this is the closest I've ever felt to my son."
        $ the_person.change_arousal(1)
        $ the_person.change_slut_temp(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."

    return

label mom_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person.char "Oh my..."
        "She pauses and moans passionately."
        the_person.char "You know just what to do to your mother feel alive. I'm going to cum!"
    else:
        the_person.char "I... I shouldn't be feeling like this... I shouldn't but you're going to..."
        "She hesitates before continuing, almost at a whisper."
        the_person.char "Make me cum."
    return

label mom_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Keep going [the_person.mc_title], make your mommy cum!"
        "[the_person.possessive_title] closes her eyes and moans passionately."
    else:
        the_person.char "This feeling... Oh... Oh this is so wrong!"
        "Her eyes close and she takes a slow, deep breath."
    return

label mom_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "That's it, fuck me [the_person.mc_title]! Fuck me like you mean it, you're going to make your mommy cum!"
        "She closes her eyes as she tenses up. She freezes for a long second, then lets out a long, slow breath."
    else:
        the_person.char "Oh god, I shouldn't be... I shouldn't be feeling like this..."
        the_person.char "I'm going to cum [the_person.mc_title], you're about to make mommy cum! Ah!"
    return

label mom_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person.char "Fuck me [the_person.mc_title], fuck mommy in the ass with your big cock and make her cum!"
    else:
        the_person.char "Oh no, this isn't happening... I'm about to..."
        "She gasps and shivers with pleasure."
        the_person.char "Cum! Ah!"
    return

label mom_date_seduction(the_person):
    if the_person.sluttiness > the_person.love:
        if the_person.sluttiness > 40:
            "When you get home your mother takes your hand and starts to lead you through the house."
            the_person.char "You've shown me such a good time tonight. Come with me and I think I can show you a few things too."
        else:
            "When you get home your mother takes your hand and holds it in hers."
            the_person.char "You were a perfect gentleman tonight [the_person.mc_title]. I think you've earned this."
            "She leans forward and kisses you on the lips. She lingers there for a couple of seconds before pulling back and sighing."
            the_person.char "Would you... like to come to my room and share a quick drink before I get to bed? Maybe you could tuck me in too."
    else:
        if the_person.love > 40:
            the_person.char "[the_person.mc_title]..."
            "When you get home your mother takes your hand and holds it in both of hers."
            the_person.char "I had such a wonderful time tonight. You make me feel so young and alive."
            "She leans in and kisses you on the cheek. She lingers there for a second, her breath warm on our ear."
            the_person.char "Would you like to share a drink in my room before we head to bed? "
        else:
            the_person.char "[the_person.mc_title]..."
            "When you get home your mother gets your attention. She leans over and kisses you on the cheek."
            the_person.char "You've been a wonderful date. Would you like to share a drink with me before we head to bed?"
    return

label mom_sex_take_control (the_person):
    if the_person.arousal > 60:
        the_person.char "[the_person.mc_title], you just sit back and let me take care of you. Mommy's going to get what she needs from you..."
    else:
        the_person.char "Oh [the_person.mc_title], you can't get a women all worked up then just walk away. Here, let me take care of both of us."
    return

label mom_sex_beg_finish(the_person):
    "Wait [the_person.mc_title], you can't stop now, I'm so close! Please, please help your mother cum!"
    return

# </editor-fold>


#######################
#### Unique - Aunt ####
#######################
# <editor-fold>

label aunt_sex_beg_finish(the_person):
    "Wait, I really need this [the_person.mc_title]! You're making me feel like a real women, please don't stop! Please!"
    return

# </editor-fold>


#########################
#### Unique - Cousin ####
#########################
# <editor-fold
#TODO
# </editor-fold>


#TODO: Go through and add unique stephanie versions for these events.
#TODO: Go through existing crises and events and add personality calls so we can get some different looking dialogue.
#TODO: Write some bimbo answers for the head researcher's new personality (and possibly as a personality you can give someone with a serum later.
#TODO: Add a screen to let you select a new Head Researcher.
#TODO: Add a tutorial!
#Idea for tutorial: Add a crisis style mandatory event for each major thing we want the player to experience.
