APP_NAME = wyrm
BIN_DIR = ./bin
INSTALL_DIR ?= $(HOME)/.local/bin

.PHONY: all build install test clean help

# Default target
all: build

# Build only
build:
	@./build.sh

# Build and install into ~/.local/bin by default, mirroring Djinn.
install: build
	@echo "📦 Installing to $(INSTALL_DIR)/$(APP_NAME)"
	@mkdir -p "$(INSTALL_DIR)"
	install -m 0755 "$(BIN_DIR)/$(APP_NAME)" "$(INSTALL_DIR)/$(APP_NAME)"
	@if command -v xattr >/dev/null 2>&1; then \
		xattr -d com.apple.quarantine "$(INSTALL_DIR)/$(APP_NAME)" 2>/dev/null || true; \
	fi
	@echo "✅ Installed. Run with: $(APP_NAME)"

# Run tests
test:
	@go test ./...

# Clean build artifacts
clean:
	@rm -rf ./bin/

# Show help
help:
	@echo "Available targets:"
	@echo "  all     - Build wyrm (default)"
	@echo "  build   - Build bin/wyrm"
	@echo "  install - Build and install to $(INSTALL_DIR)/wyrm"
	@echo "  test    - Run Go tests"
	@echo "  clean   - Clean build artifacts"
	@echo "  help    - Show this help"
