# PSFree-Luckfox
Providing PSFree exploit and some extras web server on Luckfox a single board computer
Original work by kmeps4 PSFree and thanks to harsha-0110 PPPwn-Luckfox for web dashboard.

## Note
* PSFree **ONLY** supports PS4 System `9.00`
* PSFree-Lapse exploit is working in progress currently. It can make system carsh or kernel panic. **ALL OF USING AT YOUR OWN RESPONSIBILITY**
* The exploit can be failed sometime. when failed, try again.

## How to install it?
Follow this tutorial

* Mini / Plus

    https://wiki.luckfox.com/Luckfox-Pico/Luckfox-Pico-MiniB-burn-image

* Pro / Max

    https://wiki.luckfox.com/Luckfox-Pico/Luckfox-Pico-ProMax-burn-image

**PSFree ONLY SUPPORT SPI NAND FLASHING**

## How to use it on my PS4?
### Configure Network
* Go to `Settings` and select `Network`.
* Select `Set Up Internet Connection` and choose `Use a LAN Cable`.
* Select `Custom` and choose `Automatic` in IP Address Settings.
* Select `Do Not Specify` in DHCP Host Name.
* Select `Automatic` in DNS Settings.
* Select `Automatic` in MTU Settings.
* Select `Do Not Use` in Proxy Server
### Run Exploit
* Go to `Settings` and select `User's Guide/Helpful Info` and select `User's Guide`.
    *  Or open web browser, go to `http://psfree-luckfox.local`
* Click `Exploit` button.
    * `There is not enough free memory` is showing, the exploit is failed.
    * Try again until showing `kernel exploit succeeded!`.

## How to build it?
* Build firmware first
    * Clone `luckfox-pico` repository
    * Select your Luckfox type by `./build.sh lunch`
    * Configure your build by `./build.sh buildrootconfig`
    * Add `python3-flask` dependency. (`Target Packages` -> `Interpreter languages and scripting` -> `python3` -> `External python modules`)
    * Build all by `./build.sh` or build rootfs only by `./build.sh rootfs`
* Install PSFree-Luckfox by `./install-to-rootfs-buildroot.sh <rootfs-path>`
    * rootfs path can be found at `<your-luckfox-pico-sdk-path>/output/out/rootfs_uclibc_rv1106`
* Repackage by `./build.sh firmware`
    * Firmware files can be foudn at `<your-luckfox-pico-sdk-path>/output/image`
