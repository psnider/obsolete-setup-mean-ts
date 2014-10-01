# Deployment Workspace using Git

## Background
We use git to manage a workspace for deployment.

A deployment workspace has a subset of the files that are in the development workspace, that is, only the files that are required for deployment, and generally no documentation, and limited testing.

The deployment procedure consists of a few steps:

1. The files from the previous deployment are deleted from the Deployment Workspace (but keeping the .git local repo directory).
- The working code required for deployment is copied from the Development Workspace into the new empty Deployment Workspace.
- Any local pre-deployment tests are run in the Deployment Workspace.  If they pass, the code is checked in (to the Deployment Workspace). If they don't pass, the code must be corrected in the Development Workspace, and then the deployment procedure can be restarted.
- Any final configuration changes required for deploying to remote deployment must be made.
- Any changes to the Development Workspace must be checked in for deployment.
- The git repo can now be pushed to the remote service.
- After deployment, run the automated test suite against the deployed instance.
- Once the deployment has been validated, apply the tag required to track this version.

These steps have been partially automated, by using special make targets:

1. reinit-deploy-qa
Creates a new qa deployment workspace from scratch, by pulling the git repo for the app from Heroku
- copy-code-deploy-qa
Copies the currently checked-in code from development to the qa deployment workspace
- update-deploy-qa
Updates the qa deployment workspace to contain the latest code from the development workspace,
and then reconfigures the development environment, and builds the server.
This requires that the development workspace is in a fully committed state.
- deploy-qa
Pushes the code from the qa deployment workspace up to Herkou.


## Make a new Git Deployment Workspace for Heroku

Set REPO_NAME to the name of the repo you want deploy (assuming your git repo name is the same as your heroku app repo name).

 
Then run these commands:

```
cd ~/deploy
git clone git@heroku.com:$REPO_NAME.git -o heroku
cd ~/devel/$REPO_NAME
cp bower.json Config.json SavedState.json Makefile make.py package.json Procfile SavedState.json ~/deploy/$REPO_NAME
cp -R decl patch schema src test ~/deploy/$REPO_NAME
cd ~/deploy/$REPO_NAME
make clean setup
make server
```

profile, package.json both incorrectly reference web.js


## Deploy from Development

```
```

 
# Heroku Cloud-based Servers
## Install
You must get a Heroku account from: [https://www.heroku.com/](https://www.heroku.com/)  
Then get the [Heroku Toolbelt](https://toolbelt.herokuapp.com/)  

We will not be using Heroku from our development environments, and instead will create environments specifically for deployment.

You must upload an SSH key to Heroku before you can push code to Heroku.
I had trouble with this. It didn't work until I did two things (not sure yet which matter):

- used a key without a password
- created a new key with the default name
- created a new key from an empty .shh directory

Aug 4, 2014:  
Added an SSH key for a new machine, via the Heroku Account Settings page.  
However, a subsequent git clone was rejected with this error:

    fatal: Could not read from remote repository.
    Please make sure you have the correct access rights
    and the repository exists.

I followed this by running the command:

```
heroku keys:add
```

and after this, the git clone command was accepted.


## Init Heroku Project

```
heroku login
```

Create the Procfile

## Deploy to Heroku

### Test

```
foreman start
```

## Study Resources
- [Getting started with nodejs](https://devcenter.heroku.com/articles/getting-started-with-nodejs)
  
  
