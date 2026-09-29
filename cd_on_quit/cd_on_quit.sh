wyrm() {
    os=$(uname -s)

    # Linux
    if [[ "$os" == "Linux" ]]; then
        export Wyrm_LAST_DIR="${XDG_STATE_HOME:-$HOME/.local/state}/wyrm/lastdir"
    fi

    # macOS
    if [[ "$os" == "Darwin" ]]; then
        export Wyrm_LAST_DIR="$HOME/Library/Application Support/wyrm/lastdir"
    fi

    command wyrm "$@"

    [ ! -f "$Wyrm_LAST_DIR" ] || {
        . "$Wyrm_LAST_DIR"
        rm -f -- "$Wyrm_LAST_DIR" > /dev/null
    }
}
