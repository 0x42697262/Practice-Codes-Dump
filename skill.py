import math

def skill(bits=8080, cooldown=14400, bitsModifier=0.01, cooldownModifier=0.01, tries=2):
    time = 0
    for i in range(tries):
        bits = bits + math.floor(bits*bitsModifier)
        time += cooldown
        cooldown = cooldown - (cooldown*cooldownModifier)
                
    print(f"Bits: {bits} or {bits/(8*1000*1000)} megabytes\nCooldown: {cooldown} seconds or approximately {cooldown/60} minutes")
    print(f"Time spent: {time/60/60/24} days")
    
skill(bits=15744,cooldown=43240, tries=1100)
