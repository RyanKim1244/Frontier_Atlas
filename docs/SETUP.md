# 배포와 계정 설정

순서대로 하면 됩니다. 각 단계는 한 번만 하면 됩니다.

## 1. 데이터베이스 만들기 (Supabase)

1. Supabase 대시보드 → 프로젝트 `sqoonckkmsmtojmdlrrd` → **SQL Editor** → New query.
2. `supabase/migrations/20261023000000_init.sql` 내용을 전부 붙여넣고 **Run**.
3. "Success. No rows returned"가 나오면 끝입니다.

## 2. 사이트 주소 등록 (Supabase → Authentication → URL Configuration)

- **Site URL**: `https://ryankim1244.github.io/Frontier_Atlas/`
- **Redirect URLs**에 추가: `https://ryankim1244.github.io/Frontier_Atlas/`, `http://localhost:8000/`

## 3. 로그인 제공자

세 곳 모두 콜백 주소는 같습니다: `https://sqoonckkmsmtojmdlrrd.supabase.co/auth/v1/callback`

**GitHub**
1. GitHub → Settings → Developer settings → OAuth Apps → New OAuth App.
2. Homepage URL: `https://ryankim1244.github.io/Frontier_Atlas/`, Authorization callback URL: 위 콜백 주소.
3. Client ID와 새로 만든 Client secret을 Supabase → Authentication → Sign In / Providers → GitHub에 넣고 켭니다.

**Google**
1. Google Cloud Console → APIs & Services → OAuth consent screen 설정(External).
2. Credentials → Create credentials → OAuth client ID → Web application.
3. Authorized redirect URIs에 위 콜백 주소를 넣습니다.
4. Client ID / Client secret을 Supabase → Providers → Google에 넣고 켭니다.

**Kakao** (선택)
1. Kakao Developers → 앱 만들기 → 앱 설정 → 플랫폼 키의 **REST API 키**가 Client ID입니다.
2. 같은 화면에서 Kakao Login Redirect URI에 위 콜백 주소를 넣고, Client Secret을 활성화해 코드를 복사합니다.
3. 제품 설정 → 카카오 로그인 → 사용 설정 ON. 동의항목에서 `profile_nickname`, `profile_image`, `account_email`을 설정합니다. `account_email`은 비즈 앱이어야 설정할 수 있습니다.
4. Supabase → Providers → Kakao에 REST API 키와 Client Secret을 넣고 켭니다. 이메일을 받지 않는다면 **Allow users without an email**도 켭니다.
5. `site/config.js`의 `providers`에 `"kakao"`를 추가합니다.

## 4. GitHub Pages 켜기

1. 저장소 → Settings → Pages → Build and deployment → Source: **GitHub Actions**.
2. `main`에 push하면 `.github/workflows/pages.yml`이 사이트를 빌드해 올립니다.

무료 플랜에서 Pages는 공개 저장소에서만 됩니다.

## 5. 나를 편집자로 지정

사이트에서 한 번 로그인한 뒤 SQL Editor에서 실행합니다. 가장 먼저 가입한 계정이 편집자가 됩니다.

```sql
insert into public.admins (user_id)
select id from public.profiles order by created_at limit 1;
```

편집자는 문제 제출을 검토하고(Review 메뉴) 다른 사람의 글을 지울 수 있습니다.

## 6. 개인정보 처리방침에 들어갈 값

`site/config.js`의 `contact`(문의 이메일)와 `dataRegion`(Supabase 프로젝트 지역, Project Settings → General에서 확인)을 채우면 Privacy 페이지에 표시됩니다.
