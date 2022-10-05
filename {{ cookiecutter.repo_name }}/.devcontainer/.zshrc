# Path to your oh-my-zsh installation.
export ZSH="/home/vscode/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# ZSH_THEME="codespaces"
eval "$(oh-my-posh init zsh --config https://gist.githubusercontent.com/flych3r/33bfb9e67daa7a4017838ee1753800f3/raw/2f0eeb93517b6710b8281f4fd8339354211d2740/mytheme.omp.json)"
VSCODE=code

# Which plugins would you like to load?
plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
)

source $ZSH/oh-my-zsh.sh
