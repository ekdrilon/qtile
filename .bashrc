#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

alias rr="ranger"
alias qconf="vim ~/.config/qtile/config.py"
alias rconf="vim ~/.config/ranger/rc.conf"
alias rrefflector="sudo reflector --sort rate -l 50 -p https --save /etc/pacman.d/mirrorlist"
alias rreff="sudo pacman -Syyy"
alias rm="rm -i"
alias kconf="vim ~/.config/kitty/kitty.conf"
pfetch
