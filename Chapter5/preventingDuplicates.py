# preventingDuplicates example
voted = {}

def check_voter(name):
    if voted.get(name):
        print("Kick them out")
    else:
        voted[name] = True 
        print("let them vote")

check_voter("tom")
check_voter("elias")
check_voter("tom")