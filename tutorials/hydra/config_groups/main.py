from omegaconf import DictConfig, OmegaConf
import hydra


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(f'Driver: {cfg["db"]["driver"]}')
    print(f'Password: {cfg["db"]["password"]}')
    print(f'Timeout: {cfg["db"]["timeout"]}')
    print(f'User: {cfg["db"]["user"]}')


if __name__ == "__main__":
    main()
