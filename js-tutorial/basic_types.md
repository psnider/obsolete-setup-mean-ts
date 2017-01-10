Use the node REPL to play with these types and their methods.

# string 
Read [string](http://www.w3schools.com/js/js_strings.asp)

## Become familiar with these features:   
- string primitives.  
Try to write strings so you can search for content with grep.  
(e.g. prefer "don't" to 'don\'t')
- Methods unrelated to HTML  
Learn the basic methods that have to do with string testing and manipulation, 
such as charAt(), includes(), match(), etc.  
You should know how these work, and should remember they exist, but you can look up the details, so you don't need to memorize them.
- Use ===  and !==  
(instead of == and !=)

## Don't worry about these features:
- String instaces.
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
