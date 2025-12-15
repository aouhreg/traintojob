from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Cloud Native AI Service"
    env: str = "dev"

settings = Settings()

 


#為什麼這樣做（面試用）
#提早引入設定層，未來能無痛切換 dev / staging / prod，符合 cloud-native design。


#簡單來説，這樣設計是爲了把設定與程式邏輯解耦，讓服務可以透過環境變數在 dev / staging / prod 之間切換，而不需要修改程式碼。 符合cloud-native 與 twelve-facter app的設計原則

# 就是設定是部署的差異，而不是程式的差異
"""
在實務上，不同環境的差異通常是：
- DB 連接字串
- API key
- Log level
- Model path
- GPU/CPU config

如果把dev，prod，staging的差異都寫在程式碼中，未來如果要切換環境，就會需要修改程式碼，這樣就違反了十二因數應用的設計原則
會導致程式碼分支爆炸，不同環境要改code，版本難以管控。

所以設定應該由部署來設定，而不是由程式碼來決定

2.爲什麽用BaseSettings 而不是普通的python class

BaseSettings 有以下優點：
- 自動從環境變數中讀取設定
- 自動轉換型別
- 自動驗證設定
- 自動生成docs

所以在同一份程式碼，在不同環境的自動行爲不同

3. Cloud-Native 的核心假設：不可變映像·可變設定

在Docker/ k8s中：
- Image： 不可變（同一個image跑everywhere）
- Config： 可變（根據環境不同而不同）透過env/secret注入

這樣的設計剛好符合Build once， deploy many times

我不用再為prod再build一個image
為了staging而再改一份code

4.那爲什麽是現在就放，而不是之後再加

加設定層是結構性的改變，越晚加，影響面就越大，一開始的成本幾乎為0，但是後期refactor的成本高
比如現在的app/core/config.py
以後可以擴充成
- logging config
- database config
- model config
- feature flag

這是architectural foresight 不是over-engineering


提早引入設定層，是爲了確保服務在雲端環境下可以同一份程式碼·不同設定即不同行爲，這是cloud-native服務可擴展與可運維的基本前提
"""