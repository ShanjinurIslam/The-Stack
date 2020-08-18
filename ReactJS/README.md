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

## Lifting State Up

Currently, each Square component maintains the game’s state. To check for a winner, we’ll maintain the value of each of the 9 squares in one location.

The best approach is to store the game’s state in the parent Board component instead of in each Square. The Board component can tell each Square what to display by passing a prop, just like we did when we passed a number to each Square

**To collect data from multiple children, or to have two child components communicate with each other, you need to declare the shared state in their parent component instead. The parent component can pass the state back down to the children by using props; this keeps the child components in sync with each other and with the parent component.**

Lifting state into a parent component is common when React components are refactored — let’s take this opportunity to try it out.

Add a constructor to the Board and set the Board’s initial state to contain an array of 9 nulls corresponding to the 9 squares:

```react
class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
    };
  }

  renderSquare(i) {
    return <Square value={i} />;
  }
```

We have already defined the `squares` array in the Board’s constructor, and we will modify the Board’s `renderSquare`method to read from it:

```react
renderSquare(i) {
    return <Square value={this.state.squares[i]} />;
  }
```

Each Square will now receive a `value` prop that will either be `'X'`, `'O'`, or `null` for empty squares.

Next, we need to change what happens when a Square is clicked. The Board component now maintains which squares are filled. We need to create a way for the Square to update the Board’s state. Since state is considered to be private to a component that defines it, we cannot update the Board’s state directly from Square.

Instead, we’ll pass down a function from the Board to the Square, and we’ll have Square call that function when a square is clicked. We’ll change the `renderSquare` method in Board to:

```jsx
renderSquare(i) {
    return (
      <Square
        value={this.state.squares[i]}
        onClick={() => this.handleClick(i)}
      />
    );
  }
```

We defined ```handleClick(i)``` function

```javascript
handleClick(i){
        const squares = this.state.squares.slice();
        squares[i] = 'O';
        this.setState({squares: squares});
    }
```

We modified ```Square``` component to be compitable with the changes made this step before 

```jsx
class Square extends React.Component {
  render() {
    return (
      <button
        className="square"
        onClick={() => this.props.onClick()}
      >
        {this.props.value}
      </button>
    );
  }
}
```

After these changes, we’re again able to click on the Squares to fill them, the same as we had before. However, now the state is stored in the Board component instead of the individual Square components. When the Board’s state changes, the Square components re-render automatically. Keeping the state of all squares in the Board component will allow it to determine the winner in the future.

Since the Square components no longer maintain state, the Square components receive values from the Board component and inform the Board component when they’re clicked. In React terms, the Square components are now **controlled components**. The Board has full control over them.

Note how in `handleClick`, we call `.slice()` to create a copy of the `squares` array to modify instead of modifying the existing array. We will explain why we create a copy of the `squares` array in the next section.

### ## Function Components

We’ll now change the Square to be a **function component**.

In React, **function components** are a simpler way to write components that only contain a `render` method and don’t have their own state. Instead of defining a class which extends `React.Component`, we can write a function that takes `props` as input and returns what should be rendered. Function components are less tedious to write than classes, and many components can be expressed this way.

Replace the Square class with this function:

```jsx
function Square(props) {
  return (
    <button className="square" onClick={props.onClick}>
      {props.value}
    </button>
  );
}
```

We have changed `this.props` to `props` both times it appears

## Taking Turns

We now need to fix an obvious defect in our tic-tac-toe game: the “O”s cannot be marked on the board.

We’ll set the first move to be “X” by default. We can set this default by modifying the initial state in our Board constructor:

```jsx
class Board extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      squares: Array(9).fill(null),
      xIsNext: true,
    };
  }
```

## Declaring a Winner

Now that we show which player’s turn is next, we should also show when the game is won and there are no more turns to make. Copy this helper function and paste it at the end of the file

```javascript
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
```

Given an array of 9 squares, this function will check for a winner and return `'X'`, `'O'`, or `null` as appropriate.

We will call `calculateWinner(squares)` in the Board’s `render` function to check if a player has won. If a player has won, we can display text such as “Winner: X” or “Winner: O”. We’ll replace the `status` declaration in Board’s `render` function with this code:

```jsx
const winner = calculateWinner(this.state.squares);

        const condition = this.state.squares.includes(null);

        let status;
        if (winner) {
        status = 'Winner: ' + winner;
        } 
        else if(!condition){
            status = 'Match is drawn';
        }
        else {
        status = 'Next player: ' + (this.state.xIsNext ? 'X' : 'O');
        }
```



