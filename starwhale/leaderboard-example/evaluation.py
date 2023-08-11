from __future__ import annotations

import random
import time

from starwhale import evaluation, handler

categories = [
    "STEM",
    "China Specific",
    "Social Science",
    "Humanities",
    "Business",
    "Law",
    "Medicine",
    "Other",
]

samples = [
    ("佛教最早传入中国的经典是?", ("四十二经", "法句经", "般若经", "心经"), "A"),
    ("下列哪个不是中国古代四大发明之一?", ("指南针", "火药", "印刷术", "造纸术"), "A"),
    ("文学史上第一部诗歌总集是?", ("《诗经》", "《楚辞》", "《离骚》", "《古诗十九首》"), "A"),
    ("下列哪个不是中国古代四大名著之一?", ("《三国演义》", "《水浒传》", "《红楼梦》", "《西游记》"), "A"),
    ("战国时期的哪个国家最先统一了中国?", ("秦国", "齐国", "楚国", "燕国"), "A"),
    ("史记是我国第一部纪传体通史，它的作者是?", ("司马迁", "司马光", "司马相如", "司马昭"), "A"),
    ("2002年世界杯足球赛在哪个国家举行?", ("韩国", "日本", "中国", "德国"), "A"),
    ("下列哪个不是我国古代四大美女之一?", ("杨贵妃", "西施", "貂蝉", "王昭君"), "A"),
    ("明朝的开国皇帝是?", ("朱元璋", "朱棣", "朱高炽", "朱由检"), "A"),
    ("中国古代的四大美女之一的西施是哪国人?", ("越国", "齐国", "楚国", "燕国"), "A"),
    ("三角函数中，正切函数的定义域是?", ("R-{(2k+1)π/2|k∈Z}", "R-{kπ|k∈Z}", "R-{(2k+1)π|k∈Z}", "R-{2kπ|k∈Z}"), "A"),
]

benchmark = [
    "cmmlu",
    "mmlu",
    "arc",
    "TruthfulQA",
    "C-Eval",
    "Gaokao",
    "AGIEval",
    "HellaSwag",
]

llm = [
    "llama",
    "vicuna",
    "guanaco",
    "baichuan",
    "alpaca",
    "falcon",
]

@handler(require_dataset=False)
def leaderboard_example() -> None:
    random.seed(time.time_ns())

    def _acc() -> float:
        return random.randint(1, 100) / 100

    summary = {
        "gpu": "A100",
        "mem": "500M",
        "cpu": "Intel Xeon",
        "llm": random.choice(llm),
        "accuracy": _acc(),
        "accuracy_zero_shot": _acc(),
        "accuracy_one_shot": _acc(),
        "accuracy_few_shot": _acc(),
        "benchmark/name": random.choice(benchmark),
        "benchmark/counts": random.randint(100, 1000),
        "benchmark/categories": random.randint(10, 50),
    }

    for c in categories:
        c = (c.replace(" ", "_")).lower()
        summary[f"{c}/accuracy"] = _acc()
        summary[f"{c}/accuracy_zero_shot"] = _acc()
        summary[f"{c}/accuracy_one_shot"] = _acc()
        summary[f"{c}/accuracy_few_shot"] = _acc()

    evaluation.log_summary(summary)

    for idx, (question, choices, answer) in enumerate(samples):
        evaluation.log(
            category="results",
            id=f"benchmark-{idx}",
            metrics={
                "features": {
                    "question": question,
                    "choices": ", ".join(choices),
                    "answer": answer,
                    "category": random.choice(categories),
                },
                "output": {
                    "prediction": random.choice(choices),
                    "prediction_confidence": _acc(),
                },
                "duration_seconds": random.randint(1, 100),
            }
        )

    for category in categories:
        c = (category.replace(" ", "_")).lower()

        evaluation.log(
            category="shot_summary",
            id=c,
            metrics={
                "zero_shot": _acc(),
                "one_shot": _acc(),
                "few_shot": _acc(),
            }
        )