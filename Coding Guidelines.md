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


# Style
- localization function names start with 'localize'
- Do not let strings span a line
Strings that span multiple lines are impossible to analyze with simple script tools (e.g. generateCodeVocabulary.py)
- Prefer enum values that can also be used as unquoted keys.  
This also makes them easier to read in URLs.

# Filenames
The OSX file system, is case-preserving but case insensitive, which can cause problems such as when different developers create a file at the same time with names that differ only be capitalization. To help prevent such problems, follow this file naming guideline from *npm*:  
- Use lowercase for package names and filenames, as well as for any related naming.


# Debug Support

chai['config'].includeStack = true; // turn on stack trace


    /*
    * DEBUG IDIOMS:
    *   use this line to print the errors
               console.log('report.errors=' + util.inspect(report.errors));
    */
