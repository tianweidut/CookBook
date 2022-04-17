# source.list 
# /etc/apt/sources.list

#basic software
sudo apt-get install -y wget locales make cmake build-essential software-properties-common curl sudo ca-certificates apt-transport-https iputils-ping net-tools openssh-server net-tools gcc-aarch64-linux-gnu \
	        zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev shellcheck git apt-utils
sudo apt install git curl libssl-dev libreadline-dev zlib1g-dev autoconf bison build-essential libyaml-dev libreadline-dev libncurses5-dev libffi-dev libgdbm-dev

#python
sudo add-apt-repository -y ppa:deadsnakes/ppa 
sudo apt-get update
sudo apt-get install -y python3.7 python3.8 python3.9 python3-pip
sudo pip config set global.index-url https://pypi.doubanio.com/simple/
sudo pip config set install.trusted-host pypi.doubanio.com
python3.7 -m pip install virtualenv
python3.8 -m pip install virtualenv
python3.9 -m pip install virtualenv 

export PATH=/opt/miniconda3/bin:$PATH
curl -s -o /tmp/conda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash /tmp/conda.sh -b -p /opt/miniconda3
conda init --all

#zsh
sudo apt-get install zsh
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
source ~/.zshrc

#vim
sudo add-apt-repository ppa:neovim-ppa/unstable
sudo apt update
sudo apt install -y neovim

#npm
curl -fsSL https://deb.nodesource.com/setup_17.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install gcc g++ make
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/yarnkey.gpg >/dev/null
echo "deb [signed-by=/usr/share/keyrings/yarnkey.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn

#tools
wget https://github.com/sharkdp/bat/releases/download/v0.20.0/bat_0.20.0_amd64.deb
sudo dpkg -i bat*.deb
curl -O https://raw.githubusercontent.com/denilsonsa/prettyping/master/prettyping
chmod +x prettyping
sudo mv prettypint /usr/local/bin/
sudo apt-get install fzf ncdu
sudo apt install tree autojump-zsh jq ruby-full silversearcher-ag

sudo add-apt-repository ppa:aos1/diff-so-fancy
sudo apt-get update
sudo apt-get install diff-so-fancy
sudo apt install fd-find
sudo npm install -g tldr

# docker/minikube
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get install docker-ce=5:19.03.15~3-0~ubuntu-focal docker-ce-cli=5:19.03.15~3-0~ubuntu-focal 
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo usermod -aG docker $USER && newgrp docker
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
