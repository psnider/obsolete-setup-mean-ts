## Install TextMate Editor
**Dependencies**: No dependencies. You may set up TextMate whenever you like.
Select version 2.* from [http://macromates.com/download](http://macromates.com/download)
Once it is downloaded, you must unzip it. You can do this from **Finder** (select the TextMat_*tbz file, then Menu-click, and choose open).
The app will be extracted in place, so you must now move the TextMate.app file into your /Applications folder.


### Configure so tabs are set to 4 spaces for all text files.
Edit the default configuration file: **/Applications/TextMate.app/Contents/Resources/Default.tmProperties** so it contains:  

```
[ text ]
softWrap         = false  
softTabs         = true  
tabSize          = 4  
showInvisibles   = true
```

### Configure so whitespace is standardized upon file save.
#### Strip trailing whitespace from all lines
Open the bundle editor (⌃⌥⌘B) or "Bundles" → "Edit Bundles..."  
and open "Text" → "Menu Actions" → "Converting / Stripping" → "Remove Trailing Spaces in Document / Selection".  

Then in the drawer put:

- Scope Selector: **-text.html.markdown**  
  This setting causes TextMate to not strip trailing whitespace from MarkDown documents, since trailing whitespace is significant in MarkDown.
- Semantic Class: **callback.document.will-save**  
- Input: **Document**  
- Output: **Replace Document**  

These instructions were taken from the article [Strip trailing whitespace on Save with …callbacks!](http://tm2tips.tumblr.com/post/42657705618/strip-trailing-whitespace-on-save-with-callbacks)

#### Convert tabs to spaces upon file save.
Specify that our Makefiles are the correct type, by running the following two commands:

```
echo '[ Makefile.* ]' >> ~/.tm_properties
echo 'fileType             = "source.makefile"' >> ~/.tm_properties
```

Open the bundle editor (⌃⌥⌘B) or "Bundles" → "Edit Bundles..."  
and open "Source" → "Menu Actions" → "Convert Tabs to Space".  

Then in the drawer put:

- Scope Selector: -source.makefile
- Semantic Class: **callback.document.will-save**
- Input: **Document**
- Output: **Replace Document**
- Caret Placement: Character Interpolaion

Confirm the installation:
Create a file with a ".txt" extension. Add a line of text with preceding tabs and ending with some spaces.
Save the file.
Confirm that the tabs have been converted to spaces, and that the trailing spaces have been removed.

Now do create a file with a "\*.md" extension. Add a line of text ending with some spaces.
Save the file.
Confirm that the trailing spaces have NOT been removed.

#### Add file pathname to title bar.
Modify the following shell command to contain your home directory, then run it.  
It will add configuration to the TextMate config file for your user.

```
echo 'windowTitle    = "$TM_DISPLAYNAME${TM_DIRECTORY/\A(?:\/Users\/$USER\w+\/?(.*)|(.+))\z/${2:? – ${2/\A\/Users\/$USER/~/}:${1/\A(?=.)/ – /}}/}"' >> ~/.tm_properties
```

#### Exclude some directories from file search
Run this shell command to add this configuration to the TextMate config file for your user.

```
echo 'excludeInFolderSearch = "{$excludeInFolderSearch,$extraExcludes,node_modules,bower_components,generated,amd,commonjs,cache,doc}"' >> ~/.tm_properties
```


