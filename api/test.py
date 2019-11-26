import requests

resp = requests.post(
    "http://localhost:5000/predict",
    files={
        "file": open(
            "/Users/jesse/xomnia/keurmerken-od/data/test_results/MELKAN-JONG-GESNEDEN--400GR-59981.png",
            "rb",
        )
    },
)
