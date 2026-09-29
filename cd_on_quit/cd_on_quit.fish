function wyrm
    set os $(uname -s)

    if test "$os" = "Linux"
        set wyrm_last_dir "$HOME/.local/state/wyrm/lastdir"
    end

    if test "$os" = "Darwin"
        set wyrm_last_dir "$HOME/Library/Application Support/wyrm/lastdir"
    end

    command wyrm $argv

    if test -f "$wyrm_last_dir"
        source "$wyrm_last_dir"
        rm -f -- "$wyrm_last_dir" >> /dev/null
    end
end
