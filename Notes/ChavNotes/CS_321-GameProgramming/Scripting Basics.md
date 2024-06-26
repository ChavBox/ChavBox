A scripting language is something that is used to define and control game logic/behavior.

# Anatomy

- Using: import/include package 
- Scripts will inherit from Mono-behavior
- Access modifiers are same as java (private, public, protected)
- Scripts only handle one job
	- One for tracking HP
	- One for stamina
	- Etc
- Use inheritance to avoid repetitive code
	- Enemy super class
		- Orc
			- Orc King
			- Orc Grunt
			- etc

### Methods
	Start with a capital letter: e.g. CheckIfAlive()
	Must call from update()
	Make sure a script is attached to a game object in the scene
Start:
- runs once you hit play
Update:
- runs once per frame
Variables:
- can change public fields in Inspector
- String comparison uses ==


# Game Object Manipulation

GetComponent\<T\>( ): will access an objects component, e.g.
- GetComponent\<CapsuleCollider>;

Edit an objects components:
- transform.Translate
- transform.Rotate

Input Manager
- Input.GetKeyDown
- Input.GetMouseButton
- Input.GetAxis
- etc

# Script Communication

