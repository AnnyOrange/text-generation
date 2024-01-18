import argparse
import os
from typing import List

import numpy as np
from datasets import Dataset, Features
from datasets import Image as ImageFeature
from datasets import Value

DS_NAME = "Text-style-dataset"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_root", type=str, default="Text-style-dataset")
    parser.add_argument("--instructions_path", type=str, default="prompt.txt")
    args = parser.parse_args()
    return args


def load_instructions(instructions_path: str) -> List[str]:
    with open(instructions_path, "r") as f:
        instructions = f.readlines()
    instructions = [i.strip() for i in instructions]
    return instructions


def generate_examples(data_paths: List[str], instructions: List[str]):
    def fn():
        for data_path in data_paths:
            yield {
                "init_image": {"path": data_path[0]},
                "edit_prompt": np.random.choice(instructions),
                "style_image": {"path": data_path[1]},
            }

    return fn


def map_and_create_parquet(data_paths: List[str], instructions: List[str]):
    generation_fn = generate_examples(data_paths, instructions)
    print("Mapping...")
    ds = Dataset.from_generator(
        generation_fn,
        features=Features(
            init_image=ImageFeature(),
            edit_prompt=Value("string"),
            style_image=ImageFeature(),
        ),
    )

    # You can perform additional operations here if needed
    # ...

    return ds


def main(args):
    instructions = load_instructions(args.instructions_path)

    data_paths = os.listdir(args.data_root)
    data_paths = [os.path.join(args.data_root, d) for d in data_paths]
    new_data_paths = []
    for data_path in data_paths:
        init_image = os.path.join(data_path, "init_image.jpg")
        style_image = os.path.join(data_path, "style_image.jpg")
        new_data_paths.append((init_image, style_image))

    mapped_ds = map_and_create_parquet(new_data_paths, instructions)

    # Now you have the mapped dataset locally, you can perform further actions if needed.

    # Example: Save to a local file
    mapped_ds.to_parquet("train.parquet")

if __name__ == "__main__":
    args = parse_args()
    main(args)
