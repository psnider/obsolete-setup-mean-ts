# Coding Style

## Tools that influence coding style
- Use a syntax highlighting editor.  
This will make individual code elements clear.  
There's no longer a need to use whitespace to separate elements that are colored differently by your editor.
MS VS Code works well.
- File merge  
  - Mac: FileMerge from XCode tool suite works fine
- File differences viewer
  - GitHub app uses an in-line view
  - MS VS Code: optionally uses an in-line view


## Style Guidelines
- Code layout should communicate structure.
- We use external modules only.  
These can be used in both node.js and the browser. Angular2 works well with external modules.
- Use longer lines when they are clarifying  
If you need to print a file, you can print it with a line wrap option.  
Most computer displays have a wide form factor.  
If you need to compare code with long lines, use a tool that supports an in-line comparison view.
- perform at most one complex action per line  
Don't cram a lot of computation or function calls onto a single line unless it is clarifying.
- A function should do only one thing.
- Strive for self-documenting code.
- Comment code that is not self-documenting.
- The entire definition of a function should fit on a single screen  
Assume a maximum of about 40 lines.
- Keep functions simple.  
Avoid having more than 7 decision points in a single function.  
Count each branch test as a decision point (if, loop).


## Naming Guidelines
- Put a regular expression in a const variable, named with a suffix of *_REGEXP*.  
This makes it simple to find all of the regular expressions in a project.
- Use longer variable names when they are clarifying
- localization function names start with 'localize'
- Do not let strings span a line
Strings that span multiple lines are impossible to analyze with simple script tools (e.g. generateCodeVocabulary.py)
- Prefer enum values that can also be used as unquoted keys.  
This also makes them easier to read in URLs.


## Anachronisms
Avoid these anachronisms:
- printers and narrow displays  
Don't optimize your code layout for printers or for narrow displays
- monochrome text
Don't use whitespace for indicating parentheses grouping


## File Structure
  - a file has these main sections (each is optional):
    - header, which includes comments, and imports and exports
    - constants and variables
    - classes and functions
    - executable code
  - use 4 blank lines to separate the header from the rest of a file
  - use 2 blank lines to separate major components in a file
  - use 1 blank lines to separate minor components or code sections in a file
  - use 4 spaces for indentation


# Filenames
The OSX file system is case-preserving but case insensitive, which can cause problems such as when different developers create a file at the same time with names that differ only be capitalization. To help prevent such problems, follow this file naming guideline from *npm*:  
- Use lowercase for package names and filenames, as well as for any related naming.


# A Code Base as a Domain Specific Vocabulary

Consider functions and variables as the components of a language that we are building.
We now have a utility to generate the vocabulary for a project: generateCodeVocabulary.py.

Each action function is a verb, that has a specific meaning, which should have the same meaning if also used in other contexts.
Condition testing functions primarily return true or false, but may instead throw an exception upon failure.
Getter functions may start with "get" or they may just be the name of the variable they access.

Each function variable should be named similarly to the general functions that it can hold.
Each object variable is a noun.

In all cases, try to keep the vocabulary as small as possible, that is, when you add a function or variable, try to name it the same as existing elements that have the same semantics. When there are multiple elements with similar semantics in the same scope, differentiate them with semantic naming (ones that convey what they represent).

Some variable names should be considered basic vocabulary and should be used consistently throughout the code base:

error: A value of type Error or string. An error may contain a message that is or is not intended for the end user.
error_text: A description of an error suitable for display to a human, perhaps an operator, perhaps an end user.


# Debug Support

chai['config'].includeStack = true; // turn on stack trace


    /*
    * DEBUG IDIOMS:
    *   use this line to print an error
               console.log(`error=${util.inspect(report.errors)}`)
    */
