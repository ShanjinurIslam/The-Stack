# React JS

In this section, we will learn about front-end web framework ```React.js```

## Setting Up Environment

Make sure recent ```node.js``` is installed in your system

1. In ```Terminal``` type

```` bash
npx create-react-app tic-toe
````

2. Delete all files in ```src/``` folder of the project

```bash
cd tic-toe
cd src
rm -f *
```

3. Add a file named `index.css` in the `src/` folder with [this CSS code](https://codepen.io/gaearon/pen/oWWQNa?editors=0100).
4. Add a file named `index.js` in the `src/` folder with [this JS code](https://codepen.io/gaearon/pen/oWWQNa?editors=0010).
5. Add these three lines to the top of `index.js` in the `src/` folder:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
```

6. Now if you run `npm start` in the project folder and open `http://localhost:3000` in the browser, you should see an empty tic-tac-toe field.

## Overview

### What is React? 

React is a declarative, efficient, and flexible JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called ```components```.

React has a few different kinds of components, but we’ll start with `React.Component`subclasses:

```react
class ShoppingList extends React.Component {
  render() {
    return (
      <div className="shopping-list">
        <h1>Shopping List for {this.props.name}</h1>
        <ul>
          <li>Instagram</li>
          <li>WhatsApp</li>
          <li>Oculus</li>
        </ul>
      </div>
    );
  }
}

// Example usage: <ShoppingList name="Mark" />
```

Here, ShoppingList is a **React component class**, or **React component type**. A component takes in parameters, called `props` (short for “properties”), and returns a hierarchy of views to display via the `render` method.

JSX comes with the full power of JavaScript. You can put *any* JavaScript expressions within braces inside JSX. Each React element is a JavaScript object that you can store in a variable or pass around in your program.

The `ShoppingList` component above only renders built-in DOM components like `<div />`and `<li />`. But you can compose and render custom React components too. For example, we can now refer to the whole shopping list by writing `<ShoppingList />`. Each React component is encapsulated and can operate independently; this allows you to build complex UIs from simple components.

## Inspecting the Starter Code

Open `src/index.js` in your project folder 

This Starter Code is the base of what we’re building. We’ve provided the CSS styling so that you only need to focus on learning React and programming the tic-tac-toe game.

By inspecting the code, you’ll notice that we have three React components:

- Square
- Board
- Game

The Square component renders a single `<button>` and the Board renders 9 squares. The Game component renders a board with placeholder values which we’ll modify later. There are currently no interactive components.

## Passing Data Through Props

Let’s try passing some data from our Board component to our Square component.

In Board’s `renderSquare` method, change the code to pass a prop called `value` to the Square:

```react
class Board extends React.Component {
  renderSquare(i) {
    return <Square value={i} />;
  }
  ...
}
```

```react
class Square extends React.Component {
  render() {
    return (
      <button className="square">
        {this.props.value}
      </button>
    );
  }
}
```

## Making an Interective Component

Let’s fill the Square component with an “X” when we click it. First, change the button tag that is returned from the Square component’s `render()` function to this:

```react
class Square extends React.Component {
    render() {
        console.log(this.props.index)
        return (
            <button className="square" onClick={()=>{
                alert('Click')
            }}>
            {this.props.value}
            </button>
        );
    }
}
```

If you click on a Square now, you should see an alert in your browser.

As a next step, we want the Square component to “remember” that it got clicked, and fill it with an “X” mark. To “remember” things, components use **state**.

React components can have state by setting `this.state` in their constructors. `this.state` should be considered as private to a React component that it’s defined in. Let’s store the current value of the Square in `this.state`, and change it when the Square is clicked.

First, we’ll add a constructor to the class to initialize the state:

```react
constructor(props) {
    super(props);
    this.state = {
      value: null,
    };
  }
```

In [JavaScript classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes), you need to always call `super` when defining the constructor of a subclass. All React component classes that have a `constructor` should start with a `super(props)` call.

Now we’ll change the Square’s `render` method to display the current state’s value when clicked:

- Replace `this.props.value` with `this.state.value` inside the `<button>` tag.
- Replace the `onClick={...}` event handler with `onClick={() => this.setState({value: 'X'})}`.
- Put the `className` and `onClick` props on separate lines for better readability.

After these changes, the `<button>` tag that is returned by the Square’s `render` method looks like this:

```react
render() {
    return (
      <button
        className="square"
        onClick={() => this.setState({value: 'X'})}
      >
        {this.state.value}
      </button>
    );
  }
```

By calling `this.setState` from an `onClick` handler in the Square’s `render` method, we tell React to re-render that Square whenever its `<button>` is clicked. After the update, the Square’s `this.state.value` will be `'X'`, so we’ll see the `X` on the game board. If you click on any Square, an `X` should show up.

When you call `setState` in a component, React automatically updates the child components inside of it too.