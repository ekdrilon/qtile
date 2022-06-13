# qtile
#qtile
if you somehow want this messy qtile config of my install ttf-font-awesome and remove my bashc and vimrc
mine is a shittyfile.

to install the file clone it first
git clone https://github.com/ekdrilon/qtile.git

then cd to it chmod the autostart and remove some of my files
cd qtile
rm -rf .bashrc .vimrc
chmod +x autostart.sh

then cd out of it then move it to .configs
cd
mv qtile ~/.config/

then its finished

optional dependecies
kitty for my term
nitrogen for my wallpaper
picom-jonaburg for compositor


and for stuff I use blueman for bluetooth and nmtui for some stuff
