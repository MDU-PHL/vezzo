cl-# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

## [Unreleased]

### Added

- Regex to parse version string from a larger string, and allowing for optional path number
- Parse function that takes a string and returns a semver.VersionInfo object
- Verify function that takes a expected version and a version requirement and returns a tuple with boolean and the observed version
- get_version function that takes a path to a tool and a version flag and returns the version string
- verify_from_config function that takes a path to a config file in YAML format, and checks each tool's version against the requirements. This is the main function of the library
- README.md
- Example code to show how to use the library

