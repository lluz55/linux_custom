#! /bin/sh

# check arch and download binary from github release tag

if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
fi

case $NAME in
  Ubuntu)
    # Debian based
    # install curl
    sudo apt install curl
    ;;
esac

# install nix package manager single user
sh <(curl -L https://nixos.org/nix/install) --no-daemon

. $HOME/.nix-profile/etc/profile.d/nix.sh

# using fish
#nix-env -iA nixpkgs.fish

# using zsh
nix-env -iA zsh
nixpkgs.oh-my-zsh
# install auto suggestion
git clone https://github.com/zsh-users/zsh-autosuggestions \
    ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
sed -i -E 's/\(git\)/\(git zsh-autosuggestions\)/' .zshrc

nix-env -iA \
  nixpkgs.fd \
  nixpkgs.exa \
  nixpkgs.git \
  nixpkgs.htop \
  nixpkgs.neovim \
  nixpkgs.ripgrep \

# Clone dotfiles
git clone https://github.com/lluz55/linux_custom $HOME/linux_custom
cd $HOME/linux_custom/
git checkout archcraft_conf
cp -r .config $HOME/

  #nixpkgs.du-dust \
# Install AstronVim
# backup
# mv $HOME/.config/nvim $HOME/.config/nvimbackup

# git clone https://github.com/AstroNvim/AstroNvim ~/.config/nvim
nvim +PackerSync -c "q!"
