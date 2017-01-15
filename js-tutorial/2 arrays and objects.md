Use the node REPL to play with these types and their methods.

# array 
Read [array (from w3schools)](http://www.w3schools.com/js/js_arrays.asp), [methods](http://www.w3schools.com/js/js_array_methods.asp), and [sort](http://www.w3schools.com/js/js_array_sort.asp)  
Also: [array (from MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

## Become familiar with these features:   
- creation  
Prefer the array literal notation: ```[]```  
Prefer variable names that indicate a plural.
- access  
- main methods:  
  - push(), pop(), shift(), unshift()
  - indexOf(), lastIndexOf()
  - splice()
  - concat()
  - slice()
  - sort(CompareFunction)  
    It almost never makes sense to use the default sort order.
  - test whether object is array with ```Array.isArray(array_var_name)``` or ```array_var_name instanceof Array```
- JS6 methods
  - [forEach()](http://www.w3schools.com/jsref/jsref_foreach.asp)
  - [map()](http://www.w3schools.com/jsref/jsref_map.asp)
  - [every()](http://www.w3schools.com/jsref/jsref_every.asp)
  - [some()](http://www.w3schools.com/jsref/jsref_some.asp)
  - [find()](http://www.w3schools.com/jsref/jsref_find.asp), [findIndex()](http://www.w3schools.com/jsref/jsref_findindex.asp)


# object

Read [object (from w3schools)](http://www.w3schools.com/js/js_objects.asp)  
Also [object (from MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)


## Become familiar with these features:   
- creation  
Prefer the object literal notation: ```{}```  
- access  
- main methods:  
  - Object.assign()
  - Object.keys()

Understand that JS doesn't support deep copying of objects,
so when you want data to keep separate copies, you must explicitly deep copy using some utility, such as [deep-extend](https://www.npmjs.com/package/deep-extend).

