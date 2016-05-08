# Key Knowledge required about Angular JS

Created by Google

Model-view-controller framework

### Views

- Html based template
- Templates are extended with angular elements
- html elements with `ng-` attributes, these are called `angular directives`
- A directive modifies the functionality

`{{` **Double Curly Braces** indicate that data will be replaced with data binding
`{` **Single Curly Braces** replaces a reference with an object

##### Example Code

```
<ul>
  <li ng-click='buyItem(item)' ng-class="{purchased: item.status == 'purchased'}" ng-repeat="item in items">
    {{ item.name }}
  </li>
</ul>
```

### Controllers

- Connected to each view
- Js code
- Bridge between views and data models
- Concept of **scope**: shared context of view in DOM and javascript code
- Definitions of data models that angular binds to interfaces
- Business logic

##### Example code

```
.controller('ListCtrl', function($scope){
  $scope.items = [];
  $buyItem = function(){

  }
});
```

### Custom directives

- New html elements that create components
- Exactly what [ionic](https://doolan.pw/hybrib-mobile-apps-with-ionic) does

### Factors or Services

- Singleton: Class that can only have a single instantiation at a time, only 1 object will ever exist of that class
- Encapsulate shared functions
- Closely related to **dependency injection** - inject services into controllers when required

##### Example code

```
.factory('parkData', function (){
    var theParkData = [];
    return {
      initData: function (theData){ ... some code ... },
      getParks: function (){ ...some code... }
    }
  });
```
