# ai_team.py - 대화형 AI 팀
import requests
import json
from datetime import datetime
import time
import threading
import os
from dotenv import load_dotenv

# .env 파일에서 API 키 로드
load_dotenv()
GROK_KEY = os.getenv("GROK_API_KEY")
MISTRAL_KEY = os.getenv("MISTRAL_API_KEY")

if not GROK_KEY or not MISTRAL_KEY:
    print("⚠️ Warning: API keys not found in .env file")
    print("Please create a .env file with GROK_API_KEY and MISTRAL_API_KEY")
    exit(1)

class Agent:
    def __init__(self, name, role, ai="grok"):
        self.name = name
        self.role = role
        self.ai = ai

    def work(self, task):
        url = "https://api.x.ai/v1/chat/completions" if self.ai == "grok" else "https://api.mistral.ai/v1/chat/completions"
        key = GROK_KEY if self.ai == "grok" else MISTRAL_KEY
        model = "grok-beta" if self.ai == "grok" else "mistral-small-latest"

        try:
            r = requests.post(url, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
                json={"model": model, "messages": [{"role": "system", "content": f"You are {self.role}. Give concise, actionable answers."},
                      {"role": "user", "content": task}]}, timeout=30)
            r.raise_for_status()
            r.encoding = 'utf-8'  # UTF-8 인코딩 명시
            return r.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {e}"

class Team:
    def __init__(self):
        self.agents = {
            "pm": Agent("PM", "Product Manager", "grok"),
            "dev": Agent("Dev", "Full-stack Developer", "mistral"),
            "ops": Agent("Ops", "DevOps Engineer", "grok"),
            "mkt": Agent("Marketing", "Marketing Specialist", "mistral"),
        }

        print("\n✅ AI 팀 준비됨")
        for k, a in self.agents.items():
            print(f"  /{k} - {a.name}")
        print("\n명령어:")
        print("  /pm [질문] - PM에게 물어보기")
        print("  /dev [작업] - 개발자에게 작업 지시")
        print("  /ops [작업] - DevOps에게 작업 지시")
        print("  /mkt [작업] - 마케팅에게 작업 지시")
        print("  /all [질문] - 전체 팀에게 물어보기")
        print("  [질문] - AI가 자동으로 적절한 팀원 선택")
        print("  /quit - 종료\n")

    def auto_route(self, question):
        """질문을 분석해서 적절한 팀원 자동 선택"""
        q_lower = question.lower()

        # 키워드 기반 라우팅
        keywords = {
            "pm": ["기획", "비즈니스", "전략", "로드맵", "요구사항", "기능", "우선순위", "모델", "시장", "경쟁사"],
            "dev": ["코드", "개발", "구현", "api", "데이터베이스", "프론트", "백엔드", "함수", "버그", "최적화", "프로그래밍"],
            "ops": ["배포", "도커", "docker", "ci/cd", "인프라", "aws", "서버", "클라우드", "kubernetes", "nginx"],
            "mkt": ["마케팅", "광고", "콘텐츠", "seo", "sns", "홍보", "브랜딩", "고객", "캠페인", "성장"]
        }

        # 각 팀원별 매칭 점수 계산
        scores = {k: 0 for k in self.agents.keys()}
        for agent_key, words in keywords.items():
            for word in words:
                if word in q_lower:
                    scores[agent_key] += 1

        # 가장 높은 점수의 팀원 찾기
        best_match = max(scores, key=scores.get)

        # 매칭 점수가 0이면 전체 팀에게 질문
        if scores[best_match] == 0:
            return "all"

        return best_match

    def command(self, cmd):
        """명령 처리"""
        if not cmd.strip():
            return

        parts = cmd.split(maxsplit=1)
        if len(parts) < 2:
            print("❌ 사용법: /pm [질문]")
            return

        agent_key = parts[0][1:]  # / 제거
        task = parts[1]

        if agent_key == "all":
            print("\n📢 전체 팀에게 질문 중...\n")
            for k, a in self.agents.items():
                print(f"[{a.name}]")
                result = a.work(task)
                print(f"{result}\n")
        elif agent_key in self.agents:
            a = self.agents[agent_key]
            print(f"\n💬 {a.name}에게 전달 중...\n")
            result = a.work(task)
            print(f"[{a.name}] {result}\n")
        else:
            print("❌ 알 수 없는 명령. /pm, /dev, /ops, /mkt, /all 사용")

    def run(self):
        """대화형 루프"""
        while True:
            try:
                cmd = input("👤 You> ")

                if cmd.strip() == "/quit":
                    print("👋 종료")
                    break

                if cmd.startswith("/"):
                    self.command(cmd)
                else:
                    # 자동 라우팅
                    if cmd.strip():
                        selected = self.auto_route(cmd)
                        agent = self.agents[selected]

                        if selected == "all":
                            print("\n🤔 전체 팀 회의로 진행합니다...\n")
                            for k, a in self.agents.items():
                                print(f"[{a.name}]")
                                result = a.work(cmd)
                                print(f"{result}\n")
                        else:
                            print(f"\n🎯 {agent.name}이(가) 답변합니다...\n")
                            result = agent.work(cmd)
                            print(f"[{agent.name}] {result}\n")

            except KeyboardInterrupt:
                print("\n👋 종료")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    team = Team()
    team.run()
