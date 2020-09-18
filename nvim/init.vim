let mapleader="\<Space>"

" basics
syntax on
set autoindent
set number
set relativenumber
set numberwidth=4
" set hlsearch
" set incsearch
set ignorecase
set smartcase
set nocp
set encoding=UTF-8
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab
set hlsearch!
set spell
set spelllang=en_us
set shell=/usr/bin/zsh
"theme
if (has("termguicolors"))
 set termguicolors
endif

" Theme
colorscheme OceanicNext
let g:lightline={
   \ 'colorscheme' : 'nord'
   \}

" NERDTree
"git clone https://github.com/preservim/nerdtree.git ~/.vim/pack/vendor/start/nerdtree
"vim -u NONE -c "helptags ~/.vim/pack/vendor/start/nerdtree/doc" -c q

" latex pdf live preview changed to zathura
let g:livepreview_previewer = 'zathura'

" hexokinase
let g:Hexokinase_highlighters = ['backgroundfull']
let g:Hexokinase_optInPatterns = 'full_hex,rgb,rgba,hsl,hsla,triple_hex'

autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
let NERDTreeShowHidden=1
let g:NERDSpaceDelims = 1

nmap <leader>t :NERDTreeToggle<Enter>
nmap <leader>w :w<CR>
nmap <leader>q :q<CR>
nmap <leader>Q :qa!<CR>
nmap <leader>d :w !diff % -<CR>
nmap <leader>D :bd<CR>

call plug#begin('~/.vim/plugged')

" fzf plugin
Plug 'junegunn/fzf', { 'do': './install --bin' }
Plug 'junegunn/fzf.vim'

" ctrlSF plugin
Plug 'dyng/ctrlsf.vim'

" lightline
Plug 'itchyny/lightline.vim'

"auto indent line for python
Plug 'vim-scripts/indentpython.vim'

" for suggestion
Plug 'neoclide/coc.nvim', {'branch': 'release'}

"for icons
Plug 'ryanoasis/vim-devicons'

" surrounds commands
Plug 'tpope/vim-surround'

" indent 
Plug 'yggdroot/indentline'

" for html tag
Plug 'andrewradev/tagalong.vim'
Plug 'alvan/vim-closetag'
Plug 'mattn/emmet-vim'

" for commenting
Plug 'tpope/vim-commentary'

" for checking errors
Plug 'scrooloose/syntastic'

Plug 'prettier/vim-prettier'

Plug 'tell-k/vim-autopep8'

" nerdtree
Plug 'preservim/nerdtree'

" theme
Plug 'mhartington/oceanic-next'

" latex plugin
Plug 'lervag/vimtex'
Plug 'xuhdev/vim-latex-live-preview'

" color viewer
Plug 'rrethy/vim-hexokinase', { 'do': 'make hexokinase' }

call plug#end()

" Enable file type detection.
" Also load indent files, to automatically do language-dependent indenting.
filetype plugin indent on

" Find files with fzf
nmap <leader>p :Files<CR>
nmap <leader>P :Commands<CR>

" Requires ripgrep
" https://github.com/BurntSushi/ripgrep
let $FZF_DEFAULT_COMMAND = 'rg --files --hidden --glob "!.git/*"'

" Default fzf layout
" - down / up / left / right
let g:fzf_layout = { 'down': '~40%' }


" CtrlSF setting 

let g:ctrlp_working_path_mode = 0
let g:ctrlp_by_filename = 0
let g:ctrlp_regexp_search = 0
let g:ctrlp_use_caching = 1

if has("macunix")
  set clipboard=unnamed
elseif has("unix")
  set clipboard=unnamedplus
endif

nmap <leader>a :CtrlSF -R ""<Left>
nmap <leader>A <Plug>CtrlSFCwordPath -W<CR>
nmap <leader>c :CtrlSFFocus<CR>
nmap <leader>C :CtrlSFToggle<CR>

if has("macunix")
  let g:ctrlsf_ackprg = '/usr/local/bin/rg'
elseif has("unix")
  let g:ctrlsf_ackprg = '/usr/bin/rg'
endif

let g:ctrlsf_winsize = '33%'
let g:ctrlsf_auto_close = 0
let g:ctrlsf_confirm_save = 0
let g:ctrlsf_auto_focus = {
    \ 'at': 'start',
    \ }

"Disable backup and swap files
set nobackup
set noswapfile
set nowritebackup

" easier moving of code blocks
vnoremap < <gv
vnoremap > >gv

" change exit insert mode from esc
inoremap jk <esc>

" save and quit made easier
nmap <leader>w :w<cr>
nmap <leader>q :q<cr>

" move between vim split
nmap <C-l> <C-w>l
nmap <C-h> <C-w>h
nmap <C-j> <C-w>j
nmap <C-k> <C-w>k

" open terminal in nvim
nmap <leader>T :bo 15sp +te<cr>

" Terminal go back to normal mode
tnoremap <Esc> <C-\><C-n>

" toggle search highlight
nnoremap <F3> :set hlsearch!<CR>

" coc config
" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

autocmd FileType json syntax match Comment +\/\/.\+$+
