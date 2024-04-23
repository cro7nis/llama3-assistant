from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="UI",
    settings_files=['configs/ui.yaml',
                    'configs/.secrets.yaml'],
    environments=True,
    load_dotenv=True,
    env_switcher="DYNACONF_ENV",
    env='development'
)
