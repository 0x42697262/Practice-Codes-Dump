" lua aavviki = require("aavviki")
" lua require'aavviki'.setup()

" P.S.
" I have no idea what I am doing.



" Copyright (c) 2020 Dave Gauer
" MIT License

if exists('g:loaded_avviki')
	finish
endif
let g:loaded_avviki = 1

" Initialize configuration defaults
" See 'Configuration' in the help documentation for full explanations.
"
if !exists('g:avviki_root')
    " Default root directory for (current) wiki
	let g:avviki_root = "~/wiki"
endif

if !exists('g:avviki_ext')
    " Extension to append to pages when navigating internal links
	let g:avviki_ext = ""
endif

if !exists('g:avviki_index')
    " The start document for wiki root and subdirectories
    " index + ext is the start filename (e.g. index.adoc)
    let g:avviki_index = "index"
endif

if !exists('g:avviki_conceal_links')
    " Use Vim's syntax concealing to temporarily hide link syntax
    let g:avviki_conceal_links = 1
endif

if !exists('g:avviki_page_link_syntax')
    " Set internal wiki page link syntax to one of:
    "   'link'        ->   link:foo[My Foo]
    "   'olink'       ->   olink:foo[My Foo]
    "   'xref_hack'   ->   <<foo#,My Foo>>
    let g:avviki_page_link_syntax = 'link'
endif

if !exists('g:avviki_visual_link_creation')
    " Allow link creation from selected text in visual mode
    let g:avviki_visual_link_creation = 0
endif

if !exists('g:avviki_links_include_ext')
    " Internal wiki page links include the file extension.
    " (File extension is set via g:avviki_ext.)
    let g:avviki_links_include_ext = 0
endif

" Navigation history for Backspace
let s:history = []


" Supported link styles:
function! VVEnter()
    " Attempt to match existing link under cursor, trying all link syntax
    " types (this intentionally ignores g:avviki_page_link_syntax).

	" Try to get path from AsciiDoc 'link' macro
	"   link:http://example.com[Example] - external
	"   link:page[My Page]               - internal relative page
	"   link:/page[My Page]              - internal absolute path to page
	"   link:../page[My Page]            - internal relative path to page
    let l:linkpath = VVGetLink()
	if strlen(l:linkpath) > 0
        echom "xref:".l:linkpath
		if l:linkpath =~ '^https\?://'
			call VVGoUrl(l:linkpath)
		else
			call VVGoPath(l:linkpath)
		endif
		return
	end

	" Get path from AsciiDoc 'olink' macro (anticipating future support)
	"   olink:page[My Page]    - internal relative page
	"   olink:../page[My Page] - internal relative path to page
    let l:linkpath = VVGetOLink()
	if strlen(l:linkpath) > 0
        echom "olink:".l:linkpath
        call VVGoPath(l:linkpath)
		return
	end

	" Get path from AsciiDoc '<<xref#>>' macro (for AsciiDoctor export)
	"   <<page#,My Page>>    - internal relative page
	"   <<../page#,My Page>> - internal relative path to page
    let l:linkpath = VVGetXrefHack()
	if strlen(l:linkpath) > 0
        echom "xrefhack:".l:linkpath
        call VVGoPath(l:linkpath)
		return
	end


	" Did not match a link macro. Now there are three possibilities:
	"   1. We are on whitespace
	"   2. We are on a bare URL (http://...)
	"   3. We are on an unlinked word
	let l:whole_word = expand("<cWORD>") " selects all non-whitespace chars
	let l:word = expand("<cword>") " selects only 'word' chars

    " Cursor on whitespace
	if l:whole_word == ''
		return
	endif

    " Cursor on bare URL
	if l:whole_word =~ '^https\?://'
		call VVGoUrl(l:whole_word)
		return
	endif

	" Cursor on unlinked word - make it a link!
    let l:new_link = VVMakeLink(l:word, l:word)
	execute "normal! ciw".l:new_link."\<ESC>"
endfunction


function! VVVisualEnter()
    " Creates a new page link using whatever text is visually selected.
    " Yank selection, replace with link, restore default register
    let previous_register_contents = getreg('"')
    normal! gvy
    let user_selection = getreg('"')
    call setreg('"', VVMakeLink(user_selection, user_selection))
    normal! gvp
    call setreg('"', previous_register_contents)
endfunction


function! VVGetLink()
	" Captures the <path> portion of 'link:<path>[description]' (if any)
    " \< is Vim regex for word start boundary
    return VVGetMatchUnderCursor('\<xref:\([^[]\+\)\[[^]]\+\]')
endfunction


function! VVGetOLink()
	" Captures the <path> portion of 'olink:<path>[description]' (if any)
    " \< is Vim regex for word start boundary
    return VVGetMatchUnderCursor('\<olink:\([^[]\+\)\[[^]]\+\]')
endfunction


function! VVGetXrefHack()
	" Captures the <path> portion of '<<<path>#,description>>' (if any)
    return VVGetMatchUnderCursor('<<\([^#]\+\)#,[^>]\+>>')
endfunction


function! VVGetMatchUnderCursor(matchrx)
    " Grab cursor pos and current line contents
    let l:cursor = col('.')
    let l:linestr = getline('.')

    " Loop through the regex matches on the line, see if our cursor
    " is inside one of them. If so, return it.
    let l:matchstart=0
    let l:matchend=0
    while 1
        " Note: match() always functions as if pattern were in 'magic' mode!
        let l:matchstart =     match(l:linestr, a:matchrx, l:matchend)
		let l:matched    = matchlist(l:linestr, a:matchrx, l:matchend)
        let l:matchend   =  matchend(l:linestr, a:matchrx, l:matchend)

        " No match found or we're already past the cursor; done looking
        if l:matchstart == -1 || l:matchstart > l:cursor
            return ""
        endif

        if l:matchstart <= l:cursor && l:cursor <= l:matchend
			return l:matched[1]
        endif
    endwhile
endfunction


function! VVMakeLink(uri, description)
    " Returns string with link of desired AsciiDoc syntax 'style'
    let l:uri = a:uri
    if g:avviki_links_include_ext
        " Attach the wiki file extension to the link URI
        let l:uri = l:uri.g:avviki_ext
    endif
    if g:avviki_page_link_syntax == 'link'
        return "xref:".l:uri.".adoc[".a:description."]"
    elseif g:avviki_page_link_syntax == 'olink'
        return "olink:".l:uri."[".a:description."]"
    elseif g:avviki_page_link_syntax == 'xref_hack'
        return "<<".l:uri."#,".a:description.">>"
    endif
endfunction


function! VVFindNextLink()
    " Places cursor on next link of desired AsciiDoc syntax
    if g:avviki_page_link_syntax == 'link'
        call search('xref:.\{-1,}]')
    elseif g:avviki_page_link_syntax == 'olink'
        call search('olink:.\{-1,}]')
    elseif g:avviki_page_link_syntax == 'xref_hack'
        call search('<<.\{-1,}#,.\{-1,}>>')
    endif
endfunction


function! VVGoPath(path)
    " Push current page onto history
    call add(s:history, expand("%:p"))

    let l:fname = a:path

    if l:fname =~ '/$'
        " Path points to a directory, append default 'index' page
        let l:fname = l:fname.g:avviki_index
    end

    " fname will no longer change, we can add extension here
    if !g:avviki_links_include_ext
        " Links don't already include extension, add it
        let l:fname = l:fname.g:avviki_ext
    endif

    if l:fname =~ '^/'
        " Path absolute from wiki root
        let l:fname = g:avviki_root."/".l:fname
    else
        " Path relative to current page
        let l:fname = expand("%:p:h")."/".l:fname
    endif

    let l:fname = fnameescape(l:fname)

    execute "edit ".l:fname
endfunction


function! VVGoUrl(url)
	call system('xdg-open '.shellescape(a:url).' &')
endfunction


function! VVBack()
	if len(s:history) < 1
		return
	endif

	let l:last = remove(s:history, -1)
	execute "edit ".fnameescape(l:last)
endfunction


function! VVConcealLinks()
    " Conceal the AsciiDoc link syntax until the cursor enters the line.
    set conceallevel=2

    if g:avviki_page_link_syntax == 'link'
        syntax region avvikiLink start=/xref:/ end=/\]/ keepend
        syntax match avvikiLinkGuts /link:[^[]\+\[/ containedin=avvikiLink contained conceal
        syntax match avvikiLinkGuts /\]/ containedin=avvikiLink contained conceal
    elseif g:avviki_page_link_syntax == 'olink'
        syntax region avvikiLink start=/olink:/ end=/\]/ keepend
        syntax match avvikiLinkGuts /olink:[^[]\+\[/ containedin=avvikiLink contained conceal
        syntax match avvikiLinkGuts /\]/ containedin=avvikiLink contained conceal
    elseif g:avviki_page_link_syntax == 'xref_hack'
        syntax region avvikiLink start=/<</ end=/>>/ keepend
        syntax match avvikiLinkGuts /<<[^>]\+#,/ containedin=avvikiLink contained conceal
        syntax match avvikiLinkGuts />>/ containedin=avvikiLink contained conceal
    endif

    highlight link avvikiLink Macro
    highlight link avvikiLinkGuts Comment
endfunction


function! VVSetup()
	" Set wiki pages to automatically save
	set autowriteall

	" Map ENTER key to create/follow links
	nnoremap <buffer><silent> <CR> :call VVEnter()<CR>

	" Map BACKSPACE key to go back in history
	nnoremap <buffer><silent> <BS> :call VVBack()<CR>

    " Map TAB key to find next link in page
    " NOTE: search() always uses 'magic' regexp mode.
    "       \{-1,} is Vim for match at least 1, non-greedy
    nnoremap <buffer><silent> <TAB> :call VVFindNextLink()<CR>

    if g:avviki_visual_link_creation
        vnoremap <buffer><silent> <CR> :call VVVisualEnter()<CR>
    endif

    if g:avviki_conceal_links
        call VVConcealLinks()
    endif
endfunction


" Detect wiki page
" If a buffer has the right parent directory and extension,
" map avviki keyboard shortcuts, etc.
augroup avviki
	au!
	execute "au BufNewFile,BufRead ".g:avviki_root."/*".g:avviki_ext." call VVSetup()"
augroup END
