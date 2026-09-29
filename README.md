# Wyrm

Wyrm is a personal terminal file manager forked from Superfile and reshaped for the Jamal Arcana tool ecosystem.

The command is:

```bash
wyrm
```

## Install from source

Requirements:

- Go 1.26+

Install the CLI into your Go binary directory:

```bash
go install github.com/Noswad123/wyrm@latest
```

Or from a local clone:

```bash
go install .
```

## Build locally

```bash
./build.sh
```

The binary is written to:

```text
bin/wyrm
```

## Configuration

Wyrm uses XDG-style paths. On macOS, `path-list` prints the resolved paths:

```bash
wyrm path-list
```

Default config files are embedded from:

```text
src/wyrm_config/config.toml
src/wyrm_config/hotkeys.toml
```

## Development

Run the Go test suite:

```bash
go test ./...
```

## License

MIT. This fork preserves upstream license notices in `LICENSE` and `NOTICE.md`.
