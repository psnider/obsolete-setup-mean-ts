# Project Structure
- commonjs (or amd)
The location of package files.
- decl
- doc
- generated  
This is a temporary directory into which all compiler output is directed.
The files that are published as part of the package should be copied to the comonjs or amd directories, as appropriate.
- node-modules
- src    
All Typescript sources must be in a *ts* directory (e.g. src/\*\*/ts).
- test

.gitignore  
Makefile  
Supports *build* and *test* commands.  
package.json  
tsconfig.json

# .gitignore
Must contain at least these lines:
```
.DS_Store
generated/**
node_modules/**
**/ts/*.js
```
# package.json
 
Contains:  
[ ] scripts
```
  "scripts": {
    "test": "make test",
    "postinstall": "make npm-postinstall",
    "uninstall": "make npm-uninstall"
  },
```
[ ] dependencies  
The minimally required external dependencies.

# Makefile Targets
## Variables
```
PACKAGE_NAME=remote-mail
DEFINITELY_TYPED=~/devel/reference/borisyankov/DefinitelyTyped
```
## Required Targets
[ ] install  
```
install: 
    npm install
    make decl-install
```
[ ] decl-install  
```
dev_packages=chai mocha
dependent_packages=imap jquery mailparser  node nodemailer nodemailer-direct-transport nodemailer-smtp-transport nodemailer-smtp-pool nodemailer-pickup-transport

decl-install:
	mkdir -p decl
	$(foreach package, $(dev_packages), rm -fr decl/$(package); cp -r $(DEFINITELY_TYPED)/$(package) decl;)
	$(foreach package, $(dependent_packages), rm -fr decl/$(package); cp -r $(DEFINITELY_TYPED)/$(package) decl;)
```
[ ] npm-postinstall   
```
# if this install is for a dependent package
#     copy the declaration files into the containing project
npm-postinstall:
	@if [ -f '../../package.json' ]; then \
		echo This is a dependent package, copying Typescript declaration files into main project... ;\
		mkdir -p ../../decl ;\
		cp -r decl/$(PACKAGE_NAME) ../../decl;\
	fi
```
[] npm-uninstall   
```
# if this uninstall is for a dependent package
#     remove the declaration files from the containing project
npm-uninstall:
	@if [ -f '../../package.json' ]; then \
		rm -fr ../../decl/$(PACKAGE_NAME);\
	fi
```
[] build  
Builds all files in the package.  
Depends upon variables listing the target (javascript) files.  e.g. commonjs-js, amd-js, commonjs-test-js
[] test  
Runs all tests for package.  
[] all
```
all: build test
```

## Extra Targets, not Required
[] reports 
```
reports:
	generateCodeVocabulary.py --ext ts --out reports/src.vocabulary.json src
	generateCodeVocabulary.py --ext ts --out reports/test.vocabulary.json test/src
	-rm reports/all.vocabulary.json
	generateCodeVocabulary.py --ext vocabulary.json --out reports/all.vocabulary.json reports
	cloc-1.62.pl --force-lang-def=/Users/$(USER)/.cloc.lang_def --quiet --report-file=reports/src.cloc.txt src
	cloc-1.62.pl --force-lang-def=/Users/$(USER)/.cloc.lang_def --quiet --report-file=reports/test.cloc.txt test/src

```
