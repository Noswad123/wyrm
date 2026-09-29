package main

import (
	"embed"

	"github.com/Noswad123/wyrm/src/cmd"
)

var (
	//go:embed src/wyrm_config/*
	content embed.FS
)

func main() {
	cmd.Run(content)
}
