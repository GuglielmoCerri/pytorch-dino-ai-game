# PyTorch Dino AI Game

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.10.0-%23EE4C2C)](https://pytorch.org/)
[![Python Version](https://img.shields.io/badge/python-3.10-green)](https://www.python.org/downloads/)
[![EfficientNet](https://img.shields.io/badge/EfficientNet-v2-%2300BFFF)](https://ai.googleblog.com/2020/10/revisiting-efficiency-in-self.html)

![dino-image](https://2.bp.blogspot.com/-uNHI8p4KzHY/W5PwnM7BOcI/AAAAAAAALxQ/vGdcDA5ysqQ1VLjqtVX3LBIrDF4bV0_rQCLcBGAs/s1600/Dino-Chrome-HTNovo.gif)

This repository contains code and resources for creating an AI model that can play the popular Chrome Dino Game using PyTorch and EfficientNet. The goal of this project is to train an AI agent to achieve high scores in the game by automatically detecting and reacting to obstacles.

The repository includes scripts for capturing game screens, processing the captured images to create a dataset, and a Jupyter notebook for training the AI model. By following the provided instructions, you can set up the environment, collect game data, and train your own AI model to play the Chrome Dino Game.

Feel free to explore the code, modify it according to your requirements, and experiment with different approaches to improve the AI agent's performance.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.10
- PyTorch 1.10.0
- CUDA Toolkit 11.1 (for GPU acceleration)

## Installation

To get started with the project, follow these steps:

1. Clone the repository:

    ```shell
    git clone https://github.com/GuglielmoCerri/pytorch-dino-ai-game.git
    ```

2. Create a new conda environment:

    ```shell
    conda env create -f environment.yml
    ```

3. Activate the environment:

    ```shell
    conda activate dino
    ```

## Usage

1. Start playing the [Chrome Dino Game](https://chromedino.com/)

2. Capture the game screens by running the captures.py script:

    ```shell
    python src/captures.py
    ```

3. Process the captured images and create a dataset using the process.py script:

    ```shell
    python src/process.py
    ```

4. Train the AI model using the [train.ipynb](notebook/Train.ipynb) notebook

## Contributing

Thank you for considering contributing to this project! Contributions are welcome and greatly appreciated.

To contribute to the project, please follow these steps:

1. Fork the repository and create your branch from `main`.
2. Make your desired changes to the codebase.
3. Ensure that your code follows the project's coding style and conventions.
4. Write tests to validate your changes, if applicable.
5. Commit your changes with clear and descriptive commit messages.
6. Push your changes to your forked repository.
7. Submit a pull request to the main repository, explaining the changes you have made.

Please note the following guidelines for contributing:

- Be respectful and considerate towards others.
- Ensure that your contributions align with the project's goals and scope.
- Provide detailed and constructive feedback in any discussions.
- Follow the project's code of conduct.

By contributing to this project, you agree to abide by the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

Thank you for your support and contributions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
