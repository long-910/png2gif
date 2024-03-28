import argparse
from png_to_gif_converter.converter import create_gif


def main():
    parser = argparse.ArgumentParser(description="Convert PNG images to GIF.")
    parser.add_argument(
        "input_path", type=str, help="Path to the directory containing PNG images."
    )
    parser.add_argument(
        "output_filename", type=str, help="Name of the output GIF file."
    )
    parser.add_argument(
        "--frame_rate",
        type=int,
        default=10,
        help="Frame rate of the output GIF (default: 10 FPS).",
    )

    args = parser.parse_args()

    input_path = args.input_path
    output_filename = args.output_filename
    frame_rate = args.frame_rate

    create_gif(input_path, output_filename, frame_rate)


if __name__ == "__main__":
    main()
