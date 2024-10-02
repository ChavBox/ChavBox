Controllers work together with game-state and simulator

**Game State** - provides access to a complete description of current state of game world
**Simulator** - makes changes to the game state based on rules
**Controllers** - Select actions that get sent to the simulator 

### Actions
	actions are what change our game state 
Simulator resolves the effects of actions on game state, (one at a time)

E.g. activating an exploding device
- activation sets device to on
- after some duration, device controler generates explode action
- causes simulator to play animations of explosions and fling characters around
- Might result in death of character that was NPC's friend
- Could cause NPC to choose a "shoot" action aimed at character who set explosive
- And so on...

### Controllers
Select actions that get sent to the Simulator
- Simulator requests actions from characters' associated controlelrs

Can also parameterize controllers
e.g. "braveness" parameter as a threshold in a test to decide if something should run away

#### Hierarchical Control 
	Controllers can be layered with sub-controllers
- Low level controllers that perform basic tasks (path following)
- Mid level controllers (plan paths)
- Higher level controllers (e.g. Intent Generator) to determine NPC modivations and intentions. 