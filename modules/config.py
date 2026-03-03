from environs import Env
from dataclasses import dataclass

env = Env()
env.read_env()

def load_RNC_token() -> str:
    return env.str("RNC_TOKEN")

def load_BNC_token() -> str:
    return env.str("BNC_TOKEN")

def load_COCA_token() -> str:
    return env.str("COCA_TOKEN")

@dataclass
class CorpusSettings:
    COCA_SUBCORPUS: str
    BNC_SUBCORPUS: str
    RNC_SUBCORPUS: str
    DATE_START: int
    DATE_END: int

def load_corpus_settings() -> CorpusSettings:
    return CorpusSettings(
        COCA_SUBCORPUS=env.str("COCA_SUBCORPUS", default="MAIN"),
        BNC_SUBCORPUS=env.str("BNC_SUBCORPUS", default="MAIN"),
        RNC_SUBCORPUS=env.str("RNC_SUBCORPUS", default="MAIN"),
        DATE_START=env.int("DATE_START", default=2000),
        DATE_END=env.int("DATE_END", default=2026)
    )