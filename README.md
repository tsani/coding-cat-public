# Coding cat public problems

[Coding Cat](https://github.com/tsani/coding-cat) is a simple, in-browser platform for doing small
Python problems to learn programming.

This repository contains the publicly available problems for Coding Cat.

# Structure of the problems

Each problem must be in its own directory. The directory name should meaningfully reflect the
problem description.

Each directory must contain the following files to describe the coding problem.

- `description.md`
  This is the problem prompt prompt and explains the problem.
- `io.json` TODO
- etc.

NOTE: the name in meta must be the name of the functino you want to test and
run, in most cases this is the exact same function name as the starter function
name!

# Building

Included in this repo is a build script for compiling the list of problems into `problems.js`,
which is then imported by the main Coding Cat UI.
