# Tailwind Nextjs Starter Blog

[![GitHub Repo stars](https://img.shields.io/github/stars/timlrx/tailwind-nextjs-starter-blog?style=social)](https://GitHub.com/timlrx/tailwind-nextjs-starter-blog/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/timlrx/tailwind-nextjs-starter-blog?style=social)](https://github.com/timlrx/tailwind-nextjs-starter-blog/forks)

이 프로젝트는 [Next.js](https://nextjs.org/)와 [Tailwind CSS](https://tailwindcss.com/)를 기반으로 한 블로그 스타터 템플릿입니다. 버전 2는 Next App 디렉토리와 [React Server Component](https://nextjs.org/docs/getting-started/react-essentials#server-components)를 기반으로 하며, [Contentlayer](https://www.contentlayer.dev/)를 사용하여 마크다운 콘텐츠를 관리합니다.

가장 기능이 풍부한 Next.js 마크다운 블로그 템플릿 중 하나로, 설정과 커스터마이징이 매우 쉽습니다. 기존의 Jekyll이나 Hugo 블로그를 대체하기에 완벽합니다.

## 주요 기능

- **Next.js & Typescript**: 최신 웹 기술 스택 사용
- **Contentlayer**: 강력한 콘텐츠 관리 로직
- **Tailwind CSS 3.0**: 간편한 스타일 커스터마이징
- **MDX 지원**: 마크다운 문서 내에서 JSX 사용 가능
- **고성능**: 웹 바이탈 최적화 및 85kB의 가벼운 초기 로드
- **반응형 디자인**: 모바일 친화적 뷰 지원
- **다크 모드**: 라이트/다크 테마 지원
- **다양한 분석 도구 연동**: Google Analytics, Umami 등 지원
- **댓글 시스템**: Giscus (GitHub Discussions 기반), Utterances 등 지원
- **SEO 최적화**: RSS 피드, 사이트맵 자동 생성

## 빠른 시작 가이드

1. **저장소 클론하기**

```bash
git clone https://github.com/timlrx/tailwind-nextjs-starter-blog.git my-blog
cd my-blog
```

2. **설정 수정하기**
   - `data/siteMetadata.js`: 사이트 제목, 설명, 소셜 링크 등 기본 정보를 수정하세요.
   - `data/authors/default.md`: 작성자(본인) 정보를 수정하세요.
   - `next.config.js`: 콘텐츠 보안 정책(CSP)이나 분석/댓글 제공자를 변경하려면 수정하세요.

3. **블로그 글 작성하기**
   - `data/blog` 폴더에 마크다운(.md) 또는 MDX(.mdx) 파일을 추가하여 글을 작성합니다.

## 설치 및 실행

**의존성 설치**

```bash
npm install
# 또는
yarn
```

**개발 서버 실행**

```bash
npm run dev
# 또는
yarn dev
```

브라우저에서 [http://localhost:3000](http://localhost:3000)을 열어 결과를 확인하세요.
`app` 폴더의 레이아웃이나 `data` 폴더의 콘텐츠를 수정하면 실시간으로 반영됩니다.

## 프로젝트 구조 및 커스터마이징

- `data/siteMetadata.js`: 사이트 관련 대부분의 정보가 들어있습니다. 가장 먼저 수정해야 할 파일입니다.
- `data/authors/default.md`: 기본 작성자 정보입니다. `data/authors`에 파일을 추가하여 여러 작성자를 등록할 수 있습니다.
- `data/headerNavLinks.js`: 상단 네비게이션 메뉴 링크를 수정합니다.
- `data/blog`: 블로그 게시글이 저장되는 곳입니다.
- `public/static`: 이미지나 파비콘 같은 정적 자산을 저장합니다.
- `tailwind.config.js` & `css/tailwind.css`: 사이트의 전반적인 디자인을 수정할 수 있는 Tailwind 설정 파일입니다.
- `layouts`: 페이지의 레이아웃 템플릿들이 위치합니다. (예: `PostLayout`, `ListLayout` 등)

## 배포하기 (GitHub Pages)

이 템플릿은 GitHub Pages 배포를 지원합니다.

1. `next.config.js`에서 `output: 'export'` 설정이 되어 있는지 확인하세요.
2. GitHub 저장소의 `Settings > Pages` 메뉴로 이동합니다.
3. **Source**를 `GitHub Actions`로 선택하면 자동으로 제공된 워크플로우를 통해 배포됩니다.

## 라이선스

[MIT](https://github.com/timlrx/tailwind-nextjs-starter-blog/blob/main/LICENSE) © [Timothy Lin](https://www.timlrx.com)
