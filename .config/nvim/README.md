# notes on my nvim configuration

## Plugins

- [lsp-zero.nvim](https://github.com/VonHeikemen/lsp-zero.nvim)
    - This is the LSP server I am using. It's pretty fast
- [formatter.nvim](https://github.com/mhartington/formatter.nvim)
    - A formatter which can format a document either with a keybind, or when saving or both!

## Notation

- N/V/I to the left of the keybinds refers to the mode
- `Leader` is the "main" button and it usually is used in either normal or visual mode. I have it currently configured to <kbd>Space</kbd>
- `C` refers to <kbd>Ctrl</kbd>
- `M` refers to <kbd>Alt</kbd>

## Important keybinds

- N <kbd>Space</kbd> + <kbd>e</kbd> : Open netrw
- N <kbd>J</kbd> : Append line under cursor and keep the cursor where it was
- N/V <kbd>Leader-y</kbd> : Copy to system clipboard
- N <kbd>Leader-ff</kbd>: Open Fuzzy Finder
    - <kbd>C-t</kbd>: Open selected file to a new tab 
- V <kbd>J</kbd> OR <kbd>K</kbd> : Move whatever is highlighted either down or up, very useful
- V <kbd>F2</kbd> : Renames all references of symbol under cursor
- V <kbd>K</kbd> : Display hover info about symbol
- V <kbd>gD</kbd> : *g*o to *D*efinition of symbol
- V <kbd>gr</kbd> : list all *r*eferences of symbol
- V <kbd>F4</kbd> : Code action at current position
- V <kbd>gl</kbd> : Show *all diagnostics* in a floating window

### Deprecated

- These are still in the configuration but there is no reason to use them because I have made the background of nvim transparent 
    - <kbd>Leader-qq</kbd> : Change to the dark theme
    - <kbd>Space</kbd>  : Change to the light theme
