### Day 2
# RESET
1. git log /LOG정보 확인 후 커밋 해 확인 및 복사 
    - git log --oneline /사용할경우 해쉬값 7자리만 나와서 편리
2. git reset /복사한 커밋 해쉬값을 이용해 reset 명령어로 원하는 옵션 넣어줌
    - --hard 이전 커밋으로 돌리고 그 이후 이력들 모두삭제
    - --soft 이전 커밋으로 돌리고 그 이후 이력들을 삭제 하지 않고 남겨둠
    - --mixed 이전 커밋으로 돌리고 그 이후 이력들 삭제 안함 but. 다시 커밋하기 위해서는 add . 하여 커밋을 진행해야함
 혼자만 사용하는 브랜치인 경우
 origin에 있지만 아무도 이 브랜치를 사용하지 않는다는 확신을 가지는 경우
 혼자 하는 상황에서만 사용 그 외 거의 모든 경우에서 commit을 되돌릴때 `revert`를 사용

# reflog   
 사용목적 : 실수로 reset을 사용하여 사라진 커밋을 복구하고 싶을 경우 사용
 1. git reflog /명령어를 입력하면 모든 해쉬값이 뜸(삭제포함) 그 해쉬값을 사용하여 다시 reset
 2. git reset --hard 해시값 /해쉬값을 찾아서 입력

 # Revert
사용목적 : 원하는 시점의 커밋된 내용만 되돌리고 싶을때 사용 (RESET : 솔플 , Revert : 팀플)
 1. git log /log 정보 확인 후 커밋 해시 확인 및 복사
    - git log --oneline /사용할경우 해쉬값 7자리만 나와서 편리
 2. git revert [커밋 해시] /복사한 커밋 해시를 이용해 reset 옵션으로는 hard를 사용 
 3. git log /잘 reset되어있는지 확인 

 # Branch 
 사용목적 : 독립적으로 어떤 작업을 진행하기 위한 방법 > 기본적인 틀을 복사해와서 각자 원하는 코드로 작업하고 마지막에 merge를 사용해 붙여넣기 할수 있음.
 1. git branch [브랜치 명] /예 = git branch oz 브랜치 생성
 2. git branch /브랜치 목록 확인
 3. git switch [브랜치 명] /예 = git switch oz 생성한 Branch로 이동
 4. git switch -c oz /브랜치 생성과 동시에 이동하기
 5. git branch -D (삭제할 브랜치명) /예 = git branch -D oz  브랜치 삭제하기
 6. git branch -m (기본 브랜치명) (새 브랜치명) /예 = git branch -m oz oz_new  브랜치 이름 바꾸기 
 7. git cherry-pick (해쉬명) / 다른 브랜치에서 원하는 커밋을 가져올 수 있는 명령어

 # Merge, Rebase
 사용목적 : 생성된 브랜치들을 병합하는 것 
 방식 - merge : 이력을 남기고 병합을 진행 (따로 커밋을 진행해야함)
     - rebase : 이력을 남기지 않고 병합을 진행 (따로 커밋진행 안해도 됨)
 1. Merge
   - git switch [이동을 원하는 branch] /원하는 branch로 이동하는 명령어
   - git merge [합치고 싶은 branch] /main에 branch의 커밋 이력을 합칠때 사용하는 명령어
      - 예 = git switch main -> git merge oz
   - git log /log 명령어를 통해 합쳐진 이력 확인
 2. Rebase
   - git switch [이동을 원하는 branch] /합치려는 branch로 이동하는 명령어
   - git rebase main /합치려는 branch의 커밋 이력을 합칠때 사용하는 명령어
   - git switch main /main branch로 이동 
   - git merge [합치고자하는 branch명] /#main에서 main branch와 합치고자하는 branch를 merge 진행
## Merge, Rebase 진행할떄 다 사용한 Branch는 git Branch -D [브런치 명]으로 꼭 삭제하기.