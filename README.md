# gpapis - GlobalPlatform API Manager

**gpapis is a library** — it manages GlobalPlatform API paths and is consumed by higher-level tools
like [jctool](https://github.com/ibaibing/jctool) and [gpca](https://github.com/ibaibing/gpca).
It is not a standalone application.

### Toolchain Ecosystem

gpapis lives at the **environment layer** of the toolchain:

```
┌──────────────────────────────────────────┐
│  sctool (sc) — Unified CLI               │
│  ├── sc ca (gpca) — Certificate mgmt     │
│  └── sc jc (jctool) — JavaCard dev       │
├──────────────────────────────────────────┤
│  jcsdks  │  gpapis (this project)        │
│  SDK     │  GP API path management       │
│  (library, not standalone)               │
├──────────────────────────────────────────┤
│  javacard-demo — teaching example         │
└──────────────────────────────────────────┘
```

| Project | Role |
|---------|------|
| [sctool](https://github.com/ibaibing/sctool) | Unified CLI entry point — `sc` |
| [gpca](https://github.com/ibaibing/gpca) | Certificate mgmt for SCP — `sc ca` (depends on this library) |
| [jctool](https://github.com/ibaibing/jctool) | JavaCard dev — `sc jc` (depends on this library) |
| [jcsdks](https://github.com/ibaibing/jcsdks) | JavaCard SDK path management (library) |
| **gpapis** | **GP API path management (this library)** |
| [javacard-demo](https://github.com/ibaibing/javacard-demo) | Teaching example for the complete toolchain |

You typically do not call `python -m gpapis` directly unless verifying API setup.
Instead, jctool's `jc build` / `jc detect` and gpca's certificate lookups use gpapis
internally to find GP API export files and AID information.

A simple tool to help JavaCard developers configure and access GlobalPlatform API specifications.

## Features

- 📦 **API Configuration**: Set up and manage GlobalPlatform API specifications
- 🔍 **API Validation**: Verify that API specifications are properly configured
- ⚙️ **Path Management**: Help users set up API paths correctly
- 📋 **Configuration Check**: Validate user's API configuration
- 📚 **Documentation**: Clear instructions for API usage

## Installation

```bash
pip install gpapis
```

## Getting Started

### 1. Obtain GlobalPlatform API Specifications

GlobalPlatform API specifications can be obtained from the GlobalPlatform Official Website.

### 2. Extract API Specifications

Extract the downloaded API specifications to a directory of your choice. The expected structure is:

```
E:/GlobalPlatformAPIs/
├── BROKER/
│   └── 1.0/
│       ├── exports/
│       ├── exports23/
│       ├── gpapi-globalplatform.jar
│       └── README.TXT
├── CONTACTLESS/
│   └── 1.0/
│       ├── exports/
│       ├── exports23/
│       ├── gpapi-globalplatform.jar
│       └── README.TXT
├── CORE/
│   ├── 1.0/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.1/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.2/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.3/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.4/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.5/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.6/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.7/
│   │   ├── exports/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   ├── 1.8/
│   │   ├── exports/
│   │   ├── exports23/
│   │   ├── gpapi-globalplatform.jar
│   │   └── README.TXT
│   └── 1.9/
│       ├── diff/
│       ├── exports/
│       ├── javadoc/
│       ├── gpapi-globalplatform-ext.jar
│       ├── gpapi-globalplatform.jar
│       ├── README.TXT
│       ├── src-gpapi-globalplatform-ext.jar
│       └── src-gpapi-globalplatform.jar
├── OPEN/
│   └── 1.0/
│       ├── exports/
│       ├── exports23/
│       ├── gpapi-globalplatform.jar
│       └── README.TXT
├── SCPP/
│   └── 1.0/
│       ├── exports/
│       ├── exports23/
│       ├── gpapi-globalplatform.jar
│       └── README.TXT
└── UPGRADE/
    └── 1.0/
        ├── exports/
        ├── exports23/
        ├── gpapi-globalplatform.jar
        └── README.TXT
```

### 3. Configure API Path

Set the `GLOBALPLATFORM_API_ROOT` environment variable to point to your API specifications directory:

#### Windows
```cmd
set GLOBALPLATFORM_API_ROOT=E:/GlobalPlatformAPIs
```

#### Linux/macOS
```bash
export GLOBALPLATFORM_API_ROOT=/path/to/your/apis
```

### 4. Verify Configuration

```bash
python -m gpapis validate
```

## Project Structure

```
gpapis/
├── gpapis/
│   ├── __init__.py          # Package initialization
│   ├── api.py               # API access functions
│   ├── cli.py               # Command-line interface
│   └── __main__.py          # Entry point for `python -m gpapis`
├── README.md                # This file
└── setup.py                 # Installation script
```

## Commands

### Validate API Configuration

```bash
python -m gpapis validate
```

Validates that:
- `GLOBALPLATFORM_API_ROOT` environment variable is set
- API directory exists
- API specifications are properly structured

### Show API Information

```bash
python -m gpapis info
```

Displays information about detected API specifications.

### Installation Wizard

```bash
python -m gpapis wizard
```

Interactive wizard to guide API configuration.

## Expected API Structure

### API Types

The following API types are supported:

1. **BROKER** - Broker API
2. **CONTACTLESS** - Contactless API  
3. **CORE** - Core GlobalPlatform API
4. **OPEN** - Open API
5. **SCPP** - SCPP API
6. **UPGRADE** - Upgrade API

### Expected Directory Structure

Each API type should follow this basic structure:

```
API_TYPE/
└── version/
    ├── exports/
    ├── exports23/ (optional)
    ├── gpapi-globalplatform.jar
    └── README.TXT
```

### Complete API Structure Examples

```
BROKER/
└── 1.0/
    ├── exports/
    ├── exports23/
    ├── gpapi-globalplatform.jar
    └── README.TXT

CONTACTLESS/
└── 1.0/
    ├── exports/
    ├── exports23/
    ├── gpapi-globalplatform.jar
    └── README.TXT

CORE/
├── 1.0/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.1/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.2/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.3/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.4/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.5/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.6/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.7/
│   ├── exports/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
├── 1.8/
│   ├── exports/
│   ├── exports23/
│   ├── gpapi-globalplatform.jar
│   └── README.TXT
└── 1.9/
    ├── diff/
    ├── exports/
    ├── javadoc/
    ├── gpapi-globalplatform-ext.jar
    ├── gpapi-globalplatform.jar
    ├── README.TXT
    ├── src-gpapi-globalplatform-ext.jar
    └── src-gpapi-globalplatform.jar

OPEN/
└── 1.0/
    ├── exports/
    ├── exports23/
    ├── gpapi-globalplatform.jar
    └── README.TXT

SCPP/
└── 1.0/
    ├── exports/
    ├── exports23/
    ├── gpapi-globalplatform.jar
    └── README.TXT

UPGRADE/
└── 1.0/
    ├── exports/
    ├── exports23/
    ├── gpapi-globalplatform.jar
    └── README.TXT
```

## Requirements

- Python 3.8+
- GlobalPlatform API specifications (obtained directly from GlobalPlatform or trusted sources)

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

**Important**: This project does NOT distribute any GlobalPlatform API specifications. Users must obtain specifications directly from GlobalPlatform or trusted sources and comply with their licensing terms.

## Contributing

Contributions are welcome! Please submit issues and pull requests on [GitHub](https://github.com/ibaibing/gpapis).