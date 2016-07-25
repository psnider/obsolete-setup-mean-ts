Using Genymotion instead after receiving advice to do so from https://nativescriptcommunity.slack.com/


# Install Android
Android is installed as part of the NativeScript packages.
Once installation has completed, you should setup a virtual device.

Install the Android system version you want to use,
in our case Android 6.0 (API 23)
- Run ```android``` to launch the *Android SDK Manager*
- Check the box for *Android 6.0 (API 23)*
- and click *install*

Then create an *Android Virtual Device*:
- Run the *Android Virtual Device Manager*: ```android avd```
- Select the Device Definitions tab
- Select Nexus 5, and click *Create AVD...*
  - Select target of: *Android 6.0*
  - Select skin of: *Skin with dynamic controls*
  - Set the size of the SD card to 100MB
  - Check *Emulation Options -> Use Host GPU*
  - Click OK
