# PNG to GIF Converter

[![Python package](https://github.com/long-910/png2gif/actions/workflows/python-package.yml/badge.svg)](https://github.com/long-910/png2gif/actions/workflows/python-package.yml)

This Python script converts a series of PNG images into a GIF animation.

## Requirements

- Python 3.x
- Pillow library (`pip install pillow`)

## Installation

You can install the package using pip:

```bash
pip install .
```

## Usage

### Command Line Interface

After installation, you can use the command line interface (CLI) to convert PNG images to GIF.

```bash
png2gif input_path output_filename --frame_rate 10
```

- `input_path`: Path to the directory containing PNG images.
- `output_filename`: Name of the output GIF file.
- `--frame_rate`: Frame rate of the output GIF (default: 10 FPS).

### Direct Execution

You can also execute the package directly without installation:

```bash
python -m png2gif input_path output_filename --frame_rate 10
```

### Module Usage

If you prefer to use the package as a module in your Python code:

```python
from png2gif import create_gif

input_path = "path/to/input_directory"
output_filename = "output.gif"
frame_rate = 10

create_gif(input_path, output_filename, frame_rate)
```

## Development

### Running Tests

```bash
pytest
```

You can run the tests using pytest:

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bug fixes, feature requests, or general improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
