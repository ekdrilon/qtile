#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

export EDITOR=vim

alias qconf="vim ~/.config/qtile/config.py"
alias kconf="vim ~/.config/kitty/kitty.conf"
alias yclean="yay -Sc"
alias ycclean="yay -Scc"
alias yyclean="yay -Yc"
alias usedd="df -h"
alias sfailed="systemctl --failed"
alias pclean="sudo pacman -Sc"
alias pcclean="sudo pacman -Scc"
alias findorphan="pacman -Qdtq"
alias rmorphan="sudo pacman -Rcns $(pacman -Qdtq)"
alias findcache="du -sh .cache/"
alias cclean="rm -rf .cache/*"
alias jclean="sudo journalctl --vacuum-time=2weeks"
alias fhram="free -h"
# alias rfeq="sudo reflector --sort rate -l 70 -p https --save /etc/pacman.d/mirrorlist"
alias nfetch="neofetch"
alias rfeq="sudo reflector --verbose -l 200 -n 20 -p https --sort rate --save /etc/pacman.d/mirrorlist"


pfetch
