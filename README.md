# MLOps Iris Model Serving

FastAPI 기반 Iris 분류 모델 서빙 프로젝트입니다.

## 로컬 실행

```bash
python train_model.py
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Docker

```bash
docker build -t my-ml-app .
docker run -d -p 8000:8000 my-ml-app
```

## CI/CD

`main` 브랜치에 push하면 GitHub Actions가 Docker Hub에 이미지를 빌드·푸시하고 GCP VM에 자동 배포합니다.
