import os
import pytest
from PIL import Image
from png2gif.converter import create_gif


@pytest.fixture
def test_images(tmpdir):
    # テスト用のPNG画像を作成して一時ディレクトリに保存する
    images = []
    for i in range(5):
        img = Image.new("RGB", (100, 100), color=(i * 50, i * 50, i * 50))
        img.save(os.path.join(tmpdir, f"test_image_{i}.png"))
        images.append(img)
    return tmpdir


def test_create_gif(tmpdir, test_images):
    # テスト用のPNG画像からGIFを生成し、出力ファイルが存在することを確認する
    output_filename = os.path.join(tmpdir, "test_output.gif")
    create_gif(test_images, output_filename, frame_rate=10)
    assert os.path.isfile(output_filename)

    # 出力ファイルを開いてGIFとして正しく読み込めることを確認する
    gif = Image.open(output_filename)
    assert gif.n_frames == 5  # 5枚の画像が含まれていることを確認する
    assert gif.is_animated  # GIFがアニメーションであることを確認する

    # 画像の幅と高さが正しいことを確認する
    assert gif.size == (100, 100)
