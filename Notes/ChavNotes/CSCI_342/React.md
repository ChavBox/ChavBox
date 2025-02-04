#### React Architecture (MVC)
Model mostly works with business logic
View fetches logic from an api or package to display on page
Controller is the mediator between the model and the view

#### Packages
**NPM**
- Node package manager
- Package manager for Node.js and Javascript
- Two main parts:
	- Command line interface (CLI) took for publishing and downloading packages
	- Online repository that hosts Javascript packages

**Installing Packages**
- npm install \<package name\>


#### DOM
	Document Object Model
The structural representation of all nodes in HTML document
It represents the UI of your application

#### VDOM
	The virtual representation of the real DOM
**React Methods**
createElement()
- Type: type of html element
- Props: properties
- Children

#### Vite
- Modern front-end build tool that provides a faster and leaner development experience for web projects
- Works with Vue, React, Svelte, and Javascript
- Includes built-in support for TypeScript

#### Folders and File Structure
- Node modules folder
	- installed packages go here
- public
	- contains static data for project
- src
	- contains primary source code for application
- Make sure to gitignore env file which has keys and passwords

#### JSX
	Javascript extensable markup language

### Keys 
List - collection of items
	Use map to create JSX elements from an array
	Pass props to each item
	e.g. TODO list, 
```
const list = ["item 1", "item 2", ...]
return(
  <>
	  map(list) => {
	  <ul>
		{item}
	  </ul>
)

```


### Styling
CSS-in-JS libraries
- install available libraries to use with JS
```
Inline-Style
//object
const heading = {
	color: 'blue',
	fontSize: '20px'
}

<div>
	<h1 style={heading}></h1>
</div>

<div>
	<h1 style={{color: 'red', fontSize: '32px'}}></h1>
</div>


CSS-Style
//Seperate file with .css extension
In .js file: import './App.css';

Conditional Styling
//use terinary operator to select class to style given component

CSS Modules
//create seperate style and import the module
import styles from './Button.module.css'

CSS-in-JS
//write css directly in JS code using objects to represent the styles
//many popular CSS-in-JS libraries to choose from
import {css, jsx} from '@emotion/core';

Sass
//css pre-processor
//files are executed on the server and sends css to the browser
//extension is .scss
npm install sass

Tailwind css
//utility first css framework
//reusable classes for styling
//customizable and mobile-first features
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch
```
