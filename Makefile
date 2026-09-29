.PHONY: all build install test clean help

# Default target
all: build

# Build only
build:
	@./build.sh

# Install into GOBIN/GOPATH bin
install:
	@go install .

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
	@echo "  install - Install wyrm with go install"
	@echo "  test    - Run Go tests"
	@echo "  clean   - Clean build artifacts"
	@echo "  help    - Show this help"
