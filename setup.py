# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
from io import open


def load_requirements(file_list=None):
    if file_list is None:
        file_list = ["requirements.txt"]
    if isinstance(file_list, str):
        file_list = [file_list]
    requirements = []
    for file in file_list:
        with open(file, encoding="utf-8-sig") as f:
            requirements.extend(f.readlines())
    return requirements


def readme():
    with open("README.md", encoding="utf-8-sig") as f:
        README = f.read()
    return README


setup(
    name="unstructured.paddleocr",
    packages=find_packages(),
    include_package_data=True,
    version="2.6.1.3",
    install_requires=[
        "shapely",
        "scikit-image",
        "imgaug",
        "pyclipper",
        "lmdb",
        "tqdm",
        "numpy",
        "visualdl",
        "rapidfuzz",
        "opencv-python==4.8.0.76",
        "opencv-contrib-python==4.8.0.76",
        "cython",
        "lxml",
        "premailer",
        "openpyxl",
        "attrdict",
        "Polygon3",
        "lanms-neo==1.0.2",
        "pdf2image",
    ],
    license="Apache License 2.0",
    description="Awesome OCR toolkits based on PaddlePaddle （8.6M ultra-lightweight pre-trained model, support training and deployment among server, mobile, embeded and IoT devices",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/UnstructureIO/unstructured.PaddleOCR",
    download_url="https://github.com/UnstructureIO/unstructured.PaddleOCR.git",
    keywords=[
        "ocr textdetection textrecognition paddleocr crnn east star-net rosetta ocrlite db chineseocr chinesetextdetection chinesetextrecognition"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
)
