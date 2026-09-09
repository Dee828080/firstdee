# firstdee

A Vega OS (Fire TV) Hello World app generated from the official `helloWorld` template (React Native 0.83).

| | |
| --- | --- |
| App name | `firstdee` |
| Package ID | `com.dee.firstdee` |
| Interactive component | `com.dee.firstdee.main` |
| Template | `helloWorld` (Vega SDK 0.24) |

## Prerequisites

Install the [Vega Developer Tools](https://developer.amazon.com/docs/vega/latest/install-vega-sdk.html) (CLI + SDK):

```bash
curl -fsSL https://sdk-installer.vega.labcollab.net/get_vvm.sh | bash && source ~/vega/env
vega sdk install
```

Node.js 20+ is required.

## Setup

```bash
npm install
```

## Develop

```bash
# Metro bundler (Fast Refresh)
npm start

# Unit tests
npm test

# Lint
npm run lint
```

## Build and run

```bash
# Debug package for Vega OS
npm run build:debug

# Install and launch on the Vega Virtual Device
vega run-app <path-to-vpkg> com.dee.firstdee.main -d VirtualDevice
```

See [Build a Hello World app](https://developer.amazon.com/docs/vega/latest/hello-world.html) and the [Vega CLI reference](https://developer.amazon.com/docs/vega/latest/cli-tools.html).

## Project layout

```
src/App.tsx              # Main TV UI (Hello Vega + focusable tiles)
src/components/Tile.tsx  # D-Pad focusable tile
src/data/tiles.tsx       # Tile content
manifest.toml            # Vega package identity and runtime
index.js                 # AppRegistry entry
```
