import hydra
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="conf/", config_name="config")
def main_func(cfg: DictConfig):
    print(f"Num features = {cfg.model.num_layers}")


if __name__ == "__main__":
    main_func()
