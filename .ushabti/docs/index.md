# Project Documentation

## Project Name

Ushabti

## Description

A file-backed, agent-driven development system for Claude Code. Development happens in bounded Phases that are planned (Scribe), implemented (Builder), and reviewed (Overseer). All state lives in files under `.ushabti/`, not in chat history. Six specialized agents with enforced role boundaries handle different aspects of the workflow.

## Table of Contents

- [Architecture Overview](architecture.md) — System architecture, Phase loop, state model, agent boundaries
- [Agent Reference](agents.md) — All six agents: purposes, boundaries, inputs, outputs, handoffs
- [Skills Reference](skills.md) — Domain knowledge and utility skills (20 total)
- [Phase Files Reference](phase-files.md) — Phase directory structure and file formats
- [Configuration Reference](configuration.md) — Laws, style, plugin manifest, Claude settings
- [Plugin Structure](plugin-structure.md) — Claude Code plugin packaging and validation
