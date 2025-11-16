# 🤖 AI Team - 24/7 대화형 AI 팀

완전 무료로 운영되는 AI 팀 시스템입니다. 실제 회사처럼 PM, 개발자, DevOps, 마케터 역할을 하는 AI 에이전트들과 대화하며 프로젝트를 진행할 수 있습니다.

## 🌟 주요 특징

- **🎯 자동 라우팅**: 질문만 입력하면 AI가 자동으로 적절한 팀원 선택
- **💰 완전 무료**: Grok과 Mistral의 무료 API 사용
- **👥 전문 팀 구성**: PM, 개발자, DevOps, 마케터 각 분야 전문가
- **🚀 실전 활용**: 실제 프로젝트 기획부터 개발, 배포, 마케팅까지 전 과정 지원
- **⚡️ 빠른 응답**: 병렬 처리로 여러 팀원에게 동시 질문 가능
- **🔧 확장 가능**: 디자이너, QA, 데이터 분석가 등 팀원 추가 가능

## 📦 설치 및 실행

### 1. 저장소 클론

```bash
git clone https://github.com/chosundeveloper/ai-team-24-7.git
cd ai-team-24-7
```

### 2. 가상 환경 생성 및 패키지 설치

```bash
# 가상 환경 생성
python3 -m venv venv

# 가상 환경 활성화
source venv/bin/activate  # macOS/Linux
# 또는
venv\Scripts\activate  # Windows

# 패키지 설치
pip install -r requirements.txt
```

### 3. API 키 설정

```bash
# .env 파일 생성
cp .env.example .env

# .env 파일 편집하여 실제 API 키 입력
# GROK_API_KEY=your_actual_grok_key
# MISTRAL_API_KEY=your_actual_mistral_key
```

### 4. 실행

```bash
python3 ai_team.py
```

### 3. 시작 화면

```
✅ AI 팀 준비됨
  /pm - PM
  /dev - Dev
  /ops - Ops
  /mkt - Marketing

명령어:
  /pm [질문] - PM에게 물어보기
  /dev [작업] - 개발자에게 작업 지시
  /ops [작업] - DevOps에게 작업 지시
  /mkt [작업] - 마케팅에게 작업 지시
  /all [질문] - 전체 팀에게 물어보기
  /quit - 종료

👤 You>
```

## 👥 팀 구성원

### 📊 PM (Product Manager) - Grok AI
**전문 분야:**
- 제품 전략 수립 및 로드맵 작성
- 요구사항 정의 및 우선순위 결정
- 비즈니스 모델 설계
- 기능 기획 및 스펙 문서 작성
- 시장 분석 및 경쟁사 조사

**활용 사례:**
```
/pm SaaS 구독 서비스 비즈니스 모델 기획해줘
/pm 이커머스 MVP 기능 우선순위 정해줘
/pm 경쟁사 분석해서 차별점 찾아줘
```

### 💻 Dev (Full-stack Developer) - Mistral AI
**전문 분야:**
- 백엔드/프론트엔드 개발
- API 설계 및 구현
- 데이터베이스 모델링
- 코드 리뷰 및 최적화
- 기술 스택 선정

**활용 사례:**
```
/dev FastAPI로 REST API 만들어줘
/dev React 회원가입 폼 코드 짜줘
/dev PostgreSQL 스키마 설계해줘
/dev 이 코드 성능 개선 방법 알려줘
```

### 🔧 Ops (DevOps Engineer) - Grok AI
**전문 분야:**
- Docker/Kubernetes 컨테이너화
- CI/CD 파이프라인 구축
- 클라우드 인프라 설계 (AWS, GCP, Azure)
- 모니터링 및 로깅 시스템
- 보안 및 성능 최적화

**활용 사례:**
```
/ops Docker Compose로 개발 환경 만들어줘
/ops GitHub Actions CI/CD 파이프라인 구성해줘
/ops AWS에 배포하는 방법 알려줘
/ops Nginx 리버스 프록시 설정해줘
```

### 📣 Marketing (Marketing Specialist) - Mistral AI
**전문 분야:**
- 마케팅 전략 수립
- 콘텐츠 마케팅 기획
- 그로스 해킹 전략
- SEO/SEM 최적화
- 소셜미디어 마케팅

**활용 사례:**
```
/mkt 제품 런칭 마케팅 전략 짜줘
/mkt 블로그 콘텐츠 주제 추천해줘
/mkt Product Hunt 런칭 플랜 만들어줘
/mkt 인스타그램 광고 카피 작성해줘
```

## 💬 명령어 상세 가이드

### 🎯 자동 라우팅 (NEW!)

```bash
질문만 입력하면 AI가 자동으로 적절한 팀원 선택!
```

**예시:**
```
👤 You> FastAPI로 REST API 만드는 법 알려줘
🎯 Dev이(가) 답변합니다...

👤 You> 마케팅 전략 짜줘
🎯 Marketing이(가) 답변합니다...

👤 You> Docker 배포 어떻게 해?
🎯 Ops이(가) 답변합니다...
```

**장점**:
- 명령어 입력 불필요
- AI가 질문 내용 분석해서 최적의 팀원 자동 선택
- 매칭 불확실하면 전체 팀 회의로 자동 전환

### 개별 팀원과 대화

```bash
/pm [질문이나 요청]    # PM과 1:1 대화
/dev [질문이나 요청]   # 개발자와 1:1 대화
/ops [질문이나 요청]   # DevOps와 1:1 대화
/mkt [질문이나 요청]   # 마케터와 1:1 대화
```

**장점**: 빠른 응답, 특정 분야 집중
**사용 시**: 특정 팀원을 직접 지정하고 싶을 때

### 전체 팀 회의

```bash
/all [질문]  # 모든 팀원에게 동시에 질문
```

**장점**: 다각도 분석, 통합적 관점

**사용 시나리오:**
- 중요한 의사결정 필요할 때
- 여러 분야의 전문성이 필요한 질문
- 각 팀의 입장 비교 필요할 때

### 종료

```bash
/quit  # 프로그램 종료
```

## 📝 실전 활용 예시

### 시나리오 1: 새 프로젝트 시작

```
👤 You> /pm AI 챗봇 SaaS 만들고 싶은데 비즈니스 모델 기획해줘

💬 PM에게 전달 중...

[PM]
AI 챗봇 SaaS 비즈니스 모델 제안:

**🎯 타겟 고객**
- 중소기업 고객지원팀
- 이커머스 업체
- 온라인 교육 플랫폼

**💰 가격 전략 (월 구독)**
- Starter: $49/월 (월 1,000건 대화, 1개 봇)
- Professional: $149/월 (월 10,000건, 5개 봇, 커스텀 학습)
- Enterprise: Custom (무제한, 전담 지원, API 연동)

**🎁 핵심 기능**
- 24/7 자동 응답
- 다국어 지원 (한/영/일/중)
- 기존 시스템 연동 (Slack, Discord, 웹사이트)
- 대화 분석 대시보드
- 고객 만족도 자동 수집

**📊 수익 모델**
- 기본 구독료 (MRR)
- 사용량 기반 추가 과금
- 커스텀 학습 서비스 (별도)
- API 사용료 (B2B)

**🚀 Go-to-Market**
1. 무료 체험 (14일, 카드 불필요)
2. Product Hunt 런칭
3. 파트너십 (CRM, 헬프데스크 도구)
4. 케이스 스터디 콘텐츠

**핵심 지표**
- CAC < $150
- LTV > $2,000
- Churn < 5%/월
```

---

```
👤 You> /dev 위 기획을 구현하려면 기술 스택 뭐가 필요해?

💬 Dev에게 전달 중...

[Dev]
AI 챗봇 SaaS 기술 스택 추천:

**Backend:**
- **Framework**: FastAPI (빠르고 비동기 지원)
- **Database**: PostgreSQL (사용자/대화 데이터) + Redis (세션/캐시)
- **AI/ML**: OpenAI API or Anthropic Claude API
- **Queue**: Celery + RabbitMQ (비동기 작업 처리)

**Frontend:**
- **Framework**: Next.js 14 (React + SSR)
- **UI Library**: Tailwind CSS + shadcn/ui
- **State**: Zustand or React Query
- **Charts**: Recharts (대시보드용)

**Infrastructure:**
- **Container**: Docker + Docker Compose
- **Hosting**: Vercel (Frontend) + AWS ECS (Backend)
- **Storage**: AWS S3 (파일/로그)
- **CDN**: CloudFlare

**Integrations:**
- Stripe (결제)
- SendGrid (이메일)
- Slack/Discord SDK (채널 연동)

**구현 우선순위:**
1주차: 기본 챗봇 API + 간단한 대시보드
2주차: 사용자 인증 + 구독 관리
3주차: 다국어 지원 + 커스텀 학습
4주차: 분석 대시보드 + 통합 기능

코드 예제 필요하면 말씀하세요!
```

### 시나리오 2: 개발 문제 해결

```
👤 You> /dev Python으로 JWT 인증 구현하는 방법 알려줘

💬 Dev에게 전달 중...

[Dev]
FastAPI + JWT 인증 완전 구현 예제:

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel

# 설정
SECRET_KEY = "your-secret-key-here"  # 실제로는 환경변수 사용
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 모델
class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str
    email: str

# 유틸리티 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # 실제로는 DB에서 사용자 조회
    user = {"username": username, "email": f"{username}@example.com"}
    return user

# 엔드포인트
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # 실제로는 DB에서 사용자 검증
    fake_hashed_password = get_password_hash("password123")

    if not verify_password(form_data.password, fake_hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}, this is protected!"}
```

**설치 패키지:**
```bash
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart
```

**실행:**
```bash
uvicorn main:app --reload
```

**테스트:**
```bash
# 1. 로그인 (토큰 받기)
curl -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=password123"

# 응답: {"access_token": "eyJ...", "token_type": "bearer"}

# 2. 보호된 엔드포인트 접근
curl -X GET "http://localhost:8000/protected" \
  -H "Authorization: Bearer eyJ..."
```

**보안 강화 팁:**
1. SECRET_KEY는 환경변수로 관리
2. HTTPS 필수 (프로덕션)
3. Refresh Token 추가 고려
4. Rate Limiting 적용
5. Token Blacklist 구현 (로그아웃)
```

### 시나리오 3: 전체 팀 브레인스토밍

```
👤 You> /all 우리 SaaS에 AI 자동 학습 기능 추가하면 어떨까요?

📢 전체 팀에게 질문 중...

[PM]
**제품 관점:**
훌륭한 아이디어입니다! 경쟁 우위 확보 가능.

**가치 제안:**
- 고객사의 과거 대화 데이터로 자동 학습
- "당신만의 맞춤 AI" 포지셔닝
- 업계별 특화 모델 제공 가능

**가격 전략:**
- Professional 이상 플랜에만 제공
- 학습 데이터량에 따라 추가 과금
- "Smart Learning" 기능으로 브랜딩

**우선순위:** High (차별화 요소)
**예상 전환율 증가:** +15~20%

[Dev]
**기술 구현:**

```python
# 자동 학습 파이프라인
class AutoLearningPipeline:
    def __init__(self, user_id):
        self.user_id = user_id
        self.model = load_base_model()

    async def collect_conversations(self):
        # 지난 30일 대화 수집
        conversations = await db.query(
            "SELECT * FROM conversations WHERE user_id = ? AND created_at > ?",
            user_id, thirty_days_ago
        )
        return conversations

    async def prepare_training_data(self, conversations):
        # Q&A 쌍 추출 및 전처리
        training_data = []
        for conv in conversations:
            if conv.feedback_score > 4:  # 좋은 대화만
                training_data.append({
                    "question": conv.user_message,
                    "answer": conv.bot_response
                })
        return training_data

    async def fine_tune(self, training_data):
        # OpenAI Fine-tuning API 사용
        response = await openai.FineTune.create(
            training_file=upload_jsonl(training_data),
            model="gpt-3.5-turbo",
            suffix=f"customer-{self.user_id}"
        )
        return response.id

    async def deploy_model(self, fine_tune_id):
        # 학습된 모델을 유저 설정에 연결
        await db.update(
            "users",
            {"custom_model_id": fine_tune_id},
            {"id": self.user_id}
        )
```

**예상 개발 시간:** 2-3주
**비용:** OpenAI Fine-tuning API 사용 시 학습당 $3-10

[Ops]
**인프라 관점:**

**필요 리소스:**
- **스토리지**: S3에 학습 데이터 저장 (~$5/월 per 10K conversations)
- **컴퓨팅**: AWS SageMaker or Lambda (이벤트 기반)
- **큐 시스템**: 비동기 학습 작업 처리

**자동화 워크플로우:**
```yaml
# GitHub Actions - 자동 재학습
name: Auto Retrain Models
on:
  schedule:
    - cron: '0 2 * * 0'  # 매주 일요일 새벽 2시

jobs:
  retrain:
    runs-on: ubuntu-latest
    steps:
      - name: Collect new data
        run: python scripts/collect_data.py

      - name: Fine-tune models
        run: python scripts/fine_tune.py

      - name: Deploy updated models
        run: python scripts/deploy.py

      - name: Notify users
        run: python scripts/send_notifications.py
```

**모니터링:**
- 학습 성공률 대시보드
- 모델 성능 지표 (정확도, 응답 품질)
- 비용 추적 (Fine-tuning API 사용량)

**예상 인프라 비용:** $50-100/월 (100 고객 기준)

[Marketing]
**마케팅 전략:**

**메시징:**
- 헤드라인: "당신의 데이터로 학습하는 AI, 매일 더 똑똑해집니다"
- 핵심 가치: "No-Code AI Training"

**콘텐츠 아이디어:**
1. **케이스 스터디**: "자동 학습으로 고객 만족도 40% 향상"
2. **비교 콘텐츠**: "일반 챗봇 vs 학습하는 AI 챗봇"
3. **데모 영상**: 학습 전후 성능 비교

**런칭 캠페인:**
- Product Hunt: "AI that learns from YOUR business"
- LinkedIn 광고: B2B SaaS 타겟
- 웨비나: "AI 자동 학습으로 고객 지원 혁신하기"

**차별화 포인트:**
- 경쟁사 대부분 수동 학습 or 없음
- "Set it and forget it" 자동화 강조

**예상 효과:**
- 프리미엄 플랜 전환율 +25%
- PR 기회 (혁신 기술로 주목)
- 고객 이탈률 감소 (Lock-in 효과)
```

## 🔧 커스터마이징

### 팀원 추가

`ai_team.py`의 `Team.__init__()` 메서드를 수정:

```python
self.agents = {
    "pm": Agent("PM", "Product Manager", "grok"),
    "dev": Agent("Dev", "Full-stack Developer", "mistral"),
    "ops": Agent("Ops", "DevOps Engineer", "grok"),
    "mkt": Agent("Marketing", "Marketing Specialist", "mistral"),

    # 새 팀원 추가 예시
    "design": Agent("Designer", "UI/UX Designer specialized in SaaS products", "grok"),
    "qa": Agent("QA", "Quality Assurance Engineer focusing on test automation", "mistral"),
    "data": Agent("Data", "Data Analyst specialized in product analytics", "grok"),
}
```

### AI 모델 변경

각 에이전트의 AI 모델 변경:

```python
# "grok" 또는 "mistral" 선택
Agent("역할명", "상세 역할 설명", "grok")  # Grok 사용
Agent("역할명", "상세 역할 설명", "mistral")  # Mistral 사용
```

### 역할 프롬프트 커스터마이징

`Agent.work()` 메서드에서 시스템 프롬프트 수정:

```python
{"role": "system", "content": f"You are {self.role}. Give concise, actionable answers."}
# 변경 예시:
{"role": "system", "content": f"You are {self.role}. Respond in Korean with practical code examples."}
```

## 🔑 API 키 설정

### Grok API 키 발급
1. [x.ai](https://x.ai/) 접속
2. 무료 API 키 신청
3. `ai_team.py` 파일의 `GROK_KEY` 변수에 입력

### Mistral API 키 발급
1. [Mistral AI](https://mistral.ai/) 접속
2. 무료 API 키 발급
3. `ai_team.py` 파일의 `MISTRAL_KEY` 변수에 입력

### 환경변수로 관리 (권장)

```bash
# .env 파일 생성
GROK_API_KEY=your_grok_key_here
MISTRAL_API_KEY=your_mistral_key_here
```

```python
# ai_team.py 수정
import os
from dotenv import load_dotenv

load_dotenv()
GROK_KEY = os.getenv("GROK_API_KEY")
MISTRAL_KEY = os.getenv("MISTRAL_API_KEY")
```

## 💰 비용 구조

### 무료 플랜
- **Grok API**: 월 무료 할당량 제공
- **Mistral API**: 월 무료 할당량 제공

### 예상 사용량 (중간 사용 기준)
- 하루 20-30회 질문
- 월 약 600-900회 API 호출
- **예상 비용**: $0 (무료 범위 내)

### 대량 사용 시
- 유료 플랜 전환 가능
- Grok: 사용량 기반 과금
- Mistral: 사용량 기반 과금

## 🐛 문제 해결

### 문제: "Error: EOF when reading a line"

**원인**: 백그라운드 실행 시 `input()` 함수가 입력을 받을 수 없음

**해결**: 터미널에서 직접 실행
```bash
python3 ai_team.py  # 백그라운드 실행 X
```

### 문제: API 오류 (401 Unauthorized)

**원인**: API 키가 잘못되었거나 만료됨

**해결**:
1. API 키 재확인
2. x.ai, Mistral AI 콘솔에서 키 재발급
3. `ai_team.py`에서 키 업데이트

### 문제: 느린 응답

**원인**:
- 네트워크 지연
- API 서버 부하
- 복잡한 질문

**해결**:
1. `timeout` 값 조정 (ai_team.py:25)
```python
timeout=60  # 30 → 60초로 증가
```
2. 질문을 더 구체적으로 수정
3. `/all` 대신 개별 팀원 사용

### 문제: Rate Limit 초과

**원인**: 무료 API 할당량 초과

**해결**:
1. 요청 간격 조정
2. 유료 플랜 고려
3. 여러 API 키 교대로 사용

## 🚀 실전 활용 팁

### 1. 프로젝트 시작 단계
```
/pm [아이디어] 비즈니스 모델 기획해줘
/dev 기술 스택 추천해줘
/ops 개발 환경 설정 가이드
/mkt 초기 마케팅 전략
```

### 2. 개발 단계
```
/dev [기능] 구현 코드 작성해줘
/dev 이 코드 리뷰해줘
/ops Docker 컨테이너 설정
```

### 3. 배포 단계
```
/ops CI/CD 파이프라인 구축
/ops AWS 배포 가이드
/dev API 문서 작성해줘
```

### 4. 성장 단계
```
/mkt 그로스 해킹 전략
/pm 신규 기능 우선순위
/all 사용자 피드백 분석
```

## 📊 고급 활용법

### 팀 회의 시뮬레이션

특정 주제로 팀 전체 브레인스토밍:

```
/all [주제]에 대해 각자 관점에서 분석해줘
```

각 팀원의 다양한 관점을 한 번에 확인할 수 있습니다.

### 의사결정 지원

A/B 선택지가 있을 때:

```
/all A안과 B안 중 어떤 게 나을까? 각자 입장에서 분석해줘
```

### 학습 및 멘토링

새로운 기술 학습:

```
/dev [기술명] 초보자 가이드와 예제 코드 알려줘
/ops [도구명] 실전 활용법 설명해줘
```

## 🎓 학습 리소스

### PM 역량 강화
- 비즈니스 모델 설계
- 요구사항 정의
- 우선순위 결정
- 시장 분석

### 개발 역량 강화
- 백엔드 개발 (FastAPI, Django)
- 프론트엔드 개발 (React, Next.js)
- 데이터베이스 설계
- API 설계 패턴

### DevOps 역량 강화
- Docker/Kubernetes
- CI/CD 자동화
- 클라우드 인프라 (AWS, GCP)
- 모니터링 및 로깅

### 마케팅 역량 강화
- 콘텐츠 마케팅
- 그로스 해킹
- SEO 최적화
- 소셜미디어 전략

## 🤝 기여 방법

이 프로젝트를 개선하고 싶다면:

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이센스

MIT License - 자유롭게 사용, 수정, 배포 가능합니다.

## 📞 문의 및 지원

- 이슈 리포트: GitHub Issues
- 기능 제안: GitHub Discussions
- 문의: john@example.com (실제 이메일로 변경)

---

**Made with ❤️ by AI Team** - 실제 팀처럼 일하는 AI 에이전트들
