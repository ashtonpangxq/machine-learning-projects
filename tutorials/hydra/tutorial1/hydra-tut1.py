import hydra
import os
from omegaconf import DictConfig, OmegaConf


@hydra.main(version_base=None, config_path="conf", config_name="config")
def func(cfg: DictConfig):
    working_dir = os.getcwd()
    orig_cwd = hydra.utils.get_original_cwd()

    print(f"The current working directory is {working_dir}")
    print(f"Getting original current working directory: {orig_cwd}")

    # Read file
    path = f"{orig_cwd}/test.txt"
    with open(path, "r") as f:
        print(f.read())

    # Write file
    path = f"output.txt"
    with open(path, "w") as f:
        f.write("This is a dog")

    # To access elements of the config
    print(f"The batch size is {cfg.batch_size}")
    print(f"The learning rate is {cfg['lr']}")


if __name__ == "__main__":
    func()
