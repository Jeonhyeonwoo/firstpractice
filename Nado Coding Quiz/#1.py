names = ["유튜버1","유튜버2","유튜버3","유튜버4"]
#안녕하세요? 님
#(주)나도 출판 편집자 나코입니다.
#현재 저희 출판사는 파이썬에 관한  주제로 책 출간을 기획 중입니다.
#님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
#자세한 내용은 첨부드리는 제안서를 확인 부탁 드리며, 긍정적인 회신 기다리겠습니다.

#좋은 하루 보내세요^^
#감사합니다.

#-나코 드림.

for i in names:
    with open(str(i)+".txt","w",encoding="utf8") as name:
        name.write("안녕하세요?"+ str(i)+"님\n")
        name.write("(주)나도 출판 편집자 나코입니다.\n")
        name.write("현재 저희 출판사는 파이썬에 관한  주제로 책 출간을 기획 중입니다.\n")
        name.write(str(i)+"님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n")
        name.write("자세한 내용은 첨부드리는 제안서를 확인 부탁 드리며, 긍정적인 회신 기다리겠습니다.\n")
        name.write("\n좋은 하루 보내세요^^\n")
        name.write("감사합니다.\n")
        name.write("\n-나코 드림.")