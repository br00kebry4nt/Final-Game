import pygame
import time

pygame.init()
pygame.mixer.init()

def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play(-1)

def stop_audio():
    pygame.mixer.music.stop()

def play_sound_effect(audio_file):
    pygame.mixer.Sound(audio_file).play()

def display_status(health, score):
    print(f"Health: {health} | Score: {score}")

def main():
    print("You are stranded in the jungle!")
    play_audio("birdsong.mp3") 
    getGame()
    stop_audio()

def getGame():
    health = 100 
    score = 0 
    timer = 120  
    
    gameNodes = {
        "start": ("You are stranded in the jungle. What will you do?", 
                  ["Build a Shelter", "Explore the Jungle"], 
                  ["shelter", "explore"]),
        "shelter": ("You build a lean-to shelter and rest.", 
                    ["Continue exploring", "Quit"], 
                    ["explore", "quit"]),
        "explore": ("You venture into the jungle and face obstacles.", 
                    ["Cross the river", "Face a wild animal"], 
                    ["river", "animal"]),
        "river": ("You approach a river. It looks dangerous to cross.", 
                  ["Find a rope", "Attempt to cross"], 
                  ["rope", "drown"]),
        "rope": ("You find a rope and successfully cross the river.", 
                 ["Continue exploring", "Quit"], 
                 ["explore", "quit"]),
        "animal": ("A jaguar is watching you closely.", 
                   ["Fight with your machete", "Run away"], 
                   ["fight", "quit"]),
        "fight": ("You fight the jaguar with your machete and survive. You're safe for now.", 
                  ["Continue exploring", "Quit"], 
                  ["explore", "quit"]),
        "drown": ("You tried to cross the river but were swept away. You drowned. Game Over.", [], []),
        "quit": ("Game Over. Thanks for playing!"),
    }

    currentNode = "start"
    while currentNode != "quit" and timer > 0:
        display_status(health, score)
        print(f"Time remaining: {timer} seconds")
        time.sleep(1)
        timer -= 1 
        currentNode = playNode(currentNode, gameNodes, health, score)

    if timer <= 0:
        print("\nTime's up! You didn't survive the jungle in time. Game Over!")
        play_sound_effect("levelup.mp3")

def playNode(node, gameNodes, health, score):
    description, options, outcomes = gameNodes[node]
    
    print(description) 
    
    if len(options) == 0: 
        return "quit"
    else:
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        choice = input(f"Your choice (1-{len(options)}): ")

        if choice.isdigit() and 1 <= int(choice) <= len(options):
    
            new_outcome = outcomes[int(choice) - 1]

            if new_outcome == "drown":
                health = 0 
                print("You have died!")
                play_sound_effect("wave.mp3")
            elif new_outcome == "fight":
                score += 10 
                print("You survived the jaguar fight!")
                play_sound_effect("levelup.mp3") 
            elif new_outcome == "quit":
                print("You quit the game.")
                play_sound_effect("levelup.mp3") 

            return new_outcome
        else:
            print("Please choose a valid option.")
            return node  

if __name__ == "__main__":
    main()