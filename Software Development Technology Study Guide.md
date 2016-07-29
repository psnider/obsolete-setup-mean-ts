# Software Development Technology Study Resources and Help

# HTML5

## Prerequisites

- familiarity with web pages

## Tutorials

**Basics**
- http://www.tutorialrepublic.com/html-examples.php  
This covers the older core of HTML, still used by HTML5.
View the examples, to understand what can be done with the basic elements.
### Great Examples
Studying existing great work is the best way to learn how to do great work.  

Most existing tutorials use a book metaphor.
Don't use these except for reference and backfill!  

Here are some great examples:
http://www.creativebloq.com/web-design/examples-of-html-1233547


### Book Metaphor Tutorials (for reference and backfill!)
- http://www.tutorialspoint.com/html5/  
Don't read the tutorial front to back.  
Read the parts that are relevant to the project you're working on.
- http://www.w3schools.com/html/html_examples.asp  
Read the **{some subject} explained** sections.

## Resources

- [HTML5 Weekly newsletter via email](http://html5weekly.com/)  
Subscribe to keep up on latest HTML5 news.
- [http://html5doctor.com/](http://html5doctor.com/)  
Has up to date references on best practices for HTML5.
- [http://html5doctor.com/element-index/](element index)  
You can study the element tags from here, as you need them.
- [http://gs.statcounter.com/](http://gs.statcounter.com/)  
 This shows recent browser usage statistics globally:  
- [http://caniuse.com/](http://caniuse.com/)
This shows status of each HTML5 feature in major browsers.
- [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

### Upcoming
four related W3C specifications:
- Custom Elements - Enables the extension of HTML through custom tags.
- HTML Imports - Enables packaging of various resources (HTML, CSS, JS, etc.).
- Template Element - Enables the inclusion of inert HTML in a document.
- Shadow DOM - Enables encapsulation of DOM and CSS.



# CSS3
## Prerequisites
- some familiarity with HTML

## Tutorials and Examples

- http://www.w3schools.com/css/css_examples.asp  
Read the **{some subject} explained** sections.
- http://tutorialzine.com/2014/07/20-impressive-css3-techniques-libraries-and-examples/  
  - the loading indicators should indicate the current network state (fast, degraded, slow)
- https://css3playground.com/hover/
- http://www.tutorialrepublic.com/css-examples.php  
The coding style of these examples appears to be more in line with modern conventions. There are no style attributes on HTML, only class.
- http://bavotasan.com/2010/draw-smiley-face-css3/
- http://1stwebdesigner.com/css-effects/

## Resources
- [Trello CSS Guide](https://gist.github.com/bobbygrace/9e961e8982f42eb91b80)
- Interactive Design
  - [On/Off switch](https://proto.io/freebies/onoff/)
  - [CSS clip-path maker](http://bennettfeely.com/clippy/)
- Tools
  - [NativeScript Image Builder](http://nsimage.brosteins.com/)

# Javascript
## Prerequisites
- some programming, preferably with a dynamic language

## Tutorials
- [JavaScript Design Patterns](https://addyosmani.com/resources/essentialjsdesignpatterns/book/)
- [Microsoft's Reactive Extensions (Rx) Library](http://reactivex.io/learnrx/)

## Resources
- [JavaScript Weekly newsletter via email](http://javascriptweekly.com/)  
Subscribe to keep up on latest JavaScript news.
- **node** Read-Eval-Print-Loop (REPL) interpreter  
The interpreter allows you to test javascript code in an interactive environment.
- Javascript function patterns
[http://www.adequatelygood.com/JavaScript-Module-Pattern-In-Depth.html](http://www.adequatelygood.com/JavaScript-Module-Pattern-In-Depth.html)
- [ECMAScript 2017 Language Specification](https://tc39.github.io/ecma262/)

# TypeScript
## Prerequisites

- some Javascript
- experience with a typed language like C++

## Resources

- The [main site](http://www.typescriptlang.org) has many resources.  
- This video explains the [design of Typescript](http://media.ch9.ms/ch9/c3e5/e5e02f2e-5962-48db-9ddd-85e27a4fc3e5/IntroducingTSAndersH_mid.mp4)
- on-line [Playground](http://www.typescriptlang.org/Playground/)  
Use this to learn the basics of how TypeScript is translated into javascript.  
Keep in mind that this doesn't work with external modules.
- [TypeScript Modules Demystified : Internal, AMD with RequireJS](http://www.youtube.com/watch?v=KDrWLMUY0R0)
- You can ask questions live using a [web-based IRC chat client](https://webchat.freenode.net).  
  Pick any user name, and specify the **typescript** channel.

Notes on IRC:

- You can use [pastebin](http://pastebin.com) to transfer code or data to people anonymously.
- You can get a short URL from the [Google URL Shortener](http://goo.gl)





# Node.js
##Prerequisites

- none, if just using the node Read-Eval-Print-Loop (REPL)
- strong Javascript, if writing server apps
## Tutorials
- https://www.joyent.com/developers/node/design

## Resources

- [Node.js Weekly newsletter via email](http://nodeweekly.com/)  
Subscribe to keep up on latest Node.js news.
- The [main site](http://nodejs.org) has many resources
- The [API reference](http://nodejs.org/api)
- You can ask questions live using a [web-based IRC chat client](https://webchat.freenode.net).  
  Pick any user name, and specify the **node.js** channel.
- [Three Years of Node.js in Production](https://www.joyent.com/developers/videos/reflections-on-three-years-of-nodejs-in-production)
- [zone.js](https://github.com/btford/zone.js/blob/master/lib/core.js)
- [Testing Angular 2 apps](https://developers.livechatinc.com/blog/testing-angular-2-apps-routeroutlet-and-http/)
- [ng2-table](http://valor-software.com/ng2-table/)
- [Techniques and practices for testing an Angular 2 app](https://angular.io/docs/ts/latest/guide/testing.html)
- [Jeff Harrel of PayPal: 9 Anti-Patterns for Node.js Teams](https://www.youtube.com/watch?v=6phif2t-wj0)
  - Monolithic Applications
  - Googling How do you do X in javascript?
  - Handling Errors
  - Wrapping everything in Promises
  - Git URLs in your package.json
  - Sloppy async code
  - Having Node do everything
  - Ignoring the Node ecosystem


# Mocha
## Prerequisites
- some javascript, node.js

## Tutorials

## Resources
- http://chaijs.com/api/bdd/  
The expect operations for BDD (Behavior Driven Development) testing.

# MongoDB
## Prerequisites

- experience with JSON

## Resources

- [overview](http://docs.mongodb.org/manual/tutorial/getting-started/)
- [CRUD](http://docs.mongodb.org/manual/crud/)
- [Geospatial support](http://docs.mongodb.org/manual/applications/geospatial-indexes/)


# Gulp Build Manager
Prerequisites

- experience building software

## Resources

- http://gulpjs.com/
- See examples in [people-service](https://github.com/psnider/people-service/blob/master/gulpfile.js) project.



# AngularJS Web-App Framework
## Prerequisites

- strong Javascript
- strong HTML
- strong DOM
- some CSS


## Resources

- [https://thinkster.io/angulartutorial/a-better-way-to-learn-angularjs/]()
- [http://docs.angularjs.org/guide/concepts](http://docs.angularjs.org/guide/concepts)  
Provides a clear overview of the framework.
- [When to use directives controllers or services](http://kirkbushell.me/when-to-use-directives-controllers-or-services-in-angular/)  
The first example I found for how to get a service to work.
- [Angular using Typescript](http://www.youtube.com/watch?v=u6TeBM_SC8w)


# NativeScript
You should install nativescript globally.  

```
npm install -g nativescript
```

## Resources
- [Tutorial for use with Angular2](http://docs.nativescript.org/angular/tutorial/ng-chapter-1)  
This is an excellent tutorial.  

# Twitter Bootstrap
An Javascript+CSS library that provides a clean look that adjusts well for mobile devices.

## Prerequisites

- basic HTML
- basic CSS

## Resources

- [http://getbootstrap.com/]()
- [http://getbootstrap.com/getting-started/]()

# Git
Prerequisites

- basic familiarity with source control

## Resources

- [http://git-scm.com/]()
- [Explanation of the Staging Area](http://www.gitguys.com/topics/whats-the-deal-with-the-git-index)


Some useful commands:

- git stash list
- git stash
- git stash apply
- git stash drop
- git stash -p show
- git archive --format=tar b5ba736 >~/tmp/b5ba736.tar

Git Culture:
[http://ben.balter.com/2014/11/06/rules-of-communicating-at-github/]()

# MarkDown
## Prerequisites

- familiarity with layout markup languages

## Tutorials
- practice in Atom with one of these files.  
Type Ctl+Shft+M to render an \*.md file

## Resources

- You can learn the [syntax and options](http://daringfireball.net/projects/markdown/syntax) from the author MarkDown.


# Chrome Debugger
### Prerequisites

- familiarity with javascript
- familiarity with debuggers

### Helpful console functions

[https://shellycloud.com/blog/2014/11/five-functions-of-the-console-object-you-didnt-know]()
- console.assert(expression, message)
- console.profile(name)
- console.time(name)
- console.table(object)


### Use these undocumented functions in the console:

- debug(function_name)
Puts a breakpoint at the named function
- monitor(function_name)
Logs each time the function is executed


# Services to Push Notifications to Mobile Devices
- [https://support.google.com/googleplay/android-developer/answer/2663268?hl=en](Google Cloud Messaging (GCM))
- [https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Introduction.html](Push Notifications)

# Technologies to Investigate

- [An AngularJS widget that creates a complete form given a JSON schema](https://gist.github.com/dalcib/3174225)
- [What can you do with PostgreSQL and JSON?](http://clarkdave.net/2013/06/what-can-you-do-with-postgresql-and-json/)
- [A popular DB binding for PostGres](https://github.com/brianc/node-postgres)
- [SVG editor](http://sourceforge.net/projects/inkscape/?source=dlp)
- [Overview of NoSQL Databases](http://www.getfilecloud.com/blog/2014/08/leading-nosql-databases-to-consider/?utm_source=dbweekly&utm_medium=email#.VAChb4CwJIt)

### Facebook Flux
[http://scotch.io/tutorials/javascript/learning-react-getting-started-and-concepts]()
[http://scotch.io/tutorials/javascript/build-a-real-time-twitter-stream-with-node-and-react-js]()
[http://scotch.io/tutorials/javascript/getting-to-know-flux-the-react-js-architecture]()


# General Web Application Information

[http://rauchg.com/2014/7-principles-of-rich-web-applications/]()


# Code Analysis

[https://github.com/FGRibreau/check-build]()
- [https://www.npmjs.org/package/jsinspect](jsinspect)
- [https://github.com/danielstjules/buddy.js](buddy.js)


# Performance Testing

- [wrk - Modern HTTP benchmarking tool](https://github.com/wg/wrk)
- [ab - Apache HTTP server benchmarking tool](http://httpd.apache.org/docs/2.2/programs/ab.html)



# Hosting

- [AWS Lambda](http://aws.amazon.com/lambda/)
- [Joyent](http://www.joyent.com/)


# Developement Tools
- [Node Tools for MS VisualStudio](https://nodejstools.codeplex.com/releases/view/149714?utm_source=nodeweekly&utm_medium=email)
- [Setup VM on Mac](https://msdn.microsoft.com/en-us/library/windows/apps/jj945425.aspx)


# Elm
Elm is a funcitonal language for building complex HTML pages.

- [http://elm-lang.org/]()
- [http://www.elm-tutorial.org/]()
- [https://github.com/evancz/elm-todomvc]()
- [http://mbylstra.github.io/html-to-elm/]()


# Docker

## Prerequisites

- familiarity with cloud deployment and administration

## Tutorials
- [Get Started with Docker for Mac OS X](https://docs.docker.com/mac/)
- [Why Containers and Docker are the Future](http://resources.codeship.com/hubfs/resources_PDFs/Codeship_Why_Containers_and_Docker_are_the_Future.pdf?t=1452849717341)
- [Docker Toolbox](https://www.docker.com/products/docker-toolbox)
