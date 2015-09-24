# React.js

## What is React.js

Javascript library for User Interfaces

* Open Source
* Built by Facebook
* Just a View
* High Speed Virtual DOM
* Uses JSX Syntax

## Why is React so fast?

* Reading and writing to the document object model (DOM) is slow
* JS Objects faster that the DOM
* React only reads from the virtual DOM
* React only writes to the real DOM
* No polling, when rendering only necessary changes are sent to the real DOM

## Developer Tools

* `react-detector` - lets you know when react is there
* `react-developer-tools` - check react elements
  - `ctrl + optn + j`

## Add the React library

```
<head>
  <script src="https://fb.me/react-0.13.3.min.js"></script>
</head>
```

## Rendering content

```
<script>
  React.render(React.createElement('div', null, 'Hello World!'), document.body);
</script>
```

## JSX: Javascript as XML

Need the JSX Transformer

Converts JSX to pure javascript

```
<script src="https://fb.me/JSXTransformer-0.13.3.js"></script>
```

Example of JSX:

```
var HelloWorld = React.createClass({
  //Render is required for every react component
  render: function(){
    return (
      **<div>
        <h1>Hello World</h1>
        <p>THis is some text</p>
      </div>**
    );
  }
});

React.render(**<HelloWorld/>**, document.body);
```

## Precompiling JSX

Better to precompile the JSX as it ill currently do it at run time. Slowing down the app.

#### Install React tools module

 ```
 sudo npm install -g react-tools
 ```

#### Runnning the precompiler

```
jsx src/ build
```
No longer need the transformer, just need a link to the built js.

## What is a React Component?

- Composable: a collection of components make up a page
- Reusable

A component is a `class` from `createClass`

To reuse the component just render the tag, but make sure it is wrapped in a `div`

## Properties

Giving components attributes, similar to html attributes

In component use:

```
<MyComponent text="hello world"/>
```

In component declaration:

```
render: function(){
  return <div>
          <h1>{this.props.text}</h1>
          <p></p>
        </div>;
}
```

`this.props` means this._properties_

#### Children Property

```
<MyComponent text="hello world">
Yo yo yo
</MyComponent>
```

You can use the content of the react component with:

```
{this.props.children}
```

## Handling Events

Add events to the component

```
var Note = React.createClass({
    <b>edit: function(){
      alert('editing note');
    },
    remove: function(){
      alert('removing note');
    },</b>
    render: function() {
      return (
        <div className="note">
          <p>{this.props.children}</p>
          <span>
            <button **onClick={this.edit}**/>
            <button **onClick={this.remove}**
            />
          </span>
        </div>
      );
    }
  });
```

## State

When state changes of a component it is **Render** is called again

#### Setting Initial state

```
getInitialState: function(){
  return {var: false}
},
```

#### Setting State

Use: `this.setState()`

Primary method to trigger use interface updates from event handlers

#### Changing State

`this.setState({checked: !this.state.checked})`

#### Accessing State

`this.state.checked`

## References

Access the properties of a DOM node

Also flow data to a chid component

#### Setting References

```
<input ref="myText" type="text"/>
```

#### Accessing References

```
var val = this.refs.myText.getDOMNode().value;
```

## Prototypes

`propTypes: { .. }`

* Part of the React library used to handle validations
* Usually a ECMAScipt Object

Eg.

```
propTypes: {
  count: function(props, propName){
    if (typeof props[propName] !== "number"){
      return new Error("The count property must be a Number ");
    }
    if (props[propName] > 100){
      return new Error("Creating " + props[propName] + " notes is ridiculous");
    }
  }
},
```

_Child components can inherit state and props_

## Keys

 To ensure the state and identity of our components is maintain throughout multiple renders we need to assign a **unique key**

## Component Lifecycle

Times of change of state during component lifetime

React provide hooks for creation, lifetime and tearDown

`getDefaultProps`
`getInitialState`
