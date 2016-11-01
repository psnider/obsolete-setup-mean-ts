# Upgrade NativeScript
:warning: These instructions are rough, and haven't been reproduced yet.


Follow [NativeScript Upgrade Instructions](http://docs.nativescript.org/releases/upgrade-instructions)

Upgrade the **tns** command:
```
npm install -g nativescript
```

Upgrade the mobile platforms:
```
tns platform remove android
tns platform add android
tns prepare android
tns platform remove ios
tns platform add ios
tns prepare ios
```

tried instead:
```
rm -fr platforms
tns platform add android
tns platform add ios
```


Upgrade the tns modules:
```
npm install tns-core-modules@latest --save
```

Find the latest versions of angular by generating a new template app with:
```
cd /tmp
mkdir tmp-ns-app
cd tmp-ns-app
tns create my-app --ng
cat package.json
```

and use these updated packages in your project's package.json
then reinstall in your project:
``` 
npm install
```

