# gpapis - GlobalPlatform API Manager

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
│       ├── exports/
│       ├── exports23/
│       ├── gpapi-globalplatform.jar
│       └── README.TXT
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

Each API type should follow this structure:

```
API_TYPE/
└── version/
    ├── exports/
    ├── exports23/ (optional)
    ├── gpapi-globalplatform.jar
    └── README.TXT
```

For example:
```
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