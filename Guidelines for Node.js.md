# Guidelines:
- Use external modules (and never internal).
Node.js uses commonjs format modules, which are external by definition.  
External modules can be shared with other projects.  
- Every external module must have a corresponding decl file.
- modules are named with quotes:  e.g. declare module "A" {} 
- prefer smaller modules over larger
- modules should export only the minimum required
- every module should compile standalone
- every module should have a test that covers that module's public interface
- interfaces that are used by just one module should be defined by that module
- classes should have corresponding interfaces when those classes are marshalled or unmarshalled
- any object that is marshalled or unmarshalled, and which cannot be reconstructed by plain JSON.parse(), must have a function convertJSONObjToObj(), which converts any complex fields, such as those of type Date.
- Avoid classes until them become necessary. It keeps the code lighter.
- Keep a application vocabulary dictionary, to help manage the number of symbol names in the app.
- use import when appropriate, and not var
- Keep declaration files in a ./decl directory.  
And keep imported files in a ./decl/import directory.
- Reference explicit versions in your package.json files, and update dependent packages explicitly.  
Many npm packages don't follow semantic versioning properly, so this is the best way to protect your projects.

# npm module creation Guidelines:
- each package.json must support the test target via:
```
  "scripts": {
    "test": "make test",
    "postinstall": "make npm-postinstall"
  },
```
See the notes below regarding implementing the npm-postinstall target.
- All Typescript declarations follow the conventions used by https://github.com/borisyankov/DefinitelyTyped
  - each declaration file must be in a subdirectory with the same name as its npm package name
- Each Typescript npm module contains its Typescript declaration files in the **./decl** directory
- Typescript declaration files should be copied to owning packages upon installation:
  - A Makefile for a package named PACKAGE and which has declaration files should contain a post-install target similar to:
```make
npm-postinstall:
    # if this install is for a dependent package
    @if [ -f '../../package.json' ]; then \
        # copy the declaration files into the requesting project
        echo This is a dependent package, copying Typescript declaration files into main project... ;\
        mkdir -p ../../decl ;\
        cp -r decl/PACKAGE ../../decl;\
    fi
```
<aside class="warning">
Note that you must use tabs for indentation in Makefiles, and that they don't render properly in MarkDown.
</aside>



# Style:
- Align require statements at column 40  
Requires are easier to read if aligned. 40 columns allows even space for local and imported package names. 
- Reference paths should be the shortest path relative to the referencing file's path.  
And not returning to the root, unless required.



# Issues for which I still need to develop guidelines
- When should module names include a dot  '.' or a slash '/'  ?
- When can modules be combined?
- How to best manage importing declaration files from DefinitelyTyped
- How to best manage errors found in others' packages or declaration files
