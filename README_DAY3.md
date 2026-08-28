# MLOps 3일차 - GCP 외부 배포

## VM 정보
- Project: `mlops-aiffel-260825`
- Instance: `mlops-day3-vm`
- Zone: `us-central1-a`
- Machine: `t2a-standard-1` (ARM64, Mac Silicon 호환)
- OS: Ubuntu 22.04 LTS arm64
- Disk: 30GB Standard persistent disk
- External IP: `35.225.84.157`
- Tags: `http-server`, `https-server`

## 접속
- Swagger: http://35.225.84.157/docs
- Predict: `POST http://35.225.84.157/predict`

```bash
curl -X POST http://35.225.84.157/predict \
  -H "Content-Type: application/json" \
  -d '{"data":[5.1,3.5,1.4,0.2]}'
```

## Streamlit (로컬)
```bash
cd mlops_serving
streamlit run streamlit_app.py
```

## 비용 주의 (유료 계정)
실습 후 반드시 VM 중지:

```bash
gcloud compute instances stop mlops-day3-vm --zone=us-central1-a
```

삭제:

```bash
gcloud compute instances delete mlops-day3-vm --zone=us-central1-a
```

## 참고
수업 예시 이미지 `parkhc/iris-classifier:v1`는 amd64 only라 ARM(T2A)에서 pull 불가.
Mac Silicon 경로에 맞춰 `mlops_serving` 코드를 VM에서 직접 빌드해 `iris-classifier:v1`로 배포함.
