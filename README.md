## [Armenian Phonetic Keyboard Layout](http://evoyan.org/armenian-phonetic-for-mac)

### Armenian phonetic keyboard layout for Mac OSX.

This project was initiated as an alternative keyboard layout for those who have an experience of working with Armenian Phonetic layout in Windows/Linux. It basically is created from scratch using [Ukelele](http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=ukelele) tool on Mac for editing keyboard layouts. It is hosted on [Github](https://github.com/vahe-evoyan/armenian-phonetic) page. Please feel free to file bugs right on [Github](https://github.com/vahe-evoyan/armenian-phonetic/issues). I'll do my best to address them as quickly as possible.

Below are brief instructions on the layout set-up.

#### Included Layouts

* Armenian Phonetic - Regular phonetic layout where key "R" types "ր".
* Armenian Phonetic (KDWin) - Exactly the same layout as in KDWin.
* Armenian Phonetic With English - Option key changes the keys to English in place of special characters.
* Armenian Phonetic (KDWin) With English - KDWin phonetic layout with Option key feature.

#### How To Install
1. Download [ArmenianPhonetic.dmg](https://github.com/vahe-evoyan/armenian-phonetic/releases/download/v2.1.2/ArmenianPhonetic.dmg) file from the releases section.
![Image Window](/screenshots/dmg-window.png)
2. Drag the `ArmenianPhonetic.bundle` file to the `Keyboard Layouts` folder.
3. The system will ask you to authenticate, as the directory requires super user access.
![Permission Access](/screenshots/authenticate.png)
4. The layouts should appear in the *Language & Text* (or System Preferences > Keyboard > Input Sources) preferences section. In case they didn't, simply log out and log back in, so that the OS reloads the layouts.
![Permission Access](/screenshots/layout-settings.png)

#### Manual Install(works also with mac on Apple silicon, tested on Apple M3 Pro)

1. get the needed layout files/folders and move into layouts folder:
- download the file [./ArmenianPhonetic.icns](./ArmenianPhonetic.icns) and folder [./ArmenianPhonetic.bundle](./ArmenianPhonetic.bundle) and copy them to `~/Library/Keyboard Layouts/` directory, in order to see Library folder you will need to go to home folder in finder ( Command-Shift-H) and in View->Show View Options (Command-J) check "Show Library Folder", see the screen in [screen](./screenshots/)
- or if you fluent with terminal and git tools you can run the following command(it clones git repo into folder, copy needed files into layouts directory and cleanups/deletes the git repo folder):
```sh
git clone git@github.com:vahe-evoyan/armenian-phonetic.git && cp -r ./armenian-phonetic/ArmenianPhonetic.bundle ./armenian-phonetic/ArmenianPhonetic.icns  ~/Library/Keyboard\ Layouts/ && rm -rf ./armenian-phonetic/
```
Here is what you should see in folder `~/Library/Keyboard Layouts/` when browsing from finder or looking by terminal:
[layouts folder in finder](./screenshots/manual-setup-library-keyboard-layouts-folder-finder.png),
[layouts folder in terminal](./screenshots/manual-setup-library-keyboard-layouts-folder-terminal.png)

2. Log out and log back in, or better restart the Mac
3. Here is how to activate the new layout:
 - for old Mac OS versions: go to *Language & Text* (or System Preferences > Keyboard > Input Sources) preferences and check the *Armenian - Phonetic* check-box.
 - or for new Mac OS versions: go to System Settings and search for *Keyboard layouts* (or System Settings > Keyboard > Input Sources) preferences and in bottom left corner click on "+" button and select "Armenian" language in list, and then in opened right layouts list select preferred Armenian Phonetic layout and click on "add" button.
