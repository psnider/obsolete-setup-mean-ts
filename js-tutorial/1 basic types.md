Use the node REPL to play with these types and their methods.

# string 
Read [string](http://www.w3schools.com/js/js_strings.asp)

## Become familiar with these features:   
- string primitives.  
Try to write strings so you can search for content with grep.  
(e.g. prefer "don't" to 'don\'t')
- Methods unrelated to HTML  
Learn the basic methods that have to do with string testing and manipulation.
These include:
    - indexOf(), lastIndexOf(), search()
    - slice()
    - toUpperCase(), toLowerCase()
    - concat()
    - replace()
    - charAt(), charCodeAt()
    - split()
    - includes()
    - match()
    - trim()
You should know how these work, and should remember they exist, but you can look up the details, so you don't need to memorize them.
- Use ===  and !==  
(instead of == and !=)

## Don't worry about these features:
- String instances.
- HTML wrapper methods


# number

Read [number](http://www.w3schools.com/js/js_numbers.asp)

Become familiar with all features.
- Use ===  and !==  
(instead of == and !=)

# boolean

Read [boolean](http://www.w3schools.com/js/js_booleans.asp)

Become familiar with all features.

Pay attention to testing of values in boolean expressions, as it's quirky in javascript.
- Prefer ===  and !==  
(instead of == and !=)
- Use == and != when testing for non-existence  
e.g. ```a == null``` or ```a != null```
- understand [truthy](https://developer.mozilla.org/en-US/docs/Glossary/Truthy) and [falsy](https://developer.mozilla.org/en-US/docs/Glossary/falsy) boolean comparisons

# Date
Read [Date](http://www.w3schools.com/jsref/jsref_obj_date.asp)

We only store UTC dates (times), never local dates.
UTC dates are used for computation, and local times are considered to be for display only.
For local time information, we store time-zones, then use those to display local times.

For string display for logs, and any computing related purpose, we use the ISO format, which is also the format used by the V8 interpreter. For example:
```new Date()``` displays: *2017-01-14T17:27:40.412Z*


## Become familiar with these features:   
- the equivalent forms of milliseconds, seconds, the ISO format of string
- constructor forms, including now()
- toISOString()
- get*()


# null and undefined
Read [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)

## Guidelines:   
- Avoid using null  
Prefer undefined.
*null*'s only use is to indicate that an object is deliberately missing, as opposed to simply not present in a data set, in which case absense is a sufficient indicator.
For example, if you were to use an sparse array to indicate the playing piece on the square of a row of a chessboard, you might use null to indicate that no piece is on a square: ```[pawn,null,null,null,null,knight,null,null]```
Another use is when you must serialize data that indicates something is missing, as undefined fields are ignored by JSON.stringify()
- test for existance of a primitive type value with ```x == null``` or ```x != null```
This construct tests x for both null and undefined.
- test for existance of an object with ```x``` or ```!x```  
If there is any chance the variable contains a primitive type, then use the previous form.
- understand the unusual comparisons of undefined  


# RegExp
Read [RegExp](http://www.w3schools.com/jsref/jsref_obj_regexp.asp)
Scan all of the features, but don't worry about memorizing them. Just know they exist.

For example:
```
var LOCALE_REG_EXP = /^[a-z]{2}_[A-Z]{2}$/
```
matches locale strings such as *en_US*

Regular expressions are complex. Use a [javascript RegExp tool](https://regex101.com/) to help you analyze them, and demonstrate correctness.


# JSON

Read all of the sections from W3 Schools:  
- [JSON Intro](http://www.w3schools.com/js/js_json_intro.asp)
- [JSON Syntax](http://www.w3schools.com/js/js_json_syntax.asp)
- [JSON vs XML](http://www.w3schools.com/js/js_json_xml.asp)
- [JSON Data Types](http://www.w3schools.com/js/js_json_datatypes.asp)  
Note that JSON supports null, but not undefined.
This is useful for creating objects that will be converted to JSON.
Prefer undefined for elements that are added to such an object.  
For example:  
```
function f(a) {
    var o = {a}
    return JSON.stringify(o)
}
```
If *a* is undefined, then it will not be added to the returned JSON, but if *a* is any other value, including null, it will.  
Use null rarely, and only when you want to show that a value is unset (as opposed to missing).
- [JSON Objects](http://www.w3schools.com/js/js_json_objects.asp)  
Prefer JSON objects for any data that might be serialized, as it is greatly simplifying.
- [JSON Arrays](http://www.w3schools.com/js/js_json_arrays.asp)
- [JSON.parse()](http://www.w3schools.com/js/js_json_parse.asp)  
If you encounter parse() problems or invalid JSON, then [http://jsonlint.com](http://jsonlint.com) is your friend.  
We convert the string value for date fields back into Date objects as soon as we finishing parsing or loading JSON. This includes when JSON is parsed by a 3rd party library such as *request* or *Angular2*.
- [JSON.stringify()](http://www.w3schools.com/js/js_json_stringify.asp)  
The only non-JSON objects we use are Dates. These are converted to a string by stringify().
- skip the JSON PHP section
- skip the JSON HTML section
