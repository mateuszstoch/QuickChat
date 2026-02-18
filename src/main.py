from pynput import keyboard
import random 
import time

early_game = [
    "Are you ready? Let's dominate this rift!", "Good luck everyone, let's do this!!!",
    "First blood is ours, I can feel it!", "Time to show them some real skill!",
    "Let's win every lane! Go go go!", "I'm 100% focused. Let's get that W!",
    "GL HF! Let's make this an epic game!", "Watch my mechanics, I'm feeling sharp today!",
    "Perfect day for a victory! Who's with me?", "Let's secure the early lead!",
    "I'm going all in! Support me!", "My farm is going to be legendary!",
    "Aggressive play starts now!", "No mercy in this lane!", "Let's tapure them from second one!",
    "Are you guys hyped? Because I am!!!", "This is where legends are made!",
    "Check my pings, let's coordinate!", "Victory starts at level 1!",
    "I'm ready for the outplays!", "Let's show them what teamwork looks like!",
    "Building my lead... watch out!", "My lane, my rules!", "Ready for the first gank!",
    "Let's get that early Dragon priority!", "I'm not here to play, I'm here to win!",
    "Stay sharp, let's catch them off guard!", "First turret is our priority!",
    "I'm feeling like a pro today!", "Let's make some noise on the rift!",
    "Confidence is key! Let's crush them!", "Smooth moves and clean plays only!",
    "I've got the vision, I've got the skill!", "Let's start the snowball!",
    "Nobody stops us today!", "Are you ready to climb the ranks?",
    "Fast hands, fast wins!", "Let's set the tempo of this match!",
    "My ignite is ready for that first blood!", "Time to make them tilt!",
    "Perfect execution starts now!", "Let's be the heroes of this match!",
    "Follow my lead, I know the way!", "Ready for action! Let's goooo!",
    "Eyes on the map, hearts on the win!", "I'm just getting my momentum!",
    "Every minion counts, every kill matters!", "Let's be everywhere on the map!",
    "I'm ready to carry this!", "Teamwork makes the dream work!",
    "Let's give them a game they'll never forget!", "Starting strong, finishing stronger!",
    "Who's ready for some high-level plays?", "I'm in the zone!",
    "Let's keep the energy high!", "My combos are ready!",
    "No mistakes, just wins!", "Let's outplay everyone!",
    "The rift is ours today!", "Ready to rumble!", "Let's go for the gold!",
    "I'm feeling unstoppable already!", "Watch this opening move!",
    "Pure skill, zero luck!", "Let's make them regret queuing up!",
    "I'm the master of this lane!", "Ready, set, VICTORY!"
]

mid_game = [
    "I'm just getting warmed up!!!", "I haven't even started yet, watch this!",
    "My first item is done, now it's real!", 
    "I'm starting to feel the power flow!", "Mid game belongs to us!",
    "Who's ready for a teamfight? I am!", "Let's secure that Rift Herald!",
     "You haven't seen my true power yet!",
    "Watch me carry these teamfights!", "I'm just getting my rhythm now!",
     "I'm 2 steps ahead of them!",
    "My ultimate is ready, let's engage!!!",
    "I'm just testing my limits... and I have none!", "Is that all they've got?",
    "I'm becoming a monster! Keep supporting!", 
    "My damage is through the roof!", "I'm just starting to enjoy this!",
    "The comeback? No, this is a total sweep!", "I'm feeling invincible right now!",
    "I'm just getting the hang of their patterns!",
    "Watch this flank! It's going to be epic!", "I haven't even used my full combo yet!",
    "I'm the king of the mid-game!", "Let's break their defense down!",
    "My build is coming together perfectly!", "They can't handle this tapure!",
    "I'm just starting the engine, wait for it!", "Team, we are doing amazing! Keep going!",
    "I'm reading them like an open book!", "Let's turn this match into a highlight reel!",
    "My energy is over 9000 right now!", "Stay together, win together!",
    "I'm just getting my first power spike!", "Watch me outplay them 1v2!",
    "Let's sweep the wards and take control!", "I'm feeling like a challenger today!",
    "No backing down, we have the lead!", "I'm just getting my focus back!",
    "I'm the wildcard they didn't expect!",
    "My skillshots are landing 100%!", "Let's snowball this to the end!",
    "I'm just starting to have real fun!", "Watch my cooldowns, then we go!",
    "I'm a machine on the battlefield!", "Let's dominate the river!",
    "I'm just finding my true form!", "Precision and power, that's me!",
    "Let's take all the outer turrets!", "I'm feeling a quadra kill coming!",
    "My confidence is peaking!", "Let's show them what a real team looks like!",
    "I'm just starting to peak!", "No escape for them now!",
    "I'm the nightmare they can't wake up from!", "Let's secure the map!",
    "I'm just getting my secondary items, watch out!", "Unstoppable force incoming!",
    "I'm the definition of a carry!", "Let's keep the tempo!", "I'm ready for the big plays!"
]

late_game = [
    "I haven't even started yet!!! The real fight begins now!",
    "Behold my final form! I am unstoppable!", "Full build reached. It's game over for them!",
    "One teamfight to rule them all!",
    "Witness my true power on the rift!",
    "Nexus is in sight! Don't stop now!", "I'm the carry you were waiting for!",
    "I'm just starting to show my real mechanics!", "One shot, one kill. No exceptions!",
    "Let's end this with style!", "I'm the god of this match!",
    "Elder Dragon or victory? Why not both!", "I'm just getting my final upgrade!",
    "They can't even touch me! I'm too fast!", "My damage is literally insane right now!",
    "Let's siege their base! No mercy!", "I haven't even broken a sweat yet!",
    "Watch me melt their health bars!", "I'm the reason we win this game!",
    "Final push! Give it everything you've got!", "I'm playing at 200% capacity!",
    "This is my playground, they're just guests!", "I'm just getting my pentakill ready!",
    "Victory is inevitable! Follow me!", "I'm the legend they'll talk about!",
    "Let's finish this! For the glory!", "I'm just starting to unleash the beast!",
    "Nothing can stand in my way now!", "I'm the apex predator here!",
    "Watch this final engage! It's going to be legendary!", "I haven't even reached my peak yet!",
    "I'm the master of the late game!", "Let's crush their dreams once and for all!",
    "My ultimate is a weapon of mass destruction!", "I'm just getting my finishing moves ready!",
    "Total dominance achieved!", "I'm the MVP, no doubt about it!",
    "Let's close the book on this match!", "I'm just starting to feel like a god!",
    "Every move I make is a masterpiece!", "I'm the carry they fear!",
    "Let's take the Nexus and the LP!", "I'm just getting my victory dance ready!",
    "Unstoppable, undefeatable, unbelievable!", "I haven't even used my full potential!",
    "Watch the replay, I'm a genius!", "I'm the heart of this team!",
    "Let's end this game in 60 seconds!", "I'm just starting to get my triple kills!",
    "I'm the storm that is approaching!", "Let's make this the best finish ever!",
    "I'm just starting to feel the ultimate hype!", "GG WP incoming! Let's win!",
    "I'm the king of the Nexus!", "Let's go for the grand finale!",
    "I'm just starting to enjoy the destruction!", "Watch me 1v5 their whole team!",
    "I'm the hero of the Rift!", "Let's seal the win!",
    "I haven't even peaked! Watch this!", "I'm the master of the final push!",
    "Let's give them a 5-man ace!", "I'm just getting my victory speech ready!",
    "Witness the perfection of my play!", "I'm the endgame boss!",
    "Let's finish this and go for another win!"
]

controller = keyboard.Controller()

def send_message(msg_list):
    controller.press(keyboard.Key.enter)
    controller.release(keyboard.Key.enter)
    
    time.sleep(0.05) 
    
    controller.type(f"/all {random.choice(msg_list)}")
    
    time.sleep(0.05)
    
    controller.press(keyboard.Key.enter)
    controller.release(keyboard.Key.enter)

def exit_script():
    quit()

def type_early(): send_message(early_game)
def type_mid(): send_message(mid_game)
def type_end(): send_message(late_game)

with keyboard.GlobalHotKeys({
        '[': type_early,
        ']': type_mid,
        '\\': type_end,
        '<f10>': exit_script}) as h:
    h.join()
