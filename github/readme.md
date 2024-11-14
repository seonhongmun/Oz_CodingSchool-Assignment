### Day 1

Git파일 Commiit하는 순서
1. git init
2. git config --list
3. git config 설정 
  - git config user.name "seonhongmun" ""안에 이름
  - git config user.email "mshg_@navercom" ""안에 이메일
4. git config --list 설정 리스트 확인 
5. mkdir github
6. git status 
7. git add . 하위 폴더 전체 커밋설정
8. git commit -m "제목"
9. git log 로그 확인
10. git branch -M main 마스터에서 메인으로 변경 
11. git remote add origin https://github.com/seonhongmun/Oz_08.git 깃 허브에 업로드 
12. git push -u origin main 신뢰설정

수정본 다시 보내기 
1. 저장 후 git add . (저장 후 내용 재 등록)
2. git commit -m "커밋 할 내용" (커밋 할 내용 재 설정)
3. git push -f (신뢰 설정 후에 강제로 밀어넣기)