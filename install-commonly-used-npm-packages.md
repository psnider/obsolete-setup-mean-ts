# Notes on common packages

## Typescript  
We use [TypeScript](http://www.typescriptlang.org) whenever possible, because it adds strong typing to javascript.  
Use npm to install typescript:
```
npm install typescript
```
To update:  
```
npm cache clean
npm update typescript
```
## Typescript Declaration Files Manager
We use the [TypeScript Definition manager for DefinitelyTyped](https://github.com/DefinitelyTyped/tsd) for managing TypeScript declaration files.  
However, it appears that [Typings is replacing TSD](https://github.com/DefinitelyTyped/tsd/issues/269), so we will be moving to Typings soon.

Use npm to install tsd:
```
npm install tsd
```
To update:  
```
npm cache clean
npm update tsd
```
- Test Framework  
We use [Mocha](http://visionmedia.github.io/mocha/) because it is flexible,
and karma to connect to browsers for the client.  
Use npm to install both:

```
npm install mocha karma karma-mocha karma-requirejs karma-chrome-launcher karma-firefox-launcher
```
## Source Debugger  
We'll use [Node Inspector](https://github.com/node-inspector/node-inspector/blob/master/readme.md) for source level debugging of node programs, including mocha tests.  
Use npm to install node-inspector:

```
npm install node-inspector
```
## Web Development Framework  
We use [express](https://npmjs.org/package/express), because it provides simple routing.
```
npm install express
```

## Client package management  
We use bower, when npm isn't supported.

See the Bower page: [http://http://bower.io/](http://http://bower.io/)
```
npm install bower
```
