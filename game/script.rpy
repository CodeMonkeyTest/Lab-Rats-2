init -10 python: #Init -10 is used for all project wide imports of external resources
    import os
    import copy
    import math
    import __builtin__
    import xml.etree.ElementTree as ET
    import time
    import zipfile
    import hashlib
    import io
    from collections import defaultdict

    if not renpy.mobile: #Mobile platforms do not support animation, so we only want to try to import it if we're going to use it.
        import shader

    # all image sets available
    global supported_positions
    supported_positions = ["stand2","stand3","stand4","stand5","walking_away","kissing","doggy","missionary","blowjob","against_wall","back_peek","sitting","kneeling1","standing_doggy","cowgirl"]

    # zipfile cachingF
    global mobile_zip_dict
    mobile_zip_dict = {}
    for position in supported_positions:
        file_path = "images/character_images/" + position + ".zip"
        renpy_file = renpy.file(file_path)
        mobile_zip_dict[position] = zipfile.ZipFile(renpy_file, "r") #Cache all of the zip files so we have a single static pointer to them.


#Init -5 establishes all game classes
#Init -2 is then used by all game content that will use those game classes (ie. instantiates different Crises that could be generated)
#Init 0 establishes Renpy settings, including callbacks for display code.

init -2: # Establish some platform specific stuff.
    if renpy.macintosh:
        default persistent.vren_animation = True
        $ persistent.vren_mac_scale = 1.0 #2.0 # Changes to the way the surface size is calculated has made a mac specific setting like this oboslete. This section is only here until I can confirm everything is working properly.

    else:
        default persistent.vren_animation = True
        $ persistent.vren_mac_scale = 1.0

    default persistent.pregnancy_pref = 0 # 0 = no content, 1 = predictable, 2 = realistic

init -2 python:
    list_of_positions = [] # These are sex positions that the PC can make happen while having sex.
    list_of_girl_positions = [] # These are sex positions that the girl can make happen while having sex.

    day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] #Arrays that hold the names of the days of the week and times of day. Arrays start at 0.
    time_names = ["Early Morning","Morning","Afternoon","Evening","Night"]

    global emotion_images_dict
    emotion_images_dict = {}
    for skin in ["white", "tan", "black"]:
        emotion_images_dict[skin] = {}
        for face in list_of_faces:
            emotion_images_dict[skin][face] = Expression(skin + "_" + face, skin, face)


init 0 python:
    #config.use_cpickle = False #Set to True for more useful save failure info

    config.interact_callbacks.append(take_animation_screenshot)
    config.history_callbacks.append(text_message_history_callback) #Ensures conversations had via text are recorded properly
    # config.say_arguments_callback = text_message_say_callback #Recolours and re-fonts say statements made while having a text conversation #NOTE: NOt needed now that we properly store messages into the phone and display them from a custom screen.

    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 32
    config.cache_surfaces = False   # prevent render surfaces from being cached

    # Don't predict screens, it eats resources since every screen reloaded on a screen action (like hover)
    config.predict_screen_statements = False
    config.predict_screens = False

    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if renpy.variant("pc"):
        config.image_cache_size_mb = 768
    else:
        config.image_cache_size_mb = 384

    config.has_autosave = False
    config.autosave_frequency = None
    config.has_quicksave = True

    config.rollback_enabled = True  # allows for smoother dialogs while skipping
    config.rollback_length = 32

    if persistent.colour_palette is None:
        persistent.colour_palette = [[1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]

    config.autoreload = False

    #config.debug_text_overflow = True
    config.debug_text_overflow = False #If enabled finds locations with text overflow. Turns out I have a lot, kind of blows up when enabled and generates a large text file. A problem for another day.
    config.debug_image_cache = False
    config.debug = True

    # THIS IS WHAT PREVENTS IT FROM INDEXING IMAGES
    # SEE 00images.rpy for where this is created
    config.images_directory = None
    preferences.gl_tearing = True ## Prevents juttery animation with text while using advanced shaders to display images

    _preferences.show_empty_window = False #Prevents Ren'py from incorrectly showing the text window in complex menu sitations (which was a new bug/behaviour in Ren'py v7.2)

    global animation_draw_requested #Note that this is broken down by draw layer so that multiple threads can return safely in a single interaction.
    animation_draw_requested = {} #This dict holds each draw layer request. Inside of each draw layer request are lists, which hold the character and their personal reference draw number, so that we can cull out of date draws

    global global_draw_number # Holds the draw numbers for all possible scenes ("solo" is the main one). This value is increased by one every time a scene is cleared, and is used to prevent animations from being drawn after moving on from a scene.
    global_draw_number = {}

    global prepared_animation_render #The render that has been prepared by a separate thread should be placed here.
    prepared_animation_render = {}

    global prepared_animation_arguments #Holds all of the extra arguments that should be passed onto the display code.
    prepared_animation_arguments = {}

    global draw_layers
    draw_layers = []

    add_draw_layer("front_1") # Layers used for extra characters. In theory this can be expanded infinitely, but it reacts poorly to being adjusted mid-game.
    add_draw_layer("solo") # Add the main default draw layer, used for all single character displays
    add_draw_layer("back_1")
    add_draw_layer("back_2")

    build.classify("game/images/character_images/**stand2**.png", None) # unarchived images for the different positiosn are not needed, they are all included in .zip files.
    build.classify("game/images/character_images/**stand3**.png", None)
    build.classify("game/images/character_images/**stand4**.png", None)
    build.classify("game/images/character_images/**stand5**.png", None)
    build.classify("game/images/character_images/**walking_away**.png", None)
    build.classify("game/images/character_images/**back_peek**.png", None)
    build.classify("game/images/character_images/**sitting**.png", None)
    build.classify("game/images/character_images/**kissing**.png", None)
    build.classify("game/images/character_images/**doggy**.png", None)
    build.classify("game/images/character_images/**missionary**.png", None)
    build.classify("game/images/character_images/**blowjob**.png", None)
    build.classify("game/images/character_images/**against_wall**.png", None)
    build.classify("game/images/character_images/**standing_doggy**.png", None)
    build.classify("game/images/character_images/**kneeling1**.png", None)
    build.classify("game/images/character_images/**cowgirl**.png", None)

    build.classify("game/images/character_images/**.zip", "all")

label start:
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18.":
            "Excellent, let's continue then."

        "I am not over 18.":
            $renpy.full_restart()

    "Vren" "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."
    "Vren" "Would you like to view the FAQ?"
    menu:
        "View the FAQ.":
            call faq_loop
        "Get on with the game!":
            "You can access the FAQ from your bedroom at any time."

    "Vren" "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."
    menu:
        "No pregnancy content.\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content.\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Realistic pregnancy content.\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

    $ renpy.block_rollback()
    call screen character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.
    call initialize_game_state(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2])
    $ renpy.block_rollback()
    menu:
        "Play introduction and tutorial.":
            call tutorial_start

        "Skip introduction and tutorial.":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start

init 0 python:
    def initialize_stephanie_in_our_business():
        mc.business.add_employee_research(stephanie, add_to_location = True)
        mc.business.hire_head_researcher(stephanie)
        mc.business.r_div.move_person(stephanie, lobby)
        stephanie.special_role.append(steph_role)
        return

label normal_start:
    ## For now, this ensures reloading the game doesn't reset any of the variables.
    $ renpy.scene()
    show screen tooltip_screen
    show screen phone_hud_ui
    show screen business_ui
    show screen goal_hud_ui
    show screen main_ui
    $ bedroom.show_background()
    "It's Monday, and the first day of operation for your new business!"
    "[stephanie.title] said she would meet you at your new office for a tour."
    #TODO: Have an on_enter event for Steph if you see her the first day. Minor interaction stuff.

    #Add Stepyhanie to our business and flag her with a special role.
    $ initialize_stephanie_in_our_business()

    #TODO: movement overlay tutorial thing.
    jump game_loop

init 0 python:
    def build_actions_list():
        actions_list = []
        if time_of_day == 4:
            if sleep_action not in mc.location.actions: #If they're in a location they can sleep we shouldn't show this because they can just sleep here.
                actions_list.append(["Go home and sleep {image=gui/heart/Time_Advance.png}{image=gui/heart/Time_Advance.png} (tooltip)It's late. Go home and sleep.", "Wait"])
        else:
            actions_list.append(["Wait here {image=gui/heart/Time_Advance.png}\n{color=#FFFF00}10% Extra{/color} {image=gui/extra_images/energy_token.png} (tooltip)Kill some time and wait around. Recovers more energy than working.", "Wait"])
        actions_list.append(["Go somewhere else", "Travel"])
        actions_list.append(["Check your phone", "Phone"])
        actions_list.extend(mc.location.get_valid_actions())
        actions_list.insert(0, "Do Something")
        return actions_list

    def build_people_list():
        people_list = []
        people_list.extend(mc.location.people)
        people_list.sort(key = sort_display_list, reverse = True)
        people_list.insert(0, "Talk to Someone")
        return people_list

    def main_loop_pick_talk_event(person):
        out_of_uniform = next((x for x in person.on_talk_event_list if x.name == "Uniform Disobedience LTE" and x.is_action_enabled(person)), None)
        if out_of_uniform: # out of uniform takes precedence of other LTE events
            person.on_talk_event_list.remove(out_of_uniform)
            return out_of_uniform

        enabled_talk_events = []
        for possible_talk_event in person.on_talk_event_list:
            if possible_talk_event.is_action_enabled(person):
                enabled_talk_events.append(possible_talk_event)

        if enabled_talk_events:
            chosen = get_random_from_list(enabled_talk_events)
            person.on_talk_event_list.remove(chosen)
            return chosen
        return None

    def main_loop_pick_room_event(location):
        enabled_room_events = []
        for a_person in location.people:
            for possible_room_event in a_person.on_room_enter_event_list:
                if possible_room_event.is_action_enabled(a_person): #See what events the are enabled...
                    enabled_room_events.append([a_person, possible_room_event]) #Then keep track of the person so we know who to remove it from if it triggers.

        if enabled_room_events:
            chosen = get_random_from_list(enabled_room_events)
            chosen[0].on_room_enter_event_list.remove(chosen[1]) #Remove the event from their list since we will be running it.
            return chosen
        return None

    def main_loop_select_greeter(location):
        possible_greetings = []
        for a_person in new_location.people:
            if mc.business.get_employee_title(a_person) != "None":
                possible_greetings.append(a_person)
        return get_random_from_list(possible_greetings)

    common_variable_list = ["talk_action", "new_location", "picked_option", "picked_event", "outfit", "insta_outfit", \
        "the_outfit", "new_outfit", "old_outfit", "the_uniform", "the_underwear", "person_one", "person_two", "the_person_one", \
        "the_person_two", "the_item", "the_clothing", "the_group", "the_report", "the_trait", "the_mom", "the_action", \
        "the_aunt", "the_sister", "the_student", "the_place", "the_girl", "test_outfit", "the_object", \
        "the_location", "next_item", "file_path", "title_choice", "title_one", "title_two", "placeholder", \
        "formatted_title_one", "formatted_title_two", "new_title", "the_type", "the_person", "player_choice", \
        "strip_list", "first_item", "feet_ordered", "top_feet", "crisis", "the_morning_crisis", "people_to_process", \
        "report_log", "position_choice", "object_choice", "round_choice", "start_position", "the_group", \
        "report", "the_relationship", "partner", "the_subject", "the_suggested_outfit", "stripper", \
        "not_stripper", "the_student", "strip_choice", "new_pose", "picked_pose", "pose_choice", "new_person" \
        "clothing", "formatted_name", "formatted_title", "hair_style_check", "pubic_style_check", "the_cause", \
        "text_one", "text_two", "the_goal", "the_serum", "title", "opinion_tag", "overhear_topic", "the_choice", \
        "opinion_string", "mc_opinion_string", "talk_opinion_text", "opinion_learned", "place", "the_place", "the_taboo",
        "climax_controller", "the_watcher"]

    def main_loop_cleanup():
        clear_scene()
        # generic cleanup routine for common variable names
        for name in common_variable_list:
            if name in globals():
                del globals()[name]
        renpy.block_rollback()
        renpy.checkpoint()

    def main_loop_auto_save():
        last_save_day = mc.business.event_triggers_dict.get("last_save_day", 0)
        if day > last_save_day and time_of_day == 0:
            #renpy.notify("Saving game: " + str(day))
            renpy.force_autosave(take_screenshot = False, block = True)
            mc.business.event_triggers_dict["last_save_day"] = day



label game_loop(): ##THIS IS THE IMPORTANT SECTION WHERE YOU DECIDE WHAT ACTIONS YOU TAKE
    $ main_loop_cleanup()
    $ main_loop_auto_save()
    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([build_people_list(), build_actions_list()]))
    else:
        call screen main_choice_display([build_people_list(), build_actions_list()])
    $ picked_option = _return

    if isinstance(picked_option, Person):
        $ picked_option.draw_person()
        $ talk_action = main_loop_pick_talk_event(picked_option)
        if talk_action:
            $ talk_action.call_action(picked_option)
        else:
            if picked_option.title is None:
                "You decide to approach the stranger and introduce yourself."
            else:
                "You approach [picked_option.title] and chat for a little bit."
                $ picked_option.call_dialogue("greetings")

            if picked_option.has_taboo(["underwear_nudity","bare_tits", "bare_pussy"]) and picked_option.judge_outfit(picked_option.outfit, -30): #If she's in anything close to slutty she's self-conscious enough to comment on it.
                if picked_option.outfit.vagina_visible() and picked_option.has_taboo("bare_pussy") and picked_option.outfit.tits_visible() and picked_option.has_taboo("bare_tits"):
                    "[picked_option.title] doesn't say anything about it, but seems uncomfortable being naked in front of you."
                    "As you talk she seems to become more comfortable with her own nudity, even if she isn't thrilled by it."

                if picked_option.outfit.vagina_visible() and picked_option.has_taboo("bare_pussy"):
                    "[picked_option.title] doesn't say anything about it, but angles her body to try and conceal her bare pussy from you."
                    "As you talk she seems to become more comfortable, even if she isn't thrilled about it."

                elif picked_option.outfit.tits_visible() and picked_option.has_taboo("bare_tits"):
                    "[picked_option.title] doesn't say anything about it, but brings her arms up to try and conceal her tits."
                    if picked_option.has_large_tits():
                        "Her large chest isn't easy to hide, and she quickly realizes it's hopeless."
                    else:
                        "As you talk she seems to become more comfortable, and eventually lets her arms drop again."

                elif ((picked_option.outfit.wearing_panties() and not picked_option.outfit.panties_covered()) or (picked_option.outfit.wearing_bra() and not picked_option.outfit.bra_covered())) and picked_option.has_taboo("underwear_nudity"):
                    "[picked_option.title] doesn't say anything about it, but she tries to cover up her underwear with her hands."
                    "As you talk she seems to become more comfortable, and eventually she lets her arms drop to her sides."

                $ picked_option.update_outfit_taboos()
            call talk_person(picked_option) from _call_talk_person

    elif isinstance(picked_option, Action):
        $ picked_option.call_action()


    elif picked_option == "Travel":
        call screen map_manager
        $ new_location = _return
        call change_location(new_location) from _call_change_location #_return is the location returned from the map manager.
        if new_location.people: #There are people in the room, let's see if there are any room events
            $ picked_event = main_loop_pick_room_event(new_location)
            if picked_event: #If there are room events to take care of run those right now.
                $ picked_event[1].call_action(picked_event[0]) #Run the action with the person as an extra argument.
            elif renpy.random.randint(0,2) == 0 and new_location in [mc.business.m_div, mc.business.p_div, mc.business.r_div, mc.business.s_div, mc.business.h_div]: #There are no room events, so generate a quick room greeting from an employee if one is around.
                $ the_greeter = main_loop_select_greeter(new_location)
                if the_greeter:
                    $ the_greeter.draw_person()
                    $ the_greeter.call_dialogue("work_enter_greeting")
                    $ clear_scene()
                    $ del the_greeter

    elif picked_option == "Phone":
        call browse_internet() from _call_browse_internet

    elif picked_option == "Wait":
        if time_of_day == 4:
            $ mc.change_location(bedroom)
        else:
            $ mc.change_energy(10) #Extra 10 energy gain if you spend your time waiting around
        call advance_time from _call_advance_time_15
        $ mc.location.show_background() #Redraw the background in case it has changed due to the new time.

    jump game_loop

label change_location(the_place):
    $ renpy.scene()
    $ the_place.show_background()
    if the_place.trigger_tutorial and the_place.tutorial_label is not None and mc.business.event_triggers_dict.get("Tutorial_Section",False):
        $ the_place.trigger_tutorial = False
        $ renpy.call(the_place.tutorial_label)

    return

init 0 python:
    def build_chat_action_list(the_person):
        small_talk_action = Action("Make small talk   {color=#FFFF00}-15{/color} {image=gui/extra_images/energy_token.png}", requirement = small_talk_requirement, effect = "small_talk_person", args=the_person, requirement_args=the_person,
            menu_tooltip = "A pleasant chat about your likes and dislikes. A good way to get to know someone and the first step to building a lasting relationship. Provides a chance to study the effects of active serum traits and raise their mastery level.")
        compliment_action = Action("Compliment her   {color=#FFFF00}-15{/color} {image=gui/extra_images/energy_token.png}", requirement = compliment_requirement, effect = "compliment_person", args=the_person, requirement_args=the_person,
            menu_tooltip = "Lay the charm on thick and heavy. A great way to build a relationship, and every girl is happy to receive a compliment! Provides a chance to study the effects of active serum traits and raise their mastery level.")
        flirt_action = Action("Flirt with her   {color=#FFFF00}-15{/color} {image=gui/extra_images/energy_token.png}", requirement = flirt_requirement, effect = "flirt_person", args=the_person, requirement_args=the_person,
            menu_tooltip = "A conversation filled with innuendo and double entendre. Both improves your relationship with a girl and helps make her a little bit sluttier. Provides a chance to study the effects of active serum traits and raise their mastery level.")
        date_action = Action("Ask her on a date", requirement = date_option_requirement, effect = "date_person", args=the_person, requirement_args=the_person,
            menu_tooltip = "Ask her out on a date. The more you impress her the closer you'll grow. If you play your cards right you might end up back at her place.")
        make_girlfriend_action = Action("Ask her to be your girlfriend", requirement = ask_girlfriend_requirement, effect = "ask_be_girlfriend_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Ask her to start an official, steady relationship and be your girlfriend.", priority = 10)
        bc_talk_action = Action("Talk about her birth control", requirement = bc_talk_requirement, effect = "bc_talk_label", args = the_person, requirement_args = the_person,
            menu_tooltip = "Talk to her about her use of birth control. Ask her to start or stop taking it, or just check what she's currently doing.")
        chat_list = [small_talk_action, compliment_action, flirt_action, date_action, make_girlfriend_action, bc_talk_action]
        chat_list.sort(key = sort_display_list, reverse = True)
        chat_list.insert(0,"Chat with her")
        return chat_list

    def build_specific_action_list(the_person):
        grope_action = Action("Grope her   {color=#FFFF00}-5{/color} {image=gui/extra_images/energy_token.png}", requirement = grope_requirement, effect = "grope_person", args = the_person, requirement_args = the_person,
            menu_tooltip = "Be \"friendly\" and see how far she is willing to let you take things. May make her more comfortable with physical contact, but at the cost of her opinion of you.")

        command_action = Action("Give her a command", requirement = command_requirement, effect = "command_person", args = the_person, requirement_args = the_person,
            menu_tooltip = "Leverage her obedience and command her to do something.")

        specific_action_list = ["Say goodbye", grope_action, command_action]
        specific_action_list.sort(key = sort_display_list, reverse = True)
        specific_action_list.insert(0,"Do something specific")
        return specific_action_list

    def get_special_role_actions(the_person):
        role_actions = []
        for role in the_person.special_role:
            for act in role.actions:
                role_actions.append(act)
        return role_actions

    def build_special_role_actions_list(the_person):
        special_role_actions = []
        for act in get_special_role_actions(the_person):
            special_role_actions.append([act,the_person]) #They're a list of actions and their extra arg so that gets passed through properly.

        for act in mc.main_character_actions: #The main character has a "role" that lets us add special actions as well.
            special_role_actions.append([act,the_person])

        special_role_actions.sort(key = sort_display_list, reverse = True)
        special_role_actions.insert(0,"Special Actions")
        return special_role_actions


label talk_person(the_person):
    $ mc.having_text_conversation = None #Just in case some event hasn't properly reset this.
    if the_person.title is None:
        $ the_person.draw_person()
        call person_introduction(the_person) from _call_person_introduction #If their title is none we assume it is because we have never met them before. We have a special introduction scene for new people.

label .continue_talk:
    $ renpy.restart_interaction()
    $ the_person.draw_person()
    if "action_mod_list" in globals():
        call screen enhanced_main_choice_display(build_menu_items([build_chat_action_list(the_person), build_specific_action_list(the_person), build_special_role_actions_list(the_person)]))
    else:
        call screen main_choice_display([build_chat_action_list(the_person), build_specific_action_list(the_person), build_special_role_actions_list(the_person)])

    if isinstance(_return, Action):
        $ starting_time_of_day = time_of_day
        if _return in get_special_role_actions(the_person) + mc.main_character_actions:
            $ _return.call_action(the_person)
        else:
            $ _return.call_action()

        if the_person in mc.location.people and time_of_day == starting_time_of_day:
            jump talk_person.continue_talk #If we're in the same place and time hasn't advanced keep talking to them until we stop talking on purpose.

    $ clear_scene()
    return

label advance_time:
    # 1) Turns are processed _before_ the time is advanced.
    # 1a) crises are processed if they are triggered.
    # 2) Time is advanced, day is advanced if required.
    # 3) People go to their next intended location.
    # Then: Add research crisis when serum is finished, requiring additional input from the player and giving the chance to test a serum on the R&D staff.

    #$mc.can_skip_time = False #Ensure the player cannot skip time during crises.

    $ mandatory_advance_time = False #If a crisis returns an "Advance Time" value once this turn is finished processing it will process ANOTHER turn, so a crisis can require a turn to pass.

    python:
        people_to_process = [] #This is a master list of turns of need to process, stored as tuples [character,location]. Used to avoid modifying a list while we iterate over it, and to avoid repeat movements.
        for place in list_of_places:
            for people in place.people:
                people_to_process.append([people,place])

    python:
        for (people,place) in people_to_process: #Run the results of people spending their turn in their current location.
            people.run_turn()

        mc.business.run_turn()
        mc.run_turn()


    #We make sure that all mandatory crises are run here. Mandatory crises always trigger as soon as they are able, possibly with multiple crises triggering in a single turn.
    $ count = 0
    $ max = len(mc.business.mandatory_crises_list)
    $ clear_list = []
    while count < max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
        $ crisis = mc.business.mandatory_crises_list[count]
        if crisis.is_action_enabled():
            $ crisis.call_action()
            if _return == "Advance Time":
                $ mandatory_advance_time = True
            $ clear_scene()
            $ clear_list.append(crisis)
        $ count += 1
        $ del crisis
    $ mc.location.show_background()
    python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
        for crisis in clear_list:
            mc.business.mandatory_crises_list.remove(crisis) #Clean up the list.
        del clear_list

    #Once mandatory crises are managed we may or may not run a random crisis to keep things interesting.
    if renpy.random.randint(0,100) < 10: #ie. run a crisis 10% of the time.
        python:
            possible_crisis_list = []
            for crisis in crisis_list:
                if crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                    possible_crisis_list.append(crisis) #Build a list of valid crises from ones that pass their requirement.

        $ the_crisis = get_random_from_weighted_list(possible_crisis_list)
        if the_crisis:
            $ the_crisis.call_action()
            if _return == "Advance Time":
                $ mandatory_advance_time = True
            $ del crisis
        $ del possible_crisis_list

    $ clear_scene()
    $ renpy.scene()
    $ mc.location.show_background()
    show screen business_ui

    if time_of_day == 4: ##First, determine if we're going into the next chunk of time. If we are, advance the day and run all of the end of day code.
        python:
            for (people,place) in people_to_process:
                people.run_day()

        $ mc.run_day()
        $ mc.business.run_day()

        $ time_of_day = 0
        $ day += 1

        if mc.business.funds < 0:
            $ mc.business.bankrupt_days += 1
            if mc.business.bankrupt_days == mc.business.max_bankrupt_days:
                $ renpy.say(None, "With no funds to pay your creditors you are forced to close your business and auction off all of your materials at a fraction of their value. Your story ends here.")
                $ renpy.full_restart()
            else:
                $ days_remaining = mc.business.max_bankrupt_days-mc.business.bankrupt_days
                $ renpy.say(None, "Warning! Your company is losing money and unable to pay salaries or purchase necessary supplies!")
                $ renpy.say(None, "You have [days_remaining] days to restore yourself to positive funds or the bank will reclaim the business!")
        else:
            $ mc.business.bankrupt_days = 0

        call screen end_of_day_update() # We have to keep this outside of a python block, because the renpy.call_screen function does not properly fade out the text bar.
        $ mc.business.clear_messages()

        #Now we run mandatory morning crises. Nearly identical to normal crises, but these always trigger at the start of the day (ie when you wake up and before you have control of your character.)
        $ count = 0
        $ max = len(mc.business.mandatory_morning_crises_list)
        $ clear_list = []
        while count < max: #We need to keep this in a renpy loop, because a return call will always return to the end of an entire python block.
            $ crisis = mc.business.mandatory_morning_crises_list[count]
            if crisis.is_action_enabled():
                $ crisis.call_action()
                if _return == "Advance Time":
                    $ mandatory_advance_time = True
                $ clear_scene()
                $ clear_list.append(crisis)
            $ count += 1
            $ del crisis
        $ mc.location.show_background()
        python: #Needs to be a different python block, otherwise the rest of the block is not called when the action returns.
            for crisis in clear_list:
                mc.business.mandatory_morning_crises_list.remove(crisis) #Clean up the list.
            del clear_list

        if renpy.random.randint(0,100) < 15: # We run morning crises 5% of all mornings
            python:
                possible_morning_crises = []
                for crisis in morning_crisis_list:
                    if crisis[0].is_action_enabled(): #Get the first element of the weighted tuple, the action.
                        possible_morning_crises.append(crisis) #Build a list of valid crises from ones that pass their requirement.
            $ the_morning_crisis = get_random_from_weighted_list(possible_morning_crises)
            if the_morning_crisis:
                $ the_morning_crisis.call_action()
                if _return == "Advance Time":
                    $ mandatory_advance_time = True
                $ del the_morning_crisis
            $ del possible_morning_crises

    else:
        $ time_of_day += 1 ##Otherwise, just run the end of day code.

    python:
        for (people,place) in people_to_process: #Now move everyone to where the should be in the next time chunk. That may be home, work, etc.
            people.run_move(place)

            if people.title is not None: #We don't assign events to people we haven't met.
                if renpy.random.randint(0,100) < 15: #Only assign one to 15% of people, to cut down on the number of people we're checking.
                    possible_crisis_list = []
                    for crisis in limited_time_event_pool:
                        if crisis[0].is_action_enabled(people): #Get the first element of the weighted tuple, the action.
                            possible_crisis_list.append(crisis) #Build a list of valid crises from ones that pass their requirement.

                    the_crisis = get_random_from_weighted_list(possible_crisis_list, return_everything = True)
                    del possible_crisis_list
                    if the_crisis is not None:
                        limited_time_event = Limited_Time_Action(the_crisis[0], the_crisis[0].event_duration) #Wraps the action so that we can have an instanced duration counter and add/remove it easily.\
                        #renpy.notify("Created event: " + the_crisis[0].name + " for " + people.name)
                        if the_crisis[2] == "on_talk":
                            people.on_talk_event_list.append(limited_time_event)

                        elif the_crisis[2] == "on_enter":
                            people.on_room_enter_event_list.append(limited_time_event)
                        del crisis

    $ mc.business.run_move() # In each phase it runs people->MC->Business. Policy effects are run as part of the business, and so can overwrite/alter things an employee has done (like wear their uniform)

    if time_of_day == 0:    # only free memory in the morning
        $ renpy.free_memory()
    $ mc.location.show_background()
    if mandatory_advance_time: #If a crisis has told us to advance time after it we do so.
        call advance_time from _call_advance_time_28

    $ people_to_process = [] #Clears the memory used here.
    return

init 0 python:
    ##Actions## moved to python to prevent them from being stored in save game
    hr_work_action = Action("Organize your business {image=gui/heart/Time_Advance.png}",hr_work_action_requirement,"hr_work_action_description",
        menu_tooltip = "Raise business efficiency, which drops over time based on how many employees the business has.\n+3*Charisma + 2*Skill + 1*Intelligence + 5 Efficiency.")
    research_work_action = Action("Research in the lab {image=gui/heart/Time_Advance.png}",research_work_action_requirement,"research_work_action_description",
        menu_tooltip = "Contribute research points towards the currently selected project.\n+3*Intelligence + 2*Skill + 1*Focus + 10 Research Points.")
    supplies_work_action = Action("Order Supplies {image=gui/heart/Time_Advance.png}",supplies_work_action_requirement,"supplies_work_action_description",
        menu_tooltip = "Purchase serum supply at the cost of $1 per unit of supplies. When producing serum every production point requires one unit of serum.\n+3*Focus + 2*Skill + 1*Charisma + 10 Serum Supply.")
    market_work_action = Action("Sell Prepared Serums {image=gui/heart/Time_Advance.png}",market_work_action_requirement,"market_work_action_description",
        menu_tooltip = "Sell serums that have been marked for sale. Mark serum manually from your office or set an automatic sell threshold in production.\n3*Charisma + 2*Skill + 1*Focus + 5 Serum Doses Sold.")
    production_work_action = Action("Produce serum {image=gui/heart/Time_Advance.png}",production_work_action_requirement,"production_work_action_description",
        menu_tooltip = "Produce serum from raw materials. Each production point of serum requires one unit if supply, which can be purchased from your office.\n+3*Focus + 2*Skill + 1*Intelligence + 10 Production Points.")

    interview_action = Action("Hire someone new {image=gui/heart/Time_Advance.png}", interview_action_requirement,"interview_action_description",
        menu_tooltip = "Look through the resumes of several candidates. More information about a candidate can be revealed by purchasing new business policies.")
    design_serum_action = Action("Design new serum {image=gui/heart/Time_Advance.png}", serum_design_action_requirement,"serum_design_action_description",
        menu_tooltip = "Combine serum traits to create a new design. Once a design has been created it must be researched before it can be put into production.")
    pick_research_action = Action("Assign Research Project", research_select_action_requirement,"research_select_action_description",
        menu_tooltip = "Pick the next research topic for your R&D division. Serum designs must be researched before they can be put into production.")
    pick_production_action = Action("Set production settings", production_select_action_requirement,"production_select_action_description",
        menu_tooltip = "Decide what serum designs are being produced. Production is divided between multiple factory lines, and automatic sell thresholds can be set to automatically flag serum for sale.")
    pick_supply_goal_action = Action("Set the amount of supply you would like to maintain.", pick_supply_goal_action_requirement,"pick_supply_goal_action_description",
        menu_tooltip = "Set a maximum amount of serum you and your staff will attempt to purchase.")
    policy_purhase_action = Action("Manage business policies", policy_purchase_requirement,"policy_purchase_description",
        menu_tooltip = "New business policies changes the way your company runs and expands your control over it. Once purchased business policies are always active.")
    set_head_researcher_action = Action("Select a Head Researcher", head_researcher_select_requirement, "head_researcher_select_description",
        menu_tooltip = "Pick a member of your R&D staff to be your head researcher. A head researcher with a high intelligence score will increase the amount of research produced by the entire division.")

    trade_serum_action = Action("Access production stockpile", trade_serum_action_requirement, "trade_serum_action_description",
        menu_tooltip = "Move serum to and from your personal inventory. You can only use serum you are carrying with you.")
    sell_serum_action = Action("Mark serum to be sold", sell_serum_action_requirement, "sell_serum_action_description",
        menu_tooltip = "Decide what serum should be available for sale. It can then be sold from the marketing division. Setting an automatic sell threshold in the production department can do this automatically.")
    review_designs_action = Action("Review serum designs", review_designs_action_requirement, "review_designs_action_description",
        menu_tooltip = "Shows all existing serum designs and allows you to delete any you no longer desire.")

    set_company_model_action = Action("Pick a company model", pick_company_model_requirement, "pick_company_model_description",
        menu_tooltip = "Pick one your employees to be your company model. You can run ad campaigns with your model, increasing the value of every dose of serum sold.")

    sleep_action = Action("Sleep for the night {image=gui/heart/Time_Advance.png}{image=gui/heart/Time_Advance.png}",sleep_action_requirement,"sleep_action_description",
        menu_tooltip = "Go to sleep and advance time to the next day. Night time counts as three time chunks when calculating serum durations.", priority = 20)
    bedroom_masturbate_action = Action("Masturbate {image=gui/heart/Time_Advance.png}", bedroom_masturbate_requirement, "bedroom_masturbation",
        menu_tooltip = "Jerk off. A useful way to release Clarity, but you'll grow bored of this eventually.")

    faq_action = Action("Check the FAQ",faq_action_requirement,"faq_action_description",
        menu_tooltip = "Answers to frequently asked questions about Lab Rats 2.")

    downtown_search_action = Action("Wander the streets {image=gui/heart/Time_Advance.png}", downtown_search_requirement, "downtown_search_label",
        menu_tooltip = "Spend time exploring the city and seeing what interesting locations it has to offer.")

    strip_club_show_action = Action("Watch a show", stripclub_show_requirement, "stripclub_dance",
        menu_tooltip = "Take a seat and wait for the next girl to come out on stage.")

    mom_office_person_request_action = Action("Approach the receptionist", mom_office_person_request_requirement, "mom_office_person_request",
        menu_tooltip = "The receptionist might be able to help you, if you're looking for someone.")

    import_wardrobe_action = Action("Import a wardrobe file", faq_action_requirement, "wardrobe_import",
        menu_tooltip = "Select and import a wardrobe file, adding all outfits to your current wardrobe.")

    test_action = Action("This is a test.", faq_action_requirement, "faq_action_description")
    ##Actions unlocked by policies##
    set_uniform_action = Action("Manage Employee Uniforms",set_uniform_requirement,"set_uniform_description")
    set_serum_action = Action("Set Daily Serum Doses",set_serum_requirement,"set_serum_description")

    business_wardrobe = wardrobe_from_xml("Business_Wardrobe") #Used in some of Mom's events when we need a business-ish outfit

init 0 python:
    def add_stripclub_strippers():
        for i in __builtin__.range(0,4):
            a_girl = create_random_person(start_sluttiness = renpy.random.randint(15,30))
            a_girl.generate_home()
            a_girl.set_schedule(strip_club, times = [3,4])
            a_girl.home.add_person(a_girl)
            stripclub_strippers.append(a_girl)
        return

    stripclub_wardrobe = wardrobe_from_xml("Stripper_Wardrobe")

label initialize_game_state(character_name,business_name,last_name,stat_array,skill_array,_sex_array,max_num_of_random=5): #Gets all of the variables ready. TODO: Move some of this stuff to an init block?

    $ list_of_traits = [] #List of serum traits that can be used. Established here so they play nice with rollback, saving, etc.
    $ list_of_nora_traits = []
    $ list_of_places = [] #By having this in an init block it may be set to null each time the game is reloaded, because the initialization stuff below is only called once.

    #NOTE: These need to be established in a separate label to ensure they are loaded/saved correctly
    call instantiate_serum_traits() from _call_instantiate_serum_traits #Creates all of the default LR2 serum traits. TODO: Create a mod loading list that has labels that can be externally added and called here.
    call instantiate_roles() from _call_instantiate_roles
    call instantiate_business_policies()


    python:
        ##PC's Home##
        hall = Room("main hall","Home",[],standard_house_backgrounds[:],[],[],[],False,[3,3], lighting_conditions = standard_indoor_lighting)
        bedroom = Room("your bedroom", "Your Bedroom",[],standard_bedroom_backgrounds[:],[],[],[sleep_action, bedroom_masturbate_action, faq_action],False,[3,2], lighting_conditions = standard_indoor_lighting)
        lily_bedroom = Room("Lily's bedroom", "Lily's Bedroom",[],standard_bedroom_backgrounds[:],[],[],[],False,[2,3], lighting_conditions = standard_indoor_lighting)
        mom_bedroom = Room("your mom's bedroom", "Mom's Bedroom",[], standard_bedroom_backgrounds[:],[],[],[],False,[2,4], lighting_conditions = standard_indoor_lighting)
        kitchen = Room("kitchen", "Kitchen",[],standard_kitchen_backgrounds[:],[],[],[],False,[3,4], lighting_conditions = standard_indoor_lighting)
        home_bathroom = Room("bathroom", "Bathroom", [], home_bathroom_background, [], [], [], False, [0,0], visible = False) #Note: Only used by special events. Not connected to the main map
        her_hallway = Room("Front hall", "Front hall", [], standard_house_backgrounds[:],[],[],[],False,[3,3], visible = False, lighting_conditions = standard_indoor_lighting)

        ##PC's Work##
        lobby = Room(business_name + " lobby",business_name + " Lobby",[],standard_office_backgrounds[:],[],[],[],False,[11,3], tutorial_label = "lobby_tutorial_intro", lighting_conditions = standard_indoor_lighting)
        office = Room("main office","Main Office",[],standard_office_backgrounds[:],[],[],[policy_purhase_action,hr_work_action,supplies_work_action,interview_action,sell_serum_action,pick_supply_goal_action,set_uniform_action,set_serum_action],False,[11,2], tutorial_label = "office_tutorial_intro", lighting_conditions = standard_indoor_lighting)
        m_division = Room("marketing division","Marketing Division",[],standard_office_backgrounds[:],[],[],[market_work_action,set_company_model_action],False,[12,3], tutorial_label = "marketing_tutorial_intro", lighting_conditions = standard_indoor_lighting)
        rd_division = Room("R&D division","R&D Division",[],lab_background,[],[],[research_work_action,design_serum_action,pick_research_action,review_designs_action,set_head_researcher_action],False,[12,4], tutorial_label = "research_tutorial_intro", lighting_conditions = standard_indoor_lighting)
        p_division = Room("Production division", "Production Division",[],standard_office_backgrounds[:],[],[],[production_work_action,pick_production_action,trade_serum_action],False,[11,4], tutorial_label = "production_tutorial_intro", lighting_conditions = standard_indoor_lighting)
        work_bathroom = Room("work bathroom", "Work Bathroom", [], bathroom_background, [make_wall(), make_floor()], [], [], False, [0,0], visible = False)

        ##Connects all Locations##
        downtown = Room("downtown","Downtown",[],standard_downtown_backgrounds[:],[],[],[downtown_search_action],True,[6,4], lighting_conditions = standard_outdoor_lighting)

        ##A mall, for buying things##
        mall = Room("mall","Mall",[],standard_mall_backgrounds[:],[],[],[],True,[8,2], lighting_conditions = standard_indoor_lighting)
        gym = Room("gym","Gym",[],standard_mall_backgrounds[:],[],[],[],True,[7,1], lighting_conditions = standard_indoor_lighting)
        home_store = Room("home improvement store","Home Improvement Store",[],standard_mall_backgrounds[:],[],[],[],True,[8,1], lighting_conditions = standard_indoor_lighting)
        sex_store = Room("sex store","Sex Store",[],standard_mall_backgrounds[:],[],[],[],True,[9,2], lighting_conditions = standard_indoor_lighting)
        clothing_store = Room("clothing store","Clothing Store",[],standard_mall_backgrounds[:],[],[],[import_wardrobe_action],True,[8,3], lighting_conditions = standard_indoor_lighting)
        office_store = Room("office supply store","Office Supply Store",[],standard_mall_backgrounds[:],[],[],[],True,[9,1], lighting_conditions = standard_indoor_lighting)

        ##Other Locations##
        aunt_apartment = Room("Rebecca's Apartment", "Rebecca's Apartment", [], standard_house_backgrounds[:], [], [], [], False, [4, 2], None, False, lighting_conditions = standard_indoor_lighting)
        aunt_bedroom = Room("Rebecca's bedroom", "Rebecca's Bedroom", [], standard_bedroom_backgrounds[:], [], [], [], False, [3, 1], None, False, lighting_conditions = standard_indoor_lighting)
        cousin_bedroom = Room("Gabrielle's bedroom", "Gabrielle's Bedroom", [], standard_bedroom_backgrounds[:], [], [], [], False, [4,1], None, False, lighting_conditions = standard_indoor_lighting)

        university = Room("university Campus", "University Campus", [], standard_campus_backgrounds[:], [], [], [], False, [9,5], None, False, standard_outdoor_lighting)

        strip_club_owner = get_random_male_name()
        strip_club = Room(strip_club_owner + "'s Gentlemen's Club", strip_club_owner + "'s Gentlemen's Club", [], stripclub_background, [], [], [strip_club_show_action], False, [6,5], None, False, lighting_conditions = standard_club_lighting)

        mom_office_name = get_random_male_name() + " and " + get_random_male_name() + " Ltd."

        mom_office_lobby = Room(mom_office_name + " Lobby", mom_office_name + " Lobby", [], standard_office_backgrounds[:], [], [], [mom_office_person_request_action], False, [6,3], lighting_conditions = standard_indoor_lighting)
        mom_offices = Room(mom_office_name + " Offices", mom_office_name + " Offices", [], standard_office_backgrounds[:], [], [], [], False, [5,5], visible = False, lighting_conditions = standard_indoor_lighting)


        bar_location = Room("Bar", "Bar", [], standard_bar_backgrounds[:], [], [], [], False, [10,10], visible = False, lighting_conditions = standard_indoor_lighting)

        ##PC starts in his bedroom##
        mc = MainCharacter(bedroom,character_name,last_name, Business(business_name, m_division, p_division, rd_division, office, office),stat_array,skill_array,_sex_array)

        town_relationships = RelationshipArray() #Singleton class used to track relationships. Removes need for recursive character references (which messes with Ren'py's saving methods)
        mc.generate_goals()

        ##Keep a list of all the places##
        list_of_places.append(bedroom)
        list_of_places.append(lily_bedroom)
        list_of_places.append(mom_bedroom)
        list_of_places.append(kitchen)
        list_of_places.append(hall)
        list_of_places.append(her_hallway)

        list_of_places.append(lobby)
        list_of_places.append(office)
        list_of_places.append(rd_division)
        list_of_places.append(p_division)
        list_of_places.append(m_division)
        list_of_places.append(work_bathroom)

        list_of_places.append(downtown)

        list_of_places.append(office_store)
        list_of_places.append(clothing_store)
        list_of_places.append(sex_store)
        list_of_places.append(home_store)
        list_of_places.append(gym)
        list_of_places.append(mall)

        list_of_places.append(aunt_apartment)
        list_of_places.append(aunt_bedroom)
        list_of_places.append(cousin_bedroom)
        list_of_places.append(university)
        list_of_places.append(strip_club)

        list_of_places.append(mom_office_lobby)
        list_of_places.append(mom_offices)

        for room in [bedroom, lily_bedroom, mom_bedroom, aunt_bedroom, cousin_bedroom]:
            room.add_object(make_wall())
            room.add_object(make_floor())
            room.add_object(make_bed())
            room.add_object(make_window())

        room = None

        home_bathroom.add_object(make_wall())
        home_bathroom.add_object(Object("shower door", ["Lean"], sluttiness_modifier = 5, obedience_modifier = 5))
        home_bathroom.add_object(make_floor())

        kitchen.add_object(make_wall())
        kitchen.add_object(make_floor())
        kitchen.add_object(make_chair())
        kitchen.add_object(make_table())

        hall.add_object(make_wall())
        hall.add_object(make_floor())

        her_hallway.add_object(make_front_door())
        her_hallway.add_object(make_hall_carpet())
        her_hallway.add_object(make_stairs())

        lobby.add_object(make_wall())
        lobby.add_object(make_floor())
        lobby.add_object(make_chair())
        lobby.add_object(make_desk())
        lobby.add_object(make_window())

        office.add_object(make_wall())
        office.add_object(make_floor())
        office.add_object(make_chair())
        office.add_object(make_desk())
        office.add_object(make_window())

        mom_office_lobby.add_object(make_wall())
        mom_office_lobby.add_object(make_floor())
        mom_office_lobby.add_object(make_chair())
        mom_office_lobby.add_object(make_desk())
        mom_office_lobby.add_object(make_window())

        mom_offices.add_object(make_wall())
        mom_offices.add_object(make_floor())
        mom_offices.add_object(make_chair())
        mom_offices.add_object(make_desk())
        mom_offices.add_object(make_window())

        rd_division.add_object(make_wall())
        rd_division.add_object(make_floor())
        rd_division.add_object(make_chair())
        rd_division.add_object(make_desk())

        m_division.add_object(make_wall())
        m_division.add_object(make_floor())
        m_division.add_object(make_chair())
        m_division.add_object(make_desk())

        p_division.add_object(make_wall())
        p_division.add_object(make_floor())
        p_division.add_object(make_chair())
        p_division.add_object(make_desk())

        downtown.add_object(make_floor())

        university.add_object(make_grass())

        office_store.add_object(make_wall())
        office_store.add_object(make_floor())
        office_store.add_object(make_chair())

        clothing_store.add_object(make_wall())
        clothing_store.add_object(make_floor())

        sex_store.add_object(make_wall())
        sex_store.add_object(make_floor())

        home_store.add_object(make_wall())
        home_store.add_object(make_floor())
        home_store.add_object(make_chair())

        mall.add_object(make_wall())
        mall.add_object(make_floor())

        gym.add_object(make_wall())
        gym.add_object(make_floor())

        aunt_apartment.add_object(make_wall())
        aunt_apartment.add_object(make_floor())
        aunt_apartment.add_object(make_couch())
        aunt_apartment.add_object(make_table())
        aunt_apartment.add_object(make_chair())

        strip_club.add_object(make_wall())
        strip_club.add_object(make_floor())
        strip_club.add_object(make_table())
        strip_club.add_object(make_chair())
        strip_club.add_object(make_stage())

        for place in list_of_places:
            if place.public:
                if not max_num_of_random == 0:
                    ran_num = renpy.random.randint(1,max_num_of_random)
                else:
                    ran_num = 0;
                for x in range(0,ran_num):
                    the_person = create_random_person()
                    the_person.generate_home()
                    the_person.home.add_person(the_person) #We are using create_random_person instead of make_person because we want premade character bodies to be hirable instead of being eaten up by towns-folk.

        generate_premade_list() # Creates the list with all the pre-made characters for the game in it. Without this we both break the policies call in create_random_person, and regenerate the premade list on each restart.

        stripclub_strippers = MappedList(Person, all_people_in_the_game)
        add_stripclub_strippers()

        ##Global Variable Initialization##
        day = 0 ## Game starts on day 0.
        time_of_day = 0 ## 0 = Early morning, 1 = Morning, 2 = Afternoon, 3 = Evening, 4 = Night

    return
