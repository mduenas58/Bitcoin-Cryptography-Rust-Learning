
## Overview
VIM can be transformed into a powerful DevOps IDE with the right configuration. Here's a complete setup for Kubernetes and system administration.

## Base System Setup

### 1. Install Modern VIM/Neovim
```bash
# For Ubuntu/Debian
sudo apt update
sudo apt install neovim python3-pip nodejs npm

# For CentOS/RHEL/Fedora
sudo dnf install neovim python3-pip nodejs

# Install pip packages for Neovim
pip3 install --user pynvim neovim
```

### 2. Basic .vimrc/.config/nvim/init.vim
```vim
" ~/.config/nvim/init.vim OR ~/.vimrc
" Basic Settings
set nocompatible
set encoding=utf-8
set termguicolors
set mouse=a
set number
set relativenumber
set cursorline
set tabstop=2
set shiftwidth=2
set expandtab
set smartindent
set clipboard=unnamedplus
set hidden
set splitright
set splitbelow

" System admin specific
set autowrite      " Auto save before commands
set backupcopy=yes " Keep inode when saving
set backupdir=~/.vim/backup//
set directory=~/.vim/swap//
set undodir=~/.vim/undo//
set backup
set writebackup
set undofile

" Search
set ignorecase
set smartcase
set incsearch
set hlsearch

" Filetype detection
filetype plugin indent on
syntax enable
```

## Plugin Management with vim-plug

### Install vim-plug:
```bash
# For Vim
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# For Neovim
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

### Plugin Section in init.vim:
```vim
" Plugin Section
call plug#begin('~/.vim/plugged')
" For Neovim: call plug#begin('~/.local/share/nvim/plugged')

" Theme
Plug 'morhetz/gruvbox'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" File Navigation
Plug 'preservim/nerdtree'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'airblade/vim-rooter'

" Git Integration
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'tpope/vim-rhubarb'

" Kubernetes Specific
Plug 'andrewstuart/vim-kubernetes'
Plug 'c-brenn/phoenix.vim'  " YAML syntax
Plug 'hashivim/vim-terraform'
Plug 'ekalinin/Dockerfile.vim'
Plug 'stephpy/vim-yaml'

" System Admin Tools
Plug 'tpope/vim-surround'
Plug 'tpope/vim-commentary'
Plug 'godlygeek/tabular'
Plug 'junegunn/vim-easy-align'
Plug 'mhinz/vim-startify'

" Shell/CLI Integration
Plug 'tpope/vim-dispatch'      " Async commands
Plug 'radenling/vim-dispatch-neovim'
Plug 'skywind3000/asyncrun.vim'

" Auto-completion (COC.nvim - Most comprehensive)
Plug 'neoclide/coc.nvim', {'branch': 'release'}
" OR for lighter setup:
" Plug 'hrsh7th/nvim-cmp'
" Plug 'hrsh7th/vim-vsnip'

" LSP Support
Plug 'prabirshrestha/vim-lsp'
Plug 'mattn/vim-lsp-settings'

" Terminal Integration
Plug 'voldikss/vim-floaterm'

" Remote editing
Plug 'christoomey/vim-tmux-navigator'
Plug 'jpalardy/vim-slime'

" Monitoring/Dashboard
Plug 'wfxr/minimap.vim'

call plug#end()
```

## COC.nvim Configuration for Kubernetes

### Install COC extensions:
```vim
" After installing plugins, run in Vim:
" :PlugInstall
" Then install COC extensions:
" :CocInstall coc-yaml
" :CocInstall coc-json
" :CocInstall coc-sh
" :CocInstall coc-docker
" :CocInstall coc-go
" :CocInstall coc-python
" :CocInstall coc-sql
```

### COC Configuration:
```vim
" ~/.config/nvim/coc-settings.json
{
  "coc.preferences.formatOnSaveFiletypes": ["yaml", "yml", "json", "python", "sh"],
  "yaml.format.enable": true,
  "yaml.schemas": {
    "kubernetes": "*.yaml",
    "file:///home/user/.config/nvim/schemas/k8s.json": ["/*.yaml", "/*.yml"]
  },
  "languageserver": {
    "bash": {
      "command": "bash-language-server",
      "args": ["start"],
      "filetypes": ["sh", "bash"]
    },
    "dockerfile": {
      "command": "docker-langserver",
      "filetypes": ["dockerfile"],
      "args": ["--stdio"]
    }
  }
}
```

## Kubernetes-Specific Setup

### 1. YAML/Kubernetes Configuration:
```vim
" Kubernetes filetype detection
autocmd BufNewFile,BufRead *.yaml,*.yml if search('apiVersion:', 'nw') | set filetype=yaml.kubernetes | endif

" YAML settings
autocmd FileType yaml setlocal ts=2 sts=2 sw=2 expandtab
autocmd FileType yaml setlocal foldmethod=indent

" K8s resource templates
autocmd BufNewFile deployment.yaml 0r ~/.vim/templates/k8s-deployment.yaml
autocmd BufNewFile service.yaml 0r ~/.vim/templates/k8s-service.yaml
autocmd BufNewFile ingress.yaml 0r ~/.vim/templates/k8s-ingress.yaml

" Create templates directory
mkdir -p ~/.vim/templates/
```

### 2. Useful Templates:
```bash
# ~/.vim/templates/k8s-deployment.yaml
cat > ~/.vim/templates/k8s-deployment.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: 
  namespace: default
  labels:
    app: 
spec:
  replicas: 
  selector:
    matchLabels:
      app: 
  template:
    metadata:
      labels:
        app: 
    spec:
      containers:
      - name: 
        image: 
        ports:
        - containerPort: 
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"
EOF

# ~/.vim/templates/k8s-service.yaml
cat > ~/.vim/templates/k8s-service.yaml << 'EOF'
apiVersion: v1
kind: Service
metadata:
  name: 
  namespace: default
spec:
  selector:
    app: 
  ports:
  - port: 
    targetPort: 
  type: ClusterIP
EOF
```

### 3. Kubectl Integration:
```vim
" Kubectl commands in Vim
command! -nargs=* Kubectl execute '!kubectl ' . <q-args>
command! -nargs=* K execute '!kubectl ' . <q-args>
command! Kctx execute '!kubectl config get-contexts'
command! Kns execute '!kubectl get namespaces'

" Get pods in new buffer
function! Kgetpods()
  enew
  setlocal buftype=nofile bufhidden=wipe nobuflisted noswapfile
  r !kubectl get pods --all-namespaces
endfunction
command! Kpods call Kgetpods()

" Get logs of selected pod
function! Klogs()
  let l:pod = expand('<cword>')
  execute 'FloatermNew --height=0.8 --width=0.8 kubectl logs -f ' . l:pod
endfunction
nnoremap <leader>kl :call Klogs()<CR>
```

## System Administration Tools

### 1. SSH/Remote Editing:
```vim
" SCP style editing
cnoremap scp<space> scp://
cnoremap sftp<space> sftp://

" TRAMP style (if compiled with netrw)
autocmd FileType netrw nnoremap <buffer> <C-l> :TmuxNavigateRight<cr>

" Quick SSH config editing
nnoremap <leader>ssh :e ~/.ssh/config<CR>
autocmd FileType sshconfig setlocal commentstring=#\ %s
```

### 2. Log File Handling:
```vim
" Log file settings
autocmd BufRead */log/*.log setlocal filetype=messages
autocmd FileType messages setlocal nowrap
autocmd FileType messages nnoremap <buffer> <leader>g :g/ERROR/<CR>
autocmd FileType messages nnoremap <buffer> <leader>G :g!/ERROR/<CR>

" Journalctl integration
command! Jsystem execute 'FloatermNew --height=0.9 journalctl -f'
command! Jkube execute 'FloatermNew --height=0.9 journalctl -f -u kubelet'
```

### 3. Shell Script Development:
```vim
" Shell script settings
autocmd FileType sh setlocal makeprg=shellcheck\ -f\ gcc\ %
autocmd FileType sh setlocal errorformat=%f:%l:%c:\ %m
autocmd FileType sh nnoremap <buffer> <F9> :make<CR>

" Bash shebang templates
autocmd BufNewFile *.sh 0r ~/.vim/templates/bash-script.sh
```

## Key Mappings for System Administration

```vim
" Leader key
let mapleader = " "

" File navigation
nnoremap <leader>ff :Files<CR>
nnoremap <leader>fg :Rg<CR>
nnoremap <leader>fb :Buffers<CR>
nnoremap <leader>ft :NERDTreeToggle<CR>
nnoremap <leader>fp :Files ~/projects<CR>

" Git
nnoremap <leader>gs :Git<CR>
nnoremap <leader>gc :Git commit<CR>
nnoremap <leader>gp :Git push<CR>
nnoremap <leader>gl :Git log<CR>

" Kubernetes shortcuts
nnoremap <leader>kk :K get pods<CR>
nnoremap <leader>kd :K describe pod<CR>
nnoremap <leader>kl :K logs -f<CR>
nnoremap <leader>ke :K edit<CR>
nnoremap <leader>ka :K apply -f<CR>
nnoremap <leader>kdel :K delete<CR>

" Terminal integration
nnoremap <leader>tt :FloatermToggle<CR>
nnoremap <leader>tk :FloatermNew kubectl<CR>
nnoremap <leader>td :FloatermNew docker<CR>
nnoremap <leader>ts :FloatermNew ssh<CR>

" Quick config edits
nnoremap <leader>ev :vsplit $MYVIMRC<CR>
nnoremap <leader>ek :e ~/.kube/config<CR>
nnoremap <leader>ez :e ~/.zshrc<CR>
nnoremap <leader>ea :e /etc/ansible/hosts<CR>
nnoremap <leader>et :e /etc/hosts<CR>

" Quick actions
nnoremap <leader>qq :q<CR>
nnoremap <leader>ww :w<CR>
nnoremap <leader>wa :wa<CR>
nnoremap <leader>qa :qa<CR>
nnoremap <leader>bd :bd<CR>
```

## Additional Useful Plugins

### For Advanced Users:
```vim
" Add to plugin section:

" Ansible
Plug 'pearofducks/ansible-vim'

" Helm Charts
Plug 'towolf/vim-helm'

" Prometheus/Grafana
Plug 'fatih/vim-go'  " For Prometheus Go client

" Database
Plug 'tpope/vim-dadbod'
Plug 'kristijanhusak/vim-dadbod-ui'

" Docker Compose
Plug 'docker/compose', {'rtp': 'contrib/syntax/vim/'}

" CloudFormation
Plug 'martinda/Jenkinsfile-vim-syntax'

" Monitoring/Dashboard
Plug 'wakatime/vim-wakatime'
```

## Language Server Setup

### Install LSP servers:
```bash
# Kubernetes/YAML
npm install -g yaml-language-server

# Bash
npm install -g bash-language-server

# Docker
npm install -g dockerfile-language-server-nodejs

# Python
pip3 install python-language-server

# Go
go install golang.org/x/tools/gopls@latest

# Terraform
go install github.com/hashicorp/terraform-ls@latest
```

### LSP Configuration:
```vim
" Enable LSP for filetypes
augroup LSP
  autocmd!
  autocmd User lsp_setup call lsp#register_server({
      \ 'name': 'yamlls',
      \ 'cmd': {server_info->['yaml-language-server', '--stdio']},
      \ 'whitelist': ['yaml', 'yaml.kubernetes'],
      \ })
  autocmd User lsp_setup call lsp#register_server({
      \ 'name': 'bashls',
      \ 'cmd': {server_info->['bash-language-server', 'start']},
      \ 'whitelist': ['sh'],
      \ })
augroup END

" LSP key mappings
nnoremap <silent> gd :LspDefinition<CR>
nnoremap <silent> gr :LspReferences<CR>
nnoremap <silent> gi :LspImplementation<CR>
nnoremap <silent> K :LspHover<CR>
nnoremap <silent> <leader>rn :LspRename<CR>
nnoremap <silent> <leader>ca :LspCodeAction<CR>
nnoremap <silent> <leader>f :LspDocumentFormat<CR>
```

## Workflow Examples

### 1. Editing K8s Manifests:
```
1. <leader>ff → Find deployment.yaml
2. :K apply -f % → Apply current file
3. <leader>kk → Check pods
4. <leader>kl → Follow logs
5. :K describe pod <tab> → Describe pod
```

### 2. Debugging with Terminal:
```
1. :FloatermNew kubectl get pods -w
2. Split window with :vs
3. Edit config in left pane
4. :K apply -f % in right terminal
5. Watch changes in real-time
```

### 3. Git Operations:
```
1. <leader>gs → Open fugitive
2. Stage files with -
3. <leader>gc → Commit
4. <leader>gp → Push
5. :Git log --oneline → View history
```

## Performance Tips

```vim
" Disable unused features
let g:loaded_matchparen = 1
let g:loaded_2html_plugin = 1
let g:loaded_getscriptPlugin = 1
let g:loaded_gzip = 1
let g:loaded_tarPlugin = 1
let g:loaded_zipPlugin = 1

" Optimize for large files
set synmaxcol=200
set lazyredraw
set ttyfast

" Disable bells
set noerrorbells
set visualbell
set t_vb=
```

## Quick Installation Script

```bash
#!/bin/bash
# install-vim-ide.sh

# Install dependencies
sudo apt update
sudo apt install -y neovim python3-pip nodejs npm git curl

# Install vim-plug
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

# Copy configuration
mkdir -p ~/.config/nvim/
curl -o ~/.config/nvim/init.vim https://raw.githubusercontent.com/your-repo/vim-k8s-ide/main/init.vim

# Install plugins
nvim +PlugInstall +qall

# Install LSP servers
npm install -g yaml-language-server bash-language-server dockerfile-language-server-nodejs

echo "Vim IDE setup complete!"
```

## Troubleshooting

### Common Issues:

1. **Slow performance with YAML files**:
```vim
" Add to init.vim
let g:yaml_schema_compile=1
set regexpengine=1
```

2. **FZF not working**:
```bash
# Install fzf binary
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

3. **COC.nvim errors**:
```bash
# Update node
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Reinstall COC
nvim +CocUninstall +CocInstall +qall
```

## Recommended Learning Path

1. **Week 1**: Basic navigation + NERDTree + fzf
2. **Week 2**: Git integration + fugitive
3. **Week 3**: Kubernetes shortcuts + terminal integration
4. **Week 4**: LSP + auto-completion
5. **Week 5**: Custom mappings + workflows

## Alternative: Pre-configured Distributions

If you want a ready-to-use solution:

1. **LunarVim**: https://www.lunarvim.org/
   ```bash
   LV_BRANCH='release-1.3/neovim-0.9' bash <(curl -s https://raw.githubusercontent.com/LunarVim/LunarVim/release-1.3/neovim-0.9/utils/installer/install.sh)
   ```

2. **NvChad**: https://nvchad.com/
   ```bash
   git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1
   ```

3. **SpaceVim**: https://spacevim.org/
   ```bash
   curl -sLf https://spacevim.org/install.sh | bash
   ```

This setup transforms Vim into a powerful Kubernetes/system administration IDE that's faster and more customizable than most graphical IDEs, while maintaining the efficiency of terminal-based workflows.