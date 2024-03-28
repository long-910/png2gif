import os
import argparse
from PIL import Image


def create_gif(input_path, output_filename, frame_rate):
    # ファイル名から拡張子を取り出し、出力ファイルの拡張子をGIFに変更する
    if not output_filename:
        output_filename = os.path.basename(os.path.normpath(input_path)) + ".gif"
    else:
        output_filename = os.path.splitext(output_filename)[0] + ".gif"

    # 入力パス内のPNGファイルを取得
    png_files = [f for f in os.listdir(input_path) if f.endswith('.png')]

    # PNGファイルを読み込み、GIFを作成するための画像リストを作成
    images = []
    for png_file in png_files:
        image_path = os.path.join(input_path, png_file)
        img = Image.open(image_path)
        images.append(img)

    # GIFを作成
    images[0].save(output_filename, save_all=True, append_images=images[1:], duration=frame_rate, loop=0)


def main():
    parser = argparse.ArgumentParser(description="Convert PNG images to GIF")
    parser.add_argument("input_path", help="Input path containing PNG images")
    parser.add_argument("--output_filename", help="Output GIF filename")
    parser.add_argument("--frame_rate", type=int, default=10, help="Frame rate for the GIF (default: 10 FPS)")
    args = parser.parse_args()

    create_gif(args.input_path, args.output_filename, args.frame_rate)


if __name__ == "__main__":
    main()
