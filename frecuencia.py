import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def draw_simple_circuits():
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Circuit 1: ON/OFF Circuit
    ax.text(0.1, 0.9, "Circuit 1: ON/OFF with NA and NC", fontsize=12, weight='bold')
    
    # NA Buttona
    ax.add_patch(mpatches.Rectangle((0.1, 0.8), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.12, 0.81, "NA", fontsize=10)
    # Wire to relay and bulb
    ax.plot([0.2, 0.5], [0.825, 0.825], color='black')
    
    # Relay
    ax.add_patch(mpatches.Rectangle((0.5, 0.8), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.52, 0.81, "Relay", fontsize=10)
    
    # Bulb
    ax.add_patch(mpatches.Circle((0.7, 0.825), 0.03, ec='black', fc='yellow'))
    ax.text(0.73, 0.81, "Bulb 120VAC", fontsize=10)
    
    # NC Button
    ax.add_patch(mpatches.Rectangle((0.1, 0.7), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.12, 0.71, "NC", fontsize=10)
    
    # Wire connecting NA and NC
    ax.plot([0.15, 0.15], [0.75, 0.825], color='black')
    ax.plot([0.15, 0.5], [0.725, 0.725], color='black')
    
    # Circuit 2: Control of 2 Bulbs with 3 Buttons
    ax.text(0.1, 0.55, "Circuit 2: Control 2 Bulbs with 3 Buttons", fontsize=12, weight='bold')
    
    # PB1 -> Bulb 1
    ax.add_patch(mpatches.Rectangle((0.1, 0.45), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.12, 0.46, "PB1", fontsize=10)
    ax.plot([0.2, 0.5], [0.475, 0.475], color='black')
    
    # Relay 1
    ax.add_patch(mpatches.Rectangle((0.5, 0.45), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.52, 0.46, "Relay 1", fontsize=10)
    
    # Bulb 1
    ax.add_patch(mpatches.Circle((0.7, 0.475), 0.03, ec='black', fc='yellow'))
    ax.text(0.73, 0.46, "Bulb 1", fontsize=10)
    
    # PB2 -> Bulb 2
    ax.add_patch(mpatches.Rectangle((0.1, 0.35), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.12, 0.36, "PB2", fontsize=10)
    ax.plot([0.2, 0.5], [0.375, 0.375], color='black')
    
    # Relay 2
    ax.add_patch(mpatches.Rectangle((0.5, 0.35), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.52, 0.36, "Relay 2", fontsize=10)
    
    # Bulb 2
    ax.add_patch(mpatches.Circle((0.7, 0.375), 0.03, ec='black', fc='yellow'))
    ax.text(0.73, 0.36, "Bulb 2", fontsize=10)
    
    # PB3 -> Off Both Bulbs
    ax.add_patch(mpatches.Rectangle((0.8, 0.4), 0.1, 0.05, ec='black', fc='none'))
    ax.text(0.82, 0.41, "PB3", fontsize=10)
    ax.plot([0.5, 0.85], [0.375, 0.425], color='black', lw=1, ls="--")
    ax.plot([0.5, 0.85], [0.475, 0.425], color='black', lw=1, ls="--")
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    plt.show()

draw_simple_circuits()
