# PNG to GIF Converter

This Python script converts a series of PNG images into a GIF animation.

## Requirements

- Python 3.x
- Pillow library (`pip install pillow`)

## Usage

```
python png_to_gif_converter.py input_path [--output_filename OUTPUT_FILENAME] [--frame_rate FRAME_RATE]
```

- `input_path`: Path to the directory containing PNG images.
- `--output_filename`: (Optional) Filename for the output GIF. If not provided, the default filename will be based on the input directory name.
- `--frame_rate`: (Optional) Frame rate for the GIF animation. Default is 10 FPS.

## Example

```
python png_to_gif_converter.py images/ --output_filename animation.gif --frame_rate 15
```

This command will convert all PNG images in the `images/` directory into a GIF animation named `animation.gif` with a frame rate of 15 FPS.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
